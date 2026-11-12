"""Binary sensor BYD EV Center."""
from __future__ import annotations

import logging

from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntity,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import (
    CONF_BYD_DOORS,
    CONF_BYD_LOCKED,
    CONF_BYD_ONLINE,
    CONF_BYD_VEHICLE_STATE,
    CONF_BYD_WINDOWS,
    CONF_WALLBOX_ENABLED,
    WALLBOX_CHARGING_STATES,
    DOMAIN,
)
from .coordinator import BydMateCoordinator

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    coordinator: BydMateCoordinator = hass.data[DOMAIN][entry.entry_id]
    wb = bool(
        entry.options.get(
            CONF_WALLBOX_ENABLED, entry.data.get(CONF_WALLBOX_ENABLED, False)
        )
    )

    entities: list[BinarySensorEntity] = [
        InCaricaSensor(coordinator, f"{coordinator.entry.entry_id}_in_carica",
                       "in_carica", lambda d: d["charging"]),
        BydInfoBinary(coordinator, f"{coordinator.entry.entry_id}_byd_online",
                      "byd_online", CONF_BYD_ONLINE,
                      BinarySensorDeviceClass.CONNECTIVITY, "mdi:cloud-check"),
        BydInfoBinary(coordinator, f"{coordinator.entry.entry_id}_byd_bloccata",
                      "byd_bloccata", CONF_BYD_LOCKED,
                      None, "mdi:car-key", invert=True),
        BydInfoBinary(coordinator, f"{coordinator.entry.entry_id}_byd_porte",
                      "byd_porte_aperte", CONF_BYD_DOORS,
                      BinarySensorDeviceClass.DOOR, "mdi:car-door"),
        BydInfoBinary(coordinator, f"{coordinator.entry.entry_id}_byd_finestrini",
                      "byd_finestrini_aperti", CONF_BYD_WINDOWS,
                      BinarySensorDeviceClass.WINDOW, "mdi:car-window-closed-variant"),
        BydInfoBinary(coordinator, f"{coordinator.entry.entry_id}_byd_accesa",
                      "byd_accesa", CONF_BYD_VEHICLE_STATE,
                      BinarySensorDeviceClass.POWER, "mdi:car-key"),
    ]
    if wb:
        entities.append(
            InCaricaSensor(coordinator, f"{coordinator.entry.entry_id}_wb_in_carica",
                           "wb_in_carica",
                           lambda d: d["wb_state"] in WALLBOX_CHARGING_STATES,
                           icon="mdi:ev-station"),
        )
    async_add_entities(entities)


class InCaricaSensor(CoordinatorEntity[BydMateCoordinator], BinarySensorEntity):
    _attr_has_entity_name = True

    def __init__(self, coordinator, unique_id, key, extractor,
                 device_class=BinarySensorDeviceClass.BATTERY_CHARGING, icon=None) -> None:
        super().__init__(coordinator)
        self._attr_device_info = coordinator.device_info
        self._attr_unique_id = unique_id
        self._attr_translation_key = key
        self._attr_device_class = device_class
        if icon:
            self._attr_icon = icon
        self._extractor = extractor

    @property
    def is_on(self) -> bool | None:
        return bool(self._extractor(self.coordinator.data))

class BydInfoBinary(CoordinatorEntity[BydMateCoordinator], BinarySensorEntity):
    """Stato booleano letto da un'entità dell'integrazione BYD."""

    _attr_has_entity_name = True

    def __init__(self, coordinator, unique_id, key, conf_key, device_class=None,
                 icon=None, invert=False) -> None:
        super().__init__(coordinator)
        self._attr_device_info = coordinator.device_info
        self._attr_unique_id = unique_id
        self._attr_translation_key = key
        self._attr_device_class = device_class
        self._attr_icon = icon
        self._conf_key = conf_key
        self._invert = invert

    @property
    def is_on(self) -> bool | None:
        eid = self.coordinator.opts.get(self._conf_key)
        st = self.coordinator.hass.states.get(eid) if eid else None
        if st is None or st.state in ("unknown", "unavailable", ""):
            return None
        on = str(st.state).lower() in ("on", "true", "1", "open")
        return (not on) if self._invert else on
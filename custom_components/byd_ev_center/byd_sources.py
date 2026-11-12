"""Auto-rilevamento delle entità dell'integrazione `byd_vehicle`.

L'integrazione BYD espone decine di entità con nomi tradotti nella lingua di
Home Assistant (es. `sensor.byd_dolphin_surf_livello_batteria`). Gli entity_id
non sono quindi stabili fra lingue e veicoli: qui si usano le chiavi di
traduzione (`translation_key`) del registro entità, che sono invece fisse
(`elec_percent`, `total_mileage`, `is_charging`, ...).

Il rilevamento è best-effort: ogni valore può restare vuoto e l'utente può
sempre scegliere l'entità a mano nel wizard.
"""
from __future__ import annotations

from typing import Any

from homeassistant.core import HomeAssistant
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers import entity_registry as er

from .const import (
    CONF_AC_BUTTON,
    CONF_BATTERY_LEVEL,
    CONF_BYD_BATTERY_POWER,
    CONF_BYD_CABIN_TEMP,
    CONF_BYD_CHARGE_REMAINING,
    CONF_BYD_DETECTED_MODEL,
    CONF_BYD_DOORS,
    CONF_BYD_LAST_SEEN,
    CONF_BYD_LOCKED,
    CONF_BYD_MODEL_NAME,
    CONF_BYD_ONLINE,
    CONF_BYD_OUTSIDE_TEMP,
    CONF_BYD_RECENT_ENERGY,
    CONF_BYD_TIRE_FL,
    CONF_BYD_TIRE_FR,
    CONF_BYD_TIRE_RL,
    CONF_BYD_TIRE_RR,
    CONF_BYD_TOTAL_ENERGY,
    CONF_BYD_VEHICLE_STATE,
    CONF_BYD_VIN,
    CONF_BYD_WINDOWS,
    CONF_CHARGE_START_BUTTON,
    CONF_CHARGING_ENTITY,
    CONF_CLIMATE_ENTITY,
    CONF_HORN_ENTITY,
    CONF_LIGHT_ENTITY,
    CONF_LOCATION_ENTITY,
    CONF_ODOMETER,
    CONF_PLUG_ENTITY,
    CONF_RANGE,
    MODEL_ALIASES,
    MODEL_AUTO,
)

# chiave config -> (translation_key preferiti, domini ammessi)
_KEYS: dict[str, tuple[tuple[str, ...], tuple[str, ...]]] = {
    CONF_BATTERY_LEVEL: (("elec_percent", "power_battery"), ("sensor",)),
    CONF_RANGE: (
        ("endurance_mileage", "ev_endurance", "endurance_mileage_v2"),
        ("sensor",),
    ),
    CONF_ODOMETER: (("total_mileage", "total_mileage_v2"), ("sensor",)),
    CONF_CHARGING_ENTITY: (("is_charging",), ("binary_sensor", "sensor")),
    CONF_PLUG_ENTITY: (
        ("is_charger_connected", "is_charging"),
        ("binary_sensor", "sensor"),
    ),
    CONF_LOCATION_ENTITY: (("location",), ("device_tracker",)),
    # comandi remoti: nomi BYD (button.start_charging, switch.car_on, ...)
    CONF_CHARGE_START_BUTTON: (
        ("start_charging", "charge_to_full"),
        ("button", "switch"),
    ),
    CONF_AC_BUTTON: (("car_on", "climate"), ("switch", "button")),
    CONF_CLIMATE_ENTITY: (("climate",), ("climate",)),
    CONF_LIGHT_ENTITY: (("flash_lights",), ("button", "switch", "light")),
    CONF_HORN_ENTITY: (("find_car",), ("button", "switch")),
    CONF_BYD_ONLINE: (("is_online",), ("binary_sensor",)),
    CONF_BYD_LOCKED: (("is_locked",), ("binary_sensor",)),
    CONF_BYD_DOORS: (("is_any_door_open",), ("binary_sensor",)),
    CONF_BYD_WINDOWS: (("is_any_window_open",), ("binary_sensor",)),
    CONF_BYD_VEHICLE_STATE: (("vehicle_state",), ("binary_sensor", "sensor")),
    CONF_BYD_CABIN_TEMP: (("temp_in_car", "inside_temp"), ("sensor",)),
    CONF_BYD_OUTSIDE_TEMP: (("temp_out_car", "outside_temp"), ("sensor",)),
    CONF_BYD_BATTERY_POWER: (("battery_power",), ("sensor",)),
    CONF_BYD_CHARGE_REMAINING: (("charge_remaining_time",), ("sensor",)),
    CONF_BYD_TOTAL_ENERGY: (("total_energy", "total_consumption"), ("sensor",)),
    CONF_BYD_RECENT_ENERGY: (
        ("recent_50km_energy", "last_50km_avg_ev_consumption"),
        ("sensor",),
    ),
    CONF_BYD_LAST_SEEN: (("last_updated",), ("sensor",)),
    CONF_BYD_TIRE_FL: (("left_front_tire_pressure",), ("sensor",)),
    CONF_BYD_TIRE_FR: (("right_front_tire_pressure",), ("sensor",)),
    CONF_BYD_TIRE_RL: (("left_rear_tire_pressure",), ("sensor",)),
    CONF_BYD_TIRE_RR: (("right_rear_tire_pressure",), ("sensor",)),
}


def _domain(entity: er.RegistryEntry) -> str:
    return entity.entity_id.split(".", 1)[0]


def _usable(entity: er.RegistryEntry) -> bool:
    return entity.platform == "byd_vehicle" and entity.disabled_by is None


def _pick(entries: list[er.RegistryEntry], keys: tuple[str, ...],
          domains: tuple[str, ...]) -> str | None:
    for key in keys:
        for entry in entries:
            if entry.translation_key == key and _domain(entry) in domains:
                return entry.entity_id
    return None


def detect_byd_entities(hass: HomeAssistant) -> dict[str, str]:
    """Mappa chiave config -> entity_id per il primo veicolo BYD trovato."""
    reg = er.async_get(hass)
    entries = [e for e in reg.entities.values() if _usable(e)]
    if not entries:
        return {}

    # Un veicolo per device: scegli quello con più entità riconosciute.
    by_device: dict[str | None, list[er.RegistryEntry]] = {}
    for entry in entries:
        by_device.setdefault(entry.device_id, []).append(entry)

    def score(items: list[er.RegistryEntry]) -> int:
        return sum(
            1
            for keys, domains in _KEYS.values()
            if _pick(items, keys, domains)
        )

    best = max(by_device.values(), key=score, default=[])
    out: dict[str, str] = {}
    for conf_key, (keys, domains) in _KEYS.items():
        found = _pick(best, keys, domains)
        if found:
            out[conf_key] = found

    device_id = best[0].device_id if best else None
    device = dr.async_get(hass).async_get(device_id) if device_id else None
    model = str(
        getattr(device, "model", "")
        or getattr(device, "name", "")
        or ""
    )
    if model:
        out[CONF_BYD_MODEL_NAME] = model
        guessed = guess_model(model)
        if guessed:
            out[CONF_BYD_DETECTED_MODEL] = guessed
    if device is not None and device.serial_number:
        out[CONF_BYD_VIN] = str(device.serial_number)
    return out


def guess_model(text: Any) -> str | None:
    """Riconosce il modello BYD da una stringa libera (device.model / nome)."""
    low = str(text or "").lower()
    if not low:
        return None
    # prima gli alias più specifici (es. "atto 3 evo" prima di "atto 3")
    for model in sorted(MODEL_ALIASES, key=lambda m: -max(map(len, MODEL_ALIASES[m]))):
        if any(alias in low for alias in MODEL_ALIASES[model]):
            return model
    return None


def resolve_model(opts: dict[str, Any]) -> str:
    """Modello effettivo: scelta utente, altrimenti quello rilevato dal device."""
    chosen = str(opts.get("model") or "").strip()
    if chosen and chosen != MODEL_AUTO:
        return chosen
    detected = str(opts.get(CONF_BYD_DETECTED_MODEL) or "").strip()
    if detected:
        return detected
    return guess_model(opts.get(CONF_BYD_MODEL_NAME)) or MODEL_AUTO

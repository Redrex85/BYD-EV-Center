"""Costanti per BYD EV Center."""
from __future__ import annotations

DOMAIN = "byd_ev_center"

# mesi per il filtro ricariche (indice 0 = "Tutti", così MESI.index() dà il numero del mese)
MESI_FILTRO = ["Tutti", "Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno",
               "Luglio", "Agosto", "Settembre", "Ottobre", "Novembre", "Dicembre"]
MANUFACTURER = "BYD EV Center"
PLATFORMS: list[str] = ["sensor", "binary_sensor", "button", "number", "select", "switch", "time", "device_tracker", "climate"]

# --- chiavi config flow -------------------------------------------------------
CONF_NAME = "name"
CONF_ODOMETER = "odometer_entity"
CONF_BATTERY_LEVEL = "battery_level_entity"
CONF_RANGE = "range_entity"
CONF_CHARGING_ENTITY = "charging_entity"
CONF_PLUG_ENTITY = "plug_entity"
CONF_LOCATION_ENTITY = "location_entity"

# --- entità informative BYD (opzionali, auto-rilevate dall'integrazione byd_vehicle) ---
CONF_BYD_MODEL_NAME = "byd_model_name"
CONF_BYD_ONLINE = "byd_online_entity"
CONF_BYD_LOCKED = "byd_locked_entity"
CONF_BYD_DOORS = "byd_doors_entity"
CONF_BYD_WINDOWS = "byd_windows_entity"
CONF_BYD_VEHICLE_STATE = "byd_vehicle_state_entity"
CONF_BYD_CABIN_TEMP = "byd_cabin_temp_entity"
CONF_BYD_OUTSIDE_TEMP = "byd_outside_temp_entity"
CONF_BYD_BATTERY_POWER = "byd_battery_power_entity"
CONF_BYD_CHARGE_REMAINING = "byd_charge_remaining_entity"
CONF_BYD_TOTAL_ENERGY = "byd_total_energy_entity"
CONF_BYD_RECENT_ENERGY = "byd_recent_energy_entity"
CONF_BYD_LAST_SEEN = "byd_last_seen_entity"
CONF_BYD_TIRE_FL = "byd_tire_fl_entity"
CONF_BYD_TIRE_FR = "byd_tire_fr_entity"
CONF_BYD_TIRE_RL = "byd_tire_rl_entity"
CONF_BYD_TIRE_RR = "byd_tire_rr_entity"
CONF_BYD_VIN = "byd_vin"
CONF_BYD_DETECTED_MODEL = "byd_detected_model"

CONF_WALLBOX_ENABLED = "wallbox_enabled"
# --- profilo di installazione: base (solo auto) · pro (+wallbox) · enterprise (+FV) ---
CONF_PROFILE = "profile"
PROFILE_BASE = "base"
PROFILE_PRO = "pro"
PROFILE_ENTERPRISE = "enterprise"
PROFILES = [PROFILE_BASE, PROFILE_PRO, PROFILE_ENTERPRISE]
DEFAULT_PROFILE = PROFILE_PRO
CONF_WB_POWER = "wallbox_power_entity"
CONF_WB_STATE = "wallbox_state_entity"
CONF_WB_SESSION_ENERGY = "wallbox_session_energy_entity"
CONF_WB_TOTAL_ENERGY = "wallbox_total_energy_entity"
CONF_WB_MAX_CURRENT = "wallbox_max_current_entity"
CONF_WB_SESSION_TIME = "wallbox_session_time_entity"

CONF_CAPACITY = "battery_capacity"
CONF_TARGET_SOC = "target_soc"
CONF_PRICE_HOME = "price_home"
CONF_PRICE_PUBLIC = "price_public"
CONF_PRICE_SOLAR = "price_solar"
# ricariche fatte PRIMA di installare l'integrazione (per il calcolo dei risparmi)
CONF_PRE_KWH = "pre_kwh"
CONF_PRE_EUR = "pre_eur"
# odometro al momento dell'installazione: baseline del confronto "da installazione"
# (0 = la cattura da sola al primo avvio; serve per auto usate o baseline sbagliata)
CONF_INSTALL_ODO = "install_odo"
CONF_CHARGING_EFFICIENCY = "charging_efficiency"
CONF_POLL_INTERVAL = "poll_interval"
CONF_TRIP_TIMEOUT = "trip_timeout"

# confronto con auto termica (opzionale)
CONF_FUEL_ENABLED = "fuel_comparison"
CONF_FUEL_CONSUMPTION = "fuel_consumption"
CONF_FUEL_PRICE = "fuel_price"
CONF_FUEL_LABEL = "fuel_label"
CONF_DIESEL_PRICE_ENTITY = "diesel_price_entity"

# manutenzione e bollo (per il risparmio netto)
CONF_MAINT_ENABLED = "maint_comparison"
CONF_TAG_TERMICO = "service_cost_thermal"
CONF_TAG_EV = "service_cost_ev"
CONF_BOLLO_TERMICO = "road_tax_thermal"
CONF_BOLLO_EV = "road_tax_ev"
CONF_TAGLIANDO_INTERVALLO = "service_interval_km"
CONF_TYRE_INTERVAL = "tyre_interval_km"
CONF_PURCHASE_DATE = "purchase_date"
DEFAULT_TYRE_INTERVAL = 40000
DEFAULT_TAG_TERMICO = 450.0
DEFAULT_TAG_EV = 100.0
DEFAULT_BOLLO_TERMICO = 350.0
DEFAULT_BOLLO_EV = 0.0
DEFAULT_TAGLIANDO_INTERVALLO = 15000

# notifiche scadenze
CONF_NOTIFY_SERVICE = "notify_service"
CONF_NOTIFY_DAYS = "notify_days"
CONF_NOTIFY_TEXTS = "notify_texts"

# cartella (sotto /config) dove export_data scrive i backup JSON
EXPORT_DIR = "byd_ev_center_export"
CONF_TAGLIANDO_MODE = "tagliando_mode"
CONF_TAGLIANDO_DATA = "tagliando_data"
CONF_ASSICURAZIONE_COSTO = "assicurazione_costo"
CONF_ASSICURAZIONE_DATA = "assicurazione_data"
DEFAULT_NOTIFY_DAYS = 30
DEFAULT_ASSICURAZIONE_COSTO = 400.0

# dashboard automatica e modello auto
CONF_CREATE_DASHBOARD = "create_dashboard"
CONF_MODEL = "model"
MODEL_AUTO = "Auto"
# Modelli BYD venduti in Europa con dati disponibili nell'API DiLink.
# DM-i / PHEV restano fuori da questo elenco: i calcoli EV Center assumono
# una batteria di trazione ricaricabile e sensori di consumo elettrico.
MODELS = [
    MODEL_AUTO,
    "Dolphin Surf",
    "Dolphin",
    "Atto 2",
    "Atto 3",
    "Atto 3 EVO",
    "Seal",
    "Seal U",
    "Sealion 7",
    "Tang",
    "Custom",
]

# notifiche e automazioni ricarica
CONF_NOTIFY_CHARGE_START = "notify_charge_start"
CONF_NOTIFY_CHARGE_END = "notify_charge_end"
CONF_LOW_SOC_ENABLED = "low_soc_enabled"
CONF_LOW_SOC_THRESHOLD = "low_soc_threshold"
CONF_LOW_SOC_START = "low_soc_start"
CONF_LOW_SOC_END = "low_soc_end"
CONF_LOW_SOC_DAYS = "low_soc_days"
CONF_CHARGE_SCHED_MODE = "charge_sched_mode"  # orario | percentuale
CONF_CHARGE_START_TIME = "charge_start_time"
CONF_CHARGE_STOP_TIME = "charge_stop_time"
CONF_CHARGE_START_SOC = "charge_start_soc"
CONF_CHARGE_STOP_SOC = "charge_stop_soc"
CONF_CHARGE_START_BUTTON = "charge_start_button"
CONF_AC_BUTTON = "ac_button_entity"
CONF_CLIMATE_ENTITY = "climate_entity"
CONF_CHARGE_TARGET_NUMBER = "charge_target_number"
CONF_WB_CHARGE_SWITCH = "wb_charge_switch"
CONF_WB_STOP_SWITCH = "wb_stop_switch"
CONF_LIGHT_ENTITY = "light_entity"
CONF_HORN_ENTITY = "horn_entity"
DEFAULT_LOW_SOC_THRESHOLD = 25.0
DEFAULT_LOW_SOC_START = "18:00"
DEFAULT_LOW_SOC_END = "22:00"
DEFAULT_LOW_SOC_DAYS = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
WEEKDAYS = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]

# --- bilanciamento casalingo (potenza casa / contatore) -----------------------
CONF_HOME_POWER_SENSOR = "home_power_sensor"   # sensore consumo casa (W o kW)
CONF_HOME_METER_KW = "home_meter_kw"           # contatore: 3 · 4.5 · 6 · 10 (superiore)
CONF_HOME_MAX_AMPS = "home_max_amps"           # ampere da ripristinare (carico basso)
CONF_HOME_REDUCE_AMPS = "home_reduce_amps"     # ampere da impostare (carico alto)
DEFAULT_HOME_METER_KW = 6.0
DEFAULT_HOME_MAX_AMPS = 25.0
DEFAULT_HOME_REDUCE_AMPS = 18.0
HOME_METER_OPTIONS = ["3", "4.5", "6", "10"]

# profili installazione: minimal (solo auto) · pro (auto+wallbox) · enterprise (+FV)
CONF_HAS_PV = "has_pv"

# --- fusione ricariche spezzate (una spina = una ricarica) --------------------
CONF_CHARGE_MERGE = "charge_merge"        # fondi sessioni ravvicinate nello stesso posto
DEFAULT_CHARGE_MERGE = True
CHARGE_MERGE_WINDOW_S = 1200              # finestra massima fra due sessioni da fondere (20 min:
                                          # copre il top-off dopo il target, 80% -> 81%)
CHARGE_STOP_CLOSE_S = 900                 # carica ferma per 15 min = sessione chiusa (anche se
                                          # la spina resta inserita e lo stato wallbox non è noto)

# --- sperimentazione GSE (limite di potenza a fasce orarie) -------------------
CONF_GSE_ENABLED = "gse_enabled"          # abilita la sperimentazione GSE (wizard/opzioni)
CONF_GSE_WPA = "gse_wpa"                  # watt per ampere della wallbox (230 mono, 690 trifase)
CONF_GSE_KW_MAX = "gse_kw_max"            # potenza consentita nella fascia (es. 6 kW)
CONF_GSE_KW_RIDOTTA = "gse_kw_ridotta"    # potenza fuori fascia (es. 3 kW)
CONF_GSE_START = "gse_start"              # inizio fascia consentita (es. 23:00)
CONF_GSE_END = "gse_end"                  # fine fascia consentita (es. 07:00)
CONF_GSE_DOMENICA = "gse_domenica"        # domenica: tutto il giorno a potenza piena
CONF_GSE_HOLIDAY = "gse_holiday_entity"   # binary_sensor festivi (opzionale)
DEFAULT_GSE_WPA = 230.0
DEFAULT_GSE_KW_MAX = 6.0
DEFAULT_GSE_KW_RIDOTTA = 3.0
DEFAULT_GSE_START = "23:00"
DEFAULT_GSE_END = "07:00"
GSE_TOLERANCE = 1.10                     # tolleranza +10% sulla soglia (3/4.5 kW ok sforare)

# bilanciamento solare
CONF_BALANCE_GRID_SENSOR = "balance_grid_sensor"
CONF_BALANCE_BATTERY_SENSOR = "balance_battery_sensor"
CONF_BALANCE_INVERT_GRID = "balance_invert_grid"
CONF_BALANCE_INCLUDE_BATTERY = "balance_include_battery"
CONF_BALANCE_WPA = "balance_watts_per_amp"
CONF_BALANCE_BATTERY_SOC_SENSOR = "balance_battery_soc_sensor"
CONF_BATTERY_PRIORITY_MIN = "battery_priority_min"
DEFAULT_WPA = 230.0 * 3  # monofase 230 V ≈ 690 W/A
DEFAULT_MIN_AMPS = 6.0
DEFAULT_BATTERY_PRIORITY = 80.0
DEFAULT_MAX_AMPS = 16.0
DEFAULT_WB_START_W = 10.0  # soglia: avvia il contatore tempo sessione wallbox
DEFAULT_AVG_KMH = 30.0  # velocità media stimata per l'orario di partenza dei viaggi

# extra: meteo, CO2, scadenze
CONF_TEMP_ENTITY = "temp_entity"
CONF_CO2_ENABLED = "co2_comparison"
CONF_GEOCODE_ENABLED = "geocode_enabled"
CONF_AVG_KMH = "avg_speed_kmh"
CONF_CO2_THERMAL_GKM = "co2_thermal_gkm"
CONF_CO2_GRID_GKWH = "co2_grid_gkwh"
CONF_SCADENZE_ENABLED = "scadenze_enabled"
CONF_SCAD_BOLLO = "scadenza_bollo"
CONF_SCAD_REVISIONE = "scadenza_revisione"
CONF_SCAD_ASSICURAZIONE = "scadenza_assicurazione"
DEFAULT_CO2_THERMAL_GKM = 120.0
DEFAULT_CO2_GRID_GKWH = 300.0

# zona considerata ricarica fotovoltaico/BEB ("beb", nome della tua zona...)
CONF_SOLAR_ZONE = "solar_zone"

# zone extra con tariffa propria: {"box": 0.30, "casa_genitori": 0.25}.
# Restano "Pubblica" nelle statistiche, ma con il prezzo indicato.
CONF_ZONE_PRICES = "zone_prices"

# --- valori predefiniti -------------------------------------------------------
DEFAULT_NAME = "BYD"
DEFAULT_CAPACITY = 60.4
# Capacità di fabbrica (kWh) per modello: default modificabile nel wizard.
# Fonte: schede tecniche BYD Europa (valore nominale della batteria Blade).
# Le versioni con più taglie (Dolphin Surf, Seal, Seal U, Sealion 7, Tang)
# usano la variante più diffusa: la capacità resta modificabile dall'utente.
MODEL_CAPACITY: dict[str, float] = {
    "Dolphin Surf": 43.2,
    "Dolphin": 60.4,
    "Atto 2": 64.8,
    "Atto 3": 60.4,
    "Atto 3 EVO": 74.8,
    "Seal": 82.5,
    "Seal U": 87.0,
    "Sealion 7": 82.5,
    "Tang": 108.8,
}
# Alias usati per riconoscere il modello da device.model_name dell'integrazione.
MODEL_ALIASES: dict[str, tuple[str, ...]] = {
    "Dolphin Surf": ("dolphin surf", "dolphin mini", "seagull"),
    "Dolphin": ("dolphin",),
    "Atto 2": ("atto 2", "atto2"),
    "Atto 3 EVO": ("atto 3 evo", "atto3 evo"),
    "Atto 3": ("atto 3", "atto3"),
    "Seal U": ("seal u", "seal-u", "seal u dm"),
    "Seal": ("seal",),
    "Sealion 7": ("sealion 7", "sealion7"),
    "Tang": ("tang",),
}
DEFAULT_TARGET_SOC = 80.0
DEFAULT_PRICE_HOME = 0.25
DEFAULT_PRICE_PUBLIC = 0.45
DEFAULT_PRICE_SOLAR = 0.0
DEFAULT_EFFICIENCY = 0.90
DEFAULT_POLL_INTERVAL = 30
DEFAULT_TRIP_TIMEOUT = 20
DEFAULT_FUEL_CONSUMPTION = 6.5
DEFAULT_FUEL_PRICE = 2.00
DEFAULT_FUEL_LABEL = "Diesel"
DEFAULT_SOLAR_ZONE = "beb"

CHARGE_STATE_ON_VALUES = {"on", "charging", "charge_in_progress"}
WALLBOX_CHARGING_STATES = {"charging"}
# stati dell'entità plug_entity che significano "spina collegata" (BYD + comuni)
PLUG_CONNECTED_VALUES = {"connected", "completed", "plugged", "plugged_in",
                         "cable_connected", "on", "true", "1"}

# token nello stato della wallbox (CONF_WB_STATE) che significano "ricarica finita/ferma":
# chiudono la sessione ANCHE con la spina ancora collegata (utile alle colonnine pubbliche)
WALLBOX_FINISHED_TOKENS = ("finish", "charged", "complete", "full", "ended",
                           "stopped", "no_vehicle", "not_connected", "error", "fault",
                           # Lektrico: fine transazione / colonnina in attesa di
                           # autorizzazione. Senza queste la sessione non si chiudeva
                           # mai (spina "plugged" + wallbox need_auth = resta aperta).
                           "need_auth", "available", "idle", "ready", "paused")

# vampire drain: sotto questa velocita' di calo SoC (%/h) il calo e' "da fermo",
# sopra e' guida (il cloud BYD riporta l'odometro solo a motore spento)
VAMP_RATE_MAX = 1.0

TRIP_MIN_KM = 0.5
TRIP_MIN_MINUTES = 2

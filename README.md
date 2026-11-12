<p align="center">
  <img src="brand/logo.png" alt="BYD EV Center" width="320">
</p>

# BYD EV Center

<p align="left">
  <a href="https://github.com/Redrex85/BYD-EV-Center/releases"><img src="https://img.shields.io/github/v/release/Redrex85/BYD-EV-Center" alt="Release"></a>
  <img src="https://img.shields.io/badge/Home%20Assistant-2024.7%2B-41BDF5?logo=homeassistant" alt="HA">
</p>

**Viaggi, consumi, costi e ricariche per la tua BYD elettrica — direttamente in Home Assistant.**

Un *companion* per **Dolphin Surf, Dolphin, Atto 2, Atto 3, Atto 3 EVO, Seal, Seal U, Sealion 7 e Tang**, costruito sopra l'integrazione **[BYD Vehicle](https://github.com/jkaberg/hass-byd-vehicle)** (cloud DiLink): nessun account extra, nessun codice, nessun sensore da creare a mano. Installi da HACS, scegli le entità dalla lista, e via.

☕ Sostieni il progetto

BYD EV Center è un progetto gratuito e open source, portato avanti nel tempo libero. Se ti torna utile, puoi offrirmi un caffè per sostenere i prossimi aggiornamenti — grazie di cuore! ☕

<p align="left">
  <a href="https://www.paypal.me/lamortella"><img src="https://img.shields.io/badge/Dona-PayPal-00457C?logo=paypal" alt="PayPal"></a>
  <a href="https://www.buymeacoffee.com/redrex72v"><img src="https://img.shields.io/badge/Offrimi%20un%20caffè-BuyMeACoffee-FFDD00?logo=buy-me-a-coffee" alt="BuyMeACoffee"></a>
  <a href="https://t.me/redrex_domotica"><img src="https://img.shields.io/badge/Telegram-BYD%20EV%20Center-26A5E4?logo=telegram" alt="Telegram"></a>
</p>

> 🇬🇧 [English below](#-english)

---

## ✨ Cos'è

L'integrazione **BYD Vehicle** ti dà i numeri grezzi (% batteria, autonomia, odometro, stato porte). **BYD EV Center** li trasforma in quello che manca:

| | |
|---|---|
| 🚘 **Pagina BYD Veicolo** | Modello, VIN, connessione, blocco, porte, finestrini, veicolo acceso, temperature abitacolo/esterna, potenza batteria, tempo di ricarica residuo, consumi e pressioni pneumatici — con link `more-info` a ogni entità BYD |
| 🛣️ **Viaggi automatici** | Rileva ogni spostamento dall'odometro, calcola km, batteria consumata, kWh ed efficienza (kWh/100km), chiude il viaggio da solo dopo la sosta, con **costo stimato** e **fonte dell'ultima ricarica** prima della partenza |
| ⚡ **Ricariche** | Sessioni con energia wallbox (AC) misurata, SoC iniziale→finale, durata, tipo (Casa/Fotovoltaico/Pubblica) e costo reale |
| 🔌 **Wallbox** | Pagina dedicata: stato live, potenza, corrente, tensione, temperatura e motivo limite; **tempo e kWh di sessione** (con contatore interno di riserva); **limite di carica in A**; **avvio e stop carica** con entità mappabili in configurazione; **bilanciamento solare** a inseguimento del surplus |
| 🔋 **Surplus batteria (anche di notte)** | L'auto carica dalla **batteria di casa**: il bilanciamento somma la **scarica della batteria** al surplus e regola gli ampere della wallbox per tenere il prelievo da rete ~0 — di notte l'auto **segue la batteria, non la rete** |
| 🔎 **Lista ricariche filtrabile** | Filtri per tipo e periodo (settimana/mese/anno/tutto) con **somma automatica** di kWh e € |
| 💰 **Costi veri** | €/km, €/100km, costo ricariche giorno/settimana/mese/anno/totale, prezzi separati per casa/colonnina/fotovoltaico modificabili **dalla dashboard** |
| 📊 **Statistiche e report** | Contatori con `last_period` (come utility_meter), tabelle **Generale/Settimanale/Mensile**, storico 365 giorni, report mensile |
| 🔋 **Stime ricarica** | Tempo residuo, ora di completamento prevista, energia mancante e costo stimato verso il tuo % obiettivo |
| 🌿 **Risparmio vs termica** | Quanti euro hai risparmiato rispetto alla tua vecchia diesel/benzina (totale, mese, anno) |
| 💚 **Salute batteria** | Efficienza di ricarica (mai >100%), **energia dispersa**, breakdown rete/batteria, SOH stimato dalle ricariche e **SOH ufficiale**, kWh per 1% |
| 🔧 **Manutenzione** | Registro tagliandi con spesa reale, prossimo tagliando **a scelta per km o data**, **assicurazione** con rinnovo +6 mesi/+1 anno/data e costo annuo |
| 🤖 **Automazioni integrate** | Notifica avvio/fine ricarica (con kWh, SoC e costo), **promemoria batteria bassa** a casa (% e fascia oraria), **carica programmata** via wallbox (per orario **o** percentuale) — tutto on/off e regolabile dalla vista Automazioni |
| 🖼️ **Installazione guidata** | Scelta del **modello** (imposta la foto dell'auto) e **dashboard creata automaticamente** nella barra laterale con tutte le viste già configurate |
| 🔍 **Rilevamento automatico** | Legge l'entity registry dell'integrazione BYD e mappa le entità tramite `translation_key`: funziona in ogni lingua e con qualsiasi nome del device |
| 📈 **Pagina Extra** | Grafici di analisi: trend mensile kWh/100km, efficienza per zona, vampire drain + costo €/mese, risparmio vs termica, orario di partenza, range reale vs dichiarato |
| 📍 **Cronologia posizione** | Timeline dei cambi di zona (In casa / Lavoro / Non disponibile) con orario, dentro il pannello |

Tutto è calcolato **localmente nel tuo Home Assistant** e salvato in `.storage` (persistente tra riavvii). Niente pyscript, niente package YAML, niente utility_meter da configurare a mano.

## 📦 Requisiti

1. Home Assistant **2024.7+**
2. L'integrazione **[BYD Vehicle](https://github.com/jkaberg/hass-byd-vehicle)** installata e configurata (almeno una vettura BYD visibile in HA)
3. *(Opzionale)* Una wallbox integrata in HA: Wallbox, go-e, Easee, Zappi, OCPP, Shelly EM dedicato…

> ⚠️ **Fortemente consigliato**: in Home Assistant definisci **almeno la zona Casa**
> (Impostazioni → **Zone** → nome `Casa` + latitudine/longitudine) e configura il
> **tracker GPS dell'auto**. Senza la zona `home` l'integrazione **non distingue una
> ricarica a casa da una colonnina pubblica**: tutto finisce come *Pubblica*, i prezzi
> casa/fotovoltaico non si applicano e le statistiche di costo si sbagliano.

> ⚠️ **Alcuni valori si popolano solo guidando**: viaggi, kWh/100km, efficienza per
> zona, orario di partenza, range reale, storico mensile e risparmi restano vuoti finché
> l'auto non percorre **qualche decina di km** con l'integrazione attiva. Subito dopo
> l'installazione è normale vedere ancora `—`.

> Funziona anche senza wallbox: le ricariche pubbliche vengono stimate dal delta SoC e puoi registrarle a mano col servizio `add_manual_charge`.

## 🔧 Installazione

### Via HACS (consigliato)

1. **HACS** → **Integrazioni** → menu ⋮ → **Repository personalizzati**
2. Aggiungi `https://github.com/Redrex85/BYD-EV-Center` come categoria **Integration**
3. Apri la scheda → **Scarica**
4. **Riavvia Home Assistant**
5. **Impostazioni → Dispositivi e servizi → Aggiungi integrazione → "BYD EV Center"**

> ⚠️ **Dopo aver aggiunto l'integrazione a volte la dashboard non si apre**: la prima volta che apri il
> pannello può risultare vuoto o non caricato. **Riavvia nuovamente Home Assistant** (una seconda volta)
> e ricarica la pagina con **Ctrl+Shift+R**. Serve perché la dashboard e le risorse vengono registrate
> durante il setup e HA ha bisogno di un ciclo completo per servirle.

### Manuale

Copia la cartella `custom_components/byd_ev_center/` dentro `<config>/custom_components/`, riavvia e aggiungi l'integrazione dal menu.

## 🧙 Configurazione (3 schermate)

### 0️⃣ Il profilo

La **prima schermata** chiede il **profilo**: decide quali sezioni del wizard e quali pagine del pannello avrai. Scegli in base a cosa possiedi:

| Profilo | Per chi | Cosa include | Cosa devi inserire |
|---|---|---|---|
| **Base** | solo l'auto | auto, viaggi, statistiche, ricariche (anche **pubbliche**), risparmi, **manutenzione e bollo**, **notifiche**, **confronto carburante** e **avanzate** | nome auto + entità BYD (schermata 1️⃣) |
| **Pro** | auto **+ wallbox** | tutto il Base **+ wallbox** (avvio/stop, potenza, sessione, GSE) | Base **+ schermata 2️⃣** (wallbox) |
| **Enterprise** | auto + wallbox **+ fotovoltaico** | tutto il Pro **+ fotovoltaico** e bilanciamento solare | Pro **+ sensori rete/batteria** della sezione *Fotovoltaico* |

- **Base** → la **pagina Wallbox non compare** nel pannello; tutte le altre sì.
- **Pro / Enterprise** → compaiono anche le schermate della **wallbox** e (solo Enterprise) del **fotovoltaico**.
- Cambi idea? Si può cambiare quando vuoi da ⚙️ **Integrazioni → BYD EV Center → Configura**.

### 1️⃣ L'auto

Dai un nome breve all'auto (es. `Dolphin Surf`) — diventa il prefisso di tutte le entità create (`sensor.dolphin_surf_…`). Poi seleziona il **modello** (imposta foto e capacità batteria) e conferma le entità proposte:

| Campo | Entità tipica dell'integrazione BYD Vehicle |
|---|---|
| Modello | Dolphin Surf, Dolphin, Atto 2/3/3 EVO, Seal, Seal U, Sealion 7, Tang — oppure `Auto` per leggerlo dal cloud |
| Crea dashboard | Crea da sola la plancia laterale con tutte le viste |
| Odometro | `total_mileage` |
| Batteria (%) | `elec_percent` |
| Autonomia | `endurance_mileage` / `ev_endurance` |
| In carica | `is_charging` |
| Spina (opz.) | `is_charger_connected` |
| GPS (opz.) | `location` |
| Dati BYD (auto) | connessione, blocco, porte, finestrini, veicolo acceso, temperature, potenza batteria, tempo di ricarica, consumi, pneumatici, VIN |

> 🔍 **Rilevamento automatico**: le entità vengono cercate per `translation_key` nella entity registry, non per nome. Se un campo resta vuoto puoi comunque sceglierlo a mano dalla lista.

> 🛣️ **Chilometri all'attivazione**: da dove parte il confronto "da installazione". `0` = dal **giorno in cui installi l'integrazione**; `1` = dall'**inizio della vita dell'auto** (km 0); auto **usata** → metti i **km alla data d'acquisto**.

### 2️⃣ La wallbox e le impostazioni

Attiva l'interruttore se hai una wallbox in HA e mappa i sensori:

| Campo | Esempi |
|---|---|
| Potenza istantanea | `sensor.wallbox_instant_power` (W o kW — conversione automatica) |
| Stato wallbox | `sensor.wallbox_charger_state` (cerca lo stato tipo *charging*) |
| Contatore energia sessione | kWh della sessione corrente |
| Contatore energia totale | kWh totali erogati (usato se manca quello di sessione) |
| Avvio/stop carica (per l'automazione) | switch o button della wallbox |
| Target di carica (fallback stop) | `number.*charge_target` |

Nella schermata **Impostazioni**: capacità batteria (precompilata dal modello, es. **43,2 kWh** per Dolphin Surf), % obiettivo ricarica, prezzi **casa/colonnina/fotovoltaico**, nome della zona FV (es. `beb`), intervallo aggiornamento, minuti di timeout viaggi e confronto opzionale con auto termica.

> 🇮🇹 **Prezzo carburante in tempo reale (Italia)**: nel campo *sensore prezzo carburante* puoi usare l'integrazione HACS [`nuggetz/ha-fuel-prices-ita`](https://github.com/nuggetz/ha-fuel-prices-ita), che espone i prezzi dei distributori italiani. Il confronto userà il prezzo salvato **giorno per giorno**, così le oscillazioni non riscrivono i periodi passati.

### ☀️ Ricariche dal fotovoltaico e risparmi

Con il profilo **Enterprise** mappa il **sensore rete** (e, se hai la batteria di casa, il **sensore batteria**) nella sezione *Fotovoltaico*. Ogni ricarica a casa viene ripartita per **sorgente**: prima la **rete** (la quota che **paghi**), poi la **batteria di casa**, il resto è **fotovoltaico** (gratis). Il costo della ricarica conta quindi **solo la quota prelevata dalla rete**.

**Risparmi**: il confronto con l'auto termica usa i **km** (lato termico) e il **costo effettivamente pagato** (lato elettrico). Se carichi al 100% da FV a costo `0`, il costo elettrico è `0` → il risparmio è l'**intero** carburante evitato.

⚠️ **Ricariche fatte prima dell'installazione**: dichiara **solo** i kWh **pagati** (colonnine/rete). **Non** inserire i kWh caricati dal tuo fotovoltaico: sono gratis e conteggiarli come spesa **ridurrebbe** il risparmio.

## 📈 Cosa crea

Oltre **90 entità** sul dispositivo *"BYD EV Center"* (prefisso = nome scelto), più i nuovi sensori BYD:

```
Sensori      Km G/S/M/A (+last_period) · Energia Caricata G/S/M/A/Tot · Costo Ricarica G/S/M/A/Tot
             Km per kWh · kWh/100km · Costo/km · Costo/100km · kWh Totali · %/100km
             Batteria kWh · % Caricata/Scaricata Oggi · Energia Batteria (periodi)
             Tempo/Completamento/Costo Ricarica · Tipo Ricarica · Ultima Ricarica · Ricariche
             Trip Attivo · Km/Durata Trip · Ultimo Trip · Viaggi Oggi
             Statistiche Viaggi · Archivio · Percorrenza · Report Generale
             Efficienza Ricarica · Perdite · kWh per 1% · SOH Stimato · Risparmi · CO2
             Tagliandi · Vampire Drain · Consumo per Zona · Scadenze · Viaggio Top/Stop
             Veicolo BYD · Potenza Batteria · Consumo Medio · Consumo 50 km
             Tempo Ricarica Residuo · Temp. Abitacolo · Temp. Esterna · Pressioni Pneumatici
Binary       In Carica · Wallbox in Carica · BYD Connessa · BYD Bloccata · Porte Aperte
             Finestrini Aperti · Veicolo Acceso
Switch       Notifica Avvio/Fine Ricarica · Promemoria Batteria Bassa · Carica Programmata
Number       Costo Casa/Colonnina/FV · Capacità · Obiettivo Ricarica · SOH Ufficiale
             Costo Assicurazione · % Promemoria · % Avvio/Stop Carica
Time         Promemoria Inizio/Fine · Carica Orario Avvio/Stop
Select       Filtro Tipo/Periodo/Anno Ricariche
Pulsanti     Chiudi Viaggio · Esporta CSV · Reset Km/Energia/Costi
```

## 🎛️ Dashboard incluse (create automaticamente)

Alla configurazione viene creata **da sola** la dashboard laterale con tutte le viste
(opzione disattivabile; servizio `byd_ev_center.create_dashboard` per ricrearla):

| Vista | Contenuto |
|---|---|
| Panoramica | Foto auto, batteria, efficienza, comandi BYD, mappa, box Risparmi |
| BYD Veicolo | Modello, VIN, connessione, blocco, porte/finestrini, temperature, potenza, pneumatici |
| Viaggi | Albero Anno→Mese→Giorno + dettaglio con spesa e verifica GPS |
| Statistiche | Tile totali, percorrenza, ricariche differenziate, anno→mese + grafici |
| Ricariche | Filtri tipo/periodo/**anno**, lista stile app (Δ%, ØkW), tabelle G/S/M |
| Wallbox | Stato live, potenza, sessione, bilanciamento casa/GSE/fotovoltaico |
| Salute batteria | SOH ufficiale (inline) e stimato, rete/batteria/dispersa |
| Manutenzione | Tagliandi (km o data) + Assicurazione (rinnovi, costo) |
| Risparmi | Carburante, tagliandi, bollo, netto, FV |
| Extra | Vampire drain, rotte, meteo, CO₂, scadenze, top&stop, Energy Dashboard |
| Automazioni | Interruttori + % e orari delle automazioni integrate |
| Impostazioni | Prezzi, batteria, reset, export |

Card custom opzionali (HACS → Frontend), usate **solo** dalle dashboard YAML in `dashboards/`:
**apexcharts-card** e **mini-graph-card**.
Il pannello laterale (`byd-ev-center-panel.js`) **non ne ha bisogno**: disegna tutto da sé.
La foto dell'auto viene scelta dal modello nel wizard.

> Se la tua auto non si chiama "Dolphin Surf", sostituisci `sensor.dolphin_surf_` con il prefisso giusto.

In [`examples/automazioni_esempio.yaml`](examples/automazioni_esempio.yaml) trovi notifiche pronte: ricarica completata, batteria bassa fuori casa, riassunto serale.

## 🛠️ Servizi

```yaml
# Chiude subito il viaggio in corso
service: byd_ev_center.close_trip

# Azzera contatori (scope: km | energia | costi | viaggi | ricariche | all)
service: byd_ev_center.reset_counters
data: { scope: km }

# Registra una ricarica pubblica non misurata dalla wallbox
service: byd_ev_center.add_manual_charge
data: { kwh: 24.8, costo: 11.90, tipo: Pubblica }

# Esporta tutti i viaggi in CSV (config/byd_ev_center_export/)
service: byd_ev_center.export_trips_csv

# Backup completo in un JSON: viaggi, ricariche, storico, contatori, manutenzione
service: byd_ev_center.export_data

# Ripristina quel JSON su questa installazione (sostituisce tutto, nessuna fusione)
service: byd_ev_center.import_data
data: { path: /config/byd_ev_center_export/byd_ev_center_data_20261112_120000.json }

# Prezzi per zona: le ricariche che iniziano in quelle zone usano quel prezzo
service: byd_ev_center.set_charge_zones
data: { zones: [{ zone: box, price: 0.30 }, { zone: ufficio, price: 0.45 }] }

# (Ri)crea la dashboard laterale con tutte le viste
service: byd_ev_center.create_dashboard

# Personalizza i testi delle notifiche
service: byd_ev_center.set_notify_texts
data: { texts: { cc_title: "🔋 Carica finita" } }

# Manutenzione e assicurazione
service: byd_ev_center.add_maintenance
data: { data: "2026-08-20", km: 68718, costo: 85, tipo: "Tagliando" }
service: byd_ev_center.renew_insurance
data: { mesi: 12 }

# Scadenze e tagliando
service: byd_ev_center.set_scadenza
data: { nome: bollo, data: "2026-10-12" }
service: byd_ev_center.set_tagliando
data: { mode: km, valore: "71218" }
```

## ❓ FAQ

**Come viene calcolato il tempo di viaggio?** Il viaggio si apre quando l'odometro aumenta e si chiude **dopo ~20 minuti senza movimenti**, quando l'auto si spegne e odometro/posizione si aggiornano (il cloud BYD ha qualche minuto di ritardo). La durata registrata va dall'inizio all'**ultimo movimento rilevato**: la sosta post-viaggio non viene conteggiata.

**Le entità BYD non vengono rilevate.** Verifica che `byd_vehicle` sia configurata e che le entità non siano disabilitate; poi riapri **Configura → Opzioni** e controlla la sezione **Dati BYD**. Il rilevamento usa `translation_key`, quindi funziona anche con nomi in italiano o in inglese.

**I sensori BYD restano "non disponibili" a volte.** È normale: il cloud DiLink aggiorna lentamente e alcuni valori dipendono dal modello e dalla versione software. Le entità mancanti restano vuote senza bloccare il pannello.

**Le entità hanno ID diversi da quelli delle dashboard?** Le dashboard usano il prefisso del nome che hai dato all'auto in minuscolo. Rinomina l'entry o cerca/sostituisci nei file YAML.

**Posso avere due auto?** Sì: aggiungi una seconda istanza dell'integrazione con un altro nome.

**Dove sono i miei dati?** In `.storage/byd_ev_center.<entry_id>` — restano tuoi, nessun invio esterno.

Hai un'idea? Apri una issue!

## 🤝 Crediti e disclaimer

- Ispirato a [Renault EV Center](https://github.com/Redrex85/Renault-EV-Center-Home-Assistant), a [LeapMotor Mate](https://github.com/ProtossBlaster/leapmotor-mate) e a TeslaMate.
- Richiede l'[integrazione BYD Vehicle](https://github.com/jkaberg/hass-byd-vehicle) (progetto indipendente).
- Foto dei modelli: [BYD-CARD](https://github.com/moshiko2312/BYD-CARD) (MIT).
- Progetto **non ufficiale**, non affiliato a BYD. I dati dipendono dall'affidabilità dei sensori che configuri.

Licenza: **MIT** — vedi [LICENSE](LICENSE).

---

# 🇬🇧 English

**Trips, consumption, costs and charging for your BYD EV — fully inside Home Assistant.**

A companion for **Dolphin Surf, Dolphin, Atto 2, Atto 3, Atto 3 EVO, Seal, Seal U, Sealion 7 and Tang**, built on top of the **[BYD Vehicle](https://github.com/jkaberg/hass-byd-vehicle)** integration (DiLink cloud). No extra accounts, no code, no hand-made sensors: install from HACS, pick your entities from dropdowns, done.

☕ Support

BYD EV Center is a free, open-source project kept alive in my spare time. If it saves you time, you can buy me a coffee to support the next updates — thank you so much! ☕

<p align="left">
  <a href="https://www.paypal.me/lamortella"><img src="https://img.shields.io/badge/Donate-PayPal-00457C?logo=paypal" alt="PayPal"></a>
  <a href="https://www.buymeacoffee.com/redrex72v"><img src="https://img.shields.io/badge/Buy%20me%20a%20coffee-BuyMeACoffee-FFDD00?logo=buy-me-a-coffee" alt="BuyMeACoffee"></a>
  <a href="https://t.me/redrex_domotica"><img src="https://img.shields.io/badge/Telegram-BYD%20EV%20Center-26A5E4?logo=telegram" alt="Telegram"></a>
</p>

> 🇮🇹 [Versione italiana in alto](#-cosè)

## ✨ What it is

The **BYD Vehicle** integration gives you the raw numbers (battery %, range, odometer, door state). **BYD EV Center** turns them into what's missing:

| | |
|---|---|
| 🚘 **BYD Vehicle page** | Model, VIN, connection, lock, doors, windows, vehicle on, cabin/outside temperature, battery power, remaining charge time, consumption and tire pressures — with `more-info` links to every BYD entity |
| 🛣️ **Automatic trips** | Detects every move from the odometer, computes km, battery used, kWh and efficiency (kWh/100km), auto-closes the trip after the stop, with **estimated cost** and the **source of the last charge** before departure |
| ⚡ **Charges** | Sessions with measured wallbox (AC) energy, initial→final SoC, duration, type (Home/Solar/Public) and real cost |
| 🔌 **Wallbox** | Dedicated page: live state, power, current, voltage, temperature and limit reason; **session time & kWh** (with internal fallback counter); **charge limit in A**; **start and stop charging** with entities mapped in the config flow; **solar balancing** that follows your surplus |
| 🔋 **Battery surplus (even at night)** | The car charges from the **home battery** — the balancing adds the **battery discharge** to the surplus and keeps grid import ~0, so at night the car **follows the battery, not the grid** |
| 🔎 **Filterable charge list** | Filters by type and period (week/month/year/all) with **automatic** kWh and € totals |
| 💰 **Real costs** | €/km, €/100km, charge cost per day/week/month/year/all-time, separate home/public/solar tariffs editable **from the dashboard** |
| 📊 **Statistics and reports** | Meters with `last_period` (utility_meter style), **General/Weekly/Monthly** tables, 365-day history, monthly report |
| 🔋 **Charge estimates** | Time remaining, expected completion time, missing energy and estimated cost toward your target % |
| 🌿 **Savings vs combustion** | How many euros you saved against your old diesel/petrol car (total, month, year) |
| 💚 **Battery health** | Charging efficiency (never >100%), **energy lost**, grid/battery breakdown, SOH estimated from charges and **official SOH**, kWh per 1% |
| 🔧 **Maintenance** | Service log with real spend, next service **by km or date**, **insurance** with +6 months/+1 year/date renewal and yearly cost |
| 🤖 **Built-in automations** | Charge start/finish notification (with kWh, SoC and cost), **low-battery reminder** at home (% and time window), **scheduled charging** via wallbox (by time **or** percentage) |
| 🖼️ **Guided setup** | Car **model** selection (sets the car photo) and **auto-created dashboard** in the sidebar with all views ready |
| 🔍 **Auto-detection** | Reads the BYD integration's entity registry and maps entities by `translation_key`: works in any language and with any device name |
| 📈 **Extra page** | Analysis charts: monthly kWh/100km trend, efficiency per zone, vampire drain + monthly charge cost, savings vs combustion, departure time, real vs declared range |
| 📍 **Position history** | Timeline of zone changes (Home / Work / Unavailable) with times, inside the panel |

Everything is computed **locally in your Home Assistant** and saved to `.storage` (persistent across restarts). No pyscript, no YAML packages, no utility_meter to wire by hand.

## 📦 Requirements

1. Home Assistant **2024.7+**
2. The **[BYD Vehicle](https://github.com/jkaberg/hass-byd-vehicle)** integration configured (with your BYD vehicle linked)
3. *(Optional)* A wallbox integrated into HA: Wallbox, go-e, Easee, Zappi, OCPP, dedicated Shelly EM…

> ⚠️ **Strongly recommended: at least the Home zone.** In HA go to **Settings → Zones**
> and make sure a `Home` zone exists (correct latitude/longitude) with the **car GPS
> tracker** inside it. Without the `home` zone the integration **cannot tell a home
> charge from a public charger**: everything is logged as *Public* and the home/solar
> prices never apply, so the cost statistics are wrong.

> ⚠️ **Some values only populate after driving**: trips, kWh/100km, per-zone efficiency,
> departure time, real range, monthly history and savings stay empty until the car has
> covered **a few tens of km** with the integration active. Seeing `—` right after
> install is normal.

> Works without a wallbox too: public charges are estimated from the SoC delta and you can log them manually with the `add_manual_charge` service.

## 🔧 Installation

### Via HACS (recommended)

1. **HACS** → **Integrations** → ⋮ menu → **Custom repositories**
2. Add `https://github.com/Redrex85/BYD-EV-Center` with category **Integration**
3. Open the card → **Download**
4. **Restart Home Assistant**
5. **Settings → Devices & Services → Add Integration → "BYD EV Center"**

> ⚠️ **After adding the integration the dashboard sometimes doesn't open**: the first time
> you open the panel it may look empty or unloaded. **Restart Home Assistant again**
> (a second time) and reload the page with **Ctrl+Shift+R**. The dashboard and its
> resources are registered during setup and HA needs a full cycle to serve them.

### Manual

Copy the `custom_components/byd_ev_center/` folder into `<config>/custom_components/`, restart and add the integration from the menu.

## 🧙 Setup (3 screens)

### 0️⃣ The profile

The **first screen** asks for the **profile**: it decides which wizard sections and which panel pages you get. Pick it based on what you own:

| Profile | For | Includes | You fill in |
|---|---|---|---|
| **Base** | car only | car, trips, statistics, charges (including **public**), savings, **maintenance and road tax**, **notifications**, **fuel comparison** and **advanced** | car name + BYD entities (screen 1️⃣) |
| **Pro** | car **+ wallbox** | all of Base **+ wallbox** (start/stop, power, session, GSE) | Base **+ screen 2️⃣** (wallbox) |
| **Enterprise** | car + wallbox **+ solar** | all of Pro **+ solar** and solar balancing | Pro **+ grid/battery sensors** from the *Solar* section |

- **Base** → the **Wallbox page is hidden** in the panel; every other page shows.
- **Pro / Enterprise** → the **wallbox** screen appears too, plus **solar** (Enterprise only).
- Changed your mind? Switch any time from ⚙️ **Settings → Devices & Services → BYD EV Center → Configure**.

### 1️⃣ The car

Give the car a short name (e.g. `Dolphin Surf`) — it becomes the prefix of every created entity (`sensor.dolphin_surf_…`). Then select the **model** (sets the car photo and battery capacity) and confirm the suggested entities:

| Field | Typical BYD Vehicle integration entity |
|---|---|
| Model | Dolphin Surf, Dolphin, Atto 2/3/3 EVO, Seal, Seal U, Sealion 7, Tang — or `Auto` to read it from the cloud |
| Create dashboard | Builds the sidebar dashboard with all views |
| Odometer | `total_mileage` |
| Battery (%) | `elec_percent` |
| Range | `endurance_mileage` / `ev_endurance` |
| Charging | `is_charging` |
| Plug (opt.) | `is_charger_connected` |
| GPS (opt.) | `location` |
| BYD data (auto) | connection, lock, doors, windows, vehicle on, temperatures, battery power, charge time, consumption, tires, VIN |

> 🔍 **Auto-detection**: entities are matched by `translation_key` in the entity registry, not by name. If a field stays empty you can always pick it manually from the list.

> 🛣️ **Kilometres at activation**: where the "since install" comparison starts. `0` = from the **day you install the integration**; `1` = from the **car's birth** (km 0); **used** car → set the **km at the purchase date**.

### 2️⃣ The wallbox and settings

Flip the switch if you have a wallbox in HA and map the sensors:

| Field | Examples |
|---|---|
| Instant power | `sensor.wallbox_instant_power` (W or kW — auto conversion) |
| Wallbox state | `sensor.wallbox_charger_state` (look for a *charging*-like state) |
| Session energy counter | kWh of the current session |
| Total energy counter | Total kWh delivered (used when the session counter is missing) |
| Start/stop charging (for automations) | wallbox switch or button |
| Charge target (stop fallback) | `number.*charge_target` |

In the **Settings** screen: battery capacity (pre-filled from the model, e.g. **43.2 kWh** for Dolphin Surf), target charge %, **home/public/solar** prices, solar zone name (e.g. `beb`), update interval, trip timeout minutes and optional comparison with a combustion car.

### ☀️ Solar charging & savings

With the **Enterprise** profile, map the **grid sensor** (and, if you have a home battery, the **battery sensor**) in the *Solar* section. Each home charge is split by **source**: first the **grid** (the part you **pay**), then the **home battery**, the rest is **solar** (free). The charge cost therefore counts **only the grid-drawn part**.

**Savings**: the combustion comparison uses **km** (thermal side) and the **cost actually paid** (electric side). If you charge 100% from solar at `0`, the electric cost is `0` → the saving is the **full** avoided fuel cost.

⚠️ **Charges made before installing**: declare **only** the kWh you **paid** (public/grid). **Do not** enter kWh charged from your own solar: they are free, and counting them as an expense would **reduce** the saving.

## 📈 What it creates

Over **90 entities** on the *"BYD EV Center"* device (prefix = the name you chose), plus the BYD sensors:

```
Sensors    Km D/W/M/Y (+last_period) · Energy Charged D/W/M/Y/Total · Charge Cost D/W/M/Y/Total
           Km per kWh · kWh/100km · Cost/km · Cost/100km · Total kWh · %/100km
           Battery kWh · % Charged/Discharged Today · Battery Energy (periods)
           Charge Time/Completion/Cost · Charge Type · Last Charge · Charges
           Active Trip · Trip Km/Duration · Last Trip · Trips Today
           Trip Statistics · Archive · Mileage · General Report
           Charge Efficiency · Losses · kWh per 1% · Estimated SOH · Savings · CO2
           Services · Vampire Drain · Consumption per Zone · Deadlines · Top/Stop Trip
           BYD Vehicle · Battery Power · Average Consumption · Last 50 km Consumption
           Remaining Charge Time · Cabin Temp · Outside Temp · Tire Pressures
Binary     Charging · Wallbox Charging · BYD Online · BYD Locked · Doors Open
           Windows Open · Vehicle On
Switch     Charge Start/Finish Notification · Low Battery Reminder · Scheduled Charging
Number     Home/Public/Solar Price · Capacity · Charge Target · Official SOH
           Insurance Cost · Reminder % · Start/Stop Charge %
Time       Reminder Start/End · Scheduled Charge Start/Stop
Select     Charge Type/Period/Year Filter
Buttons    Close Trip · Export CSV · Reset Km/Energy/Costs
```

## 🎛️ Included dashboards (created automatically)

On setup the sidebar dashboard is **created for you** with every view
(disableable; service `byd_ev_center.create_dashboard` to rebuild it):

| View | Contents |
|---|---|
| Overview | Car photo, battery, efficiency, BYD controls, map, Savings box |
| BYD Vehicle | Model, VIN, connection, lock, doors/windows, temperatures, power, tires |
| Trips | Year→Month→Day tree with cost detail and GPS check |
| Statistics | Total tiles, mileage, split charges, year→month + charts |
| Charges | Type/period/**year** filters, app-style list (Δ%, ØkW), D/W/M tables |
| Wallbox | Live state, power, session, home/GSE/solar balancing |
| Battery health | Official SOH (inline) and estimated, grid/battery/lost |
| Maintenance | Services (km or date) + Insurance (renewals, cost) |
| Savings | Fuel, services, road tax, net, solar |
| Extra | Vampire drain, routes, weather, CO₂, deadlines, top&stop, Energy Dashboard |
| Automations | Switches + % and times of the built-in automations |
| Settings | Prices, battery, reset, export |

Optional custom cards (HACS → Frontend), used **only** by the YAML dashboards in `dashboards/`:
**apexcharts-card** and **mini-graph-card**.
The side panel (`byd-ev-center-panel.js`) **doesn't need them**: it draws everything itself.
The car photo comes from the model chosen in the wizard.

> If your car isn't called "Dolphin Surf", replace `sensor.dolphin_surf_` with the right prefix.

[`examples/automazioni_esempio.yaml`](examples/automazioni_esempio.yaml) has ready notifications: charge finished, low battery away from home, evening summary.

## 🛠️ Services

```yaml
# Closes the current trip immediately
service: byd_ev_center.close_trip

# Resets meters (scope: km | energia | costi | viaggi | ricariche | all)
service: byd_ev_center.reset_counters
data: { scope: km }

# Logs a public charge not measured by the wallbox
service: byd_ev_center.add_manual_charge
data: { kwh: 24.8, costo: 11.90, tipo: Pubblica }

# Exports all trips to CSV (config/byd_ev_center_export/)
service: byd_ev_center.export_trips_csv

# Full backup in one JSON: trips, charges, daily history, counters, maintenance
service: byd_ev_center.export_data

# Restores that JSON on this installation (replaces everything, no merge)
service: byd_ev_center.import_data
data: { path: /config/byd_ev_center_export/byd_ev_center_data_20261112_120000.json }

# Per-zone prices: charges starting in these zones use that price
service: byd_ev_center.set_charge_zones
data: { zones: [{ zone: box, price: 0.30 }, { zone: office, price: 0.45 }] }

# (Re)creates the side dashboard with all views
service: byd_ev_center.create_dashboard

# Customize notification texts
service: byd_ev_center.set_notify_texts
data: { texts: { cc_title: "🔋 Charge finished" } }

# Maintenance and insurance
service: byd_ev_center.add_maintenance
data: { data: "2026-08-20", km: 68718, costo: 85, tipo: "Service" }
service: byd_ev_center.renew_insurance
data: { mesi: 12 }

# Deadlines and service
service: byd_ev_center.set_scadenza
data: { nome: bollo, data: "2026-10-12" }
service: byd_ev_center.set_tagliando
data: { mode: km, valore: "71218" }
```

## ❓ FAQ

**How is the trip duration calculated?** The trip opens when the odometer increases and closes **after ~20 minutes without movement**, when the car turns off and odometer/position update (the BYD cloud is a few minutes behind). The recorded duration runs from the start to the **last movement detected**: the post-trip stop isn't counted.

**BYD entities are not detected.** Make sure `byd_vehicle` is configured and its entities are not disabled; then reopen **Configure → Options** and check the **BYD data** section. Detection uses `translation_key`, so it works with Italian or English names alike.

**BYD sensors stay "unavailable" sometimes.** Normal: the DiLink cloud updates slowly and some values depend on the model and software version. Missing entities stay empty without breaking the panel.

**Entity IDs don't match the dashboards?** The dashboards use the lowercased name prefix you gave the car. Rename the entry or find/replace in the YAML files.

**Can I have two cars?** Yes: add a second instance of the integration with a different name.

**Where is my data?** In `.storage/byd_ev_center.<entry_id>` — it stays yours, nothing is sent anywhere.

Got an idea? Open an issue!

## 🤝 Credits and disclaimer

- Inspired by [Renault EV Center](https://github.com/Redrex85/Renault-EV-Center-Home-Assistant), [LeapMotor Mate](https://github.com/ProtossBlaster/leapmotor-mate) and TeslaMate.
- Requires the **[BYD Vehicle](https://github.com/jkaberg/hass-byd-vehicle)** integration (independent project).
- Model photos: [BYD-CARD](https://github.com/moshiko2312/BYD-CARD) (MIT).
- **Unofficial** project, not affiliated with BYD. Data quality depends on the sensors you configure.

License: **MIT** — see [LICENSE](LICENSE).

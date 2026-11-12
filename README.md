# BYD EV Center

<p align="center">
  <img src="brand/icon.png" alt="BYD EV Center" width="140">
</p>

<p align="center">
  <a href="https://github.com/hacs/integration"><img alt="HACS" src="https://img.shields.io/badge/HACS-Custom-41BDF5.svg"></a>
  <a href="https://github.com/Redrex85/BYD-EV-Center/actions/workflows/validate.yml"><img alt="Validate" src="https://github.com/Redrex85/BYD-EV-Center/actions/workflows/validate.yml/badge.svg"></a>
  <a href="https://github.com/Redrex85/BYD-EV-Center/releases"><img alt="Release" src="https://img.shields.io/github/v/release/Redrex85/BYD-EV-Center"></a>
  <a href="LICENSE"><img alt="License" src="https://img.shields.io/badge/License-MIT-yellow.svg"></a>
</p>

**BYD EV Center** trasforma i dati della tua auto elettrica BYD in un centro di
controllo completo per Home Assistant: dashboard dedicata, pannello laterale,
viaggi, ricariche, costi, risparmi e salute della batteria.

I dati dell'auto non vengono duplicati: l'integrazione legge le entità create da
[`hass-byd-vehicle`](https://github.com/jkaberg/hass-byd-vehicle) (cloud DiLink)
e le rielabora.

## Caratteristiche

- **Pagina BYD Veicolo** con modello, VIN, connessione, blocco, porte,
  finestrini, veicolo acceso, temperature, potenza batteria, tempo di ricarica
  residuo, consumi e pressioni pneumatici.
- **Dashboard automatica** nella barra laterale + pannello `byd-ev-center-panel`.
- **Viaggi** rilevati da odometro e spostamenti, con storico giorno/mese.
- **Ricariche** AC/DC con energia, costi per zona/tariffa e fusione delle
  sessioni spezzate.
- **Wallbox** (opzionale): potenza, sessione, bilanciamento casa, GSE e
  fotovoltaico.
- **Salute batteria**: SoH stimato, kWh per punto %, perdite di ricarica.
- **Risparmi** rispetto a un'auto termica, bollo, tagliandi e assicurazione.
- **Auto-rilevamento** delle entità BYD tramite `translation_key`, quindi
  indipendente dalla lingua e dal nome del device.
- **Multi-lingua**: italiano, inglese, francese, spagnolo, tedesco.

## Requisiti

- Home Assistant 2024.x o successivo.
- [`hass-byd-vehicle`](https://github.com/jkaberg/hass-byd-vehicle) installata e
  configurata (almeno una vettura BYD visibile in HA).
- (Opzionale) sensori della wallbox e del contatore di casa per i calcoli di
  ricarica e bilanciamento.

## Installazione

### HACS (consigliata)

1. HACS → **Integrazioni** → menu ⋮ → **Repository personalizzati**.
2. Aggiungi `https://github.com/Redrex85/BYD-EV-Center` con categoria
   **Integration**.
3. Installa **BYD EV Center** e riavvia Home Assistant.
4. **Impostazioni → Dispositivi e servizi → Aggiungi integrazione → BYD EV Center**.

### Manuale

Copia `custom_components/byd_ev_center/` in `/config/custom_components/` e
riavvia Home Assistant.

## Configurazione

Il wizard ha tre passi: **profilo** (Base / Pro / Enterprise), **wallbox** e
**auto**.

Nel passo **L'auto**:

1. scegli il **modello** (imposta foto e capacità batteria) oppure lascia
   `Auto`: in quel caso il modello viene letto dal cloud.
2. assegna un **nome breve** (es. `Dolphin Surf`): diventa il prefisso delle
   entità create.
3. conferma i sensori proposti. La sezione **Dati BYD** viene compilata
   automaticamente leggendo la device/entity registry di `byd_vehicle`
   (`battery_level`, `range`, `odometer`, `charging`, `plug`, `location`,
   comandi remoti e sensori informativi).

Le stesse voci restano modificabili in **Configura → Opzioni**.

### Modelli supportati

| Modello | Batteria (kWh) | WLTP (km) |
|---|---|---|
| Dolphin Surf | 30 / 43,2 | 220 / 322 |
| Dolphin | 44,9 / 60,4 | 340 / 427 |
| Atto 2 | 64,8 | 430 |
| Atto 3 | 49,9 / 60,4 | 344 / 420 |
| Atto 3 EVO | 74,8 | 470 |
| Seal | 61,4 / 82,5 | 460 / 520 |
| Seal U | 71,8 / 87,0 | 420 / 500 |
| Sealion 7 | 82,5 / 91,3 | 482 / 502 |
| Tang | 86,4 / 108,8 | 400 / 530 |

I valori sono indicativi e modificabili nel wizard. Le versioni **DM-i / PHEV**
non sono incluse: i calcoli assumono una batteria di trazione ricaricabile e
consumi elettrici.

## Entità create

Oltre alle entità di viaggio, ricarica, costi e manutenzione:

- **Sensori**: veicolo BYD, potenza batteria, consumo medio, consumo ultimi
  50 km, tempo di ricarica residuo, temperatura abitacolo, temperatura esterna,
  pressioni pneumatici.
- **Binary sensor**: BYD connessa, BYD bloccata, porte aperte, finestrini
  aperti, veicolo acceso.

## Pannello e card

- Pannello: `/byd_ev_center/www/byd-ev-center-panel.js` (registrato
  automaticamente come risorsa Lovelace).
- Card manuale: `custom:byd-ev-center-card`.

Il pannello include la pagina **BYD Veicolo** con i dati nativi BYD e link
`more-info` alle entità sorgente.

## Come funziona il rilevamento

L'integrazione BYD espone decine di entità con `entity_id` tradotti nella lingua
di Home Assistant. BYD EV Center non usa quegli `entity_id`: legge la
**entity registry** e riconosce le entità tramite `translation_key`
(`elec_percent`, `total_mileage`, `is_charging`, `is_locked`, …), che è stabile
fra lingue, modelli e versioni dell'auto.

Se un sensore non viene trovato (modello o software diversi), il campo resta
vuoto e può essere selezionato a mano.

## Risoluzione problemi

- **Entità BYD non rilevate**: verifica che `byd_vehicle` sia configurata e che
  le entità non siano disabilitate; poi riapri **Configura → Opzioni** e
  controlla la sezione **Dati BYD**.
- **Foto sbagliata o generica**: scegli il modello corretto nel wizard. Per
  `Seal U` viene usata la foto della Seal.
- **Dashboard non creata**: creala a mano importando il file YAML generato
  (notifica persistente) oppure riprova dopo il riavvio.
- **Sensori non disponibili**: alcuni valori BYD dipendono da modello e
  versione software; le entità mancanti restano vuote senza bloccare il
  pannello.

## Crediti e licenza

- Codice: MIT — vedi [LICENSE](LICENSE).
- Foto dei modelli: [BYD-CARD](https://github.com/moshiko2312/BYD-CARD) (MIT).
- Icona e logo BYD: [hass-byd-vehicle](https://github.com/jkaberg/hass-byd-vehicle)
  (MIT).
- `hass-byd-vehicle` è un progetto indipendente: BYD EV Center si limita a
  leggere le sue entità tramite la registry.

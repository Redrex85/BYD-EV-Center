# Changelog

## 1.0.5 - 2026-11-12

- Nuovo riepilogo giornaliero nativo: una notifica la sera (dopo le 21) con km,
  kWh consumati, costo stimato, consumo e costo/km del giorno. Si abilita con lo
  switch "Riepilogo Giornaliero".
- Nuovo servizio `byd_ev_center.test_notification` (`tipo`:
  cs, cc, lb, sum, dead, bal, sol, gse_stop, gse_go, auto_start) per inviare una
  notifica di prova con i testi correnti.
- Pannello: nella card Notifiche (Impostazioni) 10 pulsanti di prova, uno per
  tipo di notifica.
- `services.test_notification` + `entity.switch.notify_daily` tradotti in
  it/en/fr/es/de.

## 1.0.4 - 2026-11-12

- Fix pannello: `_drawByd` chiamava `this._t(...)` ma `_t` è una funzione di
  modulo, non un metodo → `TypeError: this._t is not a function` e pannello in
  errore. Ora usa `_t(...)`.

## 1.0.3 - 2026-11-12

- Eliminati gli avvisi di deprecazione del `climate`: usati
  `_attr_native_temperature_unit`, `native_current_temperature` e
  `native_target_temperature` (le vecchie proprietà smettono di funzionare da
  Home Assistant 2027.11).

## 1.0.2 - 2026-11-12

- Fix **errore di configurazione** all'apertura della dashboard: le risorse
  Lovelace ora vengono lette sia dal formato dict (Home Assistant recente) sia
  dall'oggetto (versioni precedenti); prima, su HA recente, il pannello non
  veniva registrato e la card risultava sconosciuta.
- Pannello e card registrati **prima** della creazione della dashboard, così la
  prima apertura trova subito gli asset.

## 1.0.1 - 2026-11-12

- Icona e logo custom: ovale rosso con wordmark **EV** inclinato, nello stile
  del marchio originale ma distinto.
- Asset `brand/` aggiornati (icon 256/512, logo 652/1307 px).

## 1.0.0 - 2026-11-12

Prima release di **BYD EV Center**.

- Integrazione HACS `byd_ev_center` derivata da Renault EV Center.
- Wizard di configurazione con sezione **Dati BYD**: rileva automaticamente le
  entità dell'integrazione `byd_vehicle` tramite `translation_key`.
- Selezione modello (Dolphin Surf, Dolphin, Atto 2, Atto 3, Atto 3 EVO, Seal,
  Seal U, Sealion 7, Tang, Custom) con foto dedicata e capacità batteria
  precompilata. L'opzione `Auto` usa il modello letto dal cloud.
- Nuovi sensori informativi: veicolo, potenza batteria, consumo medio e ultimi
  50 km, tempo di ricarica residuo, temperature abitacolo/esterna, pressioni
  pneumatici.
- Nuovi binary sensor: connessione, blocco, porte, finestrini, veicolo acceso.
- Dashboard e pannello con nuova pagina **BYD Veicolo**.
- Interfaccia multi-lingua: italiano, inglese, francese, spagnolo, tedesco.
- Tabelle WLTP e capacità batteria aggiornate ai modelli BYD Europa.

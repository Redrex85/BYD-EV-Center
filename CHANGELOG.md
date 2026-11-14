# Changelog

## 1.0.8 - 2026-11-14

Porta delle modifiche 1.1.29 → 1.1.34 del progetto di riferimento:

- **Vampire drain onesto**: il calo da fermo conta solo se non c'è carica, il
  viaggio non è in corso e l'odometro è noto e immobile fra due letture;
  `VAMP_RATE_MAX` da 3.0 a 1.0 %/h (prima contava anche la guida lenta:
  "oggi 4%, mese 44%").
- **Foto auto personalizzata**: se esiste `/config/www/byd-ev-center/auto.png`
  la dashboard la usa al posto dell'immagine del modello, con mtime come
  cache-busting; il pannello ripiega sul modello in caso di errore.
- **Toponimi nella lingua di Home Assistant**: Nominatim riceve
  `accept-language` dalla lingua di HA, la cache geocoding è per lingua e i
  viaggi/ricariche salvano `geo_lang`: al cambio lingua vengono rigeocodificati
  (anche quelli vecchi, con throttle ~1 req/s).
- **Testi residui del pannello tradotti** (messaggi di tabelle/grafici vuoti,
  toast, tooltip "Elimina/Modifica", etichette notifiche, interruttori):
  ~49 voci nuove in UI2 + frase "Fuori" in PHRASES per i testi composti
  (tabella Rotte: "Fuori → Fuori" ora si traduce per intero).

## 1.0.7 - 2026-11-12

- Porta delle modifiche 1.1.28/1.1.29 del progetto di riferimento:
  - pagina Automazioni: riquadro "Notifiche — attiva/disattiva" con gli
    interruttori di riepilogo giornaliero, avvio/fine ricarica e batteria bassa;
  - pagina Impostazioni compatta: card più dense, Esporta/Importa dati dentro
    "Reset & export" (la card Backup dati separata è sparita), Zone ricariche,
    Palette, Lingua e Notifiche su un solo rigo (grid g4), pulsanti di prova
    con etichette emoji tradotte;
  - CSS `.g4` + media query e classe `.compact`.
- (Il gate `notify_end` sulla fine ricarica era già in 1.0.6.)

## 1.0.6 - 2026-11-12

- Pannello, card Notifiche: i pulsanti di prova ora hanno le etichette con
  emoji (come nel progetto di riferimento) e, accanto a ciascuno, un
  interruttore per attivare o disattivare quella singola notifica.
- Nuovi switch: `Notifica Scadenze`, `Notifica Bilanciamento Casa`,
  `Notifica Bilanciamento Solare` e `Notifica GSE`. Ogni notifica ora è
  controllabile singolarmente; la fine ricarica rispetta `Notifica Fine
  Ricarica` (prima era sempre inviata) e il bilanciamento solare non dipende
  più dallo switch di avvio ricarica.
- Etichette dei 10 pulsanti di prova tradotte in it/en/fr/es/de.

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

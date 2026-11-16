## 1.0.11-beta

- **Ultimo cambio gomme / cambio tagliando**: senza il valore impostato il pannello mostrava lo stato del sensore `prossima_scadenza` (giorni) come se fossero km; ora un attributo mancante vale "—". La scadenza a km non viene più inventata dall'odometro: serve un intervento registrato o un valore impostato (porting dal riferimento).
- **Giorni stimati**: media km/giorno reale dall'installazione invece del km dell'anno solare diviso 365 (dava valori assurdi nei primi giorni d'uso); riserva 15000 km/anno (porting dal riferimento).
- **Nomi tradotti in HA**: nome dispositivo, sensori di risparmio, stato del tipo di ricarica e nomi delle scadenze seguono la lingua di Home Assistant; le scadenze portano un campo `key` stabile (porting dal riferimento).
- **Configura → Wallbox**: "Avvio carica" e "Stop carica" non sono più obbligatori: bloccavano il salvataggio a chi non ha wallbox o ne ha una senza switch (porting dal riferimento).
- **Card**: banner console con `CARD_VER` invece della versione fissa.

## 1.0.10-beta

- **Foto auto che sfarfallava**: l'URL della foto utente era rigenerato con un timestamp nuovo a ogni aggiornamento `hass`, ricaricando l'immagine più volte al secondo. Ora il cache-busting usa un timestamp per **caricamento pagina** e l'elemento viene ricostruito solo se il markup cambia (porting dal riferimento).
- **Configura → Auto**: nel form di configurazione la label del campo "Modello" compariva grezza (`model`) perché la traduzione era solo nel blocco `data` e non in `sections.car.data`. Aggiunta in tutte le 5 lingue (porting dal riferimento).
- **Manutenzione → Prossimo cambio**: il backend anteponeva "a" alla data-km (`a 105573 km`) in italiano fisso, non traducibile. Ora restituisce `105573 km` (porting dal riferimento).

# Changelog

## 1.0.9 - Porting 1.1.35-1.1.38 del riferimento

- **Archivio viaggi**: di default è espanso solo l'ultimo mese presente in archivio (prima restavano aperti tutti tranne il mese precedente); gli anni restano contenitori aperti e l'apertura manuale viene ricordata.
- **Toast tradotti**: la traduzione del DOM è stata estratta in `_trText()` e applicata anche ai toast, che prima restavano in italiano in ogni lingua.
- **~30 stringhe del pannello** che erano letterali italiani ora passano dalle tabelle (IT/EN/FR/ES/DE) e 29 voci nuove in UI2 (esiti azioni, rimandi "Configura → …", "Archivio viaggi vuoto", "Fascia di temperatura", "km mancanti", "TOTALE", "sess", "gg", "giorni", "FV/Bat/Pub").
- **Plurali**: nuova `_pl()` (singolare/plurale corretto nei contatori: "1 viaggio / 2 viaggi", "1 giorno / 5 giorni").
- **Geocoding**: il backfill non è più una tantum (prima si fermava dopo 120 viaggi + 40 ricariche e il resto restava in italiano); la lingua viene marcata solo se il toponimo è stato davvero aggiornato.
- **Options flow**: unità `€/anno` e `gg`, giorni della settimana, opzione `data` e opzione `Custom` del modello seguono la lingua di Home Assistant; fix unità `?` → `€` sulla spesa pre-integrazione.
- **Foto auto**: sostituire `auto.png` si vede subito senza ricaricare l'integrazione.

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

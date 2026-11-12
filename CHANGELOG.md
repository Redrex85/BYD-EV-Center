# Changelog

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

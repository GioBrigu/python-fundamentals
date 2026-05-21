# 📊 Operations & Service Delivery Ticket Filter

## 📝 Descrizione del Progetto
Questo modulo Python è stato sviluppato per automatizzare l'identificazione e l'isolamento dei ticket di assistenza tecnica che violano gli accordi sui livelli di servizio (SLA), impostati a un massimo di **30 minuti di attesa**. 

L'obiettivo è simulare un micro-servizio backend per un dipartimento di *Service Delivery*, riducendo il tempo di monitoraggio manuale da parte dei coordinatori delle operazioni.

## ⚙️ Architettura dei Dati e Logica
Il codice elabora una struttura dati transazionale simulata sotto forma di un dizionario nidificato Python (`dict`). Viene applicato un costrutto logico condizionale combinato per estrarre solo i record che rispettano contemporaneamente due condizioni stabili:
1. `stato == "Aperto"`
2. `tempo_attesa_min > 30`

## 🚀 Come Eseguire lo Script

Assicurati di avere Python 3 installato sul tuo sistema locale.

```bash
python ticket_filter.py
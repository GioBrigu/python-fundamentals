
# ==============================================================================
# PROGETTO: Monitoraggio e Filtraggio Ticket in Service Delivery
# OBIETTIVO: Isolare i ticket critici fuori SLA (SLA > 30 minuti)
# ==============================================================================

# Simulazione di una struttura dati transazionale (Dizionario di Dizionari)
ticket_operations = {
    "TICKET-101": {"priorita": "Alta", "stato": "Aperto", "tempo_attesa_min": 45},
    "TICKET-102": {"priorita": "Bassa", "stato": "Risolto", "tempo_attesa_min": 12},
    "TICKET-103": {"priorita": "Media", "stato": "Aperto", "tempo_attesa_min": 120},
    "TICKET-104": {"priorita": "Alta", "stato": "Risolto", "tempo_attesa_min": 25},
    "TICKET-105": {"priorita": "Alta", "stato": "Aperto", "tempo_attesa_min": 15}
}

def analizza_ticket_critici(dati_ticket):
    """
    Scansiona il dizionario dei ticket e restituisce solo quelli 
    aperti che superano la soglia critica di 30 minuti di attesa.
    """
    ticket_critici = {}
    
    for ticket_id, dettagli in dati_ticket.items():
        # Costrutto logico di filtraggio condizionale
        if dettagli["stato"] == "Aperto" and dettagli["tempo_attesa_min"] > 30:
            ticket_critici[ticket_id] = dettagli
            
    return ticket_critici

# Esecuzione del modulo
if __name__ == "__main__":
    print("Avvio analisi pipeline ticket operativi...\n")
    risultati = analizza_ticket_critici(ticket_operations)
    
    # Visualizzazione output condizionale
    for t_id, info in risultati.items():
        print(f" ALERT: Il {t_id} richiede attenzione immediata!")
        print(f"       Priorità: {info['priorita']} | Attesa: {info['tempo_attesa_min']} min\n")
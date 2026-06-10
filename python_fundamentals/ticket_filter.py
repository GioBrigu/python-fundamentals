# ==============================================================================
# OPERAZIONE: Monitoraggio e Filtraggio Ticket in Service Delivery
# OBIETTIVO: Isolare i ticket critici fuori SLA con gestione degli errori
# ==============================================================================

# Simulazione di una struttura dati reale con un record corrotto (TICKET-104)
ticket_operations = {
    'TICKET-101': {'priorita': 'Alta', 'stato': 'Aperto', 'tempo_attesa_min': 45},
    'TICKET-102': {'priorita': 'Bassa', 'stato': 'Risolto', 'tempo_attesa_min': 12},
    'TICKET-103': {'priorita': 'Media', 'stato': 'Aperto', 'tempo_attesa_min': 120},
    'TICKET-104': {'priorita': 'Alta', 'stato': 'Aperto', 'tempo_attesa_min': 'DATO_CORROTTO'}, # <- Questo farebbe crashare il vecchio script
    'TICKET-105': {'priorita': 'Alta', 'stato': 'Aperto', 'tempo_attesa_min': 15}
}

def analizza_ticket_critici_sicuro(dati_ticket):
    '''
    Scansiona i ticket e isola quelli aperti fuori SLA (>30 min).
    Gestisce le eccezioni per evitare il blocco della pipeline in caso di dati corrotti.
    '''
    ticket_critici = {}
    
    for ticket_id, dettagli in dati_ticket.items():
        try:
            # Tentativo di lettura e confronto logico
            if dettagli['stato'] == 'Aperto' and dettagli['tempo_attesa_min'] > 30:
                ticket_critici[ticket_id] = dettagli
        except TypeError:
            # Se i tipi di dato non sono confrontabili (es. Stringa > Numero), cattura l'errore
            print(f'⚠️ LOG ERROR: Impossibile analizzare {ticket_id}. Il tempo di attesa non è un numero valido.')
            continue # Salta questo ticket e passa al successivo senza bloccare il programma
            
    return ticket_critici

if __name__ == '__main__':
    print('Avvio pipeline con gestione delle eccezioni...\n')
    risultati = analizza_ticket_critici_sicuro(ticket_operations)
    
    print('\n--- REPORT TICKET CRITICI ISOLATI ---')
    for t_id, info in risultati.items():
        print(f' ALERT: Il {t_id} richiede attenzione. Attesa: {info['tempo_attesa_min']} min')
# ==============================================================================
# OPERAZIONE: Creazione Database Colonnare con DuckDB
# OBIETTIVO: Generare un database OLAP ed eseguire comandi SQL di analisi
# ==============================================================================

import duckdb

def inizializza_duckdb():
    print("Connessione a DuckDB...")

    connessione = duckdb.connect("azienda_analytics.db")

    connessione.execute("""
    CREATE TABLE IF NOT EXISTS servizi_logistici (
        id_transazione VARCHAR PRIMARY KEY,
        vettore VARCHAR NOT NULL,
        costo_spedizione DECIMAL(10,2),
        stato VARCHAR
    );
    """)

    connessione.execute("""
    INSERT INTO servizi_logistici VALUES
    ('TX-101', 'DHL', 15.50, 'Consegnato'),
    ('TX-102', 'BRT', 12.00, 'In Corso'),
    ('TX-103', 'UPS', 18.00, 'Consegnato'),
    ('TX-104', 'DHL', 25.40, 'Annullato');
    """)

# Nota di Merito: DuckDB salva in automatico (Auto-commit), non serve .commit()!
    
    print("\n--- VERIFICA IMMEDIATA TRAMITE QUERY SQL SELECT ---")
    # Eseguiamo subito una query di test direttamente da Python
    risultato = connessione.execute("SELECT * FROM servizi_logistici WHERE stato = 'Consegnato'").df()
    print(risultato)

    connessione.close()

if __name__ == "__main__":
    inizializza_duckdb()
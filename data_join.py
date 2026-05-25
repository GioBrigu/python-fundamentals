# ==============================================================================
# OPERAZIONE: Unione di DataFrame (Arricchimento Dati)
# OBIETTIVO: Associare i costi finanziari ai flussi operativi tramite merge
# ==============================================================================

import pandas as pd

def arricchisci_report_costi():
    # 1. Caricamento dei due dataset sorgente
    df_operations = pd.read_csv("operations_data_clean.csv")
    df_tariffe = pd.read_csv("vettori_tariffario.csv")
    
    print("--- TABELLA OPERATIONS (A) ---")
    print(df_operations[['id_transazione', 'vettore']])
    print("\n--- TABELLA TARIFFARIO (B) ---")
    print(df_tariffe)
    
    # Uniamo le due tabelle sfruttando la colonna comune 'vettore'
    df_consolidato = pd.merge(
        df_operations, 
        df_tariffe, 
        on='vettore', 
        how='left'
    )
    
    print(df_consolidato)
    
    # Salviamo il file
    df_consolidato.to_csv("operations_final_costs.csv", index=False)
    
    # 🌟 RESTITUIAMO il DataFrame per usi futuri
    return df_consolidato

if __name__ == "__main__":
    arricchisci_report_costi()
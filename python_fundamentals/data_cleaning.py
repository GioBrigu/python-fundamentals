# ==============================================================================
# OPERAZIONE: Data Cleaning e Standardizzazione con Pandas
# OBIETTIVO: Bonificare i valori nulli e normalizzare i formati temporali
# ==============================================================================

import pandas as pd
import numpy as np

def bonifica_pipeline_logistica(percorso_file):
    print("Inizio processo di bonifica dati...")
    df = pd.read_csv(percorso_file)
    
    # 1. Standardizzazione delle Date
    # Forza pandas a convertire tutto in formato Data reale, gestendo i formati misti
    df['data_evento'] = pd.to_datetime(df['data_evento'], errors='coerce', yearfirst=True)
    
    # 2. Gestione Valori Nulli - Colonna Vettore (Dato Categorico)
    # Sostituiamo il vettore mancante con la stringa "NON SPECIFICATO" per non perdere la riga
    df['vettore'] = df['vettore'].fillna("NON SPECIFICATO")
    
    # 3. Gestione Valori Nulli - Colonna Tempo (Dato Numerico)
    # Invece di cancellare la riga, imputiamo il valore vuoto usando la MEDIANA dei tempi
    mediana_tempi = df['tempo_elaborazione_ore'].median()
    df['tempo_elaborazione_ore'] = df['tempo_elaborazione_ore'].fillna(mediana_tempi)
    
    return df

if __name__ == "__main__":
    file_sorgente = "operations_data.csv"
    df_pulito = bonifica_pipeline_logistica(file_sorgente)
    
    print("\n--- DATASET BONIFICATO ---")
    print(df_pulito)
    print("\n--- VERIFICA TIPI DI DATO ---")
    print(df_pulito.dtypes)
    
    # Salviamo il risultato in un nuovo file CSV "pulito" pronto per la BI
    df_pulito.to_csv("operations_data_clean.csv", index=False)
    print("\nFile 'operations_data_clean.csv' generato con successo!")
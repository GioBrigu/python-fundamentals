# ==============================================================================
# OPERAZIONE: Ingestione e Ispezione Strutturale con Pandas
# OBIETTIVO: Caricare il registro operations e mappare le anomalie di struttura
# ==============================================================================

import pandas as pd

def ispeziona_dataset(percorso_file):
    print(f'--- 1. Caricamento del file: {percorso_file} ---')
    # Carichiamo il file CSV in un oggetto DataFrame (la tabella di pandas)
    df = pd.read_csv(percorso_file)
    
    print('\n--- 2. Visualizzazione delle prime righe (df.head()) ---')
    print(df.head())
    
    print('\n--- 3. Informazioni Strutturali e Tipi di Dato (df.info()) ---')
    # df.info() mostra quante righe ci sono, se ci sono valori nulli e il tipo di dato di ogni colonna
    print(df.info())
    
    print('\n--- 4. Conteggio Valori Nulli per Colonna (df.isnull().sum()) ---')
    # Isoliamo esattamente quanti dati mancano all'appello nella pipeline
    print(df.isnull().sum())
    
    return df

if __name__ == '__main__':
    file_target = 'operations_data.csv'
    dataframe_logistica = ispeziona_dataset('operations_data.csv')
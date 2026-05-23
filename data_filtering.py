# ==============================================================================
# PROGETTO: Filtraggio Avanzato con .loc e .iloc
# OBIETTIVO: Isolare record e colonne specifiche per i report direzionali
# ==============================================================================

import pandas as pd

def esegui_filtri_avanzati():
    # Carichiamo il dataset pulito ieri (assicurati che il file esista nella cartella)
    df = pd.read_csv('operations_data_clean.csv')
    print('--- DATASET ORIGINALE ---')
    print(df)
    
    print('\n==================================================================')
    print('1. ESTRARRE DATI CON .iloc (Coordinate Numeriche)')
    print('==================================================================')
    # Estraiamo le prime 3 righe e le prime 2 colonne usando solo gli indici numerici
    fetta_numerica = df.iloc[0:3, 0:2]
    print(fetta_numerica)
    
    print('\n==================================================================')
    print('2. ESTRARRE DATI CON .loc (Etichette e Condizioni Logiche)')
    print('==================================================================')
    # Isoliama solo i ticket del vettore 'DHL' e mostriamo solo le colonne id e stato
    filtro_condizionale = df.loc[df['vettore'] == 'DHL', ['id_transazione', 'stato_consegna']]
    print(filtro_condizionale)
    
    print('\n==================================================================')
    print('3. CREAZIONE NUOVA COLONNA (Feature Engineering Base)')
    print('==================================================================')
    # Creiamo una colonna che identifica se un tempo di elaborazione è 'Critico' (> 10 ore)
    df.loc[df['tempo_elaborazione_ore'] > 10, 'categoria_criticita'] = 'Critico'
    df.loc[df['tempo_elaborazione_ore'] <= 10, 'categoria_criticita'] = 'Standard'
    print(df)

if __name__ == '__main__':
    esegui_filtri_avanzati()
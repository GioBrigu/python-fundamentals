-- ==============================================================================
-- OPERAZIONE: Estrazione e Filtraggio Dati in SQL Puro
-- OBIETTIVO: Padroneggiare SELECT, WHERE, ORDER BY e LIMIT su DuckDB
-- ==============================================================================

-- Apertura e connessione al database locale (Istruzione specifica per DuckDB)
-- Dice al file SQL su quale database fisco deve lavorare
ATTACH 'azienda_analytics.db' AS db;

SHOW DATABASES;

SELECT *
FROM db.servizi_logistici;

--------------------------------------------------------------------------------
-- QUERY 1: Selezione mirata di colonne (Evitiamo SELECT *)
--------------------------------------------------------------------------------
SELECT id_transazione, vettore, costo_spedizione
FROM db.servizi_logistici;

--------------------------------------------------------------------------------
-- QUERY 2: Filtraggio condizionale avanzato (WHERE)
--------------------------------------------------------------------------------
SELECT id_transazione, vettore, costo_spedizione, stato
FROM db.servizi_logistici
WHERE stato = 'Consegnato' AND costo_spedizione > 15.00;

--------------------------------------------------------------------------------
-- QUERY 3: Ordinamento delle performance e controllo dei volumi (ORDER BY + LIMIT)
--------------------------------------------------------------------------------
SELECT vettore, costo_spedizione, stato
FROM db.servizi_logistici
WHERE stato != 'Annullato'
ORDER BY costo_spedizione DESC;
--LIMIT 2;


--------------------------------------------------------------------------------
-- OPERAZIONE: Funzioni di Aggregazione e Calcolo KPI
-- OBIETTIVO: Estrarre metriche di riepilogo (Volumi, Totali e Medie)
--------------------------------------------------------------------------------

SELECT 
    COUNT(id_transazione) AS volume_totale_spedizioni,
    SUM(costo_spedizione) AS spesa_complessiva_euro,
    AVG(costo_spedizione) AS costo_medio_per_spedizione,
    MAX(costo_spedizione) AS tariffa_massima_registrata
FROM db.servizi_logistici;


--------------------------------------------------------------------------------
-- OPERAZIONE: Raggruppamento e Filtrazione delle Aggregazioni
-- OBIETTIVO: Calcolare metriche per vettore (GROUP BY) e filtrare i totali (HAVING)
--------------------------------------------------------------------------------

SELECT 
    vettore,
    COUNT(id_transazione) AS spedizioni_gestite,
    SUM(costo_spedizione) AS totale_speso_vettore,
    AVG(costo_spedizione) AS costo_medio_vettore
FROM db.servizi_logistici
GROUP BY vettore
HAVING costo_medio_vettore > 15.00;

--------------------------------------------------------------------------------
-- OPERAZIONE: Sotto-query (Subqueries) Avanzate
-- OBIETTIVO: Isolare i record usando metriche calcolate dinamicamente
--------------------------------------------------------------------------------

SELECT id_transazione, vettore, costo_spedizione, stato
FROM db.servizi_logistici
WHERE costo_spedizione > (
    SELECT AVG(costo_spedizione) 
    FROM db.servizi_logistici
)
ORDER BY costo_spedizione DESC;
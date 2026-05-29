-- ==============================================================================
-- OPERAZIONE: Estrazione e Filtraggio Dati in SQL Puro
-- OBIETTIVO: Padroneggiare SELECT, WHERE, ORDER BY e LIMIT su DuckDB
-- ==============================================================================

-- Apertura e connessione al database locale (Istruzione specifica per DuckDB)
-- Dice al file SQL su quale database fisco deve lavorare
ATTACH 'azienda_analytics.db' AS db;

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
ORDER BY costo_spedizione DESC
LIMIT 2;
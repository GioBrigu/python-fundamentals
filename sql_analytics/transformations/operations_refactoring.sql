-- Creazione della tabella dei ticket di supporto operativo
CREATE TABLE IF NOT EXISTS operations_tickets (
    ticket_id INTEGER,
    agent_id VARCHAR,
    category VARCHAR,
    resolution_time_minutes INTEGER,
    priority VARCHAR
);

-- Inserimento record di test (con anomalie operative simulate)
INSERT INTO operations_tickets VALUES
(101, 'AG_MIL_01', 'Ripristino Password', 15, 'Low'),
(102, 'AG_MIL_02', 'Errore Pagamento', 45, 'High'),
(103, 'AG_MIL_01', 'Errore Pagamento', 60, 'High'),
(104, 'AG_MIL_03', 'Blocco Account', 120, 'Critical'),
(105, 'AG_MIL_02', 'Ripristino Password', -5, 'Low'), -- ANOMALIA: Tempo negativo
(106, 'AG_MIL_01', 'Blocco Account', NULL, 'Critical'), -- ANOMALIA: Non ancora risolto
(107, 'AG_MIL_03', 'Errore Pagamento', 30, 'Medium');
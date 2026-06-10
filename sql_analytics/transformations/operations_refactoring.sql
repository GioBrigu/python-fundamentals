-- =====================================================================
-- 1. SETUP DEL DATASET SPERIMENTALE (DUCKDB IN-MEMORY)
-- =====================================================================
CREATE TABLE IF NOT EXISTS operations_tickets (
    ticket_id INTEGER,
    agent_id VARCHAR,
    category VARCHAR,
    resolution_time_minutes INTEGER,
    priority VARCHAR
);

-- Puliamo la tabella prima di inserire per evitare record duplicati se eseguiamo il file più volte
TRUNCATE TABLE operations_tickets;

INSERT INTO operations_tickets VALUES
(101, 'AG_MIL_01', 'Ripristino Password', 15, 'Low'),
(102, 'AG_MIL_02', 'Errore Pagamento', 45, 'High'),
(103, 'AG_MIL_01', 'Errore Pagamento', 60, 'High'),
(104, 'AG_MIL_03', 'Blocco Account', 120, 'Critical'),
(105, 'AG_MIL_02', 'Ripristino Password', -5, 'Low'),  -- ANOMALIA: Tempo negativo
(106, 'AG_MIL_01', 'Blocco Account', NULL, 'Critical'),  -- ANOMALIA: Non ancora risolto
(107, 'AG_MIL_03', 'Errore Pagamento', 30, 'Medium');


-- =====================================================================
-- PASSO 1: REFACTORING CON CTE (Isolamento anomalie e calcolo Benchmark)
-- =====================================================================
-- Questa query calcola la media di ogni agente e la confronta con la media globale del reparto,
-- escludendo i ticket nulli o negativi.

WITH cleaned_tickets AS (
    SELECT 
        agent_id,
        resolution_time_minutes
    FROM operations_tickets
    WHERE resolution_time_minutes IS NOT NULL 
      AND resolution_time_minutes > 0
),
department_metrics AS (
    SELECT AVG(resolution_time_minutes) AS global_average
    FROM cleaned_tickets
)
SELECT 
    c.agent_id,
    AVG(c.resolution_time_minutes) AS agent_avg_time,
    MAX(d.global_average) AS department_benchmark
FROM cleaned_tickets c
CROSS JOIN department_metrics d
GROUP BY c.agent_id
HAVING AVG(c.resolution_time_minutes) > MAX(d.global_average);


-- =====================================================================
-- PASSO 2: APPLICAZIONE WINDOW FUNCTION (Classifica ticket per Agente)
-- =====================================================================
-- Questa query NON collassa le righe, ma assegna a ogni ticket un rango (1, 2, 3...)
-- all'interno del recinto di ogni singolo agente, partendo dal ticket più lento.

WITH ranked_tickets AS (
    SELECT 
        ticket_id,
        agent_id,
        category,
        resolution_time_minutes,
        priority,
        ROW_NUMBER() OVER (
            PARTITION BY agent_id 
            ORDER BY resolution_time_minutes DESC
        ) AS ticket_rank_by_agent
    FROM operations_tickets
    WHERE resolution_time_minutes IS NOT NULL 
      AND resolution_time_minutes > 0
)
SELECT 
    ticket_id,
    agent_id,
    category,
    resolution_time_minutes,
    priority,
    ticket_rank_by_agent
FROM ranked_tickets
ORDER BY agent_id, ticket_rank_by_agent;


-- =====================================================================
-- PASSO 3: ANALISI DEI DELTA TEMPORALI CON FUNZIONI FINESTRA (LAG)
-- =====================================================================
-- Questa query calcola la differenza in minuti tra il ticket corrente 
-- e quello precedente per lo stesso agente, ordinati per ID (sequenza temporale).

WITH time_deltas AS (
    SELECT 
        ticket_id,
        agent_id,
        category,
        resolution_time_minutes,
        -- Recuperiamo il tempo del ticket PRECEDENTE dello stesso agente
        LAG(resolution_time_minutes, 1) OVER (
            PARTITION BY agent_id 
            ORDER BY ticket_id ASC
        ) AS previous_ticket_time
    FROM operations_tickets
    WHERE resolution_time_minutes IS NOT NULL 
      AND resolution_time_minutes > 0
)
SELECT 
    ticket_id,
    agent_id,
    category,
    resolution_time_minutes,
    previous_ticket_time,
    -- Calcolo del Delta: Tempo Corrente - Tempo Precedente
    (resolution_time_minutes - previous_ticket_time) AS delta_minutes_vs_previous
FROM time_deltas
ORDER BY agent_id, ticket_id;
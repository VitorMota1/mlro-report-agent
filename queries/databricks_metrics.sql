-- =============================================================================
-- MLRO Monthly Report — Queries de referência para métricas Databricks
-- =============================================================================
-- Estas queries são referências para as métricas do report.
-- O notebook oficial roda no Databricks e popula a planilha automaticamente.
-- =============================================================================

-- -----------------------------------------------------------------------------
-- PEP — Politically Exposed Persons
-- Onboarding + Ongoing + Rejected por mês
-- -----------------------------------------------------------------------------

-- PEP Onboarding (exemplo de estrutura)
-- SELECT
--   DATE_FORMAT(created_at, 'MMM/yy') AS month,
--   COUNT(*) AS pep_onboarding
-- FROM <pep_analysis_table>
-- WHERE analysis_type = 'onboarding'
--   AND pep_flag = true
-- GROUP BY 1
-- ORDER BY MIN(created_at);

-- -----------------------------------------------------------------------------
-- Sanctions — Alerts and True Match
-- Onboarding + Ongoing por mês
-- -----------------------------------------------------------------------------

-- Sanctions Alerts (exemplo de estrutura)
-- SELECT
--   DATE_FORMAT(alert_date, 'MMM/yy') AS month,
--   SUM(CASE WHEN source = 'onboarding' THEN 1 ELSE 0 END) AS alerts_onboarding,
--   SUM(CASE WHEN source = 'ongoing' THEN 1 ELSE 0 END) AS alerts_ongoing,
--   SUM(CASE WHEN source = 'onboarding' AND true_match = true THEN 1 ELSE 0 END) AS true_match_onboarding,
--   SUM(CASE WHEN source = 'ongoing' AND true_match = true THEN 1 ELSE 0 END) AS true_match_ongoing
-- FROM <sanctions_table>
-- GROUP BY 1
-- ORDER BY MIN(alert_date);

-- -----------------------------------------------------------------------------
-- EDD — Enhanced Due Diligence
-- Ongoing, UBO, Company, Investments KYC
-- -----------------------------------------------------------------------------

-- EDD metrics (exemplo de estrutura)
-- SELECT
--   DATE_FORMAT(analysis_date, 'MMM/yy') AS month,
--   SUM(CASE WHEN queue = 'ongoing' THEN 1 ELSE 0 END) AS ongoing,
--   SUM(CASE WHEN queue = 'ubo_qualification' THEN 1 ELSE 0 END) AS ubo_qualification,
--   SUM(CASE WHEN queue = 'company_acquisition' THEN 1 ELSE 0 END) AS company_acquisition,
--   SUM(CASE WHEN queue = 'company_qualification' THEN 1 ELSE 0 END) AS company_qualification,
--   SUM(CASE WHEN queue = 'investments_kyc' THEN 1 ELSE 0 END) AS investments_kyc
-- FROM <edd_table>
-- GROUP BY 1
-- ORDER BY MIN(analysis_date);

-- -----------------------------------------------------------------------------
-- Big Picture — Effectiveness of Alerts
-- NuPag / NuInvest / NuCrypto × Reported / Clear / Canceled
-- -----------------------------------------------------------------------------

-- Alert effectiveness (exemplo de estrutura)
-- SELECT
--   DATE_FORMAT(decision_date, 'MMM/yy') AS month,
--   product,
--   SUM(CASE WHEN decision = 'reported' THEN 1 ELSE 0 END) AS reported,
--   SUM(CASE WHEN decision = 'clear' THEN 1 ELSE 0 END) AS clear,
--   SUM(CASE WHEN decision = 'canceled' THEN 1 ELSE 0 END) AS canceled
-- FROM <alerts_table>
-- WHERE product IN ('nupag', 'nuinvest', 'nucrypto')
-- GROUP BY 1, 2
-- ORDER BY MIN(decision_date);

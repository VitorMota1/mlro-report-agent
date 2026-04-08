# Mapeamento Slide × Fonte de Dados

Status: Em validação com o MLRO. Confirmados marcados com ✅.

## Legenda de Fontes

| Código | Fonte | Detalhe |
|--------|-------|---------|
| **STATIC** | Template fixo | Não muda entre reports |
| **MANUAL** | Texto escrito pelo MLRO | Atualizado manualmente cada mês |
| **JIRA** | Board MLRO (Jira) | Projeto `MLRO`, board `27971`. Tarefas/operações do mês → textos dos highlights |
| **SLACK** | Canal `#comissao-de-risco-kyc-aml` (`C05440VHFB6`) | Casos RSCR escalados à Comissão de Risco → contagem por fórum → tabela slide 23 |
| **DB→SHEETS** | Databricks → Google Sheets `output_automatics` | Notebook ID `1971106302956783` → `tbl_Databricks` → `m__data` → `output_automatics` |
| **SHEETS-MANUAL** | Google Sheets `output_manuals` | Preenchido manualmente na planilha |
| **QS** | QuickSight Dashboard | Dashboard `35046a00-8bd2-438b-b9f1-b9616121178e` (screenshots/embeds) |
| **SPA** | Planilha "Dossiê SPA Gerados" | Spreadsheet `1di9PJLWHjufFoe2MhXi1dayYHFkYEkKF4QnF1dUbzSQ` |
| **PLAYVOX** | PlayVox QA System | Scorecards de qualidade |

---

## Seção 1 — Highlights

| Slide | Título | Fonte | Confirmado |
|-------|--------|-------|------------|
| 1 | MLRO Report — Cover | STATIC (mês/ano manual) | |
| 2 | Monthly Highlights — Cover | STATIC | |
| 3 | Operações PF (ex: Carbono Oculto, Magna Fraus) | ✅ JIRA → MANUAL | ✅ Tasks do board MLRO (projeto `MLRO`, board `27971`) → MLRO redige o texto |
| 4 | Operações PF (ex: RFB, Poço de Lobato) | ✅ JIRA → MANUAL | ✅ idem |
| 5 | Operações PF (ex: Freedom CV, Sintonia PCC) | ✅ JIRA → MANUAL | ✅ idem |
| 6 | Rules / Effectiveness / Regulatory | ✅ JIRA → MANUAL | ✅ idem |
| 7 | Visit to COAF / Eventos | ✅ JIRA → MANUAL | ✅ idem |
| 8 | Cooperation / Novas medidas | ✅ JIRA → MANUAL | ✅ idem |

---

## Seção 2 — Indicadores Clientes

| Slide | Título | Gráficos | Fonte Gráficos | Texto/Notas | Confirmado |
|-------|--------|----------|-----------------|-------------|------------|
| 9 | Indicators Customers — Cover | — | STATIC | — | |
| 10 | EDD PF | "EDD PF Ongoing e Release" (line) + "EDD PJ Ongoing" (bar) | QS | MANUAL | |
| 11 | EDD PJ | "CDD PJ e PF" (line, May25→Feb26) | QS | MANUAL | |
| 12 | PEP | 4 charts: Total PEPs, Rejected, High Level Related, High Level Titular | ✅ DB→SHEETS (`output_automatics`) | — | ✅ Fonte: Notebook Databricks ID `1971106302956783` |
| 13 | PEP High Level Positions | "Tipo de PEP" (horizontal bar, `investigation__customer_id` × `pep_type`) | QS | — | |

---

## Seção 3 — Indicadores MSAC

| Slide | Título | Gráficos | Fonte Gráficos | Texto/Notas | Confirmado |
|-------|--------|----------|-----------------|-------------|------------|
| 14 | Indicators MSAC — Cover | — | STATIC | — | |
| 15 | NuPag | KPIs + "Análises mês a mês AML" (stacked bar + line % Conversão) | QS | MANUAL | |
| 16 | NuInvest | KPIs + "Análises mês a mês AML" | QS | — | |
| 17 | NuCrypto | KPIs + "Análises mês a mês AML" | QS | MANUAL (nota reclassificações) | |
| 18 | SPA Reports | 4 bars: PJ, PJ Phonetics, PF, Counterparties | ✅ SPA (planilha Dossiê SPA) | MANUAL | ✅ Planilha `1di9PJLWHjufFoe2MhXi1dayYHFkYEkKF4QnF1dUbzSQ` |
| 19 | Report Breaches 24h | "Reports After Deadline NuInvest" + "Reports After Deadline NuPag" | QS | MANUAL (root cause) | |
| 20 | Sanctions | Multi-line: Sanctions CSNU/Onboarding/Ongoing/PJ (by Nome Fila) | QS | — | |

---

## Seção 4 — Indicadores Processo MLRO

| Slide | Título | Gráficos | Fonte Gráficos | Texto/Notas | Confirmado |
|-------|--------|----------|-----------------|-------------|------------|
| 21 | Indicators MLRO Process — Cover | — | STATIC | — | |
| 22 | MLRO Deliberations | KPIs + donut "Decisão Análises MLRO" + stacked bar "Análises Mês a Mês MLRO" | QS | MANUAL | |
| 23 | MLRO Deliberations — Tabela fóruns | Tabela: AML Exit, Reputational Risk, Sanctions, KYC-PEP × meses | ✅ SLACK → SHEETS-MANUAL (`output_manuals`) | MANUAL (explicações históricas) | ✅ Contagem de casos RSCR do canal `#comissao-de-risco-kyc-aml` → categorização por fórum → `output_manuals` |
| 24 | QA COAF | Gauge 91.99% + Monitorias/Tickets/Drivers | QS + PLAYVOX | MANUAL | |
| 25 | Reports by Nubankers/MLRO | Stacked bar (por fonte) + line (alertas manuais MLRO) | DB→SHEETS (`output_automatics`) + SHEETS-MANUAL (`output_manuals`) | MANUAL | |
| 26 | Financial Crime Risks | — | STATIC | STATIC (governança + assinatura) | |

---

## Resumo: Fontes × Slides

| Fonte | Slides |
|-------|--------|
| Fonte | Slides |
|-------|--------|
| STATIC | 1, 2, 9, 14, 21, 26 |
| JIRA board MLRO → MANUAL | 3, 4, 5, 6, 7, 8 ✅ |
| MANUAL (notas narrativas) | notas em 10, 11, 15, 17, 18, 19, 22, 23, 24, 25 |
| DB→SHEETS (Databricks → `output_automatics`) | 12 ✅, 25 (gráfico esquerdo) |
| SLACK `#comissao-de-risco-kyc-aml` → SHEETS-MANUAL | 23 ✅ |
| SHEETS-MANUAL (`output_manuals`) | 25 (gráfico direito) |
| QuickSight | 10, 11, 13, 15, 16, 17, 19, 20, 22, 24 (parte) |
| Planilha Dossiê SPA | 18 ✅ |
| PlayVox | 24 (parte) |

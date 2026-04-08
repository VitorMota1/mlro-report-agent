# Fontes de Dados do MLRO Report

## Visão Geral do Pipeline

```
Databricks Notebook ──┐
                      ├──▶ Google Sheets "MLRO Monthly Report" ──▶ Google Slides
Jira AMLD Export ─────┘         │
                                │
Planilha "Dossiê SPA" ─────────┤
                                │
QuickSight Dashboard ───────────┘ (screenshots/embeds nos slides)
                                │
PlayVox (QA system) ────────────┘
```

## 1. Databricks Notebook

**Fonte primária de métricas automatizadas (PEP, Sanctions, etc.).**

- **Workspace**: `nubank-e2-general.cloud.databricks.com`
- **Notebook ID**: `1971106302956783`
- **URL**: https://nubank-e2-general.cloud.databricks.com/editor/notebooks/1971106302956783?o=2093534396923660

O notebook roda queries contra tabelas do Databricks e popula a aba `tbl_Databricks` da planilha.

### Métricas geradas automaticamente:
- PEP (Onboarding, Ongoing, Rejected)
- PEP High Level (por cargo, Titular/Related)
- Sanction Alerts e True Match
- EDD (Ongoing, UBO, Company, Investments KYC)
- Big Picture (NuPag, NuInvest, NuCrypto × Reported/Clear/Canceled)
- Cases Escalated

### Fluxo:
1. Rodar o notebook no Databricks
2. Dados fluem para `tbl_Databricks`
3. Tab `m__data` processa automaticamente
4. Tab `output_automatics` gera os gráficos (linkados ao Google Slides)

## 2. Jira (Projeto AMLD)

**Denúncias de Nubankers sobre atividades suspeitas.**

- Projeto Jira: `AMLD`
- Campos: Chave, Resumo, Customer ID, Responsável, Relator, Status, Resolução, Descrição, Tipo de Demanda, Prioridade, CPF/CNPJ
- Equipes relatoras: Ops Defense, Fraude (FinCrime), AML, Investigative Operations, Xpeer, Xtronaut, etc.
- Dados vão para tab `tbl_DenunciasNubankers`

## 3. Google Sheets — Motor de Cálculo

**Spreadsheet ID**: `1_CkseIf4UIcdnIhiKWc8ovmcBQuW1_ffQipmSE_Z340`

### Tabs de Input
| Tab | Fonte | Atualização |
|-----|-------|-------------|
| `tbl_Databricks` | Notebook Databricks | Automática |
| `tbl_DenunciasNubankers` | Jira AMLD export | Manual/Export |

### Tab de Controle
| Tab | Variáveis |
|-----|-----------|
| `c__main` | `Model Start` (Jul/25), `Model End`, `Current Month Report`, `Dash Start`, `Current Date Slides` |

### Tab de Processamento
| Tab | Função |
|-----|--------|
| `m__data` | ~283 colunas, ~1724 linhas. Processa todas as métricas por mês. Estrutura: Metric / Parameter 1-3 / Window / Jul25...Feb26 |

### Tabs de Output
| Tab | Função |
|-----|--------|
| `output_automatics` | Gráficos que atualizam automaticamente |
| `output_manuals` | Gráficos que precisam de input manual |

## 4. Planilha "Dossiê SPA Gerados — Acompanhamento"

**Spreadsheet ID**: `1di9PJLWHjufFoe2MhXi1dayYHFkYEkKF4QnF1dUbzSQ`
**URL**: https://docs.google.com/spreadsheets/d/1di9PJLWHjufFoe2MhXi1dayYHFkYEkKF4QnF1dUbzSQ

Fonte de dados para o **Slide 18 (SPA Reports)**. Contagem de CIDs únicos por mês.

| Tab | Slide 18 Chart | Descrição |
|-----|----------------|-----------|
| `CIDs SPA (PJ)` | PJ | Dossiês SPA de PJs por CNPJ |
| `CIDs SPA (PJ) Fonética` | PJ Phonetics | PJs detectados por fonética do nome |
| `CIDs SPA (PF)` | PF | Dossiês SPA de PFs |
| `Contrapartes SPA` | Counterparties | Contrapartes identificadas |
| `Consolidado` | — | Visão consolidada de todos os dossiês |
| `Resume CIDs SPA (PJ)` | — | Resumo PJ |
| `Resume CIDs SPA (PJ) Fonética` | — | Resumo PJ Fonética |
| `Resume CIDs SPA (PF)` | — | Resumo PF |

## 5. QuickSight Dashboard

**Dashboard ID**: `35046a00-8bd2-438b-b9f1-b9616121178e`
**Sheet ID**: `35046a00-8bd2-438b-b9f1-b9616121178e_eb2dc5e1-15ba-4595-822d-25287d7a0523`
**Account**: `nu-qs-prod`
**URL**: https://us-east-1.quicksight.aws.amazon.com/sn/account/nu-qs-prod/dashboards/35046a00-8bd2-438b-b9f1-b9616121178e

Charts dos slides (screenshots/embeds):
- EDD PF/PJ queues (slides 10-11)
- PEP High Level Positions (slide 13)
- Effectiveness of Alerts — NuPag, NuInvest, NuCrypto (slides 15-17)
- Report Breaches 24h (slide 19)
- Sanctions (slide 20)
- MLRO Deliberations — KPIs + donut + stacked bar (slide 22)

## 6. PlayVox (QA System)

Fonte para parte do **Slide 24 (QA COAF)**. O scorecard "Quality stats" e "Nota de Quality do mês" vêm do sistema PlayVox, que calcula o percentual de qualidade automaticamente via scorecards.

## 5. Google Slides — Apresentação Final

Cada mês é uma nova cópia do template, com ID único.

### Reports existentes (pasta Drive `1G2bH4K79paGpGS5gHeasIWjBmU0gOoD2`):
| Mês | Presentation ID |
|-----|-----------------|
| 04.2026 | `1lnn0AP6WZA8n9UyKOOJzDtr_ng0ZW3eWfYFwRFa6otE` |
| 03.2026 | `1I2lbbhKtrhzfpNA9qbWemPEOL_4V0BBtI8zYfi0kMo4` |
| 02.2026 | `1iuRSn6Kq0_zhq5nOg9x65p3WWgLcGop0SxrZF9HLRJU` |
| 01.2026 | `1NXRngwkyKWoSzLhBUXwW3tzwTwN_8WArYWmZ4eG6jWU` |
| 12.2025 | `1FWjghvRbwmXp983TO0qXQUYzUlOyhjBX-T4aH5s2pPY` |
| 11.2025 | `1NLD33mlZe6Eh3TskHjU4Kxf4qtjWdlxhJ0bXnvN-1HE` |
| 10.2025 | `1MJ64wTUQJ7VYz2QkgIpVIlJgQAbDwKC3OP4jkwzrZeg` |
| 09.2025 | `1ooXbPJI4wPdMJQthAWxz1hMqL4kNbQJw0jivqng9tlw` |

### Template de referência:
- **Revamp MLRO**: `12Nyfi8kLjg_t3kqmzUZGikjBaxZEXcNWtqDQYOrUkvM`

## Processo de Atualização Mensal

### Step 1: Atualizar dados no Databricks
Rodar o notebook de métricas

### Step 2: Atualizar gráficos automáticos
Atualizar variáveis em `c__main` (se necessário). O notebook atualiza `tbl_Databricks` → `m__data` → `output_automatics`

### Step 3: Atualizar gráficos manuais
Preencher valores em `output_manuals` e `c__main` para as métricas manuais

### Step 4: Atualizar slides
Habilitar atualização de gráficos linkados no Google Slides (3 pontinhos → ver objetos linkados)

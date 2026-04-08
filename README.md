# MLRO Report Agent

**Agente especializado na geração e automação do MLRO Monthly Report** — relatório mensal que consolida indicadores de AML/CFT (Anti-Money Laundering / Counter-Terrorist Financing) para o Board do Nubank.

## Contexto

O **MLRO (Money Laundering Reporting Officer)** é a figura central na governança de PLD/FT. O relatório mensal consolida:

- **Highlights**: Operações da Polícia Federal, eventos críticos, tendências e atualizações regulatórias
- **Indicadores de Clientes**: EDD (Enhanced Due Diligence) PF/PJ, PEPs (Pessoas Politicamente Expostas)
- **Indicadores MSAC**: Efetividade de alertas NuPag, NuInvest, NuCrypto, SPA Reports
- **Indicadores do Processo MLRO**: Deliberações, qualidade de reports ao COAF, sanções, breaches

## Pipeline de Dados

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Databricks     │     │  Google Sheets   │     │  QuickSight     │     │  Google Slides  │
│  (métricas)     │────▶│  (processamento) │────▶│  (gráficos)     │────▶│  (apresentação) │
└─────────────────┘     └─────────────────┘     └─────────────────┘     └─────────────────┘
  Notebook ETL           tbl_Databricks           Dashboard MLRO          Report mensal
  queries SQL            tbl_Denuncias            Charts embed            26 slides
                         m__data (calc)
                         output_automatics
                         output_manuals
```

### Fontes de Dados

| Fonte | Tipo | Descrição |
|-------|------|-----------|
| Databricks Notebook | ETL | Métricas automatizadas → `tbl_Databricks` |
| Jira (AMLD) | Manual/Export | Denúncias de Nubankers → `tbl_DenunciasNubankers` |
| QuickSight Dashboard | Gráficos | Maioria dos charts do report |
| Inputs Manuais | Planilha | Operações PF, deliberações MLRO, QA COAF |

### Spreadsheet (Motor de Cálculo)

| Tab | Função |
|-----|--------|
| `c__main` | Variáveis globais (mês corrente, período do dash) |
| `m__data` | Processamento: métricas por mês, categorização, totais |
| `tbl_Databricks` | Input automático do notebook Databricks |
| `tbl_DenunciasNubankers` | Input de denúncias (Jira AMLD) |
| `output_automatics` | Gráficos automatizados (atualizam com notebook) |
| `output_manuals` | Gráficos manuais (preenchidos mensalmente) |

## Seções do Report (26 slides)

### 1. Highlights (Slides 2-8)
- Operações relevantes da PF (Carbono Oculto, Magna Fraus, Poço de Lobato, etc.)
- Eventos críticos (RFB, Sintonia PCC, Freedom CV)
- Regras de efetividade
- Visita/cooperação com COAF
- Tags e procedimentos novos

### 2. Indicadores - Clientes (Slides 9-13)
- **EDD PF**: Enhanced Due Diligence Pessoa Física (Ongoing, UBO, Company, Investments KYC)
- **EDD PJ**: Enhanced Due Diligence Pessoa Jurídica
- **PEP**: Onboarding, Ongoing, Rejected (Total e High Level)
- **PEP High Level Positions**: Senador, Governador, Presidente, etc.

### 3. Indicadores - MSAC (Slides 14-20)
- **NuPag**: Alertas, Reported, Clear, Canceled (conversão de alertas)
- **NuInvest**: Mesma estrutura
- **NuCrypto**: Mesma estrutura + OnChain
- **SPA Reports**: PJ, PJ Phonetics, PF, Counterparties
- **Report Breaches 24h**: Atrasos regulatórios no envio ao COAF
- **Sanctions**: Alerts e True Match (Onboarding/Ongoing)

### 4. Indicadores - Processo MLRO (Slides 21-26)
- **Deliberações MLRO**: Cases escalated, decisões por fórum (AML Exit, Reputational Risk, Sanctions, KYC-PEP)
- **QA Reports COAF**: % qualidade (OPS QA vs MLRO QA)
- **Reports by Nubankers**: Denúncias internas (Ops Defense, Fraude, AML Gov, Google Forms, Conta Global, Ofícios Judiciais, Cripto)
- **Financial Crime Risks**: Estrutura de governança

## Métricas Principais

### Automáticas (via Databricks)
| Métrica | Parâmetros |
|---------|------------|
| PEP | Onboarding, Ongoing, Rejected (por mês) |
| PEP High Level | Titular/Related × Onboarding/Ongoing × Cargo |
| PEP Rejected | Final decision Onboarding/Ongoing |
| Sanction Alerts | Onboarding, Ongoing |
| Sanction True Match | Onboarding, Ongoing |
| EDD | Ongoing, UBO Qualification, Company Acquisition/Qualification, Investments KYC |
| Big Picture | NuPag/NuInvest/NuCrypto × Reported/Clear/Canceled |
| Cases Escalated | NuPag, NuInvest, NuCrypto |

### Manuais
| Métrica | Parâmetros |
|---------|------------|
| Alerts created by MLRO | Total por mês |
| MLRO Deliberations | AML Exit Mgmt Forum, Reputational Risk Commission, Sanctions, KYC-PEP/Media |
| EDD PF/PJ | Ongoing, queues |
| QA Reports COAF | % OPS QA, % MLRO QA |
| Report Breaches 24h | Casos de atraso e root cause |
| Highlights | Operações PF, eventos críticos, atualizações regulatórias |

## Estrutura do Repositório

```
mlro-report-agent/
├── .cursor/rules/
│   └── mlro-agent.mdc              # Regra do agente especialista
├── docs/
│   ├── 01-report-structure.md       # Estrutura completa do report
│   ├── 02-data-sources.md           # Fontes de dados e pipelines
│   ├── 03-metrics-catalog.md        # Catálogo de métricas
│   ├── 04-quicksight-charts.md      # Mapeamento dos gráficos QuickSight
│   └── 05-monthly-checklist.md      # Checklist de geração mensal
├── scripts/
│   └── update_report.py             # Script de atualização automatizada
├── queries/
│   └── databricks_metrics.sql       # Query de métricas (referência)
├── notebooks/                       # Notebooks Databricks (referência)
├── data/                            # Dados de exemplo/referência
└── README.md
```

## Links

- [QuickSight Dashboard](https://us-east-1.quicksight.aws.amazon.com/sn/account/nu-qs-prod/dashboards/35046a00-8bd2-438b-b9f1-b9616121178e/sheets/35046a00-8bd2-438b-b9f1-b9616121178e_eb2dc5e1-15ba-4595-822d-25287d7a0523)
- [Pasta Google Drive (Reports)](https://drive.google.com/drive/folders/1G2bH4K79paGpGS5gHeasIWjBmU0gOoD2)
- [Spreadsheet MLRO Monthly Report](https://docs.google.com/spreadsheets/d/1_CkseIf4UIcdnIhiKWc8ovmcBQuW1_ffQipmSE_Z340)
- [Report Exemplo (04.2026)](https://docs.google.com/presentation/d/1lnn0AP6WZA8n9UyKOOJzDtr_ng0ZW3eWfYFwRFa6otE/edit)
- [Revamp MLRO](https://docs.google.com/presentation/d/12Nyfi8kLjg_t3kqmzUZGikjBaxZEXcNWtqDQYOrUkvM)

## Regulamentação

- **Circular BCB 3.978/2020**: PLD/FT — estrutura, políticas e procedimentos
- **CVM Resolução 50**: Prevenção à lavagem de dinheiro no mercado de capitais
- **COAF**: Conselho de Controle de Atividades Financeiras (destinatário dos reports)
- **Portaria 566**: Regulamentação sobre apostas ilegais (bets)

## Responsáveis

- **MLRO**: Roger Miura (AML Expert)
- **Estrutura**: Financial Crime Risks → AML/CTF Director delegation
- **Times envolvidos**: OPS Defense, AML Analytics, Fraud, Governance, BIS Engineering

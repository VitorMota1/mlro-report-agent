# Mapeamento QuickSight → Slides

## Dashboard

- **Account**: `nu-qs-prod`
- **Dashboard ID**: `35046a00-8bd2-438b-b9f1-b9616121178e`
- **Sheet ID**: `35046a00-8bd2-438b-b9f1-b9616121178e_eb2dc5e1-15ba-4595-822d-25287d7a0523`
- **URL**: [QuickSight MLRO Dashboard](https://us-east-1.quicksight.aws.amazon.com/sn/account/nu-qs-prod/dashboards/35046a00-8bd2-438b-b9f1-b9616121178e/sheets/35046a00-8bd2-438b-b9f1-b9616121178e_eb2dc5e1-15ba-4595-822d-25287d7a0523)

## Charts por Seção

### Indicadores de Clientes
| Chart | Slide | Tipo Provável | Notas |
|-------|-------|---------------|-------|
| EDD PF | 10 | Bar/Line chart | Dashboard anterior descontinuado; OPS construindo novo |
| EDD PJ | 11 | Bar/Line chart | Volume high/medium risk PJ |
| PEP Total | 12 | Stacked bar chart | Onboarding + Ongoing, série temporal |
| PEP High Level | 12 | Stacked bar chart | Related + Titular, série temporal |
| PEP Positions | 13 | Table/Heatmap | Breakdown por cargo político |

### Indicadores MSAC
| Chart | Slide | Tipo Provável | Notas |
|-------|-------|---------------|-------|
| NuPag Alerts | 15 | Bar chart | Reported/Clear/Canceled por mês |
| NuInvest Alerts | 16 | Bar chart | Mesma estrutura |
| NuCrypto Alerts | 17 | Bar chart | + OnChain considerations |
| SPA Reports | 18 | Multi-series bar | PJ, PJ Phonetics, PF, Counterparties |
| Report Breaches 24h | 19 | Table/timeline | Casos específicos com root cause |
| Sanctions | 20 | Bar chart | Alerts + True Match por mês |

### Indicadores Processo MLRO
| Chart | Slide | Tipo Provável | Notas |
|-------|-------|---------------|-------|
| MLRO Deliberations | 22 | Bar chart | Cases escalated por mês |
| Deliberations by Forum | 23 | Table | Recorrente por fórum |
| QA COAF | 24 | Gauge/Bar | % OPS vs % MLRO (migrado de Looker) |
| Nubanker Reports | 25 | Stacked bar | Por fonte (Ops, Fraude, AML, Forms, etc.) |

## Notas sobre Migração

- O dashboard de Quality foi migrado de **Looker** para **QuickSight**
- O dashboard de controle de Engineering (report breaches) está em avaliação para migração para QuickSight
- O dashboard antigo de EDD PF foi descontinuado; novo em construção pelo OPS

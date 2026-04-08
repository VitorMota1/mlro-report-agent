# Catálogo de Métricas MLRO

## Métricas Automáticas (Databricks → Sheets)

### PEP — Politically Exposed Persons

| Métrica | Parâmetro 1 | Descrição |
|---------|-------------|-----------|
| PEP Onboarding | Onboarding | Novos clientes PEP identificados no onboarding |
| PEP Ongoing | Ongoing | Clientes PEP identificados em monitoramento contínuo |
| PEP Rejected Onboarding | Final decision Onboarding | PEPs rejeitados no onboarding |
| PEP Rejected Ongoing | Final decision Ongoing | PEPs rejeitados no ongoing |

### PEP High Level

Breakdown por cargo político de alto nível:

| Cargo | Escopo |
|-------|--------|
| Presidente da República | Nacional |
| Vice-Presidente da República | Nacional |
| Senador | Nacional |
| Deputado Federal (Suplente) | Nacional |
| Governador de Estado e DF | Regional |
| Vice Governador | Regional |

Dimensões: Titular/Related × Onboarding/Ongoing

### Sanctions

| Métrica | Descrição |
|---------|-----------|
| Sanction Alerts Onboarding | Alertas de sanções no onboarding |
| Sanction Alerts Ongoing | Alertas de sanções em monitoramento |
| Sanction True Match Onboarding | Matches verdadeiros (onboarding) |
| Sanction True Match Ongoing | Matches verdadeiros (ongoing) |

### EDD — Enhanced Due Diligence

| Métrica | Descrição |
|---------|-----------|
| EDD Ongoing | Casos EDD em andamento |
| EDD UBO Qualification | Qualificação de UBO (Ultimate Beneficial Owner) |
| EDD Company Acquisition | Aquisição de empresas |
| EDD Company Qualification | Qualificação de empresas |
| EDD Investments KYC | KYC de investimentos |

### Big Picture — Effectiveness of Alerts

Por produto (NuPag, NuInvest, NuCrypto-OnChain):

| Métrica | Descrição |
|---------|-----------|
| Reported | Casos reportados ao COAF |
| Clear | Casos considerados limpos |
| Canceled | Casos cancelados |

### Cases Escalated

| Produto | Descrição |
|---------|-----------|
| NuPag | Casos escalados ao MLRO (pagamentos) |
| NuInvest | Casos escalados ao MLRO (investimentos) |
| NuCrypto | Casos escalados ao MLRO (cripto) |

---

## Métricas Manuais

### Alerts Created by MLRO
Total de alertas manuais criados mensalmente pelo MLRO (ex: operações PF, mídia adversa).

### MLRO Deliberations (por fórum recorrente)

| Fórum | Frequência | Descrição |
|-------|------------|-----------|
| AML Exit Mgmt Forum | Mensal | Saídas de clientes por AML |
| Reputational Risk Commission | Mensal | Mídia adversa com exposição |
| Sanctions | Ad-hoc | Casos de sanções para deliberação |
| KYC - PEP/Media | Ad-hoc | Casos PEP/mídia adversa |

### QA Reports COAF

| Métrica | Descrição |
|---------|-----------|
| % QA OPS | Percentual de qualidade avaliado pelo time de Quality OPS |
| % QA MLRO | Percentual de qualidade avaliado pelo MLRO |
| Avaliação | Satisfatória se ambos acima do threshold |

### Report Breaches 24h
Número de reports ao COAF com atraso superior a 24h da decisão. Inclui root cause analysis.

### Internal Reports by Nubankers

| Fonte | Descrição |
|-------|-----------|
| Ops Defense | Denúncias do time de operações |
| Fraude | Denúncias do time de fraude (FinCrime) |
| AML Gov / MLRO | Denúncias do MLRO e governança AML |
| Google Forms | Formulários externos |
| Conta Global | Denúncias de conta global |
| Ofícios Judiciais | Ordens judiciais recebidas |
| Cripto | Denúncias relacionadas a cripto |

---

## Janela Temporal

- **Model Start**: Jul/25
- **Série temporal padrão**: últimos 8 meses
- **Granularidade**: Mensal
- **Atualização**: Mensal (até dia ~10 do mês seguinte)

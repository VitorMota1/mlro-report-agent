# Checklist de Geração Mensal do MLRO Report

## Pré-requisitos
- [ ] Mês anterior encerrado (dados completos)
- [ ] Acesso ao Databricks, Google Sheets, QuickSight e Google Slides

## Step 1 — Atualizar Dados (Databricks)
- [ ] Rodar o notebook de métricas MLRO no Databricks
- [ ] Verificar se os dados fluíram para a aba `tbl_Databricks` da planilha
- [ ] Validar completude: todas as métricas têm dados do mês corrente

## Step 2 — Atualizar Variáveis (Google Sheets)
- [ ] Abrir aba `c__main`
- [ ] Atualizar `Current Month Report` para o mês corrente (ex: Mar/26)
- [ ] Atualizar `Current Date Slides` para o texto do slide (ex: March, 2026)
- [ ] Verificar `Model End` se necessário
- [ ] Confirmar que `m__data` calculou corretamente

## Step 3 — Atualizar Gráficos Automáticos
- [ ] Verificar aba `output_automatics`
- [ ] Confirmar que os gráficos PEP, Sanctions, etc. estão atualizados
- [ ] Validar que não há valores zerados inesperados

## Step 4 — Preencher Dados Manuais
- [ ] Atualizar aba `output_manuals`:
  - [ ] Alerts created by MLRO (total do mês)
  - [ ] MLRO Deliberations por fórum (AML Exit, Reputational Risk, Sanctions, KYC-PEP)
- [ ] Preencher dados de EDD PF/PJ (se disponíveis)
- [ ] Atualizar QA COAF (% OPS e % MLRO)

## Step 5 — Criar Apresentação
- [ ] Fazer cópia do report do mês anterior na pasta Drive
- [ ] Renomear para "MLRO Monthly Report - MM.YYYY"
- [ ] Atualizar título na capa (mês e ano)

## Step 6 — Atualizar Gráficos nos Slides
- [ ] Abrir a apresentação
- [ ] Clicar nos 3 pontinhos → ver objetos linkados
- [ ] Atualizar todos os gráficos linkados à planilha
- [ ] Verificar que os dados nos gráficos correspondem ao mês corrente

## Step 7 — Atualizar Conteúdo Narrativo
- [ ] **Highlights**: Adicionar novas operações PF, eventos críticos, atualizações regulatórias
- [ ] **EDD PF/PJ**: Atualizar notas sobre filas e volumes
- [ ] **NuPag/NuInvest/NuCrypto**: Atualizar notas sobre alertas
- [ ] **SPA Reports**: Atualizar tendências
- [ ] **Report Breaches**: Documentar incidentes do mês (se houver)
- [ ] **MLRO Deliberations**: Atualizar notas sobre mudanças de processo
- [ ] **QA COAF**: Atualizar avaliação e número de samples
- [ ] **Nubanker Reports**: Atualizar notas sobre processo de mídia/operações

## Step 8 — Screenshots QuickSight
- [ ] Acessar dashboard QuickSight com filtro do mês corrente
- [ ] Capturar screenshots dos gráficos que não são linkados via Sheets
- [ ] Inserir nos slides correspondentes

## Step 9 — Revisão Final
- [ ] Revisar todos os slides — dados consistentes?
- [ ] Verificar se não há dados do mês anterior esquecidos
- [ ] Validar totais e percentuais
- [ ] Confirmar que todos os gráficos têm dados do mês corrente
- [ ] Revisar ortografia e formatação

## Step 10 — Distribuição
- [ ] Mover para a pasta compartilhada no Drive
- [ ] Notificar stakeholders (Board, AML/CTF Director)

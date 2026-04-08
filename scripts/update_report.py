"""
MLRO Report Agent — Script de referência para atualização do report.

Este script documenta o fluxo de atualização mensal e serve como
referência para automação futura. A execução real depende dos MCPs
do Google Workspace e Databricks.

Uso via Cursor Agent:
  1. O agente lê a planilha via MCP (sheets_getText/sheets_getRange)
  2. Verifica se o mês corrente tem dados
  3. Atualiza variáveis em c__main se necessário
  4. Gera/atualiza slides via MCP (slides_*)
"""

from dataclasses import dataclass
from typing import Optional


SPREADSHEET_ID = "1_CkseIf4UIcdnIhiKWc8ovmcBQuW1_ffQipmSE_Z340"
QUICKSIGHT_DASHBOARD_ID = "35046a00-8bd2-438b-b9f1-b9616121178e"
DRIVE_FOLDER_ID = "1G2bH4K79paGpGS5gHeasIWjBmU0gOoD2"

MONTH_NAMES = {
    1: "January", 2: "February", 3: "March", 4: "April",
    5: "May", 6: "June", 7: "July", 8: "August",
    9: "September", 10: "October", 11: "November", 12: "December",
}

SHEETS = {
    "control": "c__main",
    "data": "m__data",
    "output_auto": "output_automatics",
    "output_manual": "output_manuals",
    "databricks": "tbl_Databricks",
    "denuncias": "tbl_DenunciasNubankers",
}


@dataclass
class ReportConfig:
    month: int
    year: int
    model_start: str = "Jul/25"

    @property
    def month_label(self) -> str:
        short_year = str(self.year)[-2:]
        return f"{MONTH_NAMES[self.month][:3]}/{short_year}"

    @property
    def slides_date(self) -> str:
        return f"{MONTH_NAMES[self.month]}, {self.year}"

    @property
    def report_title(self) -> str:
        return f"MLRO Monthly Report - {self.month:02d}.{self.year}"


@dataclass
class MetricSnapshot:
    """Snapshot de métricas de um mês para validação."""
    month: str
    pep_onboarding: Optional[int] = None
    pep_ongoing: Optional[int] = None
    pep_rejected_onboarding: Optional[int] = None
    pep_rejected_ongoing: Optional[int] = None
    sanctions_alerts_onboarding: Optional[int] = None
    sanctions_alerts_ongoing: Optional[int] = None
    sanctions_true_match_onboarding: Optional[int] = None
    sanctions_true_match_ongoing: Optional[int] = None
    mlro_manual_alerts: Optional[int] = None

    def has_automated_data(self) -> bool:
        return self.pep_onboarding is not None and self.pep_onboarding > 0

    def has_manual_data(self) -> bool:
        return self.mlro_manual_alerts is not None


REPORT_SECTIONS = [
    {"section": "cover", "slides": [1], "type": "static"},
    {"section": "highlights", "slides": [2, 3, 4, 5, 6, 7, 8], "type": "manual"},
    {"section": "indicators_customers", "slides": [9, 10, 11, 12, 13], "type": "mixed"},
    {"section": "indicators_msac", "slides": [14, 15, 16, 17, 18, 19, 20], "type": "quicksight"},
    {"section": "indicators_mlro_process", "slides": [21, 22, 23, 24, 25, 26], "type": "mixed"},
]

EXISTING_REPORTS = {
    "04.2026": "1lnn0AP6WZA8n9UyKOOJzDtr_ng0ZW3eWfYFwRFa6otE",
    "03.2026": "1I2lbbhKtrhzfpNA9qbWemPEOL_4V0BBtI8zYfi0kMo4",
    "02.2026": "1iuRSn6Kq0_zhq5nOg9x65p3WWgLcGop0SxrZF9HLRJU",
    "01.2026": "1NXRngwkyKWoSzLhBUXwW3tzwTwN_8WArYWmZ4eG6jWU",
    "12.2025": "1FWjghvRbwmXp983TO0qXQUYzUlOyhjBX-T4aH5s2pPY",
    "11.2025": "1NLD33mlZe6Eh3TskHjU4Kxf4qtjWdlxhJ0bXnvN-1HE",
    "10.2025": "1MJ64wTUQJ7VYz2QkgIpVIlJgQAbDwKC3OP4jkwzrZeg",
    "09.2025": "1ooXbPJI4wPdMJQthAWxz1hMqL4kNbQJw0jivqng9tlw",
}

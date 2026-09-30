import pandas as pd
from typing import List, Dict
from utils import validate_inputs

class ReportGenerator:
    def __init__(self, portfolio: Dict[str, float], total_returns: List[float], max_drawdowns: List[float]):
        self.portfolio = validate_inputs(portfolio)
        self.total_returns = validate_inputs(total_returns)
        self.max_drawdowns = validate_inputs(max_drawdowns)

    def generate_report(self) -> pd.DataFrame:
        report = pd.DataFrame({'Portfolio': self.portfolio, 'Total Return': self.total_returns, 'Max Drawdown': self.max_drawdowns})
        return report

    def save_report(self, file_path: str) -> None:
        report = self.generate_report()
        report.to_csv(file_path, index=False)

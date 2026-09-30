from typing import Dict, List
from portfolio_management import PortfolioManager
from utils import validate_inputs

# Constants
TAX_RATE = 0.25
MIN_SELL_VALUE = 1000

class TaxLossHarvesting:
    def __init__(self, portfolio: PortfolioManager, tax_rate: float = TAX_RATE):
        self.portfolio = portfolio
        self.tax_rate = tax_rate
        self.sold_symbols = []

    def harvest(self) -> Dict[str, float]:
        sell_values = self.calculate_sell_values()
        sold_balances = {symbol: balance for symbol, balance in self.portfolio.get_balances().items() if symbol in sell_values}
        self.portfolio.remove_symbols([symbol for symbol, _ in sold_balances.items()])
        return sold_balances

    def calculate_sell_values(self) -> Dict[str, float]:
        symbols = self.portfolio.get_symbols()
        sell_values = {symbol: balance * (1 - self.tax_rate) for symbol, balance in self.portfolio.get_balances().items() if balance < MIN_SELL_VALUE}
        return sell_values

    def get_sold_symbols(self) -> List[str]:
        return self.sold_symbols

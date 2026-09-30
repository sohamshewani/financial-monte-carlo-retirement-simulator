import pandas as pd
from typing import List, Dict
from utils import validate_input, sanitize_symbols

# Constants
MIN_BALANCE = 10000
MAX_PORTFOLIO_SIZE = 100

class PortfolioManager:
    def __init__(self, symbols: List[str], balances: Dict[str, float]):
        self.symbols = sanitize_symbols(symbols)
        self.balances = validate_input(balances)

    def add_symbol(self, symbol: str, balance: float) -> None:
        self.symbols.append(symbol)
        self.balances[symbol] = balance

    def remove_symbol(self, symbol: str) -> None:
        if symbol in self.symbols:
            del self.balances[symbol]
            self.symbols.remove(symbol)

    def get_total_value(self) -> float:
        return sum(self.balances.values())

    def get_symbols(self) -> List[str]:
        return self.symbols

    def get_balances(self) -> Dict[str, float]:
        return self.balances

    def validate_input(self, balances: Dict[str, float]) -> Dict[str, float]:
        for symbol, balance in balances.items():
            if symbol not in self.symbols:
                raise ValueError(f'Symbol {symbol} not found in portfolio')
            if balance < 0:
                raise ValueError('Balance cannot be negative')
        return balances

    def sanitize_symbols(self, symbols: List[str]) -> List[str]:
        return [symbol.upper() for symbol in symbols if symbol.isalpha()]

    def rebalance(self, new_balances: Dict[str, float]) -> None:
        self.balances = self.validate_input(new_balances)

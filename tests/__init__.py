from unittest.mock import MagicMock
from portfolio_management import PortfolioManager
from monte_carlo import MonteCarloSimulator
from tax_loss_harvesting import TaxLossHarvesting
from reporting import ReportGenerator

# Mocks
portfolio_manager = PortfolioManager(symbols=[], balances={})
monte_carlo_simulator = MonteCarloSimulator(portfolio=portfolio_manager)
tax_loss_harvesting = TaxLossHarvesting(portfolio=portfolio_manager)
report_generator = ReportGenerator(portfolio={}, total_returns=[], max_drawdowns=[])

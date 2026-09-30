from portfolio_management import PortfolioManager
from monte_carlo import MonteCarloSimulator
from tax_loss_harvesting import TaxLossHarvesting
from reporting import ReportGenerator
from utils import validate_inputs
from config import get_config
import pandas as pd
from examples import example_input

# Load configuration
config = get_config('portfolio')
symbols = config.get('symbols')
balances = {symbol: config.get(symbol, 0) for symbol in symbols}

# Initialize portfolio
portfolio = PortfolioManager(symbols, balances)

# Initialize Monte Carlo simulator
mc_simulator = MonteCarloSimulator(portfolio, simulations=config.get('simulations'), years=config.get('years'))

# Harvest tax losses
tax_loss_harvesting = TaxLossHarvesting(portfolio)
sold_symbols = tax_loss_harvesting.harvest()

# Generate report
report_generator = ReportGenerator(portfolio.get_balances(), mc_simulator.get_total_returns(), [0.05] * len(mc_simulator.get_total_returns()))
report = report_generator.generate_report()
report.to_csv('report.csv', index=False)

import unittest
from tax_loss_harvesting import TaxLossHarvesting
from portfolio_management import PortfolioManager
from utils import validate_inputs

class TestTaxLossHarvesting(unittest.TestCase):
    def setUp(self):
        self.portfolio = PortfolioManager(symbols=['AAPL', 'GOOGL', 'AMZN'], balances={'AAPL': 10000, 'GOOGL': 5000, 'AMZN': 20000})
        self.tlh = TaxLossHarvesting(self.portfolio)

    def test_harvest(self):
        sold_symbols = self.tlh.harvest()
        self.assertIn('AAPL', sold_symbols)
        self.assertIn('GOOGL', sold_symbols)
        self.assertNotIn('AMZN', sold_symbols)

    def test_calculate_sell_values(self):
        sell_values = self.tlh.calculate_sell_values()
        self.assertIn('AAPL', sell_values)
        self.assertIn('GOOGL', sell_values)
        self.assertNotIn('AMZN', sell_values)

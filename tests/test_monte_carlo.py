import unittest
from monte_carlo import MonteCarloSimulator
from portfolio_management import PortfolioManager
from utils import validate_inputs

class TestMonteCarloSimulator(unittest.TestCase):
    def setUp(self):
        self.portfolio = PortfolioManager(symbols=['AAPL', 'GOOGL', 'AMZN'], balances={'AAPL': 10000, 'GOOGL': 5000, 'AMZN': 20000})
        self.mc = MonteCarloSimulator(self.portfolio)

    def test_run_simulation(self):
        results = self.mc.run_simulation()
        self.assertEqual(len(results), self.mc.simulations)
        self.assertEqual(len(results[0]), self.mc.years + 1)

    def test_get_results(self):
        results = self.mc.get_results()
        self.assertEqual(len(results), self.mc.simulations)
        self.assertEqual(len(results[0]), self.mc.years + 1)

    def test_get_total_returns(self):
        total_returns = self.mc.get_total_returns()
        self.assertEqual(len(total_returns), self.mc.simulations)

    def test_get_average_return(self):
        average_return = self.mc.get_average_return()
        self.assertGreaterEqual(average_return, 0)

    def test_get_max_drawdown(self):
        max_drawdown = self.mc.get_max_drawdown()
        self.assertGreaterEqual(max_drawdown, 0)

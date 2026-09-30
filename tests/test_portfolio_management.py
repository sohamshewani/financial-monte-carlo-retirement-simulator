import unittest
from portfolio_management import PortfolioManager, validate_input, sanitize_symbols

class TestPortfolioManager(unittest.TestCase):
    def test_init(self):
        symbols = ['AAPL', 'GOOGL', 'AMZN']
        balances = {'AAPL': 10000, 'GOOGL': 5000, 'AMZN': 20000}
        pm = PortfolioManager(symbols, balances)
        self.assertEqual(pm.get_symbols(), ['AAPL', 'GOOGL', 'AMZN'])
        self.assertEqual(pm.get_balances(), {'AAPL': 10000, 'GOOGL': 5000, 'AMZN': 20000})

    def test_add_symbol(self):
        symbols = ['AAPL', 'GOOGL', 'AMZN']
        balances = {'AAPL': 10000, 'GOOGL': 5000, 'AMZN': 20000}
        pm = PortfolioManager(symbols, balances)
        pm.add_symbol('MSFT', 15000)
        self.assertEqual(pm.get_symbols(), ['AAPL', 'GOOGL', 'AMZN', 'MSFT'])
        self.assertEqual(pm.get_balances(), {'AAPL': 10000, 'GOOGL': 5000, 'AMZN': 20000, 'MSFT': 15000})

    def test_remove_symbol(self):
        symbols = ['AAPL', 'GOOGL', 'AMZN']
        balances = {'AAPL': 10000, 'GOOGL': 5000, 'AMZN': 20000}
        pm = PortfolioManager(symbols, balances)
        pm.remove_symbol('GOOGL')
        self.assertEqual(pm.get_symbols(), ['AAPL', 'AMZN'])
        self.assertEqual(pm.get_balances(), {'AAPL': 10000, 'AMZN': 20000})

    def test_validate_input(self):
        symbols = ['AAPL', 'GOOGL', 'AMZN']
        balances = {'AAPL': 10000, 'GOOGL': 5000, 'AMZN': 20000}
        pm = PortfolioManager(symbols, balances)
        with self.assertRaises(ValueError):
            pm.validate_input({'AAPL': -10000, 'GOOGL': 5000, 'AMZN': 20000})

    def test_sanitize_symbols(self):
        symbols = ['AAPL', 'GOOgl', 'AMZN', '123', 'MSFT']
        sanitized_symbols = sanitize_symbols(symbols)
        self.assertEqual(sanitized_symbols, ['AAPL', 'GOOGL', 'AMZN', 'MSFT'])

import unittest
from reporting import ReportGenerator
from utils import validate_inputs

class TestReportGenerator(unittest.TestCase):
    def setUp(self):
        self.portfolio = {'AAPL': 10000, 'GOOGL': 5000, 'AMZN': 20000}
        self.total_returns = [0.1, 0.2, 0.3, 0.4, 0.5]
        self.max_drawdowns = [0.05, 0.1, 0.15, 0.2, 0.25]
        self.rg = ReportGenerator(self.portfolio, self.total_returns, self.max_drawdowns)

    def test_generate_report(self):
        report = self.rg.generate_report()
        self.assertEqual(len(report), 5)
        self.assertIn('Portfolio', report.columns)
        self.assertIn('Total Return', report.columns)
        self.assertIn('Max Drawdown', report.columns)

    def test_save_report(self):
        self.rg.save_report('test_report.csv')
        with open('test_report.csv', 'r') as file:
            lines = file.readlines()
        self.assertEqual(len(lines), 6)

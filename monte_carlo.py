import numpy as np
from typing import List, Dict
from portfolio_management import PortfolioManager
from utils import validate_inputs

# Constants
NUM_SIMULATIONS = 10000
YEARS_SIMULATED = 30

class MonteCarloSimulator:
    def __init__(self, portfolio: PortfolioManager, simulations: int = NUM_SIMULATIONS, years: int = YEARS_SIMULATED):
        self.portfolio = portfolio
        self.simulations = simulations
        self.years = years
        self.results = self.run_simulation()

    def run_simulation(self) -> List[List[float]]:
        returns = self.portfolio.get_returns()
        final_values = np.zeros((self.simulations, self.years + 1))
        initial_value = self.portfolio.get_total_value()
        final_values[:, 0] = initial_value * (1 + returns)

        for i in range(1, self.years + 1):
            final_values[:, i] = final_values[:, i - 1] * (1 + returns)

        return final_values.tolist()

    def get_results(self) -> List[List[float]]:
        return self.results

    def get_total_returns(self) -> List[float]:
        final_values = self.get_results()
        total_returns = [final[0] / initial - 1 for initial, final in zip(final_values[:, 0], final_values[:, -1])]
        return total_returns

    def get_average_return(self) -> float:
        return np.mean(self.get_total_returns())

    def get_max_drawdown(self) -> float:
        final_values = self.get_results()
        max_drawdowns = []
        for path in final_values:
            peak = path[0]
            drawdown = 0
            for value in path:
                if value > peak:
                    peak = value
                else:
                    drawdown = max(drawdown, (peak - value) / peak)
            max_drawdowns.append(drawdown)
        return np.mean(max_drawdowns)

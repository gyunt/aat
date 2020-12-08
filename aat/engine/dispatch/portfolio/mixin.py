from aat.core import Instrument, ExchangeType
from aat.strategy import Strategy

from .portfolio import Portfolio


class StrategyManagerPortfolioMixin(object):
    # *********************
    # Risk Methods        *
    # *********************
    def portfolio(self) -> Portfolio:
        return self._portfolio_mgr.portfolio()

    def positions(
        self,
        strategy: Strategy,
        instrument: Instrument = None,
        exchange: ExchangeType = None,
    ):
        return self._portfolio_mgr.positions(
            strategy=strategy, instrument=instrument, exchange=exchange
        )

    def priceHistory(self, instrument: Instrument = None):
        return self._portfolio_mgr.priceHistory(instrument=instrument)

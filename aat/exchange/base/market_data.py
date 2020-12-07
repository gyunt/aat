from abc import ABCMeta
from typing import List, AsyncGenerator, Any

from aat import Instrument, Event


class _MarketData(metaclass=ABCMeta):
    """internal only class to represent the streaming-source
    side of a data source"""

    async def instruments(self) -> List[Instrument]:
        """get list of available instruments"""
        return []

    async def subscribe(self, instrument) -> None:
        """subscribe to market data for a given instrument"""

    async def tick(self) -> AsyncGenerator[Any, Event]:
        """return data from exchange"""

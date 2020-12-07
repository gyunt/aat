from typing import Optional, List, Tuple

from aat.config import ExitRoutine
from aat.core import Event, Order, Trade, Position
from aat.core.handler import EventHandler
from ..base import ManagerBase


class RiskManager(ManagerBase):
    def __init__(self) -> None:
        # Track active (open) orders
        self._active_orders: List[Order] = []

        # Restricted hours
        self._restricted_trading_hours = {}

    def _setManager(self, manager) -> None:
        """install manager"""
        self._manager = manager

    def updateAccount(self, positions: List[Position]) -> None:
        """update positions tracking with a position from the exchange"""
        pass

    def updateCash(self, positions: List[Position]) -> None:
        """update cash positions from exchange"""
        pass

    def restrictTradingHours(
        self,
        strategy,
        start_second: Optional[int] = None,
        start_minute: Optional[int] = None,
        start_hour: Optional[int] = None,
        end_second: Optional[int] = None,
        end_minute: Optional[int] = None,
        end_hour: Optional[int] = None,
        on_end_of_day: ExitRoutine = ExitRoutine.NONE,
    ) -> None:
        pass

    # *********************
    # Risk Methods        *
    # *********************
    def risk(self, position: Position = None) -> None:
        # TODO
        return "risk"

    # *********************
    # Order Entry Methods *
    # *********************
    async def newOrder(self, strategy, order: Order) -> Tuple[Order, bool]:
        # TODO
        self._active_orders.append(order)  # TODO use strategy
        return order, True

    # **********************
    # EventHandler methods *
    # **********************
    async def onTrade(self, event: Event) -> None:
        # TODO
        pass

    async def onCancel(self, event) -> None:
        # TODO
        pass

    async def onOpen(self, event: Event) -> None:
        # TODO
        pass

    async def onFill(self, event: Event) -> None:
        # TODO
        pass

    async def onChange(self, event: Event) -> None:
        # TODO
        pass

    async def onData(self, event: Event) -> None:
        # TODO
        pass

    async def onHalt(self, event: Event) -> None:
        # TODO
        pass

    async def onContinue(self, event: Event) -> None:
        # TODO
        pass

    async def onError(self, event: Event) -> None:
        # TODO
        pass

    async def onStart(self, event: Event) -> None:
        # TODO
        pass

    async def onExit(self, event: Event) -> None:
        # TODO
        pass

    #########################
    # Order Entry Callbacks #
    #########################
    async def onTraded(  # type: ignore[override]
        self, event: Event, strategy: Optional[EventHandler]
    ) -> None:
        trade: Trade = event.target  # type: ignore

        if (
            trade.my_order in self._active_orders
            and trade.my_order.filled >= trade.my_order.volume
        ):
            self._active_orders.remove(trade.my_order)

    async def onReceived(  # type: ignore[override]
        self, event: Event, strategy: Optional[EventHandler]
    ) -> None:
        # TODO
        pass

    async def onRejected(  # type: ignore[override]
        self, event: Event, strategy: Optional[EventHandler]
    ) -> None:
        order: Order = event.target  # type: ignore

        if order in self._active_orders:
            self._active_orders.remove(order)

    async def onCanceled(  # type: ignore[override]
        self, event: Event, strategy: Optional[EventHandler]
    ) -> None:
        order: Order = event.target  # type: ignore

        if order in self._active_orders:
            self._active_orders.remove(order)

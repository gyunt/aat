from typing import Tuple
from .data import Event, Order, Trade
from .handler import EventHandler

try:
    from perspective import Table  # type: ignore
except ImportError:

    class Table(object):  # type: ignore
        def __init__(*args, **kwargs):
            pass

        def update(self, *args):
            pass

        def remove(self, *args):
            pass


class TableHandler(EventHandler):
    onData = None  # type: ignore
    onHalt = None  # type: ignore
    onContinue = None  # type: ignore
    onError = None  # type: ignore
    onStart = None  # type: ignore
    onExit = None  # type: ignore

    def __init__(self):
        self._trades = Table(Trade.schema(), index="timestamp")
        self._orders = Table(Order.schema(), index="id")

    def installTables(self, manager) -> None:
        manager.host_table("trades", self._trades)
        manager.host_table("orders", self._orders)

    def tables(self) -> Tuple[Table, Table]:
        return self._trades, self._orders

    def onTrade(self, event: Event):
        """onTrade"""
        trade: Trade = event.target  # type: ignore
        self._trades.update([trade.json()])

    def onOpen(self, event: Event):
        """onOpen"""
        order: Order = event.target  # type: ignore
        self._orders.update([order.json()])

    def onCancel(self, event: Event):
        """onCancel"""
        order: Order = event.target  # type: ignore
        self._orders.remove([order.id])

    def onChange(self, event: Event):
        """onChange"""
        order: Order = event.target  # type: ignore
        self._orders.update([order.json()])

    def onFill(self, event: Event):
        """onFill"""
        order: Order = event.target  # type: ignore
        self._orders.remove([order.id])

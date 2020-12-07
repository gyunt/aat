from typing import TYPE_CHECKING, Dict, Union, List

from aat.core import Order, Instrument
from aat.config import Side, OrderType, OrderFlag


if TYPE_CHECKING:
    from .client import CoinbaseExchangeClient


def _new_order(client: "CoinbaseExchangeClient", order: Order) -> bool:
    jsn: Dict[str, Union[str, int, float]] = {}

    if order.type == OrderType.LIMIT:
        jsn["type"] = "limit"
        jsn["side"] = order.side.value.lower()
        jsn["price"] = order.price
        jsn["size"] = order.volume

        if order.flag == OrderFlag.FILL_OR_KILL:
            jsn["time_in_force"] = "FOK"
        elif order.flag == OrderFlag.IMMEDIATE_OR_CANCEL:
            jsn["time_in_force"] = "IOC"
        else:
            jsn["time_in_force"] = "GTC"

    elif order.type == OrderType.MARKET:
        jsn["type"] = "market"
        jsn["side"] = order.side.value.lower()
        jsn["size"] = order.volume

    else:
        jsn["type"] = order.stop_target.side.value.lower()
        jsn["price"] = order.stop_target.price
        jsn["size"] = order.stop_target.volume

        if order.stop_target.side == Side.BUY:
            jsn["stop"] = "entry"
        else:
            jsn["stop"] = "loss"

        jsn["stop_price"] = order.price

        if order.stop_target.type == OrderType.LIMIT:
            jsn["type"] = "limit"
            if order.flag == OrderFlag.FILL_OR_KILL:
                jsn["time_in_force"] = "FOK"
            elif order.flag == OrderFlag.IMMEDIATE_OR_CANCEL:
                jsn["time_in_force"] = "IOC"
            else:
                jsn["time_in_force"] = "GTC"

        elif order.stop_target.type == OrderType.MARKET:
            jsn["type"] = "market"

    id = client.newOrder(jsn)
    if id > 0:
        order.id = id
        return True
    return False


def _cancel_order(client: "CoinbaseExchangeClient", order: Order) -> bool:
    jsn = {}
    jsn["client_oid"] = order.id
    jsn["product_id"] = order.instrument.brokerId
    return client.cancelOrder(jsn)


def _order_book(client: "CoinbaseExchangeClient", instrument: Instrument) -> List:
    # ob = client.orderBook(instrument.brokerId)
    # print(ob)
    return []

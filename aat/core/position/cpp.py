from typing import Tuple, Dict
from ...common import _in_cpp

try:
    from aat.binding import PositionCpp, CashPositionCpp, AccountCpp  # type: ignore

    _CPP = _in_cpp()

except ImportError:
    _CPP = False


def _make_cpp_position(*args: Tuple, **kwargs: Dict) -> PositionCpp:
    return PositionCpp(*args, **kwargs)


def _make_cpp_cash(*args: Tuple, **kwargs: Dict) -> CashPositionCpp:
    return CashPositionCpp(*args, **kwargs)


def _make_cpp_account(*args: Tuple, **kwargs: Dict) -> AccountCpp:
    return AccountCpp(*args, **kwargs)

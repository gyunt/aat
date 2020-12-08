from .risk import RiskManager


class StrategyManagerRiskMixin(object):
    _risk_mgr: RiskManager

    # *********************
    # Risk Methods        *
    # *********************
    def risk(self, position=None) -> None:
        return self._risk_mgr.risk(position=position)

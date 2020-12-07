class StrategyManagerRiskMixin(object):
    # *********************
    # Risk Methods        *
    # *********************
    def risk(self, position=None) -> None:
        return self._risk_mgr.risk(position=position)

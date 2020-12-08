from .handler import EventHandler
from ..data import Event


class PrintHandler(EventHandler):
    #########################
    # Event Handler Methods #
    #########################
    def onTrade(self, event: Event) -> None:
        """Called whenever a `Trade` event is received"""
        print(event)

    def onOrder(self, event: Event) -> None:
        """Called whenever an Order `Open` event is received"""
        print(event)

    def onData(self, event: Event) -> None:
        """Called whenever other data is received"""
        print(event)

    def onHalt(self, event: Event) -> None:
        """Called whenever an exchange `Halt` event is received, i.e. an event to stop trading"""
        print(event)

    def onContinue(self, event: Event) -> None:
        """Called whenever an exchange `Continue` event is received, i.e. an event to continue trading"""
        print(event)

    def onError(self, event: Event) -> None:
        """Called whenever an internal error occurs"""
        print(event)

    def onStart(self, event: Event) -> None:
        """Called once at engine initialization time"""
        print(event)

    def onExit(self, event: Event) -> None:
        """Called once at engine exit time"""
        print(event)

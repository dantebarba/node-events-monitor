from abc import abstractmethod
from node_events_monitor.wol_server import WakeOnLan
from node_events_monitor.servers import ServerList
import asyncio
import logging


class Event(object):
    """This class represents the event type"""

    @abstractmethod
    def action(self, payload={}):
        """fire an action based on an event"""


class WakeOnLanEvent(Event):
    def action(self, payload={}):
        if payload["status"].lower() == "down":
            logging.debug("Instance {} is down".format(payload["server"]))
            WakeOnLan.instance().wake(ServerList.find(payload["server"]))
        if payload["status"].lower() == "up":
            logging.debug("Instance {} is up".format(payload["server"]))
            WakeOnLan.instance().stop(ServerList.find(payload["server"]))

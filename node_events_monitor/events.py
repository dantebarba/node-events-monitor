from abc import abstractmethod
from wakeonlan import WakeOnLan

class Event(object):
    """ This class represents the event type """
    @abstractmethod
    def action(self, payload={}):
        """ fire an action based on an event """
    
class WakeOnLanEvent(Event):
    def action(self, payload={}):
        if payload["status"].lower() == "down":
            WakeOnLan.instance().wake(payload["server"])
        if payload["status"].lower() == "up":
            WakeOnLan.instance().stop(payload["server"])
        


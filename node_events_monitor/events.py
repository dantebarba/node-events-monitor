from abc import abstractmethod


class Event(object):
    """ This class represents the event type """
    @abstractmethod
    def action(self, payload={}):
        """ fire an action based on an event """
    
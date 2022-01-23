



class Event(object):
    """ This class represents the event type """
    @abstractmethod
    def action(payload={}):
        """ fire an action based on an event """
    
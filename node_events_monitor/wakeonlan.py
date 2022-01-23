from time import sleep
from wakeonlan import send_magic_packet

class WakeOnLan():

    _instance = None

    def __init__(self):
        self.servers = {}

    @classmethod
    def instance(cls):
        if not cls._instance:
            cls._instance = WakeOnLan()
        return cls._instance

    def send_wol(self, server):
        while server in self.servers:
            send_magic_packet('ff.ff.ff.ff.ff.ff',
                            ip_address=server)
            sleep(120)

    def wake(self, server):
        if server in self.servers:
            self.servers[server] = "down"
            self.send_wol(server)

    def stop(self, server):
        if server in self.servers:
            self.servers.pop(server)

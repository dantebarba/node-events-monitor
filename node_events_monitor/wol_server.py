from time import sleep
from typing import List
from wakeonlan import send_magic_packet
from servers import Server

class WakeOnLan():

    _instance = None

    def __init__(self):
        self.servers: List[Server] = []

    @classmethod
    def instance(cls):
        if not cls._instance:
            cls._instance = WakeOnLan()
        return cls._instance

    def send_wol(self, server):
        while server in self.servers:
            send_magic_packet(server.mac,
                            ip_address=server.ip)
            sleep(120)

    def wake(self, server):
        if server in self.servers:
            self.send_wol(server)

    def stop(self, server):
        if server in self.servers:
            self.servers.pop(server)

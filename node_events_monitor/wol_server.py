import logging
import os
from time import sleep
from typing import List
from wakeonlan import send_magic_packet
from node_events_monitor.servers import Server


class WakeOnLan:

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
            logging.warn("Running WoL command on server {}".format(server.name))
            send_magic_packet(server.mac, ip_address=server.ip)
            sleep(os.environ.get("WOL_DELAY", 120))

        logging.warn("Stopping WoL. Server is back online: {}".format(server.name))

    def wake(self, server):
        self.servers.append(server)
        self.send_wol(server)

    def stop(self, server):
        if server in self.servers:
            logging.warn("Stopping server {}".format(server.name))
            self.servers.remove(server)

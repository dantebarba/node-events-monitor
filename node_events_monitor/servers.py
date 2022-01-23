from ast import List
from servers import ServerList
import jsons

class Server():

    def __init__(self):
        self.name = ""
        self.ip = ""
        self.port = ""

class ServerList():
    servers: List[Server] = []

    def __init__(self):
        pass

    @classmethod
    def from_file(cls, file_name):
        with open(file_name, "r") as file:
            data = file.readlines()
            server_list = ServerList()
            server_list.servers = jsons.load(file, Server)
            return server_list
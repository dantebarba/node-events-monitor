from typing import List
from flask import abort
import jsons

class Server():

    def __init__(self, name="", ip="", port=""):
        self.name = ""
        self.ip = ""
        self.port = ""
        self.mac = ""
        
class ServerList(object):

    servers: List[Server] = []

    @classmethod
    def from_file(cls, file_name):
        with open(file_name, "r") as file:
            server_list = ServerList()
            server_list.servers = jsons.load(file, Server)
            return server_list

    @classmethod
    def find(cls, server_name):
        for server in cls.servers:
            if server.name == server_name:
                return server
        
        abort(404)

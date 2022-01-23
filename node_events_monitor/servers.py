import json
import logging
from typing import List
from flask import abort, jsonify
import jsons

class Server():

    def __init__(self):
        self.name = ""
        self.ip = ""
        self.port = ""
        self.mac = ""
        
class ServerList(object):

    servers: List[Server] = []

    @classmethod
    def from_file(cls, file_name):
        with open(file_name, "r") as file:
            cls.servers = jsons.load(json.load(file), List[Server])

    @classmethod
    def find(cls, server_name):
        for server in cls.servers:
            if server.name == server_name:
                return server
        
        jsonify({ "message" : "the server name was not found in list"}), 404
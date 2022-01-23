from flask import Flask
from node_events_monitor.api import api
from node_events_monitor.servers import ServerList
import os

app = Flask(__name__)
app.register_blueprint(api)
ServerList.from_file(os.environ.get("SERVER_FILE", "servers.json"))

from flask import Flask
from node_events_monitor.api import api
from node_events_monitor.servers import ServerList
import os

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api)
    ServerList.from_file(os.environ.get("SERVER_FILE", "servers.json"))
    return app

if __name__ == "__main__":
    create_app().run()
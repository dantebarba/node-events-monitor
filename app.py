from venv import create
from flask import Flask
from node_events_monitor.servers import ServerList
import os

def create_app():
    app = Flask(__name__)
    from node_events_monitor.api import api
    @app.route("/")
    def home():
        return "Hello World!"

    app.register_blueprint(api)
    ServerList.from_file(os.environ.get("SERVER_FILE", "servers.json"))
    return app

 
if __name__ == "__main__":
    create_app().run(debug=True, host='0.0.0.0')
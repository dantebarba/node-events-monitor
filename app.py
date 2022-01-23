from flask import Flask
from node_events_monitor.api import api

app = Flask(__name__)
app.register_blueprint(api)

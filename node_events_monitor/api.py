import logging
import node_events_monitor.events as events
import concurrent.futures
from flask import Blueprint, abort, request, app

api = Blueprint("api", __name__)

@api.route("/")
def hello_world():
    return "api is running"

@api.route("/event", methods=["POST"])
def event():
    data = request.get_json()
    logging.warn("Input data: {}".format(data))
    # instantiate the event
    try:
        event = getattr(events, data["event"])()
        executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
        future = executor.submit(event.action, data)
        return "OK"
    except Exception as e:
        logging.exception(e)
        abort(404)




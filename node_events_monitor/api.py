from flask import Blueprint, abort, request
import events

api = Blueprint('api', __name__)

@api.route('/event', methods=["POST"])
def event():
    data = request.get_json()
    # instantiate the event
    try:
        event = getattr(events, data["event"])()
        event.action(data)
        return "OK"
    except Exception:
        abort(404)

    return "Event"

@api.route('/')
def hello_world():
    return 'api is running'
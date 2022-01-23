import unittest
from create_app import create_app

class ApiTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_wol_event(self):
        data = {"server" : "papini", "event": "WakeOnLanEvent", "status": "down"}
        self.client.post(base_url="127.0.0.1", port=5000, data=data)
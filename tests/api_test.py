import unittest
from app import create_app

class ApiTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_wol_event(self):
        data = {"server" : "papini", "event": "WakeOnLanEvent", "status": "down"}
        response = self.client.get(base_url="http://127.0.0.1", data=data)

        print(response.__dict__)

        self.assertEqual(response.status_code, 200)
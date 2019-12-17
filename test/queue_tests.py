import unittest
import requests

class QueueTestCase(unittest.TestCase):
    def test_create_queue(self):
        payload = {
            "name": "Test"
        }
        response = requests.post('http://127.0.0.1:5000/queues', json=payload)
        self.assertEqual(response.status_code, 201)
        queue = response.json()
        self.assertIsNotNone(queue['id'])
        self.assertEqual(queue['name'], payload['name'])

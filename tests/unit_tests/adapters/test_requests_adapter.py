import unittest
from unittest.mock import ANY

from adapters.requests_adapter import RequestsAdapter


class TestRequestsAdapter(unittest.TestCase):
	def setUp(self) -> None:
		self._requests_adapter = RequestsAdapter()

	def test_http_get(self):
		response = self._requests_adapter.http_get('status/v3/shard-data')
		self.assertEqual(response, {
			'url': ANY,
			'status_code': 200,
			'json': ANY
		})

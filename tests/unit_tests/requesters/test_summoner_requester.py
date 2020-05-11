import unittest
from unittest.mock import Mock

from adapters.requests_adapter import RequestsAdapter
from requesters.summoner_requester import SummonerRequester


class TestSummonerRequester(unittest.TestCase):
    def setUp(self) -> None:
        self._requests_adapter = Mock(spec=RequestsAdapter)
        self._summoner_requester = SummonerRequester(self._requests_adapter)

    def test_get_by_name(self):
        self._requests_adapter.http_get.return_value = {
            'json': {
                'account_id': 'account_id_123'
            }
        }
        response = self._summoner_requester.get_by_name('Lets Coin Flip')
        self._requests_adapter.http_get.assert_called_once_with(
            'summoner/v4/summoners/by-name/Lets Coin Flip')
        self.assertEqual(response, {'account_id': 'account_id_123'})

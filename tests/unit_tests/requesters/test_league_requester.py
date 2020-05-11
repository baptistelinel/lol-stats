import unittest
from unittest.mock import Mock

from adapters.requests_adapter import RequestsAdapter
from requesters.league_requester import LeagueRequester


class TestLeagueRequester(unittest.TestCase):
    def setUp(self) -> None:
        self._requests_adapter = Mock(spec=RequestsAdapter)
        self._league_requester = LeagueRequester(self._requests_adapter)

    def test_get_by_id(self):
        self._requests_adapter.http_get.return_value = {
            'json': {
                'summoner_id': 'summoner_id_123'
            }
        }
        response = self._league_requester.get_by_summoner_id('summoner_id_123')
        self._requests_adapter.http_get.assert_called_once_with(
            f'league/v4/entries/by-summoner/summoner_id_123')
        self.assertEqual(response, {'summoner_id': 'summoner_id_123'})

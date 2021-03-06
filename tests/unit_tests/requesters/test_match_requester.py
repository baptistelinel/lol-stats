import unittest
from unittest.mock import Mock

from adapters.requests_adapter import RequestsAdapter
from requesters.match_requester import MatchRequester


class TestMatchRequester(unittest.TestCase):
    def setUp(self) -> None:
        self._requests_adapter = Mock(spec=RequestsAdapter)
        self._match_requester = MatchRequester(self._requests_adapter)

    def test_get_list_with_champion_id(self):
        self._requests_adapter.http_get.return_value = {
            'json': {
                'matches': [{
                    'match_id': 'match_id_123'
                }]
            }
        }
        response = self._match_requester.get_list('account_id_123',
                                                  'champion_id')
        self._requests_adapter.http_get.assert_called_once_with(
            'match/v4/matchlists/by-account/account_id_123',
            payload={
                'season': 13,
                'endIndex': 10,
                'beginIndex': 0,
                'queue': 420,
                'champion': 'champion_id'
            })
        self.assertEqual(response, [{'match_id': 'match_id_123'}])

    def test_get_list_without_champion_id(self):
        self._requests_adapter.http_get.return_value = {
            'json': {
                'matches': [{
                    'match_id': 'match_id_123'
                }]
            }
        }
        response = self._match_requester.get_list('account_id_123')
        self._requests_adapter.http_get.assert_called_once_with(
            'match/v4/matchlists/by-account/account_id_123',
            payload={
                'season': 13,
                'endIndex': 10,
                'beginIndex': 0,
                'queue': 420
            })
        self.assertEqual(response, [{'match_id': 'match_id_123'}])

    def test_get_by_id(self):
        self._requests_adapter.http_get.return_value = {
            'json': {
                'match_id': 'match_id_123'
            }
        }
        response = self._match_requester.get_details('match_id_123')
        self._requests_adapter.http_get.assert_called_once_with(
            'match/v4/matches/match_id_123')
        self.assertEqual(response, {'match_id': 'match_id_123'})

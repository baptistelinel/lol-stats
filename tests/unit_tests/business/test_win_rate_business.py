import unittest
from unittest.mock import Mock

from business.win_rate_business import WinRateBusiness
from requesters.league_requester import LeagueRequester
from requesters.match_requester import MatchRequester


class TestWinRateBusiness(unittest.TestCase):
    def setUp(self) -> None:
        self._league_requester = Mock(spec=LeagueRequester)
        self._match_requester = Mock(spec=MatchRequester)
        self._win_rate_business = WinRateBusiness(self._league_requester,
                                                  self._match_requester)

    def test_get_from_match_history(self):
        self._match_requester.get_details.return_value = {
            'participants': [{
                'stats': {
                    'participantId': 1,
                    'win': True
                }
            }, {
                'stats': {
                    'participantId': 2,
                    'win': False
                }
            }],
            'participantIdentities': [{
                'participantId': 1,
                'player': {
                    'summonerName': 'Lets Coin Flip',
                }
            }, {
                'participantId': 2,
                'player': {
                    'summonerName': 'Toto',
                }
            }]
        }
        response = self._win_rate_business.get_from_match_history(
            'Lets Coin Flip', [1])
        self._match_requester.get_details.assert_called_once_with(1)
        self.assertEqual(response, 100.0)

    def test_get_general_info(self):
        self._league_requester.get_by_summoner_id.return_value = [{
            'tier':
            'GOLD',
            'rank':
            'IV',
            'summonerName':
            'Lets Coin Flip',
            'leaguePoints':
            30,
            'wins':
            124,
            'losses':
            127,
            'veteran':
            False,
        }]
        response = self._win_rate_business.get_general_info('summoner_id_123')
        self._league_requester.get_by_summoner_id.assert_called_once_with(
            'summoner_id_123')
        self.assertEqual(
            response, {
                'summoner_name': 'Lets Coin Flip',
                'wins': 124,
                'losses': 127,
                'ratio': 49.40239043824701,
                'total_games': 251,
                'rank': 'GOLD IV',
                'league_points': 30,
                'hard_stuck': False
            })

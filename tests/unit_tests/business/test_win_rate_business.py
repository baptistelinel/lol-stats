import unittest
from unittest.mock import Mock

from business.win_rate_business import WinRateBusiness
from requesters.league_requester import LeagueRequester
from requesters.match_requester import MatchRequester
from requesters.summoner_requester import SummonerRequester


class TestWinRateBusiness(unittest.TestCase):
    def setUp(self) -> None:
        self._league_requester = Mock(spec=LeagueRequester)
        self._match_requester = Mock(spec=MatchRequester)
        self._summoner_requester = Mock(spec=SummonerRequester)
        self._win_rate_business = WinRateBusiness(self._league_requester,
                                                  self._match_requester,
                                                  self._summoner_requester)

    def test_get_from_match_history(self):
        self._summoner_requester.get_by_name.return_value = {
            'accountId': 'account_id_123'
        }
        self._match_requester.get_list.return_value = [{
            'gameId': 'game_id_123'
        }]
        self._match_requester.get_details.return_value = {
            'participants': [{
                'stats': {
                    'participantId': 1,
                    'win': True,
                    'kills': 10,
                    'deaths': 2,
                    'assists': 15
                }
            }, {
                'stats': {
                    'participantId': 2,
                    'win': False,
                    'kills': 1,
                    'deaths': 6,
                    'assists': 7
                }
            }],
            'participantIdentities': [{
                'participantId': 1,
                'player': {
                    'accountId': 'account_id_123',
                }
            }, {
                'participantId': 2,
                'player': {
                    'accountId': 'account_id_456',
                }
            }]
        }
        response = self._win_rate_business.get_from_match_history(
            'Lets Coin Flip')
        self._summoner_requester.get_by_name.assert_called_once_with(
            'Lets Coin Flip')
        self._match_requester.get_list.assert_called_once_with(
            'account_id_123', None)
        self._match_requester.get_details.assert_called_once_with(
            'game_id_123')
        self.assertEqual(
            response, {
                'wins': 1,
                'kills': 10,
                'deaths': 2,
                'assists': 15,
                'losses': 0,
                'total_games': 1,
                'ratio': 100.0
            })

    def test_get_general_info(self):
        self._summoner_requester.get_by_name.return_value = {
            'id': 'summoner_id_123'
        }
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
        response = self._win_rate_business.get_general_info('Lets Coin Flip')
        self._summoner_requester.get_by_name.assert_called_once_with(
            'Lets Coin Flip')
        self._league_requester.get_by_summoner_id.assert_called_once_with(
            'summoner_id_123')
        self._summoner_requester.get_by_name.assert_called_once_with(
            'Lets Coin Flip')
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

import unittest
from unittest.mock import Mock

from business.win_rate_business import WinRateBusiness
from requesters.league_requester import LeagueRequester


class TestWinRateBusiness(unittest.TestCase):
    def setUp(self) -> None:
        self._league_requester = Mock(spec=LeagueRequester)
        self._win_rate_business = WinRateBusiness(self._league_requester)

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

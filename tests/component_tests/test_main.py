import json
import sys
import unittest
from unittest.mock import ANY

from main import app


class TestMain(unittest.TestCase):
    def setUp(self) -> None:
        self._client = app.test_client()

    def test_home(self):
        response = self._client.get('http://127.0.0.1:5000/')
        json_response = json.loads(response.get_data().decode(
            sys.getdefaultencoding()))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json_response, {'response': 'Home'})

    def test_win_rate(self):
        response = self._client.get('http://127.0.0.1:5000/win-rate/MikyB2')
        json_response = json.loads(response.get_data().decode(
            sys.getdefaultencoding()))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            json_response, {
                'hard_stuck': ANY,
                'league_points': ANY,
                'losses': ANY,
                'rank': ANY,
                'ratio': ANY,
                'summoner_name': 'MikyB2',
                'total_games': ANY,
                'wins': ANY
            })

    def test_win_rate_last_ten_games(self):
        response = self._client.get(
            'http://127.0.0.1:5000/win-rate/MikyB2/filtered')
        json_response = json.loads(response.get_data().decode(
            sys.getdefaultencoding()))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            json_response, {
                'win_rate_last_ten_games': {
                    'losses': ANY,
                    'ratio': ANY,
                    'total_games': ANY,
                    'wins': ANY
                }
            })

    def test_win_rate_champion_last_ten_games(self):
        response = self._client.get(
            'http://127.0.0.1:5000/win-rate/MikyB2/875/filtered')
        json_response = json.loads(response.get_data().decode(
            sys.getdefaultencoding()))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            json_response, {
                'win_rate_last_ten_games': {
                    'champion_id': 875,
                    'losses': ANY,
                    'ratio': ANY,
                    'total_games': ANY,
                    'wins': ANY
                }
            })

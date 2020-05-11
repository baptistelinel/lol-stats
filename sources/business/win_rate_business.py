from requesters.league_requester import LeagueRequester


class WinRateBusiness:
    def __init__(self, league_requester: LeagueRequester):
        self._league_requester = league_requester

    def get_general_info(self, summoner_id):
        league = self._league_requester.get_by_summoner_id(summoner_id)[0]
        total_games = int(league['wins']) + int(league['losses'])
        return {
            'summoner_name': league['summonerName'],
            'wins': league['wins'],
            'losses': league['losses'],
            'ratio': (league['wins'] / total_games) * 100,
            'total_games': total_games,
            'rank': f"{league['tier']} {league['rank']}",
            'league_points': league['leaguePoints'],
            'hard_stuck': league['veteran']
        }

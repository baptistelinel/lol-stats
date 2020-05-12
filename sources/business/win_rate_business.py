from requesters.league_requester import LeagueRequester
from requesters.match_requester import MatchRequester


class WinRateBusiness:
    def __init__(self, league_requester: LeagueRequester,
                 match_requester: MatchRequester):
        self._league_requester = league_requester
        self._match_requester = match_requester

    def get_from_match_history(self, summoner_name: str,
                               match_id_list: list) -> float:
        win_count = 0
        for match_id in match_id_list:
            match = self._match_requester.get_details(match_id)
            summoner = next(
                (participant_identity
                 for participant_identity in match['participantIdentities']
                 if participant_identity['player']['summonerName'] ==
                 summoner_name), None)
            summoner_game_detail = next(
                (participant for participant in match['participants']
                 if participant['stats']['participantId'] ==
                 summoner['participantId']), None)
            if summoner_game_detail['stats']['win']:
                win_count += 1
        return (win_count / len(match_id_list)) * 100

    def get_general_info(self, summoner_id) -> dict:
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

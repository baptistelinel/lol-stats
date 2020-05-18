from requesters.league_requester import LeagueRequester
from requesters.match_requester import MatchRequester
from requesters.summoner_requester import SummonerRequester


class WinRateBusiness:
    def __init__(self, league_requester: LeagueRequester,
                 match_requester: MatchRequester,
                 summoner_requester: SummonerRequester):
        self._league_requester = league_requester
        self._match_requester = match_requester
        self._summoner_requester = summoner_requester

    def get_from_match_history(self,
                               summoner_name: str,
                               champion_id=None) -> dict:
        win_count = 0
        kills = 0
        deaths = 0
        assists = 0
        account_id = self._summoner_requester.get_by_name(
            summoner_name)['accountId']
        match_list = self._match_requester.get_list(account_id, champion_id)
        for match in match_list:
            match_details = self._match_requester.get_details(match['gameId'])
            summoner = next(
                (participant_identity for participant_identity in
                 match_details['participantIdentities']
                 if participant_identity['player']['accountId'] == account_id),
                None)
            summoner_game_detail = next(
                (participant for participant in match_details['participants']
                 if participant['stats']['participantId'] ==
                 summoner['participantId']), None)
            if summoner_game_detail['stats']['win']:
                win_count += 1
            kills += summoner_game_detail['stats']['kills']
            deaths += summoner_game_detail['stats']['deaths']
            assists += summoner_game_detail['stats']['assists']

        return {
            'kills': kills / len(match_list),
            'deaths': deaths / len(match_list),
            'assists': assists / len(match_list),
            'wins': win_count,
            'losses': len(match_list) - win_count,
            'total_games': len(match_list),
            'ratio': (win_count / len(match_list)) * 100
        }

    def get_general_info(self, summoner_name: str) -> dict:
        summoner_id = self._summoner_requester.get_by_name(summoner_name)['id']
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
            'hard_stuck': league['veteran'],
        }

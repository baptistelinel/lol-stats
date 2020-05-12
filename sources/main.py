from adapters.requests_adapter import RequestsAdapter
from business.win_rate_business import WinRateBusiness
from requesters.league_requester import LeagueRequester
from requesters.match_requester import MatchRequester


class Main:
    def __init__(self, win_rate_business: WinRateBusiness):
        self._win_rate_business = win_rate_business

    def run(self):
        match_id = [
            '4594008545', '4593809699', '4593862618', '4592000594',
            '4591938736'
        ]
        result = self._win_rate_business.get_from_match_history(
            'Lets Coin Flip', match_id)
        print(result)


if __name__ == '__main__':
    requests_adapter = RequestsAdapter()
    league_requester = LeagueRequester(requests_adapter)
    match_requester = MatchRequester(requests_adapter)
    Main(WinRateBusiness(league_requester, match_requester)).run()

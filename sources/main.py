from adapters.requests_adapter import RequestsAdapter
from business.win_rate_business import WinRateBusiness
from requesters.league_requester import LeagueRequester


class Main:
    def __init__(self, win_rate_business: WinRateBusiness):
        self._win_rate_business = win_rate_business

    def run(self):
        summoner_id = '-yFYyOXG7NoGI5ABu1XrAp7softSSDeOnBfX-EwQ72Ha'
        result = self._win_rate_business.get_general_info(summoner_id)
        print(result)


if __name__ == '__main__':
    league_requester = LeagueRequester(RequestsAdapter())
    Main(WinRateBusiness(league_requester)).run()

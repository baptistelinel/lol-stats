from flask import Flask
from flask_caching import Cache

from adapters.requests_adapter import RequestsAdapter
from business.win_rate_business import WinRateBusiness
from requesters.league_requester import LeagueRequester
from requesters.match_requester import MatchRequester
from requesters.summoner_requester import SummonerRequester

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
requests_adapter = RequestsAdapter()


@app.route('/')
def home():
    return 'Home'


@app.route('/win-rate')
@cache.cached(timeout=50, key_prefix='win-rate')
def win_rate():
    win_rate_business = WinRateBusiness(LeagueRequester(requests_adapter),
                                        MatchRequester(requests_adapter),
                                        SummonerRequester(requests_adapter))
    general_info = win_rate_business.get_general_info('Lets Coin Flip')
    win_rate_last_ten_days = win_rate_business.get_from_match_history('Lets Coin Flip')
    return {**general_info, **win_rate_last_ten_days}


if __name__ == '__main__':
    app.run(debug=True)

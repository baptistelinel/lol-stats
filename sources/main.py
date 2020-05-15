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
win_rate_business = WinRateBusiness(LeagueRequester(requests_adapter),
                                    MatchRequester(requests_adapter),
                                    SummonerRequester(requests_adapter))


@app.route('/')
def home():
    return 'Home'


@app.route('/win-rate/<summoner_name>')
@cache.cached(timeout=50, key_prefix='win_rate')
def win_rate_general(summoner_name):
    general_info = win_rate_business.get_general_info(summoner_name)
    win_rate_last_ten_games = win_rate_business.get_from_match_history(
        summoner_name)
    return {**general_info, **win_rate_last_ten_games}


@app.route('/win-rate/<summoner_name>/<champion_id>')
@cache.cached(timeout=50, key_prefix='win_rate_champion')
def win_rate_champion(summoner_name, champion_id):
    win_rate = win_rate_business.get_from_match_history(summoner_name, champion_id)
    win_rate['win_rate_last_ten_games']['champion_id'] = champion_id
    return win_rate


if __name__ == '__main__':
    app.run()

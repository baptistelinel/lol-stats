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
    return {'response': 'Home'}


@app.route('/win-rate/<summoner_name>')
@cache.cached(timeout=50)
def win_rate(summoner_name):
    return win_rate_business.get_general_info(summoner_name)


@app.route('/win-rate/<summoner_name>/filtered')
@cache.cached(timeout=50)
def win_rate_last_ten_games(summoner_name):
    return win_rate_business.get_from_match_history(summoner_name)


@app.route('/win-rate/<summoner_name>/<champion_id>/filtered')
@cache.cached(timeout=50)
def win_rate_champion_last_ten_games(summoner_name: str, champion_id: str):
    result = win_rate_business.get_from_match_history(summoner_name,
                                                      champion_id)
    result['win_rate_last_ten_games']['champion_id'] = int(champion_id)
    return result


if __name__ == '__main__':
    app.run()

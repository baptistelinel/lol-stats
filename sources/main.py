from flask import Flask
from flask_caching import Cache

from adapters.requests_adapter import RequestsAdapter
from requesters.summoner_requester import SummonerRequester

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
requests_adapter = RequestsAdapter()


@app.route('/')
def home():
    return 'Home'


@app.route('/match-details')
@cache.cached(timeout=50, key_prefix='match_details')
def match_details():
    summoner_requester = SummonerRequester(requests_adapter)
    summoner = summoner_requester.get_by_name('Lets Coin Flip')
    return summoner


if __name__ == '__main__':
    app.run(debug=True)

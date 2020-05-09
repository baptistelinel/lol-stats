from adapters.requests_adapter import RequestsAdapter


class LeagueRequester:
    def __init__(self, requests_adapter: RequestsAdapter):
        self._requests_adapter = requests_adapter

    def get_by_id(self, summoner_id: str):
        response = self._requests_adapter.http_get(
            f'league/v4/entries/by-summoner/{summoner_id}')
        return response['json']

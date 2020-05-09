from adapters.requests_adapter import RequestsAdapter


class SummonerRequester:
	def __init__(self, requests_adapter: RequestsAdapter):
		self._requests_adapter = requests_adapter

	def get_by_name(self, summoner_name: str) -> dict:
		response = self._requests_adapter.http_get(f'summoner/v4/summoners/by-name/{summoner_name}')
		return response['json']

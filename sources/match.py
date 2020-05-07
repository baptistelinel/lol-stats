from adapters.requests_adapter import RequestsAdapter


class Match:
	def __init__(self, requests_adapter: RequestsAdapter):
		self._requests_adapter = requests_adapter

	def get_list(self, account_id: str) -> list:
		payload = {'endIndex': 1, 'beginIndex': 0, 'queue': 420}
		response = self._requests_adapter.http_get(f'match/v4/matchlists/by-account/{account_id}', payload=payload)
		return response['json']['matches']

	def get_details(self, match_id: str):
		return self._requests_adapter.http_get(f'match/v4/matches/{match_id}')


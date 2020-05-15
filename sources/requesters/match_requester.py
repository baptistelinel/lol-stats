from adapters.requests_adapter import RequestsAdapter


class MatchRequester:
    def __init__(self, requests_adapter: RequestsAdapter):
        self._requests_adapter = requests_adapter

    def get_list(self, account_id: str, champion_id=None) -> list:
        payload = {'season': 13, 'endIndex': 10, 'beginIndex': 0, 'queue': 420}
        if champion_id is not None:
            payload = {**payload, 'champion': champion_id}
        response = self._requests_adapter.http_get(
            f'match/v4/matchlists/by-account/{account_id}', payload=payload)
        return response['json']['matches']

    def get_details(self, match_id: str):
        response = self._requests_adapter.http_get(
            f'match/v4/matches/{match_id}')
        return response['json']

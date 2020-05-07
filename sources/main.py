from adapters.requests_adapter import RequestsAdapter
from match import Match
from summoner import Summoner


class Main:
	def __init__(self, match: Match, summoner: Summoner):
		self._match = match
		self._summoner = summoner

	def run(self):
		account_id = self._summoner.get_by_name('Lets Coin Flip')['accountId']
		match = self._match.get_list(account_id)
		match_id = match[0]['gameId']
		match_details = self._match.get_details(match_id)
		print(match_details)


if __name__ == '__main__':
	requests_adapter = RequestsAdapter()
	Main(Match(requests_adapter), Summoner(requests_adapter)).run()

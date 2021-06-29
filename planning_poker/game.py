from planning_poker.utils import *


class Issue(object):

    def __init__(self, name: str, issue_id: str):
        self.name = name
        self._score = {}
        self.id = issue_id

    def vote(self, score: int, user_id: str):
        self._score.update({user_id: score})

    def score(self) -> int:
        return sum(self._score.values())


class Game(object):

    def __init__(self, name: str, game_id: str):
        self.name = name
        self.id = game_id
        self._issues = {}

    def add_issue(self, name: str) -> str:
        issue_id = get_uuid()
        self._issues.update({issue_id: Issue(name, issue_id)})
        return issue_id

    def issue(self, issue_id: str):
        return self._issues.get(issue_id)

    def issues(self) -> list:
        return [{"name": issue.name, "id": issue.id} for issue in self._issues.values()]


class Games(object):

    def __init__(self):
        self._all = {}

    def new(self, name: str) -> str:
        game_id = get_uuid()
        self._all.update({game_id: Game(name, game_id)})
        return game_id

    def get(self, game_id: str) -> Game:
        return self._all.get(game_id)

    def all(self) -> list:
        return [{"name": game.name, "id": game.id} for game in self._all.values()]

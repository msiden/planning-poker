from planning_poker.utils import *
from planning_poker.models import *


class Issue(object):

    def __init__(self, name: str, issue_id: str):
        self.name = name
        self.score = 0
        self.id = issue_id

    def vote(self, score: int):
        self.score += score


class Game(object):

    def __init__(self, name: Name, game_id: str):
        self.name = name
        self.id = game_id
        self.issues = {}

    def add_issue(self, name: str) -> str:
        issue_id = get_uuid()
        self.issues.update({issue_id: Issue(name, issue_id)})
        return issue_id

    def issue(self, issue_id: str):
        return self.issues.get(issue_id)


class Games(object):

    def __init__(self):
        self.all = {}

    def new(self, name: Name) -> str:
        game_id = get_uuid()
        self.all.update({game_id: Game(name, game_id)})
        return game_id

    def get(self, game_id: str) -> Game:
        return self.all.get(game_id)

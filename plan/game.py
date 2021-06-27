from plan.utils import *
from plan.schemas import *


class Games(object):

    def __init__(self):
        self.all = dict

    def new(self, name: Name) -> str:
        game_id = get_uuid()
        self.all.update({game_id: Game(name, game_id)})
        return game_id


class Game(object):

    def __init__(self, name: Name, game_id: str):
        self.name = name
        self.id = game_id
        self.issues = dict

    def add_issue(self, name: Name):
        self.issues.update({name: Issue(name)})


class Issue(object):

    def __init__(self, name: Name):
        self.name = name
        self._score = 0

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, points):
        self._score += points

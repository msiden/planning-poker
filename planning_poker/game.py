from planning_poker.utils import *
from planning_poker.enums import *


class Issue(object):
    """Describes a votable issue in a game"""

    def __init__(self, name: str, issue_id: str):
        self.name = name
        self._score = {}
        self.id = issue_id

    def vote(self, score: int, user_id: str) -> None:
        """Register a vote"""
        self._score.update({user_id: score})

    def score(self) -> int:
        """Returns the issue's total score"""
        return sum(self._score.values())

    def votes(self) -> dict:
        """Returns the number of votes each option has received"""
        all_votes = list(self._score.values())
        return {score_.value: all_votes.count(score_.value) for score_ in Score}


class Game(object):
    """Describes a game of votable issues"""

    def __init__(self, name: str, game_id: str):
        self.name = name
        self.id = game_id
        self._issues = {}

    def add_issue(self, name: str) -> str:
        """Adds a new issue to the game and returns its ID"""
        issue_id = get_uuid()
        self._issues.update({issue_id: Issue(name, issue_id)})
        return issue_id

    def issue(self, issue_id: str) -> Issue:
        """Returns a specific issue in the game"""
        return self._issues.get(issue_id)

    def issues(self) -> list:
        """Returns the name and ID of all issues in the game"""
        return [{"name": issue.name, "id": issue.id} for issue in self._issues.values()]


class Games(object):
    """Container for all active games"""

    def __init__(self):
        self._all = {}

    def new(self, name: str) -> str:
        """Create a new game and return its ID"""
        game_id = get_uuid()
        self._all.update({game_id: Game(name, game_id)})
        return game_id

    def get(self, game_id: str) -> Game:
        """Returns one specific game"""
        return self._all.get(game_id)

    def all(self) -> list:
        """Returns the name and ID of all active games"""
        return [{"name": game.name, "id": game.id} for game in self._all.values()]

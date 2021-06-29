from pydantic import BaseModel
from planning_poker.enums import *


class Name(BaseModel):
    name: str


class Id(BaseModel):
    id: str


class Vote(BaseModel):
    score: Score
    game_id: str
    issue_id: str
    user_id: str


class Issues(BaseModel):
    game_id: str
    name: str = ""
    issue_id: str = ""

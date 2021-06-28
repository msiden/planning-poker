from pydantic import BaseModel
from planning_poker.enums import *
from typing import Optional


class Name(BaseModel):
    name: str


class Id(BaseModel):
    id: str


class Vote(BaseModel):
    score: Score


class Issues(BaseModel):
    game_id: str
    name: str
    issue_id: str = ""

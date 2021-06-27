from pydantic import BaseModel
from typing import List


class Vote(BaseModel):
    score: int


class Name(BaseModel):
    name: str



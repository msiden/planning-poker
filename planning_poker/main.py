from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from planning_poker.game import *
from planning_poker.models import *


app = FastAPI()
games = Games()
app.mount("/static", StaticFiles(directory="frontend/"), name="static")
app.mount("/img", StaticFiles(directory="frontend/img/"), name="img")
app.mount("/js", StaticFiles(directory="frontend/js/"), name="js")
templates = Jinja2Templates(directory="frontend/")


@app.get("/", response_class=HTMLResponse)
def index(request: Request) -> templates.TemplateResponse:
    response = templates.TemplateResponse("index.html", {"request": request})
    return response


@app.post("/new_game")
def new_game(name: Name) -> str:
    game_id = games.new(name.name)
    return game_id


@app.post("/new_issue")
def new_issue(issue: Issues) -> str:
    issue_id = games.get(issue.game_id).add_issue(issue.name)
    return issue_id


@app.post("/vote")
def vote(score: Vote) -> None:
    games.get(score.game_id).issue(score.issue_id).vote(score.score, score.user_id)


@app.get("/game/{game_id}", response_class=HTMLResponse)
def game(request: Request) -> templates.TemplateResponse:
    response = templates.TemplateResponse("game.html", {"request": request})
    return response


@app.get("/list_games")
def list_games() -> list:
    return games.all()


@app.post("/list_issues")
def list_issues(game_id: Id):
    return games.get(game_id.id).issues()


@app.get("/game/{game_id}/{issue_id}", response_class=HTMLResponse)
def issue_page(request: Request):
    response = templates.TemplateResponse("issue.html", {"request": request})
    cookie = request.headers.get("cookie")
    if not cookie:
        response.set_cookie(key="uuid", value=get_uuid())
    return response


@app.post("/total_score")
def total_score(issue: Issues) -> int:
    return games.get(issue.game_id).issue(issue.issue_id).score()

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from plan.game import *


app = FastAPI()
app.mount("/static", StaticFiles(directory="frontend/"), name="static")
app.mount("/img", StaticFiles(directory="frontend/img/"), name="img")
app.mount("/js", StaticFiles(directory="frontend/js/"), name="js")
templates = Jinja2Templates(directory="frontend/")
games = Games()


@app.get("/", response_class=HTMLResponse)
def index(request: Request) -> templates.TemplateResponse:
    response = templates.TemplateResponse("index.html", {"request": request})
    #token = get_uuid()
    #response.set_cookie(key="uuid", value=token)
    return response


@app.get("/game/create/", response_class=HTMLResponse)
def new_game(request: Request, name: Name = "new game") -> templates.TemplateResponse:
    games.new(name)
    response = templates.TemplateResponse("game.html", {"request": request})
    return response


from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from sorting_funcitons import *
from codes import Code
from Databases import Database

api = FastAPI()

template = Jinja2Templates(directory="html")

api.mount("/static", StaticFiles(directory="static"), name="static")

@api.get("/", response_class = HTMLResponse)
async def index(request: Request):
    return template.TemplateResponse("index.html", {"request": request})

@api.get("/api/message")
async def get_message():
    # loading the data
    database_data = Database().get_all_edu_empl()
    provinces = get_edu_data(Code(), database_data)
    return {"Education_data": provinces}
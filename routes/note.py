from fastapi import APIRouter
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from models.note import Note
from config.db import conn
from schemas.note import notesEntity,notesEntity
from fastapi.templating import Jinja2Templates

note =  APIRouter()
templates = Jinja2Templates(directory="templates")

@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.notes.notes.find({})
    newdocs = []

    for doc in docs:
        newdocs.append({
            "id": str(doc["_id"]),
            "title" :doc["title"],
            "desc" :doc["desc"],
            "important": doc["important"],
        })

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "newdocs": newdocs
        }
    )
@note.post("/")
async def create_item(request: Request):
    form = await request.form()
    formDict = dict(form)

    print(formDict)
    formDict["important"] = True if formDict.get("important") == "on" else False
    note = conn.notes.notes.insert_one(formDict)
    return {"Success":True}
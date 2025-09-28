from fastapi import FastAPI,Request,APIRouter,Form
from fastapi.responses import HTMLResponse
from models.note import Note
from config.db import conn
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from schemas.note import noteEntity,notesEntity
from typing import Union
from bson import ObjectId

note = APIRouter()
templates = Jinja2Templates(directory="templates")


@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs=conn.notes.notes.find({})
    newdocs=[]
    for doc in docs:
       newdocs.append({
                     "id":doc["_id"] ,
                     "title":doc["title"],
                     "desc":doc["desc"],
                     "important":doc["important"],


       })
    return templates.TemplateResponse("index.html", {"request":request,"newdocs":newdocs}
       
    )
    




@note.post("/")
def create_note(
    title: str = Form(...),
    desc: str = Form(...),
    important: bool = Form(...)
    
):
    
    new_note = {"title": title, "desc": desc, "important": important}
    result = conn.notes.notes.insert_one(new_note)
    return {"inserted_id": str(result.inserted_id)}




@note.delete("/delete/{id}")
def delete_note(id: str):
    result = conn.notes.notes.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 1:
        return {"status": "success", "message": "Note deleted"}
    raise HTTPException(status_code=404, detail="Note not found")









# @note.post("/")
# async def create_item(request: Request):
#     form = await request.form()
#     formdict=dict(form)
#     formdict["important"]=True if formdict.get("important")=="on" else False
#     note=conn.notes.notes.insert_one(formdict)
#     return {"success":True}


# @note.post("/")
# def add_note(note:Note):
#     inserted_note=conn.notes.notes.insert_one(dict(note))
#     return noteEntity(inserted_note)

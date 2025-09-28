from pydantic import BaseModel,Field

class Note(BaseModel):
    title:str 
    desc:str
    important:bool
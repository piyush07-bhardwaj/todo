from pydantic import BaseModel, Field

class TodoCreate(BaseModel):
    title:str = Field(..., min_length=1, max_length=200)
    description: str | None = None

class TodoUpdate(BaseModel):
    title:str = Field(..., min_length=1, max_length=200)
    description:str | None = None
    completed:bool = False

class TodoResponse(BaseModel):
    id:int
    title:str
    description:str | None
    completed:bool

    class Config:
        from_attributes = True
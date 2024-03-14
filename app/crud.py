from fastapi import FastAPI, Body,Depends
from app.db import Todos,engine
from sqlmodel import Session, select
from typing import  Annotated



app:FastAPI = FastAPI()

def get_session():
    with Session(engine) as session:
        yield session

@app.get("/")
async def get_all_todos(session: Annotated[Session, Depends(get_session)]):
        statement = select(Todos)
        results = session.exec(statement)
        todos = results.all()
        return todos

@app.get("/done")
async def list_done_todos(session: Annotated[Session, Depends(get_session)]):
        statement = select(Todos).where(Todos.is_done == True)
        results = session.exec(statement)
        todos = results.all()
        return todos

@app.post("/create")
async def create_todo(session: Annotated[Session, Depends(get_session)],text: str = Body(embed=True), is_complete: bool = False):
        todo = Todos(text=text, is_done=is_complete)
        session.add(todo)
        session.commit()
        return {"todo created": todo.text}
     
@app.put("/update/{id}")
async def update_todo(
    session: Annotated[Session, Depends(get_session)],
    id: int,
    text: str = Body(embed=True),
    
):
        todo_query = select(Todos).where(Todos.id == id)
        results = session.exec(todo_query)
        todo = results.one()
        if todo:
            todo.text = text
        session.add(todo)
        session.commit()
        return {"todo updated": todo.text}

@app.delete("/delete/{id}")
async def delete_todo(id: int,session: Annotated[Session, Depends(get_session)]):
        todo_query = select(Todos).where(Todos.id == id)
        results = session.exec(todo_query)
        todo = results.one()
        session.delete(todo)
        session.commit()
        return {"todo deleted": todo.text}
from fastapi import FastAPI, Body
from app.db import Todos,engine
from sqlmodel import Session, select



app:FastAPI = FastAPI()


@app.get("/")
async def get_all_todos():
    with Session(engine) as session:
        statement = select(Todos)
        results = session.exec(statement)
        todos = results.all()
        return todos

@app.get("/done")
async def list_done_todos():
    with Session(engine) as session:
        statement = select(Todos).where(Todos.is_done == True)
        results = session.exec(statement)
        todos = results.all()
        return todos

@app.post("/create")
async def create_todo(text: str  = Body(embed=True), is_complete: bool = False):
    with Session(engine) as session:
        todo = Todos(text=text, is_done=is_complete)
        session.add(todo)
        session.commit()
        return {"todo created": todo.text}
     
@app.put("/update/{id}")
async def update_todo(
    id: int,
    text: str = Body(embed=True),
):
    with Session(engine) as session:
        todo_query = select(Todos).where(Todos.id == id)
        results = session.exec(todo_query)
        todo = results.one()
        if todo:
            todo.text = text
        session.add(todo)
        session.commit()
        return {"todo updated": todo.text}

@app.delete("/delete/{id}")
async def delete_todo(id: int):
    with Session(engine) as session:
        todo_query = select(Todos).where(Todos.id == id)
        results = session.exec(todo_query)
        todo = results.one()
        session.delete(todo)
        session.commit()
        return {"todo deleted": todo.text}
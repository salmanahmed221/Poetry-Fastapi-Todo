from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine

from app.crud import app, get_session

from dotenv import load_dotenv, find_dotenv
from os import getenv

_:bool = load_dotenv(find_dotenv())
postgress_url:str = getenv("TEST_DATABASE_URL")

def test_post_route():

    engine = create_engine(
    postgress_url,
    echo= True
    )

    SQLModel.metadata.create_all(engine)  

    with Session(engine) as session:  

        def get_session_override():  
                return session  

        app.dependency_overrides[get_session] = get_session_override 

        client = TestClient(app=app)

        todo_content = "buy bread"

        response = client.post("/create",
            json={"text": todo_content}
        )
        data = response.json()
        assert response.status_code == 200
        assert data["todo created"] == todo_content


def test_get_route():

    engine = create_engine(
    postgress_url,
    echo= True
    )

    SQLModel.metadata.create_all(engine)  

    with Session(engine) as session:  

        def get_session_override():  
                return session  

        app.dependency_overrides[get_session] = get_session_override 
        client = TestClient(app=app)

        response = client.get("/")
        assert response.status_code == 200


def test_put_route():

    engine = create_engine(
    postgress_url,
    echo= True
    )

    SQLModel.metadata.create_all(engine)  

    with Session(engine) as session:  

        def get_session_override():  
                return session  

        app.dependency_overrides[get_session] = get_session_override 

        client = TestClient(app=app)

        updated_todo_content = "buy milk"

        response = client.put("/update/4", json={"text": updated_todo_content})
        assert response.status_code == 200

        updated_data = response.json()
        assert updated_data["todo updated"] == updated_todo_content    


def test_delete_route():

    engine = create_engine(
    postgress_url,
    echo= True
    )

    SQLModel.metadata.create_all(engine)  

    with Session(engine) as session:  

        def get_session_override():  
                return session  

        app.dependency_overrides[get_session] = get_session_override 
        client = TestClient(app=app)

        response = client.delete("/delete/7")
        assert response.status_code == 200
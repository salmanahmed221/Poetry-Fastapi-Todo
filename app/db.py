from sqlmodel import Field, SQLModel, create_engine
from typing import Optional
from dotenv import load_dotenv, find_dotenv
from os import getenv


_:bool = load_dotenv(find_dotenv())
postgress_url:str = getenv("POSTGRESS_URL")

class Todos(SQLModel, table=True):
    id:int = Field(primary_key=True)
    text:str = ""
    is_done:Optional[bool] = Field(default=False)


engine = create_engine(
 postgress_url,
    echo= True
)

SQLModel.metadata.create_all(engine)
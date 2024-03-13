from sqlmodel import Field, SQLModel, create_engine
from typing import Optional



class Todos(SQLModel, table=True):
    id:int = Field(primary_key=True)
    text:str = ""
    is_done:Optional[bool] = Field(default=False)


engine = create_engine(
f'postgresql://salmanahmed121221:YDeWwV7EH3gm@ep-blue-cake-56162237.us-east-2.aws.neon.tech/neondb?sslmode=require',
    echo= True
)

SQLModel.metadata.create_all(engine)
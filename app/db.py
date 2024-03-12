from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm.session import Session

class Base(DeclarativeBase):
    pass

class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True)
    text = Column(String)
    is_done = Column(Boolean, default=False)


engine: Engine = create_engine(
f'postgresql://salmanahmed121221:YDeWwV7EH3gm@ep-blue-cake-56162237.us-east-2.aws.neon.tech/neondb?sslmode=require',
    echo= True
)


Session = sessionmaker(bind=engine)

session = Session()
Base.metadata.create_all(engine)
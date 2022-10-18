from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URI= "sqlite:///todo-app.sqlite"
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo = True)
meta = MetaData()
Base = declarative_base()
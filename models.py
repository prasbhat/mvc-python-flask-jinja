from . import engine, Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

class Tasks(Base):
    __tablename__="tasks"

    systemTaskId = Column(Integer, primary_key = True)
    title = Column(String)
    description = Column(String)
    status = Column(String)
    dueDate = Column(Date)
    creationDate = Column(Date)
    todoTaskCommentsSet = relationship("TodoTaskComments", backref = "task", lazy='subquery', cascade="all, delete-orphan")

class TodoTaskComments(Base):
    __tablename__="todoTaskComments"

    systemTodoTaskCommentsId = Column(Integer, primary_key = True)
    taskComments = Column(String)
    creationDate = Column(Date)
    task_systemTaskId = Column(Integer, ForeignKey('tasks.systemTaskId'))

Base.metadata.create_all(engine)
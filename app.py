from flask import Flask, render_template, request, redirect, jsonify, abort, url_for
from .models import Tasks, TodoTaskComments
from datetime import datetime,date
from . import engine
from sqlalchemy.orm import sessionmaker
import pyautogui

app = Flask(__name__)
Session = sessionmaker(bind= engine)

@app.route('/todo-app/tasks/', methods=['GET'])
def index():
    with Session() as session:
        data = []
        taskList = session.query(Tasks).all()
        
        for task in taskList:
            todoTaskCommentsList = session.query(TodoTaskComments).filter(TodoTaskComments.task_systemTaskId == task.systemTaskId)
            data.append(__jsonResponse(task, todoTaskCommentsList))
    return render_template("index.html",tasks=data)

@app.route('/todo-app/tasks/create/', methods=['GET', 'POST'])
def create_task():
    # If the request method is GET, display the create_task.html page.
    if(request.method == 'GET'):
        return render_template("create_task.html", statusList=__getTodoStatusAsList())

    if not request.form:
        abort(400)
    task = Tasks(title = request.form.get('title'), description = request.form.get('description'), status = request.form.get('status'), 
    dueDate = datetime.strptime(request.form.get('dueDate'), '%Y-%m-%d').date(), creationDate = date.today())
    
    with Session() as session:
        session.add(task)
        session.commit()
        session.refresh(task)
        
    return redirect(url_for("index")) 

def __getTodoStatusAsList():
    statusList = {"Not Started", "In Progress", "On Hold", "Completed", "Deferred"}
    return statusList

@app.route('/todo-app/tasks/<int:id>', methods=['GET'])
def view_task(id):
    return render_template("view_task.html", task=__get_one_task(id))

def __get_one_task(id):
    with Session() as session:
        task = session.query(Tasks).get(id)

    if task is None:
        abort(404)

    return __jsonResponse(task, task.todoTaskCommentsSet)

@app.route('/todo-app/tasks/update/<int:id>', methods=['GET', 'POST'])
def update_task(id):
    # If the request method is GET, display the update_task.html page.
    if(request.method == 'GET'):
        return render_template("update_task.html", task=__get_one_task(id), statusList=__getTodoStatusAsList())
    
    with Session() as session:
        task = session.query(Tasks).get(id)
        if task is None:
            abort(404)

        task.title = request.form.get('title')
        task.description = request.form.get('description')
        task.status = request.form.get('status')
        task.dueDate = datetime.strptime(request.form.get('dueDate'), '%Y-%m-%d').date()

        todoTaskComments = TodoTaskComments(taskComments = request.form.get('taskComments'), creationDate = date.today(), task_systemTaskId=task.systemTaskId)
        session.add(todoTaskComments) 

        session.commit()
        session.refresh(task)

    return redirect(url_for("index")) 

@app.route("/todo-app/tasks/delete/<int:id>", methods=["GET"])
def delete_task(id):
    # python -m pip install pyautogui 
    answer = pyautogui.confirm(text="Are you sure you want to delete?", title="Delete Confirmation")
    print("Answer=",answer)

    if answer == "OK":
        with Session() as session:
            task = session.query(Tasks).get(id)
            if task is None:
                abort(404)
        
            session.delete(task)
            session.commit()
    return redirect(url_for("index"))

def __jsonResponse(task, todoTaskCommentsList):
    todoTaskCommentSet = []
    taskDict = {
        'systemTaskId' : task.systemTaskId,
        'title' : task.title,
        'description' : task.description,
        'status' : task.status,
        'dueDate' : task.dueDate,
        'creationDate' : task.creationDate,
        'todoTaskCommentSet' : todoTaskCommentSet,
        }
    
    if (todoTaskCommentsList is not None):
        for todoTaskComment in todoTaskCommentsList:
            todoTaskCommentDict = {
                'systemTodoTaskCommentsId': todoTaskComment.systemTodoTaskCommentsId,
                'taskComments': todoTaskComment.taskComments,
                'creationDate': todoTaskComment.creationDate,
                'task_systemTaskId': todoTaskComment.task_systemTaskId
            }

            taskDict["todoTaskCommentSet"].append(todoTaskCommentDict)
       
    return taskDict
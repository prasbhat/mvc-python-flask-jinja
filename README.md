# mvc-python-flask-jinja

We will build a ***MVC application using Python with Flask Framework and Jinja Template*** for a **Todo Task Application** in that:

- Each **Todo Task** has *id, title, description, creation date, due date, status and comments*.
- User can *Create New Task, Update Existing Task, View All Tasks as List, View a Task and Delete a Task*.

## Requirements
### Install Python 
Install latest version for your platform from [here](https://www.python.org/downloads/windows/). Select the latest version of **Python 3** and download the Windows Installer. Click on the downloaded *.exe* and follow the on-screen instructions to complete the download.

### Integrated Development Environment (IDE) for Code Development
You can use any Text Editor or IDE of your choice. I will be using the **Visual Studio Code**.

If you wish to use the **Visual Studio Code**, download the latest version from [here](https://aka.ms/win32-x64-user-stable). Click on the downloaded *.exe* and complete the installation.

### Install the Python Extension for the VS Code
Install the [Python extension for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python) from the Visual Studio Marketplace.
1. You can browse and install extensions from within VS Code. Bring up the Extensions view by clicking on the *Extensions icon* in the **Activity Bar** on the side of VS Code or the **View: Extensions** command (`Ctrl+Shift+X`).
2. Browse for **Python** and click on **Install** button.

## Running the application locally
Run this Python application on your local machine by following below steps:

```shell
git clone https://github.com/prasbhat/mvc-python-flask-jinja.git
cd mvc-python-flask-jinja
py -3 -m venv .venv
.venv\Scripts\activate
flask run --port 8080
```

More detailed documentation regarding this project can be found [here](https://myzonesoft.com/post/mvc-python-flask-jinja/).
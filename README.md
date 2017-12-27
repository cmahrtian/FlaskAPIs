# How to Run/Deploy

1. Navigate into the root directory of the project and create a virtual environment by typing the command **virtualenv venv**. This creates a **venv** directory in the project folder.

2. Type **source venv/bin/activate** (or **source venv/scripts/activate**) to run the program in the aforementioned virtual environment.

3. Run **pip install** for the following packages:
* flask
* flask-cors
* flask-jsonpify
* flask-restful
* flask-sqlalchemy
* pymssql
* python-dotenv

4. Run **pip freeze** so that the virtual environment remembers which packages to use moving forward.

5. Run **python server.py** to run the program and open the page at [http://127.0.0.1:5002/](http://127.0.0.1:5002/).

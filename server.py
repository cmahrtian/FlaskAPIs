# custom packages
import os
from os import getenv
import pymssql
from dotenv import load_dotenv
import collections

# from Agarwal Python REST tutorial
from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify

# from Agarwal Python REST tutorial
app = Flask(__name__)
api = Api(app)

# custom DB connection
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

server = getenv('MSSQL_SERVER')
user = getenv('MSSQL_USER')
password = getenv('MSSQL_PASS')
db = getenv('MSSQL_DB')

conn = pymssql.connect(server, user, password, db)
cursor = conn.cursor()

class Teachers(Resource):
	def get(self):
		# perform query, return JSON result
		cursor.execute(getenv('TEACHERS_QUERY'))
		return cursor.fetchall()

class Schools(Resource):
	def get(self):
		cursor.execute(getenv('SCHOOLS_QUERY'))
		return cursor.fetchall()

# routes
api.add_resource(Teachers, '/teachers')
api.add_resource(Schools, '/schools')

if __name__ == '__main__':
	app.run(port=5002)
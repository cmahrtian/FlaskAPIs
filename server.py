# custom packages
import os
import pymssql
from dotenv import load_dotenv

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

db_uri_string = 'mssql+pymssql://' + os.getenv('MSSQL_USER') +':'+ os.getenv('MSSQL_PASS') +'@'+ os.getenv('MSSQL_SERVER') +':'+ os.getenv('MSSQL_PORT') +'/'+ os.getenv('MSSQL_DB')
db_connect = create_engine(db_uri_string)

class Teachers(Resource):
	def get(self):
		# connect to database
		conn = db_connect.connect()
		# perform query, return JSON result
		query = conn.execute("select Top 100 EmployeeID, LastName, FirstName from GEX_RBAC")
		result =  {'teachers': [dict(zip(tuple (query.keys()), i)) for i in query.cursor]}
		return jsonify(result)

# routes
api.add_resource(Teachers, '/teachers')

if __name__ == '__main__':
	app.run(port=5002)
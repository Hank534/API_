from flask import Flask
from flask_restful import Resource, Api ,reqparse
import pandas as pd
import ast

app = Flask(__name__)
api = Api(app)

class Users(Resource):
    def get(self):
        data = pd.read_csv('users.csv') # Read local CSV
        data = data.to_dict() # convert to Json ish py Dict {}
        return {'data': data}, 200 # res 200 for successful getter()
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('myID', required=True)
        parser.add_argument('Name', required=True)
        parser.add_argument('city', required=True)
        parser.add_argument('location', required=True)
        arg = parser.parse_args()

        # Reading CSV
        data = pd.read_csv('users.csv')



class Locations(Resource):
    pass
api.add_resource(Locations, '/locations')

if __name__ == '__main__':
    app.run()

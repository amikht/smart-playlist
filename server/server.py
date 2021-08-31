from flask import Flask
from flask_restful import Resource, Api

import server.api.psql_util as psql
from server.api.smpl_api import *


app = Flask(__name__)

api = Api(app)

# Add API endpoints
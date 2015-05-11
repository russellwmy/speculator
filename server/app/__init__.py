import os
import sys

from flask import Flask, render_template
from flask.ext.restful import Api
from flask.ext.sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config.from_object('config')
config = app.config

api = Api(app)

db = SQLAlchemy(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from app.users.models import *
from app.tickers.models import *
db.create_all()


API_URI = ''

from app.auth.resources import LoginResource
api.add_resource(LoginResource, API_URI+'/login')




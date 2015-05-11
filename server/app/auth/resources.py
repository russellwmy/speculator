from flask import jsonify
from flask.ext.restful import request, Resource
import jwt
import datetime
from app import db, app
from app.users.models import User

class LoginResource(Resource):
    def post(self):
        resp = dict()
        try:
            data = request.get_json(force=True)
            username = data.get('username')
            password = data.get('password')
            user =user = User.query.filter(User.username==username).first()
            if user:
                if user.verify_password(password):
                    data = dict(
                        uid = user.id,
                        exp = datetime.datetime.now() + app.config.get('JWT_EXP_DELTA')
                    )
                    token = jwt.encode(data,app.config.get('SECRET'))
                    resp['access_token'] = token.decode('utf-8')
                else:
                  raise Exception('Incorrect credential')
            else:
                raise Exception('User doesn\'t exist')
        except Exception as e:
          return str(e), 401
        return resp, 201


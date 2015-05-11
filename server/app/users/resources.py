from flask import jsonify
from flask.ext.restful import request, Resource
from app.users.models import User
from app import db, app
import jwt
import datetime

class LoginResource(Resource):

    def post(self):
        resp = dict()
        try:
            data = request.get_json(force=True)
            email = data.get('email')
            password = data.get('password')
            user =user = User.query.filter(User.email==email).first()
            if user:
                if user.verify_password(password):
                    data = dict(
                        uid = user.id,
                        exp = datetime.datetime.now() + app.config.get('JWT_EXP_DELTA')
                    )
                    token = jwt.encode(data,app.config.get('SECRET_KEY'))
                    resp['data'] = dict(
                        toekn = token.decode("utf-8")
                    )
            else:
                raise Exception('User does\'nt exist')
        except Exception as e:
          return e.message, 401
        return jsonify(resp), 201

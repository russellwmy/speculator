from functools import wraps
from flask import request, _request_ctx_stack
import jwt
from app import app
from app.users.models import User
from werkzeug.local import LocalProxy
current_user = LocalProxy(lambda: getattr(_request_ctx_stack.top, 'current_user', None))

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth = request.headers.get('Authorization')
        try:
            m, token = auth.split(' ')
            data = jwt.decode(token, app.config.get('SECRET'))
            uid = data.get('uid')
            user =  User.query.get(uid)
            if user:
                _request_ctx_stack.top.current_user = user
                return f(*args, **kwargs)
        except:
            return 'Access Denied', 401
    return decorated_function
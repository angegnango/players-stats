import jwt
from functools import wraps
from flask import jsonify, request
from api.config.database import jwt_secret


def generate_token(payload):

    """ generate token 
    param (object) : user json object { email: admin@test.fr }
    return (str): json web token
    """

    token = jwt.encode(payload, jwt_secret, algorithm="HS256")

    return token


def auth_required(f):

    """ auth decorator to secure our endpoints 
    param (function) : function to wrap
    """

    @wraps(f)
    def decorator(*args, **kwargs):

        token = None

        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']

        if not token:
            return jsonify({'message': 'a valid token is missing'}), 400

        try:
            current_user = jwt.decode(token, jwt_secret, algorithms="HS256")
         
        except:
            return jsonify({'message': 'token is invalid'}), 403

        return f(*args, **kwargs)

    return decorator
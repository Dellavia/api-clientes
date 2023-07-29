from flask import request
from functools import wraps


auth = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-DV-API-KEY'
        }
    }


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'X-DV-API-KEY' in request.headers:
            token = request.headers.get('X-DV-API-KEY')

        if not token:
            return {'message' : 'Token is missing'}, 401

        if token != 'a10b20c30':
            return {'message': 'Invalid Token'}, 401

        return f(*args, **kwargs)
    return decorated
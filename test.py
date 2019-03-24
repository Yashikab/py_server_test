from bottle import route, run 
from bottle import post, get, put, delete, request, response
import json

tests = [ 
        {'user_id': "TaroYamada", 'passwird': 'PaSSwd4TY', 'nickname': 'たろー', 'comment': '僕は元気です'}
]

@get('/tests')
def tests_list():
    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'
    return json.dumps(tests)

@get('/tests/users/<user_id>')
def a_book(id):
    search = filter(lambda book: book['id'] == id, tests)
    obj = next(search, None)
    if obj is not None:
        return obj
    else:
        response.status = 404 
        return {}

@post('/tests/signup')
def create_info():
    tests.append(request.json)
    return request.json

@put('/tests/users/<user_id>')
def update_info(id):
    search = filter(lambda book: book['id'] == id, tests)
    obj = next(search, None)

    if obj is not None:
        index = tests.index(obj)
        tests[index] = request.json
        return request.json
    else:
        response.status = 404 
        return {}

@delete('/tests/close')
def delete_info(id):
    search = filter(lambda book: book['id'] == id, tests)
    obj = next(search, None)

    if obj is not None:
        index = tests.index(obj)
        del tests[index]
        return {}
    else:
        response.status = 404
        return {}

run (host='localhost', port=8081, debug=True, reloader=True)
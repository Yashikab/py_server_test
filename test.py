# -*- coding: utf-8 -*-
import os
from bottle import route, run 
from bottle import post, get, put, delete, request, response
import json

tests = [ 
        {'user_id': "TaroYamada", 'password': 'PaSSwd4TY', 'nickname': 'たろー', 'comment': '僕は元気です'}
]

def _make_format(msg: str, obj: dict) -> dict:
    ret_dict = {}
    ret_dict["message"] = msg
    ret_dict["user"] = obj
    return obj

@get('/tests')
def tests_list():
    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'
    return json.dumps(tests)

@get('/tests/users/<user_id>')
def a_book(user_id):
    try:
        search = filter(lambda t: t['user_id'] == user_id, tests)
        obj = next(search, None)
        if obj is not None:
            response.status = 200
            return _make_format("User details by user_id", obj)
        else:
            response.status = 404 
            return {"message":"No User found"}
    except:
        response.status = 401
        return {"message":"Authentication Faild"}

@post('/tests/signup')
def create_info():
    try:
        body = request.params
        if body.user_id is None or body.password is None:
            response.status = 400
            return {
                    "message": "Account creation failed",
                    "cause": "required user_id and password"
                    }
        else:
            form = {}
            form["user_id"] = body.user_id
            form["password"] = body.password
            if body.nickname is None:
                form["nickname"] = body.user_id
            else:
                form["nickname"] = body.nickname
        response.status = 200
        return request.json
    except:
        response.status = 400
        return {
                "message": "Account creation failed",
                "cause": "required user_id and password"
                }


@put('/tests/users/<user_id>')
def update_info(user_id):
    search = filter(lambda book: book['id'] == id, tests)
    obj = next(search, None)

    if obj is not None:
        index = tests.index(obj)
        tests[index] = request.json
        response.status = 200
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
        response.status = 200
        return {"message": "Account and user successfully removed"}
    else:
        response.status = 404
        return {}

run (host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
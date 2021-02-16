from flask import Flask, request, Response
import json 

from db_connection import get_students, add_student, delete_student, update_student
from validation import validate


app = Flask(__name__)

@app.route('/students', methods = ['GET'])
def students():
    data = get_students()
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/students/add', methods = ['POST'])
def add():
    args = request.get_json()

    check = validate(args['name'],args['mark'])
    if check['isValid']:
        result = add_student(args['name'],args['mark'])
    else:
        result = check
    response = app.response_class(
        response=json.dumps(result),
        status=200,
        mimetype='application/json'
    )
    
    return response

@app.route('/students/delete', methods = ['POST'])
def delete():
    args = request.get_json()
    result = delete_student(args['id'])
    response = app.response_class(
        response=json.dumps(result),
        status=200,
        mimetype='application/json'
    )
    
    return response
	
@app.route('/students/update', methods = ['POST'])
def update():

    args = request.get_json()

    check = validate(args['name'],args['mark'])
    if check['isValid']:
        result = update_student(args['id'],args['name'],args['mark'])
    else:
        result = check
    response = app.response_class(
        response=json.dumps(result),
        status=200,
        mimetype='application/json'
    )
    
    return response
	

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)

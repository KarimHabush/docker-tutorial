from flask import Flask, request, Response
import json 



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
	

#Database functions 
  
import mysql.connector

db = mysql.connector.connect(
  host="db",
  user="root",
  password="root",
  database="students_manager"
)
db_cursor = db.cursor()

def get_students(): 
  data={}
  try:
    db_cursor.execute("SELECT * from students")
    data['result'] = db_cursor.fetchall()
    data['status'] = "success"
  except Exception:
    data['error'] = "An unexpected error occured!"
    data['status'] = "failure"
  return data


def add_student(name,mark): 
  data = {}
  query = ("INSERT INTO students (name, mark) VALUES (%s, %s)")
  args = (name,mark)
  try:
    db_cursor.execute(query, args)
    db.commit()
    data['result'] = "L'étudiant est ajouté avec succès"
    data['status'] = "success"
  except Exception:
    data['error'] = "L'étudiant n'est pas ajouté"
    data['status'] = "failure"
  return data

def delete_student(id):
  data = {}
  try:
    query = ("DELETE FROM students where id = %s")
    args= (id,)

    db_cursor.execute(query,args)
    db.commit()
    data['result'] = "L'étudiant est supprimé avec succès"
    data['status'] = "success"
  except Exception:
    data['error'] = "L'étudiant n'est pas été supprimé"
    data['status'] = "failure"
  return data

def update_student(id,name,mark):
  data = {}
  try:
    query = ("UPDATE students SET name=%s , mark=%s WHERE id = %s")
    args= (name,mark,id)
    db_cursor.execute(query,args)
    db.commit()
    data['result'] = "L'étudiant est modifié avec succès"
    data['status'] = "success"
  except Exception:
    data['error'] = "L'étudiant n'est pas été modifié"
    data['status'] = "failure"
  return data


#Validation 
import re

def validate(name,mark): 
    error={
        "isValid": True,
        "status":"success"
    }
    if float(mark)<0 or float(mark)>20: 
        error['status'] = "failure"
        error['isValid'] = False
        error['mark'] = "Mark should be between 0 & 20"
    if not bool(re.fullmatch('[A-Za-z]{2,25}( [A-Za-z]{2,25})?', name)):
        error['isValid'] = False
        error['status'] = "failure"
        error['name'] = "Name is not valid"

    return error



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)

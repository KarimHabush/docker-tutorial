  
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
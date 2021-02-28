from flask import Flask, render_template, request,redirect, url_for
import requests
import json

app = Flask(__name__, template_folder='.')
@app.route('/')
def homepage():
    msg=""
    r = requests.get(
        'http://localhost:5000/students')
    if request.args.get("status")=="failure":
        msg="L'opération a échoué, vérifiez vos données et réessayez!"
    elif request.args.get("status")=="success":
        msg="L'opération a bien été executé!"
    return render_template('./templates/index.html',students=r.json()['result'],messages=msg)

@app.route('/delete',methods=['POST'])
def delete():
    data = {
        "id": request.form['id']
    } 
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

    res = requests.post('http://localhost:5000/students/delete', json=data, headers=headers)
    return redirect(url_for(".homepage",status=json.loads(res.text)['status']))

@app.route('/update',methods=['POST'])
def update():
    data = {
        "id": request.form['id'],
        "name": request.form['name'],
        "mark": request.form['mark'],
    } 
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

    res = requests.post('http://localhost:5000/students/update', json=data, headers=headers)
    return redirect(url_for(".homepage",status=json.loads(res.text)['status']))

@app.route('/add',methods=['POST'])
def add():
    data = {
        "name": request.form['name'],
        "mark": request.form['mark'],
    } 
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

    res = requests.post('http://localhost:5000/students/add', json=data, headers=headers)
    print(res.text)
    return redirect(url_for(".homepage",status=json.loads(res.text)['status']))


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3000)

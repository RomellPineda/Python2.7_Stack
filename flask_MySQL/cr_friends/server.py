from flask import Flask, render_template, request, session, redirect, flash
from mysqlconnection import connectToMySQL
app = Flask(__name__)
app.secret_key = 'elohel'

mysql = connectToMySQL('twitter')
print('/// cleared hot ' * 20)

mysql = connectToMySQL('mydb') # target database

@app.route('/')
def index():
    # pulling from db
    # operational
    users = mysql.query_db('SELECT * FROM users;')
    print('got em, Coach' * 20)
    return render_template('index.html', friends = users)

@app.route('/add', methods=['POST'])
def validate():
    # insert into db
    # not yet operational
    print(request.form)
    mysql.query_db("INSERT INTO users (first_name, last_name, occupation) VALUES ('request.form['first_name']', 'request.form['last_name']', 'request.form['occupation']')")
    return redirect('/added')

@app.route('/added')
def created():
    users = mysql.query_db('SELECT * FROM users;')
    return render_template('index.html', friends = users)

app.run(debug = True)
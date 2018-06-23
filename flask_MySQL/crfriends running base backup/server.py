from flask import Flask, render_template, request, session, redirect, flash
from mysqlconnection import connectToMySQL
app = Flask(__name__)
app.secret_key = 'elohel'

mysql = connectToMySQL('twitter')
print('/// cleared hot ' * 20)

mysql = connectToMySQL('twitter') # target database

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def validate():
    return redirect('/added')

@app.route('/added')
def created():
    print(session)
    return render_template('created.html')

app.run(debug = True)
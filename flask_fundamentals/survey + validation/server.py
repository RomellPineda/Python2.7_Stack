from flask import Flask, render_template, request, session, redirect, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'Yaaaaaaas'

print('/// cleared hot ' * 20)
@app.route('/')
def index():
    print('indexed')
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def validate():
    error = False
    if len(request.form['name']) < 2:
         flash('Name must be 2 more characters')
         error = True
    if not EMAIL_REGEX.match(request.form['email']):
        flash('Email is invalid')
        error = True
    if len(request.form['comment']) > 10:
        flash('No more words')
        error = True
    if error:
        return redirect('/')
    else:
        # !!! Hand off to created through session !!!
        session['name'] = request.form['name']
        session['email'] = request.form['email']
        session['location'] = request.form['location']
        session['language'] = request.form['language']
        session['comment'] = request.form['comment']
        return redirect('/created')

@app.route('/created')
def created():
    print(session)
    return render_template('created.html')

app.run(debug = True)
from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = 'FiddlersGreen'

print('/// cleared hot ' * 20)
@app.route('/')
def index():
    print('indexed')
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def create():
    print(request.form)
    print('name', request.form['name'])
    print('location', request.form['location'])
    print('language', request.form['language'])
    print('comment', request.form['comment'])
    return render_template('created.html')

@app.route('/danger')
def getout():
    print('a user tried to visit /danger.  we have redirected the user to /')
    return render_template('index.html')

app.run(debug = True)
from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = 'FiddlersGreen'

print(__name__ * 50)
@app.route('/')
def mockdb():
    shmusers = ({'first_name' : 'Michael', 'last_name' : 'Choi'}, {'first_name' : 'John', 'last_name' : 'Supsupin'}, {'first_name' : 'Mark', 'last_name' : 'Guillen'}, {'first_name' : 'KB', 'last_name' : 'Tonel'})
    how_far = int(len(shmusers))
    return render_template('index.html', users = shmusers, how_far = how_far)

app.run(debug = True)
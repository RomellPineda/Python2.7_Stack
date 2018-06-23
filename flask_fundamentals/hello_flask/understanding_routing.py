from flask import Flask
app = Flask(__name__)

print(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def yo_dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def say(name):
    print(name)
    return 'Hi ' +name

@app.route('/repeat/<x>/<word>')
def repeat(word, x):
    print(word, x)
    return word * int(x)

if __name__=="__main__":
    app.run(debug=True)
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def holla_world():
    return 'Holla World!'

@app.route('/play')
def play():
    return render_template('index.html')

@app.route('/play/<x>')
def more(x):
    return render_template('index.html', x = int(x))

# run some logic here for x = 1...

@app.route('/play/<x>/<newcolor>')
def newcolor(x, newcolor):
    return render_template('index.html', x = int(x), newcolor = newcolor)

if __name__=='__main__':
    app.run(debug=True)
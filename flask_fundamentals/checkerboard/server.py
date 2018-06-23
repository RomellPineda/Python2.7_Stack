from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def eights():
    return render_template('index.html', x = 4, y = 4)

@app.route('/<x>/<y>')
def more(x, y):
    return render_template('index.html', x = int(x), y = int(y))

if __name__=='__main__':
    app.run(debug=True)
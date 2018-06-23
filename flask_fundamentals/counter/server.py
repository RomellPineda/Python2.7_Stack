from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = 'ICantEven'

print('// cleared hot' * 23)

@app.route('/')
def index():
    if "totes" not in session:
        session['totes'] = 0
    else:
        session['totes'] += 1
    print(session['totes'])
    return render_template('index.html')

@app.route('/reset')
def reset():
    session['totes'] = 0
    return redirect('/')

@app.route('/addtwo')
def addtwo():
    session['totes'] +=1
    return redirect('/')

if __name__=='__main__':
    app.run(debug = True)
from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = 'FiddlersGreen'

print('// fruit_store_open ' * 12)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/checkout', methods=['POST'])
def checkout():
    print(request.form)
    return redirect('/checkedout')

@app.route('/checkedout')
def checkedout():
    print('//' * 47)
    f_totes = int(request.form['apple']) + int(request.form['banana']) + int(request.form['orange'])
    return render_template('checkedout.html', fruit_totes = f_totes, date = 5)

if __name__=='__main__':
    app.run(debug = True)
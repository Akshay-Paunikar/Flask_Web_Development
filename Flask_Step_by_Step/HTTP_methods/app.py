from flask import Flask, url_for, redirect, request, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('login.html')

@app.route('/success/<name>')
def success(name):
    return 'Welcome %s' %name

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        user = request.form['name']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('name')
        return redirect(url_for('success', name=user))
    
if __name__ == "__main__":
    app.run(debug=True)
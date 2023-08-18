from flask import Flask, url_for, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("index.html")

@app.route('/', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        score = int(request.form['marks'])
        user = request.form['name']
        return render_template("result.html", score=score, name=user)
    else:
        score = int(request.args.get('marks'))
        user = request.args.get('name')
        return render_template("result.html", score=score, name=user)
    
if __name__ == "__main__":
    app.run(debug=True)
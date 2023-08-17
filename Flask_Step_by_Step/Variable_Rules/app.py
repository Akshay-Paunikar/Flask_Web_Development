from flask import Flask

app = Flask(__name__)

@app.route('/hello/<name>')
def site_name(name):
    return 'Hello %s!' %name

@app.route('/flask')
def hello_flask():
   return 'Hello Flask'

@app.route('/python/')
def hello_python():
   return 'Hello Python'

if __name__ == "__main__":
    app.run(debug=True)
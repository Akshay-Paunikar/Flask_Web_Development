from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World ! Let's Learn Flask today !!!!"

@app.route('/products')
def products():
    return "this is products page"

if __name__ == "__main__":
    app.run(debug=True)
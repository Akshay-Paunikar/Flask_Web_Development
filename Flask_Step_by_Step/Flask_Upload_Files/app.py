from flask import Flask, request, render_template, url_for, redirect
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return "file uploaded successfully"
    
if __name__ == "__main__":
    app.run(debug=True)
# import libraries
from flask import Flask, render_template, redirect, url_for, request, flash 
from flask_sqlalchemy import SQLAlchemy

# create extension
db = SQLAlchemy()

# create the app
app = Flask(__name__)

# configure the SQLite database, relative to the app instance folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# initialize app with the extension
db.init_app(app)

class students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    zipcode = db.Column(db.Integer, nullable=False)
    
with app.app_context():
    db.create_all()
    
@app.route('/')
def home():
    return render_template('home.html', students=students.query.all())

@app.route('/student')
def info():
    return render_template('student.html')

@app.route('/new', methods=['GET', 'POST'])
def create_new():
    if request.method == 'POST':
        student = students(
            name = request.form['name'],
            gender = request.form['gender'],
            city = request.form['city'],
            zipcode = int(request.form['zipcode'])
        )
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('home', id = student.id))
    return render_template('student.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    if request.method=='POST':
        name = request.form['name']
        gender = request.form['gender']
        city = request.form['city']
        zipcode = int(request.form['zipcode'])
        student = students.query.filter_by(id=id).first()
        student.name = name
        student.gender = gender
        student.city = city
        student.zipcode = zipcode
        db.session.add(student)
        db.session.commit()
        return redirect("/")
        
    student = students.query.filter_by(id=id).first()
    return render_template('update.html', student=student)

@app.route('/delete/<int:id>')
def delete(id):
    student = students.query.filter_by(id=id).first()
    db.session.delete(student)
    db.session.commit()
    return redirect("/")    

if __name__ == "__main__":
    app.run(debug=True)
        
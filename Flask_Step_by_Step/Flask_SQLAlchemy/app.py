from flask import Flask, render_template, redirect, url_for, request, flash 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

app = Flask(__name__)

e = create_engine("sqlite:///students.db")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    zipcode = db.Column(db.Integer, nullable=False)
    
def __init__(self, name, gender, city, zipcode):
    self.name = name
    self.gender = gender
    self.city = city
    self.zipcode = zipcode
    
@app.route('/')
def home():
    return render_template('home.html', students=students.query.all())

@app.route('/newStudent', methods=['GET','POST'])
def new():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['gender'] or not request.form['city'] or not request.form['zipcode']:
            flash("Please check and enter data in all fields")
        else:
            name = request.form['name']
            gender = request.form['gender']
            city = request.form['city']
            zipcode = int(request.form['zipcode'])
            student = students(name=name, gender=gender, city=city, zipcode=zipcode)
            
            db.session.add(student)
            db.session.commit()
            flash("Record added successfully")
            return redirect(url_for('home'))
    return render_template('student.html')

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
        
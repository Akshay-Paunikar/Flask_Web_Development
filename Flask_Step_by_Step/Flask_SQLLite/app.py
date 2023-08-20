from flask import Flask, request, render_template, url_for, redirect
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/student')
def student():
    return render_template('student.html')

@app.route('/student', methods=['GET','POST'])
def addData():
    if request.method == 'POST':
        try:
            name = request.form['name']
            gender = request.form['gender']
            city = request.form['city']
            zipcode = int(request.form['zipcode'])
            
            with sql.connect("database.db") as con:
                cur = con.cursor()
                
                cur.execute("INSERT INTO STUDENTS (name, gender, city, zipcode) VALUES (?, ?, ?, ?)", (name, gender, city, zipcode))
                
                con.commit()
                message = "Record added successfully"
        except:
            con.rollback()
            message = "Error occured during insert operation"
        finally:      
            return render_template('result.html', message = message)
            con.close()

@app.route('/database')
def database():
    con = sql.connect('database.db')
    con.row_factory = sql.Row
    
    cur = con.cursor()
    cur.execute("SELECT * FROM STUDENTS")
    
    rows = cur.fetchall();    
    return render_template('database.html', rows = rows)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, url_for, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("student.html")

@app.route('/', methods=['GET', 'POST'])
def average():
    if request.method == 'POST':
        form_data = request.form
        name = request.form['Name']
        physics = int(request.form['Physics'])
        chemistry = int(request.form['Chemistry'])
        maths = int(request.form['Mathematics'])
        
        total_marks = physics + chemistry + maths
        final_average = round(total_marks/3,0)
        
        return render_template("result.html", average_total = final_average, data=form_data, name = name, total=total_marks)
    
if __name__ == '__main__':
   app.run(debug = True)
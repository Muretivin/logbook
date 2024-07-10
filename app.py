from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import date, datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(100), nullable=False)
    registration_no = db.Column(db.String(50), nullable=False)
    faculty = db.Column(db.String(50), nullable=False)
    course_of_study = db.Column(db.String(50), nullable=False)
    stage_year_of_study = db.Column(db.String(50), nullable=False)
    company_address = db.Column(db.Text, nullable=False)
    supervisor_name = db.Column(db.String(100), nullable=False)
    designation = db.Column(db.String(50), nullable=False)
    contact_number = db.Column(db.String(20), nullable=False)
    duration_from = db.Column(db.Date, nullable=False)
    duration_to = db.Column(db.Date, nullable=False)
    weekly_summary = db.Column(db.Text, nullable=False)
    supervisor_comments = db.Column(db.Text, nullable=False)
    supervisor_name_final = db.Column(db.String(100), nullable=False)
    supervisor_department = db.Column(db.String(50), nullable=False)
    supervisor_date = db.Column(db.Date, nullable=False)
    supervisor_signature = db.Column(db.String(100), nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        student_name = request.form['student_name']
        registration_no = request.form['registration_no']
        faculty = request.form['faculty']
        course_of_study = request.form['course_of_study']
        stage_year_of_study = request.form['stage_year_of_study']
        company_address = request.form['company_address']
        supervisor_name = request.form['supervisor_name']
        designation = request.form['designation']
        contact_number = request.form['contact_number']
        duration_from = datetime.strptime(request.form['duration_from'], '%Y-%m-%d').date()
        duration_to = datetime.strptime(request.form['duration_to'], '%Y-%m-%d').date()
        weekly_summary = request.form['week_summary']
        supervisor_comments = request.form['supervisor_comments']
        supervisor_name_final = request.form['supervisor_name_final']
        supervisor_department = request.form['supervisor_department']
        supervisor_date = datetime.strptime(request.form['supervisor_date'], '%Y-%m-%d').date()
        supervisor_signature = request.form['supervisor_signature']

        new_student = Student(student_name=student_name, registration_no=registration_no, faculty=faculty,
                              course_of_study=course_of_study, stage_year_of_study=stage_year_of_study,
                              company_address=company_address, supervisor_name=supervisor_name, designation=designation,
                              contact_number=contact_number, duration_from=duration_from, duration_to=duration_to,
                              weekly_summary=weekly_summary, supervisor_comments=supervisor_comments,
                              supervisor_name_final=supervisor_name_final, supervisor_department=supervisor_department,
                              supervisor_date=supervisor_date, supervisor_signature=supervisor_signature)

        db.session.add(new_student)
        db.session.commit()

        return redirect(url_for('show_students'))

@app.route('/students')
def show_students():
    students = Student.query.all()
    return render_template('students.html', students=students)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

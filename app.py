from flask import Flask, jsonify
from models import db, Students, Subjects, Teachers

app = Flask("server")

# Configuration for the PostgreSql database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg://@localhost:5432/school_flask_postgres'
app.json.sort_keys = False

db.init_app(app)

@app.route("/students/", methods=['GET'])
def get_students():
    students = []

    for student in Students.query.all():
        student_subject = student.subject

        for subject in Subjects.query.all():
            subject_id = subject.id

            if subject.id == student_subject:
                for teacher in Teachers.query.all():
                    if teacher.id == subject_id:
                        student = {
                            "id": student.id,
                            "first_name": student.first_name,
                            "last_name": student.last_name,
                            "age": student.age,
                            "class": {
                                "subject": subject.subject,
                                "teacher": f"{teacher.first_name} {teacher.last_name}"
                            }
                        }
        students.append(student)
    return jsonify(students)


@app.route("/teachers/", methods=['GET'])
def get_teachers():
    teachers = []
    students_list = []

    for teacher in Teachers.query.all():
        teacher_subject = teacher.subject

        for subject in Subjects.query.all():
            subject_name = subject.subject
            
            for student in Students.query.all():
                if student.subject == teacher_subject:
                    students_list.append(f"{student.first_name} {student.last_name}")
            
            individual = {
                        "first_name": teacher.first_name,
                        "last_name": teacher.last_name,
                        "age": teacher.age,
                        "subject": {
                        "class": subject_name,
                        "students": students_list
                        }
            }   
            students_list = []
        teachers.append(individual)
    return jsonify(teachers)


@app.route("/individuals/", methods=['GET'])
def get_individuals():
    subj = []
    students_list = []

    for subject in Subjects.query.all():
        for teacher in Teachers.query.all():
            if subject.id == teacher.subject:
                for student in Students.query.all():
                    if student.subject == subject.id:
                        students_list.append(f"{student.first_name} {student.last_name}")
                data = {
                    subject.subject: {
                        "students": students_list,
                        "teachers": f"{teacher.first_name} {teacher.last_name}"
                    }
                }
        subj.append(data)
        students_list = []
    return jsonify(subj)


app.run(debug=True, port=8000)
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Individual(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    subject = db.Column(db.String(50))

    def to_dictionary(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "subject": self.subject,
        }

class Teachers(Individual):
    id = db.Column(db.Integer, primary_key=True)

    def to_dictionary(self):
        return super().to_dictionary()


class Students(Individual):
    id = db.Column(db.Integer, primary_key=True)

    def to_dictionary(self):
        return super().to_dictionary()


class Subjects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(50))

    def to_dictionary(self):
        return {
            "id": self.id,
            "subject": self.subject
        }

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Staff(db.Model):
    __tablename__ = "staff"

    id_no = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    designation = db.Column(db.String, nullable=False)
    mts_no = db.Column(db.String)
    section = db.Column(db.String)


class ExamDate(db.Model):
    __tablename__ = "exam_dates"

    exam_date = db.Column(db.Date, primary_key=True)
    exam_name = db.Column(db.String, nullable=False)
    duty_type = db.Column(db.String, nullable=False)   # NEW
    active = db.Column(db.Boolean, default=True)


class Attendance(db.Model):
    __tablename__ = "attendance"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)

    id_no = db.Column(db.String, nullable=False, index=True)
    name = db.Column(db.String, nullable=False)
    designation = db.Column(db.String, nullable=False)

    exam_name = db.Column(db.String, nullable=False, index=True)
    exam_dates = db.Column(db.String, nullable=False)

    pdf_path = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class User(db.Model):
    __tablename__ = "users"

    username = db.Column(db.String, primary_key=True)
    password_hash = db.Column(db.String, nullable=False)
    role = db.Column(db.String, nullable=False)  # admin / user

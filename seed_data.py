from app import app
from db.models import db, Staff, ExamDate

from datetime import date

with app.app_context():

    # STAFF
    staff_data = [
        ("A_DS01", "Sanjay Chhabra", "DS"),
        ("B_US01", "Ajit Singh", "US"),
        ("L_MTS22", "Prem Pal Singh", "MTS"),
    ]

    for s in staff_data:
        if not Staff.query.get(s[0]):
            db.session.add(Staff(
                id_no=s[0],
                name=s[1],
                designation=s[2]
            ))

    # EXAM DATES
    exam_data = [
        (date(2024, 8, 19), "NDA & NA (II)", True),
        (date(2024, 9, 1), "CDS (II)", True),
    ]

    for e in exam_data:
        if not ExamDate.query.get(e[0]):
            db.session.add(ExamDate(
                exam_date=e[0],
                exam_name=e[1],
                active=e[2]
            ))

    db.session.commit()
    print("Seed data inserted")

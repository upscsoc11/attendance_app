from datetime import date
from db.models import ExamDate, db

e1 = ExamDate(
    exam_date=date(2025, 4, 21),
    exam_name="NDA & NA (II)",
    duty_type="Examination Duty"
)

e2 = ExamDate(
    exam_date=date(2025, 4, 22),
    exam_name="NDA & NA (II)",
    duty_type="Examination Duty"
)

db.session.add_all([e1, e2])
db.session.commit()

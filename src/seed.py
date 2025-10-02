from datetime import date
from faker import Faker
from models import Student, Group, Teacher, Subject, Grade
from connect import session


def seed():
    fake = Faker()

    student_1 = Student(name=fake.name())
    student_2 = Student(name=fake.name())

    teacher_1 = Teacher(name=fake.name())

    group_1 = Group(name=fake.domain_name(), students=[student_1, student_2])

    subject_1 = Subject(name="Math", teacher=teacher_1)

    grade_student_1 = Grade(
        value=4.4,
        created_at=date.today(),
        subject=subject_1,
        student=student_1
    )
    grade_student_2 = Grade(
        value=4.2,
        created_at=date.today(),
        subject=subject_1,
        student=student_2
    )

    session.add_all(
        [
            student_1,
            student_2,
            teacher_1,
            group_1,
            subject_1,
            grade_student_1,
            grade_student_2,
        ]
    )
    session.commit()
    session.close()


if __name__ == "__main__":
    seed()

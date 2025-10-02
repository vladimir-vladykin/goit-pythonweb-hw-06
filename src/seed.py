from datetime import date
import random
from faker import Faker
from models import Student, Group, Teacher, Subject, Grade
from connect import session


def seed():
    fake = Faker()
    
    groups_count = 3
    groups = [generate_group(fake, i + 1) for i in range(groups_count)]

    subject_groups = [
        ["Basic math", "Applied math", "Analysis"],
        ["Grammar", "Literature", "History"],
        ["Chemistry", "Biology"],
    ]

    teachers = []
    all_subjects = []
    for subject_group in subject_groups:
        teacher, subjects = generate_teacher_and_subjects(fake, subject_group)
        teachers.append(teacher)
        all_subjects.extend(subjects)

    grades = generate_grades(fake, groups, all_subjects)

    all_entities = []
    all_entities.extend(groups)
    all_entities.extend(teachers)
    all_entities.extend(all_subjects)
    all_entities.extend(grades)
    session.add_all(all_entities)

    session.commit()
    session.close()


def generate_group(fake: Faker, index: int) -> Group:
    group_name = f"ORM-GR-0{index}"
    group = Group(name=group_name)

    students = [Student(name=fake.name()) for i in range(1, 15)]
    group.students = students

    return group


def generate_teacher_and_subjects(
    fake: Faker, subject_names: list[str]
) -> tuple[Teacher, list[Subject]]:
    teacher = Teacher(name=fake.name())

    subjects = [Subject(name=name) for name in subject_names]
    teacher.subjects = subjects

    return teacher, subjects


def generate_grades(
    fake: Faker, groups: list[Group], subjects: list[Subject]
) -> list[Grade]:
    all_grades = []
    for group in groups:
        students = group.students

        for subject in subjects:
            for student in students:
                grade_value = round(random.uniform(1.0, 5.0), 2)
                all_grades.append(
                    Grade(
                        value=grade_value,
                        created_at=date.today(),
                        subject=subject,
                        student=student,
                    )
                )

    return all_grades


if __name__ == "__main__":
    seed()

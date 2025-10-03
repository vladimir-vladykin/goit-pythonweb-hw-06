from sqlalchemy import select, func, desc
from connect import session
from models import Student, Grade, Group, Subject, Teacher


def run_selects():
    selects = [
        select_1,
        select_2,
        select_3,
        select_4,
        select_5,
        select_6,
        select_7,
        select_8,
        select_9,
        select_10,
    ]

    for select in selects:
        print(f"\nExecute {select.__name__}()")
        print("-" * 40)
        select()
        print("-" * 40)


def select_1():
    q = (
        session.execute(
            select(
                Student.id,
                Student.name,
                func.avg(Grade.value).label("average_grade"),
            )
            .select_from(Student)
            .join(Grade)
            .group_by(Student.id)
            .order_by(desc(func.avg(Grade.value)))
            .limit(5)
        )
        .mappings()
        .all()
    )

    print(q)
    session.close()


def select_2():
    subject_name = "Basic math"
    q = (
        session.execute(
            select(
                Student.id,
                Student.name,
                func.avg(Grade.value).label("average_grade"),
            )
            .select_from(Student)
            .join(Grade)
            .where(Subject.name == subject_name)
            .group_by(Student.id, Subject.name)
            .order_by(desc(func.avg(Grade.value)))
        )
        .mappings()
        .first()
    )

    print(q)
    session.close()


def select_3():
    subject_name = "Analysis"
    q = (
        session.execute(
            select(
                Group.id,
                Group.name,
                func.avg(Grade.value).label("group_average_grade_by_subject"),
            )
            .select_from(Student)
            .join(Group)
            .join(Grade)
            .join(Subject)
            .where(Subject.name == subject_name)
            .group_by(Group.id, Group.name, Subject.name)
            .order_by(Group.id)
        )
        .mappings()
        .all()
    )

    print(q)
    session.close()


def select_4():
    group_id = 2

    q = (
        session.execute(
            select(
                Group.id,
                Group.name,
                func.avg(Grade.value).label("group_average_grade_in_total"),
            )
            .select_from(Student)
            .join(Group)
            .join(Grade)
            .where(Student.group_id == group_id)
            .group_by(Group.id, Group.name)
        )
        .mappings()
        .all()
    )

    print(q)
    session.close()


def select_5():
    teacher_id = 2

    q = (
        session.execute(
            select(
                Teacher.name.label("teacher_name"), Subject.name.label("subject_name")
            )
            .select_from(Teacher)
            .join(Subject)
            .where(Teacher.id == teacher_id)
        )
        .mappings()
        .all()
    )

    print(q)
    session.close()


def select_6():
    group_id = 3

    q = (
        session.execute(
            select(Student.id, Student.name, Group.name.label("group_name"))
            .select_from(Student)
            .join(Group)
            .where(Student.group_id == group_id)
            .order_by(Student.id)
        )
        .mappings()
        .all()
    )

    print(q)
    session.close()


def select_7():
    group_id = 1
    subject_name = "Chemistry"

    q = (
        session.execute(
            select(
                Student.id.label("student_id"),
                Student.name.label("student_name"),
                Subject.name.label("subject_name"),
                Grade.value.label("grade"),
                Group.name.label("group_name"),
            )
            .select_from(Grade)
            .join(Student)
            .join(Subject)
            .join(Group)
            .where(Group.id == group_id, Subject.name == subject_name)
            .order_by(desc(Grade.value))
        )
        .mappings()
        .all()
    )

    print(q)
    session.close()


def select_8():
    teacher_id = 1

    q = (
        session.execute(
            select(
                Teacher.id.label("teacher_id"),
                Teacher.name.label("teacher_name"),
                func.avg(Grade.value).label("average_grade_from_teacher"),
            )
            .select_from(Teacher)
            .join(Subject)
            .join(Grade)
            .where(Teacher.id == teacher_id)
            .group_by(Teacher.id, Teacher.name)
        )
        .mappings()
        .first()
    )

    print(q)
    session.close()


def select_9():
    student_id = 20

    q = (
        session.execute(
            select(
                Student.name.label("student_name"), Subject.name.label("subject_name")
            )
            .select_from(Student)
            .join(Grade)
            .join(Subject)
            .where(Student.id == student_id)
            .order_by(Subject.name)
        )
        .mappings()
        .all()
    )

    print(q)
    session.close()


def select_10():
    student_id = 40
    teacher_id = 1

    q = (
        session.execute(
            select(
                Student.name.label("student_name"), 
                Teacher.name.label("teacher_name"),
                Subject.name.label("subject_name")
            )
            .select_from(Student)
            .join(Grade)
            .join(Subject)
            .join(Teacher)
            .where(Student.id == student_id, Teacher.id == teacher_id)
            .order_by(Subject.name)
        )
        .mappings()
        .all()
    )

    print(q)
    session.close()


if __name__ == "__main__":
    run_selects()

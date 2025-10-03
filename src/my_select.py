from sqlalchemy import select, func, desc
from connect import session
from models import Student, Grade, Group, Subject


def run_selects():
    selects = [select_1, select_2, select_3, select_4]

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
                func.avg(Grade.value).label("group_average_grade_in_total")
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


if __name__ == "__main__":
    run_selects()

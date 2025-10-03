from sqlalchemy import select, func, desc
from connect import session
from models import Student, Grade, Group, Subject


def run_selects():
    selects = [select_1, select_2]

    for select in selects:
        print(f"Execute {select.__name__}()")
        select()
        print("-" * 40)


def example():
    q = (
        session.execute(
            select(
                Student.name,
                Group.name.label("group_name"),
                Subject.name.label("subject_name"),
                Grade.value.label("grade"),
            )
            .select_from(Student)
            .join(Group)
            .join(Grade)
            .join(Subject)
            .order_by(Student.id)
            .limit(10)
        )
        .mappings()
        .all()
    )

    print(q)

    session.close()


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


if __name__ == "__main__":
    run_selects()

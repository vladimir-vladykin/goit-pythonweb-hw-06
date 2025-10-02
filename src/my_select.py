from sqlalchemy import select
from connect import session
from models import Student, Grade, Group, Subject


def run_selects():
    select_1()


def select_1():
    q = (
        session.execute(
            select(Student.name, Group.name.label("group_name"), Subject.name.label("subject_name"), Grade.value.label("grade"))
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


if __name__ == "__main__":
    run_selects()

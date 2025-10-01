from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

# docker run --name orm-postgres-container -p 5432:5432 -e POSTGRES_DB=orm-university -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=567234 -d postgres
SQLALCHEMY_DATABASE_URL = (
    f"postgresql+psycopg2://postgres:567234@localhost:5432/orm-university"
)


engine = create_engine(SQLALCHEMY_DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

import pymysql
from sqlmodel import SQLModel, create_engine, Session

# MySQL Connection Details
DB_USER = "root"
DB_PASSWORD = ""
DB_HOST = "localhost"
DB_PORT = 3306  # XAMPP MySQL port
DB_NAME = "retinaai"

# 1. Create database if not exists using pymysql
def ensure_database_exists():
    connection = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT  # make sure port is specified here
    )
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        connection.commit()
    finally:
        connection.close()

# 2. SQLModel Setup
# Handle empty password properly in URL
auth_part = f"{DB_USER}:{DB_PASSWORD}" if DB_PASSWORD else f"{DB_USER}"
DATABASE_URL = f"mysql+pymysql://{auth_part}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

print(f"Connecting to database at: {DB_HOST}:{DB_PORT}/{DB_NAME}")
engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    try:
        ensure_database_exists()
        SQLModel.metadata.create_all(engine)
        print("Database tables synchronized successfully.")
    except Exception as e:
        print(f"DATABASE ERROR during startup: {e}")
        # Don't let the app crash silently

def get_session():
    with Session(engine) as session:
        yield session
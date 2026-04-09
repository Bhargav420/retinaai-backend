from sqlmodel import Session, select
from database import engine
from models.user import User

def verify_all_users():
    print(f"Verifying all users in MySQL database...")
    try:
        with Session(engine) as session:
            users = session.exec(select(User)).all()
            if not users:
                print("No users found.")
                return
            for u in users:
                if not u.is_verified:
                    u.is_verified = True
                    print(f"Verified user: {u.email} (ID: {u.id})")
            session.commit()
            print("Successfully verified all users.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    verify_all_users()

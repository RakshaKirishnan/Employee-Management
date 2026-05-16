from src.db.database import Base, engine
from src.schema.create_emp_table import Employee

def reset_db():
    print("Dropping all tables...")
    Base.metadata.drop_all(bind=engine)
    print("Recreating tables...")
    Base.metadata.create_all(bind=engine)
    print("Done! Tables recreated successfully.")

if __name__ == "__main__":
    reset_db()

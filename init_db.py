from src.db.database import Base, engine
# Import all models here so Base.metadata.create_all can discover them
from src.schema.create_emp_table import Employee

def init_db():
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully.")

if __name__ == "__main__":
    init_db()

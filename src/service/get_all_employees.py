from sqlalchemy.orm import Session
from src.schema.create_emp_table import Employee

def get_all_employees_service(db: Session):
    try:
        return db.query(Employee).all()
    except Exception as e:
        db.rollback()
        raise e
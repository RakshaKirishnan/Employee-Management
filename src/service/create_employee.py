from src.schema.create_emp_table import Employee
from src.models.create_employee import CreateEmployee
from sqlalchemy.orm import Session


def create_employee_service(employee: CreateEmployee, db: Session):
    try:
        new_emp=Employee(
            name=employee.name,
            age=employee.age,
            designation=employee.designation,
            email=employee.email,
            address=employee.address,
            phone=employee.phone
        )
        db.add(new_emp)
        db.commit()
        db.refresh(new_emp)
        return new_emp
    except Exception as e:
        db.rollback()
        raise e
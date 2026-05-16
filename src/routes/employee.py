from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.models.create_employee import CreateEmployee
from src.service.create_employee import create_employee_service
from src.service.get_all_employees import get_all_employees_service
from src.db.database import get_db

router = APIRouter(tags=["Employees"])  


@router.post("/employees")
def create_employee(employee: CreateEmployee, db: Session = Depends(get_db)):
    try:
        result = create_employee_service(employee, db)

        return {
            "message": "Employee created successfully",
            "data": result
        }
    except Exception as e:
        return {
            "message": "Employee creation failed",
            "error": str(e)
        }
@router.get("/employees")
def get_all_employees(db: Session = Depends(get_db)):
    try:
        result = get_all_employees_service(db)
        return {
            "message": "Employees fetched successfully",
            "data": result
        }
    except Exception as e:
        return {
            "message": "Failed to fetch employees",
            "error": str(e)
        }

from app.schema.employee import Employee as EmployeeModel
from sqlalchemy import select


class EmployeeRepository:

    @staticmethod
    async def create(db, employee):
        db_employee = EmployeeModel(
            employee_id=employee.employee_id,
            name=employee.name,
            phone=employee.phone,
            department_id=employee.department_id,
            role_id=employee.role_id,
            address=employee.address,
            email=employee.email,
        )
        db.add(db_employee)
        await db.commit()
        await db.refresh(db_employee)
        return db_employee

    @staticmethod
    async def get_by_id(db, employee_id):
        result = await db.execute(
            select(EmployeeModel).where(EmployeeModel.id == employee_id)
        )
        return result.scalar_one_or_none()

from app.repository.employee import EmployeeRepository
from app.repository.department import DepartmentRepository
from app.repository.role import RoleRepository
from app.exceptions.exceptions import NotFoundError, BadRequestError
from app.utils.logger import logger


class EmployeeService:

    @staticmethod
    async def create_employee(employee, db):

        # phone validation
        if len(employee.phone) != 10:
            raise BadRequestError("Invalid phone number")

        # check department exists
        dept = await DepartmentRepository.get_by_id(db, employee.department_id)
        if not dept:
            raise NotFoundError("Department not found")

        # check role exists
        role = await RoleRepository.get_by_id(db, employee.role_id)
        if not role:
            raise NotFoundError("Role not found")

        logger.info(f"Creating employee: {employee.name}")
        return await EmployeeRepository.create(db, employee)

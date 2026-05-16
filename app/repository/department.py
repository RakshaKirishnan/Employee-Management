
from sqlalchemy import select
from app.schema.department import Department


class DepartmentRepository:

    @staticmethod
    async def get_by_id(db, dept_id):
        result = await db.execute(
            select(Department).where(Department.id == dept_id)
        )
        return result.scalar_one_or_none()
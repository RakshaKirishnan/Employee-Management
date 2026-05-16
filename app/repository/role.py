from app.schema.role import Role
from sqlalchemy import select


class RoleRepository:

    @staticmethod
    async def get_by_id(db, role_id):
        result = await db.execute(
            select(Role).where(Role.id == role_id)
        )
        return result.scalar_one_or_none()
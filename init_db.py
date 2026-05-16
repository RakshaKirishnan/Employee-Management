# init_db.py

import asyncio
from app.db.base import engine
from app.db.base import Base

# import all models so they register on Base
from app.schema.employee import Employee
from app.schema.department import Department
from app.schema.role import Role


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


if __name__ == "__main__":
    asyncio.run(init_db())
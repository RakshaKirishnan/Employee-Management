from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.base import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    employee_id = Column(Integer, unique=True, nullable=False)

    name = Column(String, nullable=False)

    phone = Column(String(10), nullable=False)

    department_id = Column(
        UUID(as_uuid=True),
        ForeignKey("departments.id"),
        nullable=False
    )

    role_id = Column(
        UUID(as_uuid=True),
        ForeignKey("roles.id"),
        nullable=False
    )

    address = Column(String, nullable=True)

    department = relationship("Department")
    role = relationship("Role")
    email = Column(String, unique=True)
    created_at = Column(DateTime, server_default=func.now())
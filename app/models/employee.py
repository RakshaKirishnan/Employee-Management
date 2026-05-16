from pydantic import BaseModel


class Employee(BaseModel):
    employee_id: int
    name: str
    phone: str
    department_id: str
    role_id: str
    address: str | None = None
    email: str | None = None

    class Config:
        from_attributes = True


class EmployeeUpdate(BaseModel):
    name: str | None = None
    phone: str | None = None
    department_id: str | None = None
    role_id: str | None = None
    address: str | None = None
    email: str | None = None

    class Config:
        from_attributes = True

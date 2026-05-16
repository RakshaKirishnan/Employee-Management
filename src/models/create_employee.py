from pydantic import BaseModel

class CreateEmployee(BaseModel):
    name: str
    age: int
    designation: str
    email: str
    address: str
    phone: str
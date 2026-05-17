# New Employee APIs — Implementation Plan

## APIs to Build

| # | Method | Endpoint | Service File |
|---|--------|----------|--------------|
| 1 | `GET` | `/employees/{employee_id}` | `get_employees_service.py` (extend) |
| 2 | `GET` | `/employees/phone/{phone}` | `get_employees_service.py` (extend) |
| 3 | `DELETE` | `/employees/{employee_id}` | `delete_employee_service.py` (new file) |

---

## Step 1 — Extend `get_employees_service.py`

Add two new functions below the existing `get_all_employees_service`.

**File:** `src/service/get_employees_service.py`

```python
from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.schema.create_emp_table import Employee


def get_all_employees_service(db: Session):
    try:
        return db.query(Employee).all()
    except Exception as e:
        db.rollback()
        raise e


def get_employee_by_id_service(employee_id: str, db: Session):
    try:
        employee = db.query(Employee).filter(Employee.id == employee_id).first()
        if not employee:
            raise HTTPException(status_code=404, detail="Employee not found")
        return employee
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


def get_employee_by_phone_service(phone: str, db: Session):
    try:
        employee = db.query(Employee).filter(Employee.phone == phone).first()
        if not employee:
            raise HTTPException(status_code=404, detail="Employee not found")
        return employee
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
```

---

## Step 2 — Create `delete_employee_service.py`

**File:** `src/service/delete_employee_service.py` *(new file)*

```python
from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.schema.create_emp_table import Employee


def delete_employee_by_id_service(employee_id: str, db: Session):
    try:
        employee = db.query(Employee).filter(Employee.id == employee_id).first()
        if not employee:
            raise HTTPException(status_code=404, detail="Employee not found")
        db.delete(employee)
        db.commit()
        return employee
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
```

---

## Step 3 — Add routes to `employee.py`

**File:** `src/routes/employee.py`

Add imports at the top:
```python
from src.service.get_employees_service import (
    get_all_employees_service,
    get_employee_by_id_service,
    get_employee_by_phone_service,
)
from src.service.delete_employee_service import delete_employee_by_id_service
```

Add the three new route functions:

```python
@router.get("/employees/phone/{phone}")
def get_employee_by_phone(phone: str, db: Session = Depends(get_db)):
    try:
        result = get_employee_by_phone_service(phone, db)
        return {
            "message": "Employee fetched successfully",
            "data": result
        }
    except Exception as e:
        return {
            "message": "Failed to fetch employee",
            "error": str(e)
        }


@router.get("/employees/{employee_id}")
def get_employee_by_id(employee_id: str, db: Session = Depends(get_db)):
    try:
        result = get_employee_by_id_service(employee_id, db)
        return {
            "message": "Employee fetched successfully",
            "data": result
        }
    except Exception as e:
        return {
            "message": "Failed to fetch employee",
            "error": str(e)
        }


@router.delete("/employees/{employee_id}")
def delete_employee_by_id(employee_id: str, db: Session = Depends(get_db)):
    try:
        result = delete_employee_by_id_service(employee_id, db)
        return {
            "message": "Employee deleted successfully",
            "data": result
        }
    except Exception as e:
        return {
            "message": "Failed to delete employee",
            "error": str(e)
        }
```

> **Note:** `GET /employees/phone/{phone}` is registered **before** `GET /employees/{employee_id}`.
> FastAPI matches routes top-to-bottom — if `/{employee_id}` comes first, it will swallow the `/phone/{phone}` path and return a 404.

---

## Edge Cases Covered

| Scenario | Status Code | Response |
|---|---|---|
| Employee not found (by ID or phone) | `404` | `"Employee not found"` |
| DB / unexpected error | `500` | `str(e)` |
| Successful fetch | `200` | Employee object |
| Successful delete | `200` | Deleted employee object |

---

## Files Summary

| File | Action |
|---|---|
| `src/service/get_employees_service.py` | Add `get_employee_by_id_service` and `get_employee_by_phone_service` |
| `src/service/delete_employee_service.py` | Create new file with `delete_employee_by_id_service` |
| `src/routes/employee.py` | Add 3 new routes + update imports |




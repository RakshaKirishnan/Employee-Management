from fastapi import APIRouter
from app.db.db import get_db
from app.exceptions.exceptions import NotFoundError, BadRequestError
from fastapi import HTTPException, status, Depends
from app.models.employee import Employee, EmployeeUpdate
from app.models.response import APIResponse
from app.service.employee import EmployeeService



router = APIRouter(prefix="/api/v1", tags=["Employees"])

@router.post("/employees/")
async def create_employee(employee: Employee, db=Depends(get_db)):
    try:
        result = await EmployeeService.create_employee(employee, db)

        return {
            "success": True,
            "message": "Employee created",
            "data": result
        }

    except NotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )

    except BadRequestError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
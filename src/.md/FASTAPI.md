# FastAPI-overview

## what is query param and what is path param

## query param

Query parameters are optional parameters that are appended to the URL after a question mark (?). They are used to filter or sort the data that is returned by the server. For example, if you want to get all the employees with the name "John", you can use the query parameter "name". The URL would look like this: http://localhost:8000/employees?name=John

### code example

@router.post("/employees/pagination")
def get_employees_with_pagination(
    name: Optional[str] = None,
    designation: Optional[str] = None,
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db)
):


All this input arguments will be treated as query params


## path param

Path parameters are mandatory parameters that are appended to the URL after a slash (/). They are used to identify a specific resource. For example, if you want to get the employee with the ID "1", you can use the path parameter "employee_id". The URL would look like this: http://localhost:8000/employees/1

### code example

@router.get("/employees/{employee_id}") ---> {employee_id} is a path param
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

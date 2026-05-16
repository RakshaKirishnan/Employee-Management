from fastapi import FastAPI
import uvicorn

from app.api.employee import router as employee_router
# from app.routes.department import router as department_router
# from app.routes.role import router as role_router

app = FastAPI(title="Employee Management API")

app.include_router(employee_router)
# app.include_router(department_router, prefix="/departments", tags=["Departments"])
# app.include_router(role_router, prefix="/roles", tags=["Roles"])


@app.get("/")
async def root():
    return {"message": "API is running"}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
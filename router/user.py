from fastapi import APIRouter, Query, Depends
from fastapi.responses import JSONResponse
from auth.oauth2 import get_authenticated_user
from schemas import Employee, Pagination
from db import db_user


router = APIRouter(
    prefix='/user',
    tags=['user']
)


@router.post('/')
async def create_employee(request: Employee, admin: dict = Depends(get_authenticated_user)):
    """
    rest post method to create employee 
    """
    try:
        output = db_user.create_employee(request)
        return output
    except Exception as exp:
        return JSONResponse(
            status_code=400,
            content=str(exp)
        )


@router.get('/list')
async def find_all_employee(request: Pagination = Depends(), 
                            admin: dict = Depends(get_authenticated_user)):
    """
    rest get method to list all employee
    """
    res = db_user.find_all_employee(request.skip, request.limit, False)
    return res


@router.get('/')
async def find_employee(national_code: str = Query(default=..., max_length=10, min_length=10), 
                        admin: dict = Depends(get_authenticated_user)):
    """
    rest get method to find employee
    """
    res = db_user.find_employee(national_code)
    if res:
        return res
    return JSONResponse(
        status_code=404,
        content={"detail":"Employee not found."}
    )


@router.put('/{national_code}/update')
async def modify_employee(request: Employee, 
                          national_code: str = Query(default=..., max_length=10, min_length=10),
                          admin: dict = Depends(get_authenticated_user)):
    """
    rest put method to update employee
    """
    res = db_user.modify_employee(national_code, request)
    if res:
        return db_user.find_employee(national_code)
    return JSONResponse(
        status_code=400,
        content={"detail":"Failed to update employee."}
    )


@router.delete('/delete/{national_code}')
async def remove_employee(national_code: str = Query(default=..., max_length=10, min_length=10),
                          admin: dict = Depends(get_authenticated_user)):
    """
    rest delete method to update employee is_deleted flag
    """
    res = db_user.remove_employee(national_code)
    if res:
        return JSONResponse(
            status_code=200,
            content={"detail":"seccussful delete employee."}
        )
    return JSONResponse(
        status_code=400,
        content={"detail":"Failed to delete employee."}
    )


@router.get('/arrival_departure')
async def employees_arrival_departure(request: Pagination = Depends(), 
                            admin: dict = Depends(get_authenticated_user)):
    """
    rest get method to list all employee with their arrival departure
    """
    res = db_user.find_all_arrival_departure(request.skip, request.limit, False)
    return res

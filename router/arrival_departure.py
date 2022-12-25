from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from db import db_arrival_departure


router = APIRouter(
    prefix='/arrival_departure',
    tags=['arrival_departure']
)


@router.put('/{national_code}/arrived')
async def employee_arrived(national_code: str = Query(default=..., max_length=10, min_length=10)):
    """
    rest put method to change employee arrived
    """
    res = db_arrival_departure.employee_arrived(national_code)
    if res:
        return JSONResponse(
            status_code=200,
            content={"detail": "done."}
        )
    return JSONResponse(
        status_code=400,
        content={"detail": "Failed to update employee arrival departure."}
    )


@router.put('/{national_code}/departured')
async def employee_departured(national_code: str = Query(default=..., max_length=10, min_length=10)):
    """
    rest put method to change employee departured
    """
    res = db_arrival_departure.employee_departured(national_code)
    if res:
        return JSONResponse(
            status_code=200,
            content={"detail": "done."}
        )
    return JSONResponse(
        status_code=400,
        content={"detail": "Failed to update employee departured departure."}
    )
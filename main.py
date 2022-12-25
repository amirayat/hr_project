import uvicorn
from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from exception import UnicornException, ValidationError
import json

from auth import authentication
from router import user, arrival_departure

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=['*']
)


app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(arrival_departure.router)


@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    """
    handling unicorn exception
    :param request: required
    :param exc: UnicornException class
    :return: None
    """
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "status": exc.status_code,
            "data": exc.data,
        },
    )


@app.exception_handler(ValidationError)
async def validate_exception_handler(request: Request, exc: ValidationError):
    """
    handling unicorn exception
    :param request: required
    :param exc: UnicornException class
    :return: None
    """
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "status": exc.status_code,
            "data": exc.content,
        },
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """
    handling validation exception
    :param request: required
    :param exc: required
    :return: None
    """
    return JSONResponse(
        status_code=400,
        content=jsonable_encoder(
            {
                "statusCode": 400,
                'validationMsg': {
                    'entity': str(request.url).replace(str(request.base_url), ''),
                    'errors': [
                        {
                            'field': obj['loc'][1],
                            'msg': [f'{k} : {v}' for k, v in obj['ctx'].items()].pop() if obj.get('ctx') else None
                        } for obj in json.loads(exc.json())
                    ]
                },
                "msg": 'پارامتر ورودی مناسب نمیباشد',
            }
        ),
    )


def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()

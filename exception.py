from pydantic import BaseModel


class UnicornException(Exception):
    """
    Unicorn Exception
    """

    def __init__(self, data: str):
        self.status_code = 500
        self.data = data


class ValidationError(Exception):
    """
    Validation Exception
    """

    def __init__(self, entity: str, errors: list):
        self.status_code = 400
        self.content = {
            'statusCode': 400,
            'validationMsg': {
                'entity': entity,
                "errors": errors,
            },
            'msg': 'پارامترهای ورودی صحیح نمیباشد'
        }


class NotFoundException:
    """
    not found
    """
    status_code = 404
    content = {'msg': 'آبجکت مورد نظر یافت نشد',
               'statusCode': 404}


class NotAcceptableException:
    """
    not acceptable
    """

    def __init__(self, entity, errors: list):
        self.status_code = 400
        self.content = {
            'statusCode': 400,
            'validationMsg': {
                'entity': entity,
                "errors": errors,
            },
            'msg': "پارامترهای ورودی قابل قبول نمیباشد"
        }


class Message404(BaseModel):
    """
    Error 404 Not Found
    """
    statusCode = 404
    msg = "آبجکت مورد نظر یافت نشد"


class Message400(BaseModel):
    """
    HTTP status code that describes an error caused by an invalid request
    """
    statusCode = 400
    validationMsg = {
        'entity': "entity",
        "errors": [{'field': 'field1', 'msg': 'message1'}, {'field': 'field2', 'msg': 'message2'}],
    }
    msg = "پارامترهای ورودی صحیح نمیباشد"


class Message422(BaseModel):
    """
    example
    """
    statusCode = 422
    msg = "message"


RESPONSE = {
    400: {"model": Message400},
    404: {"model": Message404},
    422: {"model": Message422},
}

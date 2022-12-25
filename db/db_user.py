from db import employee_collection
from schemas import Employee
from pymongo.errors import PyMongoError


def create_employee(employee: Employee):
    """
    to create employee data object
    """
    employee = dict(employee)
    employee["is_deleted"] = False
    res = employee_collection.insert_one(employee)
    if res.acknowledged:
        employee.pop("_id")
        return employee
    raise PyMongoError()


def find_employee(national_code: str):
    """
    to find employee data object
    """
    res = employee_collection.find_one(
        {'national_code': national_code, 'is_deleted': False}, {'_id': 0})
    return res


def find_all_employee(skip: int, limit: int, all: bool):
    """
    to find all employee data objects
    """
    res = employee_collection.aggregate([
        {
            '$match': {
                'is_deleted': False
            }
        }, {
            '$limit': limit
        }, {
            '$skip': skip
        }, {
            '$project': {
                '_id': 0
            }
        }
    ])
    if all:
        res = employee_collection.aggregate([
            {
                '$match': {
                    'is_deleted': False
                }
            }, {
                '$project': {
                    '_id': 0
                }
            }
        ])
    return list(res)


def modify_employee(national_code: str, data: Employee):
    """
    to update employee data object
    """
    data = dict(data)
    data.pop("national_code")
    filter = {'national_code': national_code, 'is_deleted': False}
    newvalues = {"$set": data}
    res = employee_collection.update_one(filter, newvalues)
    if res.acknowledged and res.modified_count:
        return res.acknowledged


def remove_employee(national_code: str):
    """
    to update employee is_deleted flag
    """
    filter = {'national_code': national_code, 'is_deleted': False}
    newvalues = {"$set": {'is_deleted': True}}
    res = employee_collection.update_one(filter, newvalues)
    if res.acknowledged and res.modified_count:
        return res.acknowledged


def find_all_arrival_departure(skip: int, limit: int, all: bool):
    """
    to find all employees arrival departure
    """
    res = employee_collection.aggregate([
        {
            '$match': {
                'is_deleted': False
            }
        }, {
            '$lookup': {
                'from': 'arrival_departure',
                'localField': 'national_code',
                'foreignField': 'national_code',
                'as': 'arrival_departure',
                'pipeline': [
                    {
                        '$project': {
                            '_id': 0
                        }
                    }
                ]
            }
        }, {
            '$skip': skip
        }, {
            '$limit': limit
        }, {
            '$project': {
                '_id': 0
            }
        }
    ])
    if all:
        res = employee_collection.aggregate([
            {
                '$match': {
                    'is_deleted': False
                }
            }, {
                '$lookup': {
                    'from': 'arrival_departure',
                    'localField': 'national_code',
                    'foreignField': 'national_code',
                    'as': 'arrival_departure',
                    'pipeline': [
                        {
                            '$project': {
                                '_id': 0
                            }
                        }
                    ]
                }
            }, {
                '$project': {
                    '_id': 0
                }
            }
        ])
    return list(res)

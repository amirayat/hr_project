from db import arrival_departure_collection, db
from db.db_user import find_all_employee
from datetime import datetime


def create_emloyees_arrival_departure():
    """
    create arrival departure document of date for each employee
    """
    employees = find_all_employee(skip=0, limit=10, all=True)
    national_code_list = [employee['national_code'] for employee in employees]
    arrival_departure = [
        {
            "national_code": nc,
            "arrived": False,
            "arrival_time": None,
            "departured": False,
            "departure_time": None,
            "date": datetime.today().replace(hour=0, minute=0, second=0, microsecond=0),
            "presence_duration": 0
        } for nc in national_code_list]

    res = arrival_departure_collection.insert_many(arrival_departure)
    if res.acknowledged:
        return True
    return False


def employee_arrived(national_code: str):
    """
    to update employee arrival departure data to arrived
    """
    filter = {'national_code': national_code}
    newvalues = {"$set": {"arrived": True,
                          "arrival_time": datetime.now()}}
    res = arrival_departure_collection.update_one(filter, newvalues)
    if res.acknowledged and res.modified_count:
        return res.acknowledged


def employee_departured(national_code: str):
    """
    to update employee arrival departure data to departured
    """
    filter = {'national_code': national_code}
    newvalues = {"$set": {"departured": True,
                          "departure_time": datetime.now()}}
    res = arrival_departure_collection.update_one(filter, newvalues)
    if res.acknowledged and res.modified_count:
        return res.acknowledged


def presence_duration():
    """
    update employees presence duration till function call
    """
    query = {
        "update": "arrival_departure",
        "updates": [
            {
                "q": {'date': datetime.today().replace(
                    hour=0, minute=0, second=0, microsecond=0),
                    'arrived': True,
                    'departured': False},
                "u": [
                    {
                        "$set": {
                            "presence_duration": {
                                "$subtract": [
                                    "$$NOW", "$arrival_time"
                                ]
                            }
                        }
                    }
                ],
                "multi": True
            }
        ],
        "ordered": False,
        "writeConcern": {"w": "majority", "wtimeout": 5000}
    }
    res = db.command(query)
    if res['ok'] == 1.0 and res['nModified']>0:
        return True

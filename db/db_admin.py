from db import admin_collection
from schemas import Admin
from pymongo.errors import PyMongoError
from db.hash import Hash


def create_admin(data: Admin):
    """
    method to create employee data object
    """
    data = dict(data)
    if admin_collection.find_one({"username": data['username']}):
        return False
    data['password'] = Hash.bcrypt(data.get('password'))
    res = admin_collection.insert_one(data)
    if res.acknowledged:
        return res.acknowledged
    raise PyMongoError()


def find_admin(username: str):
    """
    method to find employee data object
    """
    res = admin_collection.find_one({'username': username})
    return res


def modify_admin(data: Admin):
    """
    method to update employee data object
    """
    filter = {"username": data.username}
    data.password = Hash.bcrypt(data.password)
    newvalues = {"$set": dict(data)}
    res = admin_collection.update_one(filter, newvalues)
    if res.acknowledged and res.modified_count:
        return res.acknowledged
    return False

from pymongo import MongoClient
from config.config import Config


URI = Config.get("mongo", "URI")
DB = Config.get("mongo", "db")
ADMIN_COLLECION = Config.get("mongo", "admin_collection")
EMPLOYEE_COLLECION = Config.get("mongo", "employee_collection")
ARRIVAL_DEPARTURE_COLLECION = Config.get(
    "mongo", "arrival_departure_collection")

CLIENT = MongoClient(URI)
db = CLIENT[DB]
admin_collection = db[ADMIN_COLLECION]
employee_collection = db[EMPLOYEE_COLLECION]
arrival_departure_collection = db[ARRIVAL_DEPARTURE_COLLECION]

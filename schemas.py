from datetime import datetime
from pydantic import BaseModel


class Admin(BaseModel):
    """
    admin schema
    """
    username: str
    password: str


class Employee(BaseModel):
    """
    employee schema
    """
    firstname: str
    lastname: str
    email: str
    national_code: str 
    phone_number: str


class Pagination(BaseModel):
    """
    pagination schema
    """
    limit: int
    skip: int


class ArrivalDeparture(BaseModel):
    """
    emloyee arrival departure schema 
    """
    national_code: str 
    arrived: bool
    arrival_time: datetime = None
    departured: bool
    departure_time: datetime = None
    date: datetime
    presence_duration: float 

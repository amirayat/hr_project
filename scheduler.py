import time
import schedule
from db.db_arrival_departure import create_emloyees_arrival_departure


schedule.every().day.at("05:00").do(create_emloyees_arrival_departure)


while True:
    schedule.run_pending()
    time.sleep(1)
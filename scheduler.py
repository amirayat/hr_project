import time
import schedule
from db.db_arrival_departure import create_emloyees_arrival_departure, presence_duration


schedule.every().day.at("05:00").do(create_emloyees_arrival_departure)
schedule.every(5).minutes.do(presence_duration)


while True:
    schedule.run_pending()
    time.sleep(1)
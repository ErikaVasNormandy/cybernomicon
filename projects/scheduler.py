import schedule
import time

print("Hello Scheduler")
def job():
    print("I'm working...")

schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("17:36").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)

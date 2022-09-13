import schedule
import time

print("Hello Scheduler")
def job():
    print("I'm working...")
#I think this just does local time for me..... Pacific time so whatever
schedule.every(1).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("17:36").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)

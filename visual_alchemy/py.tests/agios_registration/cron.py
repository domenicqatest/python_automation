### Place cron.py in the same folder as the pytests. ###

import schedule
import time
import os
import datetime

def job():
    print('\n')  # adds line break
    print("The date / time is:")
    print datetime.datetime.now()

    # pytests (or test entire folder)
    os.system("pytest agios_registration1.py -s")
    os.system("pytest agios_registration2.py -s")

#schedule.every(10).seconds.do(job)
#schedule.every(2).minutes.do(job)
#schedule.every(2).hours.do(job)
#schedule.every().day.at("10:12").do(job)
#schedule.every().monday.do(job)
schedule.every().wednesday.at("10:05").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
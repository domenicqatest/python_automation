### Place cron2.py in the same folder as the pytests. ###

from crontab import CronTab
#init cron
cron   = CronTab()

#add new cron job
job = cron.new(command='/usr/bin/echo')

#job settings
job.minute.every(1)
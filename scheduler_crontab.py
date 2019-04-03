from crontab import CronTab

cron = CronTab(user='MacBook Pro')
job = cron.new(command='python script.py')
job.minute.every(10)

cron.write()

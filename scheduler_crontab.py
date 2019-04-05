from crontab import CronTab

cron = CronTab(user='MacBook Pro')
job = cron.new(command='python /Users/macbook/Desktop/projects/TestChekh/cur_conv/script2.py')
job.minute.every(60*24)

cron.write()

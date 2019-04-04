from crontab import CronTab

cron = CronTab(user='MacBook Pro')
job = cron.new(command='python /Users/macbook/Desktop/projects/TestChekh/cur_conv/script2.py')
job.minute.every(10)

cron.write()

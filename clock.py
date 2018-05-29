from apscheduler.schedulers.blocking import BlockingScheduler
from django.core import management

sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=3)
def timed_job():
    print('This job is run every three minutes.')


@sched.scheduled_job('cron', day_of_week='mon-fri', hour=22)
def scheduled_job():
    print('Run generate_call_list')
    management.call_command('generate_call_list')
    print('Run reset_should_be_contacted')
    management.call_command('reset_should_be_contacted')


sched.start()

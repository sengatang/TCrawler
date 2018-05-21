# -*- coding: utf-8 -*-
from pymongo import MongoClient
from datetime import datetime
import time

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
from apscheduler.jobstores.mongodb import MongoDBJobStore  # 选择MongoDB因为要保存作业
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from django_apscheduler.jobstores import DjangoJobStore
# http://apscheduler.readthedocs.io/en/latest/modules/triggers/cron.html

# SHEDULER settings 
HOST = '127.0.0.1'
PORT = 27017
client = MongoClient(HOST, PORT)

jobstores = {
    'mongo': MongoDBJobStore(collection='job', database='test', client=client),
    'default': MemoryJobStore()
}

executors = {
    'default': ThreadPoolExecutor(20),
    'processpool': ProcessPoolExecutor(5)
}

job_defaults = {
    'coalesce': False,
    'max_instances': 3
}

# setting ends 

# 任务监听
# https://segmentfault.com/a/1190000007739974
def my_listener(event):
    if event.exception:
        print('The job crashed :(')
    else:
        print('The job worked :)')




# def add_corn(start_date, end_date, weeklist, spider_func, hour, minute):
#     weekdays = weeklist.split(',')
#     for weekday in weekdays:
#         @sched.scheduled_job(spider_func, 'corn', day_of_week=weekday, hour=hour, minute=minute)



def method(job_id):
    print('Job ' + str(job_id) + ' begin! The time is: %s' % datetime.now())
    time.sleep(2)
    print('Job ' + str(job_id) + ' end! The time is: %s' % datetime.now())


class JobManager(object):
    def __init__(self):
        self.scheduler = BackgroundScheduler(executors=executors, job_defaults=job_defaults)
        self.jobs = {}
        self.scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
        self.scheduler.add_jobstore(DjangoJobStore(), 'djangojobstore')
        self.scheduler.start()
        print(datetime.now())

    def add_job(self, jobid):
        def job():
            print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        trigger = dict(hour=17, minute=52)
        Trigger = CronTrigger(**trigger)
        job = self.scheduler.add_job(method, Trigger, id=jobid, args=[jobid])
        print("add job %s successful!" % jobid + "; next_run_time: " + str(job.next_run_time))

if __name__ == "__main__":
    a = JobManager()
    for i in range(1, 3):
        a.add_job('%d' % i)

    try:
        while True:
            time.sleep(1)

    except (KeyboardInterrupt, SystemExit):
        a.scheduler.shutdown()
    # scheduler = BackgroundScheduler(executors=executors, job_defaults=job_defaults, timezone='Asia/Shanghai')
    # scheduler.shutdown()
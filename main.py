import schedule
import time
import datetime
import requests
from data.config import BOT_TOKEN, CHAT_ID
from utils.db_api import DBS
import os 
import asyncio

# data = DBS.getSetting(DBS)
# print(data)


def job():
    print(111)
    schedule.clear()
    execute_cron_jobs()
    # url = f"https://api.telegram.org/bot{BOT_TOKEN}/copyMessage?chat_id={data[0][1]}&from_chat_id={data[0][3]}&message_id={data[0][4]}"
    # requests.get(url)

def job_2():
    print(222)
    schedule.clear()
    execute_cron_jobs()
    # url = f"https://api.telegram.org/bot{BOT_TOKEN}/copyMessage?chat_id={data[0][1]}&from_chat_id={data[0][3]}&message_id={data[0][4]}"
    # requests.get(url)

def job_3():
    print(333)
    schedule.clear()
    execute_cron_jobs()
    # url = f"https://api.telegram.org/bot{BOT_TOKEN}/copyMessage?chat_id={data[0][1]}&from_chat_id={data[0][3]}&message_id={data[0][4]}"
    # requests.get(url)

def execute_cron_jobs():
    query = "SELECT * FROM Send WHERE categoryId=1 ORDER BY RANDOM() LIMIT 1;"
    f_data = DBS.post_sql_query(query)[0]
    print(f_data[3])
    schedule.every(f_data[3]).seconds.do(job)

    s_query = "SELECT * FROM Send WHERE categoryId=2 ORDER BY RANDOM() LIMIT 1;"
    s_data = DBS.post_sql_query(s_query)[0]
    schedule.every(int(s_data[3])).seconds.do(job_2)

    t_query = "SELECT * FROM Send WHERE categoryId=3 ORDER BY RANDOM() LIMIT 1;"
    t_data = DBS.post_sql_query(t_query)[0]
    schedule.every(int(t_data[3])).seconds.do(job_3)
    while True:
        schedule.run_pending()
        time.sleep(1)

execute_cron_jobs()


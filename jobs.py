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
msg_1 = 1
msg_2 = 3
msg_3 = 6
msg_4 = 5

def job():
    print(111)
    schedule.clear()
    execute_cron_jobs()
    # print("sended")
    # data = DBS.getSetting(DBS)
    # await asyncio.sleep(10)
    # url = f"https://api.telegram.org/bot{BOT_TOKEN}/copyMessage?chat_id={data[0][1]}&from_chat_id={data[0][3]}&message_id={data[0][4]}"
    # requests.get(url)

def execute_cron_jobs():
    query = "SELECT * FROM Send WHERE categoryId=1 ORDER BY RANDOM() LIMIT 1;"
    f_data = DBS.post_sql_query(query)[0]
    print(f_data[3])
    schedule.every(11).seconds.do(job)

    s_query = "SELECT * FROM Send WHERE categoryId=2 ORDER BY RANDOM() LIMIT 1;"
    s_data = DBS.post_sql_query(s_query)[0]
    schedule.every(int(s_data[3])).seconds.do(job)

    t_query = "SELECT * FROM Send WHERE categoryId=3 ORDER BY RANDOM() LIMIT 1;"
    t_data = DBS.post_sql_query(t_query)[0]
    schedule.every(int(t_data[3])).seconds.do(job)

execute_cron_jobs()
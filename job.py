import schedule
import time
import datetime
import requests
from data.config import BOT_TOKEN, CHAT_ID
from utils.db_api import DBS
import os 

data = DBS.getSetting(DBS)

msg_1 = 1
msg_2 = 3
msg_3 = 6
msg_4 = 5

def job():
    print("sended")
    data = DBS.getSetting(DBS)
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/copyMessage?chat_id={data[0][1]}&from_chat_id={data[0][3]}&message_id={data[0][4]}"
    requests.get(url)
schedule.every(msg_1).seconds.do(job)


def job2():
    data = DBS.getSetting(DBS)
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/copyMessage?chat_id={data[1][1]}&from_chat_id={data[1][3]}&message_id={data[1][4]}"
    requests.get(url)
schedule.every(msg_2).seconds.do(job2)

def job3():
    data = DBS.getSetting(DBS)
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/copyMessage?chat_id={data[2][1]}&from_chat_id={data[2][3]}&message_id={data[2][4]}"
    requests.get(url)
schedule.every(msg_3).seconds.do(job3)

def job4():
    data = DBS.getSetting(DBS)
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/copyMessage?chat_id={data[3][1]}&from_chat_id={data[3][3]}&message_id={data[3][4]}"
    requests.get(url)
schedule.every(msg_4).seconds.do(job4)

while True:
    schedule.run_pending()
    time.sleep(1)
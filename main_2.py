from datetime import datetime
import pytz
import schedule
import time
import requests
from data.config import BOT_TOKEN, CHAT_ID
from utils.db_api import DBS
import asyncio

print(BOT_TOKEN)

class Job_first:
    _id = 0
    def job(self):
        print("okk")
        query = f"SELECT * FROM Send WHERE categoryId=2 AND id={self._id}"
        data = DBS.post_sql_query(query)
        print("runn")
        if data:
            print("runed")
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/copyMessage?chat_id={CHAT_ID}&from_chat_id={data[0][2]}&message_id={data[0][1]}"
            print(url)
            requests.get(url)
        self._id *= 0
        schedule.clear()
        self.execute_cron_jobs()


    def execute_cron_jobs(self):
        try:
            uz_tz = pytz.timezone('Asia/Tashkent')
            now_uz = datetime.now(uz_tz)
            
            _time = f'{str(now_uz.hour).zfill(2)}:{str(now_uz.minute).zfill(2)}'
            print(_time)
            
            query = f"SELECT *  FROM Send WHERE  interval NOTNULL AND strftime('%H:%M', interval) >= '{_time}' AND categoryId=2 ORDER BY  strftime('%H:%M', interval) ASC"
            print(query)
            data = DBS.post_sql_query(query)
            
            if len(data) == 0:
                time.sleep(5)
                self.execute_cron_jobs()
            else:
                for x in data:
                    print(x)
                    self._id += int(x[0])
                    print(x[3])
                    schedule.every().day.at(x[3]).do(self.job)

        except Exception as e: 
            print(e)
            time.sleep(1)
            self.execute_cron_jobs()
        

Job_first().execute_cron_jobs()

while True:
    schedule.run_pending()
    time.sleep(1)


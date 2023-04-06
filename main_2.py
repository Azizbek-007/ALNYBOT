import schedule
import time
import requests
from data.config import BOT_TOKEN, CHAT_ID
from utils.db_api import DBS

class Job_first:
    _id = 0
    def job(self):
        query = f"SELECT * FROM Send WHERE id={self._id}"
        data = DBS.post_sql_query(query)
        if data:
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/copyMessage?chat_id={CHAT_ID}&from_chat_id={data[0][2]}&message_id={data[0][1]}"
            requests.get(url)
            self._id *= 0
        
        schedule.clear()
        self.execute_cron_jobs()


    def execute_cron_jobs(self):
        query = "SELECT * FROM Send WHERE categoryId=2 ORDER BY RANDOM() LIMIT 1;"
        data = DBS.post_sql_query(query)
        if data:
            f_data = data[0] 
            self._id += int(f_data[0])
            print(f_data[3])
            schedule.every(f_data[3]).seconds.do(self.job)
        while True:
            schedule.run_pending()
            time.sleep(1)


Job_first().execute_cron_jobs()

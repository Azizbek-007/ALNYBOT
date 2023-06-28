from datetime import datetime
import pytz
import schedule
import time
import requests
from data.config import BOT_TOKEN, CHAT_ID
from utils.db_api import DBS

print(BOT_TOKEN)

def job():
    if DBS.GetBotStatus():
        uz_tz = pytz.timezone('Asia/Tashkent')
        now_uz = datetime.now(uz_tz)
        _time = now_uz.strftime('%H:%M')
        print(_time)

        categories = [1, 2, 3, 4]
        for category in categories:
            query = f"SELECT * FROM Send WHERE interval NOTNULL AND strftime('%H:%M', interval) = '{_time}' AND categoryId = {category} ORDER BY strftime('%H:%M', interval) ASC LIMIT 1"
            data = DBS.post_sql_query(query)
            print(data)

            if data:
                url = f"https://api.telegram.org/bot{BOT_TOKEN}/copyMessage?chat_id={CHAT_ID}&from_chat_id={data[0][2]}&message_id={data[0][1]}"
                print(url)
                requests.get(url)
                
schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)


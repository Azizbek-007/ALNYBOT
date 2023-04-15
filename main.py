from datetime import datetime
import pytz
import schedule
import time
import requests
from data.config import BOT_TOKEN, CHAT_ID
from utils.db_api import DBS

print(BOT_TOKEN)



def job():
    if DBS.GetBotStatus(DBS) == True:
        uz_tz = pytz.timezone('Asia/Tashkent')
        now_uz = datetime.now(uz_tz)
                
        _time = f'{str(now_uz.hour).zfill(2)}:{str(now_uz.minute).zfill(2)}'
        print(_time)
    
        query = f"SELECT *  FROM Send WHERE  interval NOTNULL AND strftime('%H:%M', interval) == '{_time}' AND categoryId=1 ORDER BY  strftime('%H:%M', interval) ASC LIMIT 1;"
        data = DBS.post_sql_query(query)
        print(data)

        if len(data) != 0: 
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/copyMessage?chat_id={CHAT_ID}&from_chat_id={data[0][2]}&message_id={data[0][1]}"
            print(url)
            requests.get(url)

        
        query_2 = f"SELECT *  FROM Send WHERE  interval NOTNULL AND strftime('%H:%M', interval) == '{_time}' AND categoryId=2 ORDER BY  strftime('%H:%M', interval) ASC LIMIT 1;"
        data_2 = DBS.post_sql_query(query_2)
        print(data_2)

        if len(data_2) != 0: 
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/copyMessage?chat_id={CHAT_ID}&from_chat_id={data_2[0][2]}&message_id={data_2[0][1]}"
            print(url)
            requests.get(url)

        
        query_3 = f"SELECT *  FROM Send WHERE  interval NOTNULL AND strftime('%H:%M', interval) == '{_time}' AND categoryId=3 ORDER BY  strftime('%H:%M', interval) ASC LIMIT 1;"
        data_3 = DBS.post_sql_query(query_3)
        print(data_3)
        
        if len(data_3) != 0: 
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/copyMessage?chat_id={CHAT_ID}&from_chat_id={data_3[0][2]}&message_id={data_3[0][1]}"
            print(url)
            requests.get(url)

        
        query_4 = f"SELECT *  FROM Send WHERE  interval NOTNULL AND strftime('%H:%M', interval) == '{_time}' AND categoryId=4 ORDER BY  strftime('%H:%M', interval) ASC LIMIT 1;"
        data_4 = DBS.post_sql_query(query_4)
        print(data_4)
        
        if len(data_4) != 0: 
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/copyMessage?chat_id={CHAT_ID}&from_chat_id={data_4[0][2]}&message_id={data_4[0][1]}"
            print(url)
            requests.get(url)
    



 
schedule.every(1).minutes.do(job)
    



while True:
    schedule.run_pending()
    time.sleep(1)


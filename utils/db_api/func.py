from sqlite3 import Error
import sqlite3
import schedule
import datetime
import pytz


class DBS:
    @staticmethod
    def connect_to_database():
        return sqlite3.connect("./bot.db")

    @staticmethod
    def execute_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    @staticmethod
    def post_sql_query(sql_query):
        try:
            with DBS.connect_to_database() as connection:
                result = DBS.execute_query(connection, sql_query)
            return result
        except sqlite3.Error as e:
            print("ERROR:", e)
            return None

    @staticmethod
    def create_users_table():
        query = '''
        CREATE TABLE IF NOT EXISTS USERS(           
            user_id TEXT,
            username TEXT,
            full_name TEXT)
        '''
        DBS.post_sql_query(query)

    @staticmethod
    def user_register(user_id, user_name, full_name):
        query = f"SELECT * FROM USERS WHERE user_id='{user_id}'"
        data = DBS.post_sql_query(query)
        if not data:
            insert_query = f"INSERT INTO USERS(user_id, username, full_name) VALUES ('{user_id}', '{user_name}', '{full_name}')"
            DBS.post_sql_query(insert_query)

    @staticmethod
    def add_count(user_id, chat_id):
        query = f"SELECT * FROM reckon WHERE user_id='{user_id}' AND chat_id='{chat_id}'"
        data = DBS.post_sql_query(query)
        print(data)
        if len(data) == 0:
            insert_query = f"INSERT INTO reckon(count, user_id, chat_id) VALUES (1, '{user_id}', '{chat_id}')"
            DBS.post_sql_query(insert_query)
        else:
            new_count = data[0][0] + 1
            sql = f"UPDATE reckon SET count={new_count} WHERE user_id='{user_id}' AND chat_id='{chat_id}'"
            DBS.post_sql_query(sql)

    @staticmethod
    def reckon_count(user_id, chat_id):
        query = f"SELECT * FROM reckon WHERE user_id='{user_id}' AND chat_id='{chat_id}'"
        data = DBS.post_sql_query(query)
        if not data:
            return 0
        else:
            return data[0][1]

    @staticmethod
    def GetQuantity():
        sql = "SELECT * FROM setting"
        data = DBS.post_sql_query(sql)
        if len(data) == 0 or data[0][6] == 0:
            return False
        else:
            return data[0][6]

    @staticmethod
    def SetQuantity(clock):
        sql = f"UPDATE setting SET quantity={clock}"
        DBS.post_sql_query(sql)

    @staticmethod
    def SetRefLink(link):
        sql = f"UPDATE setting SET link='{link}'"
        DBS.post_sql_query(sql)

    @staticmethod
    def CreateInterview(msgID, fromID, categoryId):
        # O'zbekiston uchun vaqt zonasi
        uz_tz = pytz.timezone('Asia/Tashkent')

        # Vaqt sanoq
        dt = datetime.datetime.now()

        # Vaqtni O'zbekiston vaqti bilan muximlash
        uz_dt = uz_tz.localize(dt)
        print(uz_dt)
        insert_query = f"INSERT INTO Send(msgId, fromId, categoryId, createdAt) VALUES ('{msgID}', '{fromID}', {categoryId}, '{uz_dt}')"
        DBS.post_sql_query(insert_query)
        data = DBS.post_sql_query("SELECT * FROM Send ORDER BY id DESC LIMIT 1;")[0][0]
        return data

    @staticmethod
    def SetInterval(interval, _id):
        print(interval)
        sql = f"UPDATE Send SET interval='{interval}' WHERE id={_id}"
        DBS.post_sql_query(sql)
        schedule.clear()
        DBS.execute_cron_jobs()

    @staticmethod
    def GetAll(_id):
        sql = f"SELECT * FROM Send WHERE categoryId={_id} AND interval NOTNULL"
        print(sql)
        data = DBS.post_sql_query(sql)
        return data

    @staticmethod
    def SetSettingData(from_chat_id, message_id, reply_markup, _id):
        sql = f"UPDATE setting SET from_chat_id='{from_chat_id}', message_id='{message_id}', reply_markup='{reply_markup}' WHERE id={_id}"
        DBS.post_sql_query(sql)

    @staticmethod
    def GetSettingData(_id):
        sql = f"SELECT * FROM setting WHERE id=1"
        data = DBS.post_sql_query(sql)
        return data

    @staticmethod
    def GetUserCount(user_id, chat_id):
        print(user_id, chat_id)
        query = f"SELECT * FROM reckon WHERE user_id='{user_id}' AND chat_id='{chat_id}'"
        data = DBS.post_sql_query(query)
        print(data)
        if len(data) == 0:
            return False
        else:
            return data[0][1]

    @staticmethod
    def getSetting():
        query = "select * from setting"
        return DBS.post_sql_query(query)

    @staticmethod
    def ok():
        print('ok')

    @staticmethod
    def execute_cron_jobs():
        query = "SELECT * FROM Send"
        data = DBS.post_sql_query(query)[0]
        print(data)
        # schedule.every(int(data[3])).seconds.do(self.ok)
        # while True:
        #     schedule.run_pending()
        #     time.sleep(1)

    @staticmethod
    def GetBotStatus():
        data = DBS.post_sql_query("SELECT status FROM setting WHERE id=1")
        if data[0][0] == 1:
            return True
        else:
            return False

    @staticmethod
    def SetStatus(status):
        sql = f"UPDATE setting SET status={status} WHERE id=1"
        DBS.post_sql_query(sql)


print(DBS.GetBotStatus())

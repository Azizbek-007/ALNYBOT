from sqlite3 import Error
import sqlite3 
import schedule
import time

class DBS:
    def post_sql_query(sql_query):
        with sqlite3.connect("./bot.db") as connection:
                cursor = connection.cursor()
                try:
                    cursor.execute(sql_query)
                except Error:
                    pass
                result = cursor.fetchall()
                return result
        
    def create_users_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS USERS(           
            user_id TEXT,
            username TEXT,
            full_name TEXT)
        '''
        self.post_sql_query(query)
    
    def user_register (self, user_id, user_name, full_name):
        query = f"SELECT * FROM users WHERE user_id='{user_id}'"
        data = self.post_sql_query(query)
        if not data:
            insert_query = f"INSERT INTO users(user_id, username, full_name) VALUES ('{user_id}', '{user_name}', '{full_name}')"
            self.post_sql_query(insert_query)

    def add_count(self, user_id, chat_id):
        query = f"SELECT * FROM reckon WHERE user_id='{user_id}' AND chat_id='{chat_id}'"
        data = self.post_sql_query(query)
        print(data)
        if len(data) == 0:
            insert_query = f"INSERT INTO reckon(count, user_id, chat_id) VALUES (1, '{user_id}', '{chat_id}')"
            self.post_sql_query(insert_query)
        else:
            new_count = data[0][1] + 1
            sql = f"UPDATE reckon SET count={new_count} WHERE user_id='{user_id}' AND chat_id='{chat_id}'"
            self.post_sql_query(sql)

    def reckon_count(self, user_id, chat_id):
        query = f"SELECT * FROM reckon WHERE user_id='{user_id}' AND chat_id='{chat_id}'"
        data = self.post_sql_query(query)
        if not data:
            return 0
        else: return data[0][1]

    def GetQuantity(self):
        sql = "SELECT * FROM setting"
        data = self.post_sql_query(sql)
        return data[0][6]      

    def SetQuantity(self, clock):
        sql = f"UPDATE setting SET quantity={clock}"
        self.post_sql_query(sql)

    def SetRefLink(self, link):
        sql = f"UPDATE setting SET link='{link}'"
        self.post_sql_query(sql)
    
    def CreateInterview(self, msgID, fromID, categoryId):
        insert_query = f"INSERT INTO Send(msgId, fromId, categoryId) VALUES ('{msgID}', '{fromID}', {categoryId})"
        self.post_sql_query(insert_query)
        data = self.post_sql_query("SELECT * FROM Send ORDER BY id DESC LIMIT 1;")[0][0]
        return data
    
    def SetInterval(self, interval, _id):
        sql = f"UPDATE Send SET interval={interval} WHERE id={_id}"
        self.post_sql_query(sql)
        schedule.clear()
        self.execute_cron_jobs(DBS)
    
    def SetSettingData(self, from_chat_id, message_id, reply_markup, _id):
        sql = f"UPDATE setting SET from_chat_id='{from_chat_id}', message_id='{message_id}', reply_markup='{reply_markup}' WHERE id={_id}"
        self.post_sql_query(sql)
    
    def GetSettingData(self, _id):
        sql = f"SELECT * FROM setting WHERE id=1"
        data = self.post_sql_query(sql)
        return data 
    
    
    def GetUserCount(self, user_id, chat_id):
        print(user_id, chat_id)
        query = f"SELECT * FROM reckon WHERE user_id='{user_id}' AND chat_id='{chat_id}'"
        data = self.post_sql_query(query)
        print(data)
        if len(data) == 0:
            return False
        else: 
            return data[0][1]
    
    def getSetting (self):
        query = "select * from setting"
        return self.post_sql_query(query)
    
    def ok():
        print('ok')

    def execute_cron_jobs(self):
        query = "SELECT * FROM Send"
        data = self.post_sql_query(query)[0]
        print(data)
        # schedule.every(int(data[3])).seconds.do(self.ok)
        # while True:
        #     schedule.run_pending()
        #     time.sleep(1)

        
import sqlite3
import os
import time


class DBUtils:
    def __init__(self):
        db_path = os.path.join(os.path.dirname(__file__), "../db/asm.db")
        if not os.path.exists(os.path.dirname(db_path)):
            os.mkdir(os.path.dirname(db_path))

        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.cu = self.conn.cursor()
        self.create_table()

    def __new__(cls, *args, **kwargs):
        if not hasattr(DBUtils, '_instance'):
            DBUtils._instance = super().__new__(cls)
        return DBUtils._instance

    def create_table(self):
        try:
            self.cu.execute('''create table email_game_tab(
            email text NOT NULL, 
            game_id text NOT NULL, 
            payment text,
            club_id text,
            UNIQUE(email, game_id, payment, club_id)
            );''')
        except Exception as e:
            pass
        try:
            self.cu.execute('''create table payment_info_tab(
            id integer primary key autoincrement, 
            transaction_id text NOT NULL,
            email text NOT NULL,
            amount real NOT NULL,
            unit text,
            transaction_date text,
            status text,
            payment text NOT NULL,
            create_time integer,
            UNIQUE (transaction_id,payment) 
            );''')
        except:
            pass
        try:
            self.cu.execute('''create table send_chips_info_tab(
            id integer primary key autoincrement, 
            transaction_id text,
            email text,
            game_id text,
            chips_amount integer,
            status text,
            message text,
            payment text,
            club_id text,
            update_time integer,
            UNIQUE (transaction_id,payment) 
            );''')
        except:
            pass
        try:
            self.cu.execute('''create table claim_back_info_tab(
            id integer primary key autoincrement, 
            game_id text,
            chips_amount integer,
            status text,
            message text,
            club_id text,
            update_time integer
            );''')
        except:
            pass
        self.conn.commit()

    def email_game_tab_update(self, email, game_id, payment):
        self.cu.execute(f"delete from email_game_tab where email='{email}' and payment='{payment}'")
        self.cu.execute(
            f"insert into email_game_tab(email, game_id, payment) values('{email}', '{game_id}', '{payment}')")
        self.conn.commit()

    def get_game_id_by_email(self, email, payment):
        cursor = self.cu.execute(f"select game_id from email_game_tab where email='{email}' and payment='{payment}'")
        for row in cursor:
            return row[0]
        return None

    def get_email_id_by_page(self, page_size, page_index, paymment):
        result = []
        offset = (page_index-1)*page_size
        cursour = self.cu.execute(f"select email, game_id from email_game_tab where payment='{paymment}' limit {page_size} offset {offset}")
        for row in cursour:
            d = {}
            d["email"] = row[0]
            d["game_id"] = row[1]
            result.append(d)
        return result

    def payment_info_tab_insert(self, **kwargs):
        sql_pre_str = '''insert into payment_info_tab(
            transaction_id, email, amount, unit, transaction_date, status, payment, create_time)'''
        transaction_id = kwargs.get("transaction_id")
        email = kwargs.get("email")
        amount = kwargs.get("amount")
        unit = kwargs.get("unit")
        transaction_date = kwargs.get("transaction_date")
        status = kwargs.get("status")
        payment = kwargs.get("payment")
        create_time = int(time.time())

        self.cu.execute(
            f"{sql_pre_str} values('{transaction_id}', '{email}', '{amount}', '{unit}', '{transaction_date}', '{status}', '{payment}', {create_time})")
        self.conn.commit()

    def send_chips_info_tab_insert(self, **kwargs):
        sql_pre_str = '''insert into send_chips_info_tab(
                    transaction_id, email, game_id, chips_amount, status, message, payment, club_id, update_time)'''
        transaction_id = kwargs.get("transaction_id")
        email = kwargs.get("email")
        game_id = kwargs.get("game_id")
        chips_amount = kwargs.get("chips_amount")
        status = kwargs.get("status")
        message = kwargs.get("message")
        payment = kwargs.get("payment")
        club_id = kwargs.get("club_id")
        update_time = int(time.time())

        print(f"{sql_pre_str} values('{transaction_id}', '{email}', '{game_id}', '{chips_amount}', '{status}', '{message}', '{payment}', '{club_id}', '{update_time}')")

        self.cu.execute(
            f"{sql_pre_str} values('{transaction_id}', '{email}', '{game_id}', '{chips_amount}', '{status}', '{message}', '{payment}', '{club_id}', {update_time})")
        self.conn.commit()

    def send_chips_info_tab_update_status(self, **kwargs):
        transaction_id = kwargs.get("transaction_id")
        game_id = kwargs.get("game_id")
        status = kwargs.get("status")
        message = kwargs.get("message")
        payment = kwargs.get("payment")
        update_time = int(time.time())

        self.cu.execute(
            f"update send_chips_info_tab set game_id='{game_id}', status='{status}', message='{message}', update_time={update_time} where transaction_id='{transaction_id}' and payment='{payment}'")
        self.conn.commit()

    def get_send_results(self, page_size, payment=None, club_id=None, id=None):
        sql = '''select p.transaction_id, p.email, p.amount, p.unit, p.transaction_date, p.payment, s.id,
         s.game_id, s.chips_amount, s.status, s.message, s.club_id 
         from payment_info_tab AS p LEFT OUTER JOIN send_chips_info_tab AS s 
         on p.transaction_id=s.transaction_id and p.payment=s.payment where p.status=\'succeed\''''
        if payment:
            sql = f"{sql} and s.payment='{payment}'"
        if club_id:
            sql = f"{sql} and s.club_id='{club_id}'"
        if id:
            sql = f"{sql} and s.id<{id}"
        sql = f"{sql} order by p.id desc limit {page_size}"
        cursor = self.cu.execute(sql)
        return self._traversal_cursor(cursor)

    def get_send_results_by_time(self, start_time, payment=None, club_id=None, end_time=None):

        sql = '''select p.transaction_id, p.email, p.amount, p.unit, p.transaction_date, p.payment, s.id,
         s.game_id, s.chips_amount, s.status, s.message, s.club_id 
         from payment_info_tab AS p LEFT OUTER JOIN send_chips_info_tab AS s 
         on p.transaction_id=s.transaction_id and p.payment=s.payment where p.create_time>='''
        sql = f"{sql}{start_time}"
        if payment:
            sql = f"{sql} and s.payment='{payment}'"
        if club_id:
            sql = f"{sql} and s.club_id='{club_id}'"
        if end_time:
            sql = f"{sql} and p.create_time<={end_time}"
        sql = f"{sql} order by p.id desc"
        cursor = self.cu.execute(sql)
        return self._traversal_cursor(cursor)

    def _traversal_cursor(self, cursor):
        result = []
        for row in cursor:
            row_info = {}
            row_info["transaction_id"] = row[0]
            row_info["email"] = row[1]
            row_info["amount"] = row[2]
            row_info["unit"] = row[3]
            row_info["transaction_date"] = row[4]
            row_info["payment"] = row[5]
            row_info["send_id"] = row[6]
            row_info["game_id"] = row[7]
            row_info["chips_amount"] = row[8]
            row_info["status"] = row[9]
            row_info["message"] = row[10]
            row_info["club_id"] = row[11]
            result.append(row_info)
        return result

    def claim_back_info_tab_insert(self, **kwargs):
        sql_pre_str = '''insert into claim_back_info_tab(
                    game_id, chips_amount, status, message, club_id, update_time)'''
        game_id = kwargs.get("game_id")
        chips_amount = kwargs.get("chips_amount")
        status = kwargs.get("status")
        message = kwargs.get("message")
        club_id = kwargs.get("club_id")
        update_time = int(time.time())

        self.cu.execute(
            f"{sql_pre_str} values('{game_id}', '{chips_amount}', '{status}', '{message}', '{club_id}', {update_time})")
        self.conn.commit()

    def claim_back_info_tab_update_status(self, **kwargs):
        id = kwargs.get("id")
        status = kwargs.get("status")
        message = kwargs.get("message")
        update_time = int(time.time())

        self.cu.execute(
            f"update claim_back_info_tab set status='{status}', message='{message}', update_time={update_time} where id={id}")
        self.conn.commit()

    def get_claim_back_results(self, page_size, club_id=None, id=None):
        sql = '''select game_id, chips_amount, status, message, club_id, update_time, id
         from claim_back_info_tab'''
        if club_id:
            sql = f"{sql}  where  club_id='{club_id}'"
        if id:
            if "where" in sql:
                sql = f"{sql} and id<{id}"
            else:
                sql = f"{sql} where id<{id}"

        sql = f"{sql} order by id desc limit {page_size}"
        cursor = self.cu.execute(sql)
        result = []
        for row in cursor:
            row_info = {}
            row_info["game_id"] = row[0]
            row_info["chips_amount"] = row[1]
            row_info["status"] = row[2]
            row_info["message"] = row[3]
            row_info["club_id"] = row[4]
            row_info["update_time"] = row[5]
            row_info["id"] = row[6]
            result.append(row_info)
        return result

db_util = DBUtils()

# p_info = {
#     "transaction_id":"1111111111",
#     "email":"guitest@163.com",
#     "amount":1.5,
#     "unit":"CAD",
#     "transaction_date":"2012",
#     "status":"succeed",
#     "payment":"neteller",
#     "game_id":"100011",
#     "chips_amount":"200"
# }
#
# p_info1 = {
#     "transaction_id":"22222",
#     "email":"guitest@163.com",
#     "amount":1.5,
#     "unit":"CAD",
#     "transaction_date":"2012",
#     "status":"succeed",
#     "payment":"neteller",
#     "game_id":"100012",
#     "chips_amount":"200"
# }
#
# s_info = {
#     "transaction_id":"1111111111",
#     "email":"guitest@163.com",
#     "amount":1.5,
#     "unit":"CAD",
#     "transaction_date":"2012",
#     "status":"fail",
#     "payment":"neteller",
#     "game_id":"100011",
#     "chips_amount":"200",
#     "club_id":"1212",
#     "message":"test"
# }
#
# s_info1 = {
#     "transaction_id":"22222",
#     "email":"guitest@163.com",
#     "amount":1.5,
#     "unit":"CAD",
#     "transaction_date":"2012",
#     "status":"fail",
#     "payment":"neteller",
#     "game_id":"100012",
#     "chips_amount":"200",
#     "club_id":"1212",
#     "message":"test"
# }
# start_time=int(time.time())
# db_util.payment_info_tab_insert(**p_info)
# db_util.send_chips_info_tab_insert(**s_info)
# db_util.payment_info_tab_insert(**p_info1)
# db_util.send_chips_info_tab_insert(**s_info1)
# print(db_util.get_send_results(5))
# print(db_util.get_send_results_by_time(start_time))
from utils.constains import NETELLER_PAYMENT
db_util.email_game_tab_update("victoryxu666@gmail.com", "100347", NETELLER_PAYMENT)
db_util.get_claim_back_results(10)
print(db_util.get_send_results(10, NETELLER_PAYMENT, "100050"))


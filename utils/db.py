import sqlite3
import os
import time


class DBUtils:
    def __init__(self):
        db_path = os.path.join(os.path.dirname(__file__), "../db/asm.db")
        self.conn = sqlite3.connect(db_path)
        self.cu = self.conn.cursor()
        self.create_table()

    def __new__(cls, *args, **kwargs):
        if not hasattr(DBUtils, '_instance'):
            DBUtils._instance = super().__new__(cls)
        return DBUtils._instance

    def create_table(self):
        try:
            self.cu.execute('''create table email_game_tab(
            email text, 
            game_id text, 
            payment text
            );''')
        except:
            pass
        try:
            self.cu.execute('''create table payment_info_tab(
            id integer primary key autoincrement, 
            transaction_id text,
            email text,
            amount real,
            unit text,
            transaction_date text,
            status text,
            payment text,
            create_time integer
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
            f"{sql_pre_str} values('{transaction_id}', '{email}', '{amount}', '{unit}', '{transaction_date}', '{status}', '{payment}', '{create_time}')")
        self.conn.commit()

    def send_chips_info_tab_insert(self, **kwargs):
        sql_pre_str = '''insert into send_chips_info_tab(
                    transaction_id, email, game_id, chips_amount, status, message, payment, update_time)'''
        transaction_id = kwargs.get("transaction_id")
        email = kwargs.get("email")
        game_id = kwargs.get("game_id")
        chips_amount = kwargs.get("chips_amount")
        status = kwargs.get("status")
        message = kwargs.get("message")
        payment = kwargs.get("payment")
        update_time = int(time.time())

        self.cu.execute(
            f"{sql_pre_str} values('{transaction_id}', '{email}', '{game_id}', '{chips_amount}', '{status}', '{message}', '{payment}', '{update_time}')")
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

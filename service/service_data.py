import queue
from utils.db import db_util

unit_list = ["usa", "cad", "eur", "gbp"]
resend_queue = queue.Queue()
last_transaction_id = None

def set_email_gameid(email, game_id):
    global email_gameid_dict
    email_gameid_dict[email] = game_id


def add_resend_info(data_info):
    global resend_queue
    resend_queue.put(data_info)

def get_resend_queue():
    return resend_queue

def get_gameid_by_email(email, payment):
    return db_util.get_game_id_by_email(email, payment)

def get_last_transaction_id():
    global last_transaction_id
    return last_transaction_id

def set_last_transaction_id(id):
    global last_transaction_id
    last_transaction_id = id

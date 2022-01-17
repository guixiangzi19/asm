import queue
from utils.excel_handler import get_bind_data

unit_list = ["usa", "cad", "eur", "gbp"]
email_gameid_dict = {}
resend_queue = queue.Queue()

def read_email_gameid(payment):
    global email_gameid_dict
    email_gameid_dict = {}
    email_gameid_list = get_bind_data(payment)
    if email_gameid_dict:
        for email_gameid in email_gameid_list:
            email_gameid_dict[email_gameid.get("email")] = email_gameid.get("gameid")

def set_email_gameid(email, game_id):
    global email_gameid_dict
    email_gameid_dict[email] = game_id


def add_resend_info(data_info):
    global resend_queue
    resend_queue.put(data_info)

def get_resend_queue():
    return resend_queue

def get_gameid_by_email(email):
    return email_gameid_dict.get(email)

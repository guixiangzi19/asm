import re, os
face_location = {"row": 1, "column": 1, "rowspan": 4, "columnspan": 4, 'sticky': 'news'}
menu_face_location = {"row": 0, "column": 0, "rowspan": 4, 'sticky': 'news'}
title_face_location = {"row": 0, "column": 1, "columnspan": 3, 'sticky': 'news'}
data_face_location = {"row": 3, "column": 0, "rowspan": 10, "columnspan": 3, 'sticky': 'news'}
payment_methods = ["neteller", "skrill", "ecopayz"]
transactions_table_header = ["transaction_id", "email", "game_id", "amount", 'unit', "chips", "date", "state"]
bind_table_header = ["email", "game_id"]


NETELLER_EMAIL_GAMEID_FILE = os.path.join(os.path.dirname(__file__), "../resource/data/neteller_email_gameid.xls")

PORK_DEFAULT_PATH = "C:\Program Files (x86)\DDL GAME LTD\Poker Hub\PokerHub.exe"
VERSION_RE = re.compile(r'\d+\.\d+\.\d+')
SPACE_RE = re.compile(r'\s+')

CHROME_DATA_PATH = os.path.join(os.path.expanduser("~"), "AppData/Local/Google/Chrome/User Data ams")
DRIVER_PATH = os.path.join(os.path.dirname(__file__), "../resource/chromeDriver/chromedriver.exe")

NETELLER_URL = "https://member.neteller.com/wallet/ng/transaction-history-v2"
LAST_TRANSACTION_ID = None


STATUS_SUCCEED = "succeed"
STATUS_FAILED = "failed"


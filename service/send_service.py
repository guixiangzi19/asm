import random, time

from threading import Thread

from service_data import *
from ui.poker_hub_ui import PokerHubUI
from ui.neteller_ui import NetellerUi
from utils.check_settings import check_settings
from utils.constains import *
from utils.db import db_util

send_loop = False

def is_send_service_run():
    return send_loop

def start(payment):

    global send_loop
    send_loop = True
    send = SendThread(payment)
    send.start()


def stop():
    global send_loop
    send_loop = False

class SendThread(Thread):
    def __init__(self, payment):
        super().__init__()
        self.payment = payment
        self.club_id = check_settings.get_setting_value("clubid")
        user_id = check_settings.get_setting_value("email")
        pwd = check_settings.get_setting_value("pwd")
        self.poker_ui = PokerHubUI(user_id, pwd, self.club_id)

    def run(self) -> None:

        self.exchange_rate={}
        for unit in unit_list:
            money = check_settings.get_setting_value("money", unit)
            chips = check_settings.get_setting_value("chips", unit)
            if money and chips:
                self.exchange_rate[unit] = float(chips)/float(money)


        payment_ui = None
        if self.payment == "neteller":
            payment_ui = NetellerUi()

        global send_loop
        while send_loop:
            try:
                from utils.constains import LAST_TRANSACTION_ID
                pay_info_queue = payment_ui.get_transaction_datas(LAST_TRANSACTION_ID)

                while not pay_info_queue.empty():
                    pay_info = pay_info_queue.get()
                    LAST_TRANSACTION_ID = pay_info.get("transaction_id")
                    db_util.payment_info_tab_insert(**pay_info)
                    if pay_info.get("status") == STATUS_FAILED:
                        continue
                    result = self._send_chips(pay_info)
                    db_util.send_chips_info_tab_insert(result)

            except:
                pass

            resend = get_resend_queue()
            while not resend.empty():
                resend_info = resend.get()
                result = self._send_chips(resend_info)
                db_util.send_chips_info_tab_update_status(result)

            time.sleep(random.randint(120, 240))


    def _send_chips(self, pay_info):
        send_record = {}
        send_record["transaction_id"] = pay_info.get("transaction_id")
        send_record["email"] = pay_info.get("email")
        pay_email = pay_info.get("email")
        game_id = get_gameid_by_email(pay_email, pay_info.get("payment"))
        send_record["game_id"] = game_id

        send_reslut = "0"
        message = "succeed"
        if game_id:
            chips_count = int(self.exchange_rate.get(pay_info.get("unit")) * pay_info.get("amount"))
            send_record["chips_amount"] = chips_count

            if chips_count > 0:
                try:
                    send_reslut = self.poker_ui.send_recovery_gold(game_id, chips_count)
                    if send_reslut == "-2":
                        message = "not find game id"
                    elif send_reslut == "-1":
                        message = "send chips failed"
                except:
                    # 记录失败
                    send_reslut = "-3"
                    message = "send chips has except"
        else:
            send_reslut = "-4"
            message = "email and game id is no binding"

        send_record["status"] = send_reslut
        send_record["message"] = message
        send_record["payment"] = pay_info.get("payment")
        send_record["club_id"] = self.club_id

        return send_record




start("neteller")
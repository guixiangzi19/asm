import random, time

from threading import Thread

from service_data import *
from ui.poker_hub_ui import PokerHubUI
from ui.neteller_ui import NetellerUi
from utils.check_settings import check_settings
from utils.constains import *

send_loop = True

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
        club_id = check_settings.get_setting_value("clubid")
        user_id = check_settings.get_setting_value("email")
        pwd = check_settings.get_setting_value("pwd")
        self.poker_ui = PokerHubUI(user_id, pwd, club_id)

    def run(self) -> None:


        read_email_gameid(self.payment)

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
                    if pay_info.get("status") == STATUS_FAILED:
                        continue
                    self._send_chips(pay_info)

            except:
                pass

            resend = get_resend_queue()
            while not resend.empty():
                resend_info = resend.get()
                self._send_chips(resend_info)


    def _send_chips(self, pay_info):
        pay_email = pay_info.get("email")
        game_id = get_gameid_by_email(pay_email)
        send_reslut = "0"
        message = "succeed"
        if game_id:
            chips_count = int(self.exchange_rate.get(pay_info.get("unit")) * pay_info.get("amount"))
            if chips_count > 0:
                try:
                    send_reslut = self.poker_ui.send_recovery_gold(game_id, chips_count)
                    if send_reslut == "-2":
                        message = "not find game id"
                    elif send_reslut == "-1":
                        message = "send chips failed"
                except:
                    # 记录失败
                    message = "send chips has except"
        else:
            message = "email and game id is no binding"


start("neteller")
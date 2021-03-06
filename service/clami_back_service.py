import random, time

from threading import Thread

from service.service_data import *
from ui.poker_hub_ui import PokerHubUI
from ui.neteller_ui import NetellerUi
from utils.check_settings import check_settings
from utils.constains import *
from utils.db import db_util

clami_back_loop = False

def is_clami_back_service_run():
    return clami_back_loop

def start(clami_back_list):
    global clami_back_loop
    if len(clami_back_list) <= 0:
        return
    clami_back_loop = True
    clami_back = ClamiBackThread(clami_back_list)
    clami_back.start()


class ClamiBackThread(Thread):
    def __init__(self, clami_back_list):
        super().__init__()
        self.clami_back_list = clami_back_list
        self.club_id = clami_back_list[0].get("clubid")
        user_id = check_settings.get_setting_value("email")
        pwd = check_settings.get_setting_value("pwd")
        self.poker_ui = PokerHubUI(user_id, pwd, self.club_id)

    def run(self) -> None:

        for clami_back_info in self.clami_back_list:
            result_info = {}
            game_id = clami_back_info.get("game_id")
            chips_count = clami_back_info.get("count")
            result_info["game_id"] = game_id
            result_info["chips_amount"] = chips_count
            result_info["club_id"] = self.club_id
            result = 0
            message = "succeed"
            try:
                claim_back_reslut = self.poker_ui.send_recovery_gold(game_id, chips_count, "counter_claim_back")
                if claim_back_reslut == "-2":
                    message = "not find game id"
                elif claim_back_reslut == "-1":
                    message = "send chips failed"
            except:
                # 记录失败
                claim_back_reslut = "-3"
                message = "send chips has except"

            result_info["status"] = claim_back_reslut
            result_info["message"] = message
            if clami_back_info.get("id"):
                result_info["id"] = clami_back_info.get("id")
                db_util.claim_back_info_tab_update_status()

            else:
                db_util.claim_back_info_tab_insert(**result_info)



# start("neteller")
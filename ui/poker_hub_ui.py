import os

from airtest.core.api import *
from airtest.core import settings as ST

from utils.constains import *
from utils.process_utils import *
from ui.win_ui import win_app, connect_app

class PokerHubUI:
    def __init__(self, user_id, pwd, club_id, poker_path=PORK_DEFAULT_PATH):
        self.poker_path = poker_path
        self.user_id = user_id
        self.pwd = pwd
        self.club_id = club_id
        self.app = win_app
        self.login_poker()
        self.switch_club_id(club_id)

    def __new__(cls, *args, **kwargs):
        if not hasattr(PokerHubUI, '_instance'):
            PokerHubUI._instance = super().__new__(cls)
        return PokerHubUI._instance

    def poker_to_top(self):
        poker_name = "PokerHub.exe"
        if not process_is_exists(poker_name):
            bak_path = os.getcwd()
            if os.path.isfile(self.poker_path):
                self.poker_path = os.path.dirname(self.poker_path)
            os.chdir(self.poker_path)
            self.app.start_app(poker_name)
            os.chdir(bak_path)
            sleep(3)
        poker_pid = get_process_pid(poker_name)
        if len(poker_pid)>0:
            connect_app(poker_pid.pop())


    def login_poker(self, retry_times=3):
        for i in range(retry_times):
            self.poker_to_top()
            if self.__exists("login_flag"):
                try:
                    self.__click_template("register_login", timeout=3)
                except:
                    pass
                try:
                    self.__click_template("login_in_now", timeout=3)
                except:
                    pass
                try:
                    self.__click_template("userid_edit", timeout=3)
                    self.__text(self.user_id)
                    self.__click_template("pwd_edit")
                    self.__text(self.pwd)
                    self.__click_template("login_btn")
                    return
                except:
                    pass
            else:
                return


        # touch

    def switch_club_id(self, club_id):
        pos = self.__exists("back_btn")
        while pos:
            touch(pos)
            pos = self.__exists("back_btn")

        self.__click_template("club_id_filter")
        self.__click_template("club_id_edit")
        self.__text(club_id)
        self.__click_template("club_id_search")
        self.__click_template("club_counter")


    def open_counter(self):
        self.poker_to_top()
        if not self.__exists("counter_flag"):
            if self.__exists("login_flag"):
                self.login_poker()

            self.switch_club_id(self.club_id)
        else:
            self.__click_template("back_btn")
        self.__click_template("club_counter")


    def send_recovery_gold(self, id, count, type="send"):
        self.open_counter()
        self.__click_template("counter_search", offset=(-100, 0), threshold=0.7)
        self.__text(id)
        if self.__exists("counter_check_box_0"):
            self.__click_template("counter_check_box_0")
        elif not self.__exists("counter_check_box_1"):
            return "-2"  #没有找到对应的游戏ID

        btn_name = "counter_send_out" if "send"==type else "counter_claim_back"
        self.__click_template(btn_name)
        self.__click_template("send_out_edit")
        self.__text(count)
        self.__click_template("send_out_confirm")

        if self.__exists("send_out_confirm"):
            self.__click_template("back_btn")
            return "-1"   #执行失败

        return "0"



    def __get_template(self, name, threshold=0.9):
        path = os.path.dirname(__file__)
        file = os.path.join(path, f"../resource/image/{name}.png")
        return Template(file, resolution=(468, 867), threshold=threshold)

    def __click_template(self, name, offset=(0, 0), threshold=0.9, timeout=20):
        t = self.__get_template(name, threshold=threshold)
        t_pos = loop_find(t, timeout=timeout)
        touch_pos = (t_pos[0] + offset[0], t_pos[1] + offset[1])
        touch(touch_pos)

    def __exists(self, name, threshold=0.9):
        return exists(self.__get_template(name, threshold))

    def __text(self, text_str, account_len=22):
        for i in range(account_len):
            keyevent("{BACKSPACE}")
        text(text_str)

if __name__ == "__main__":
    p = PokerHubUI("test@163.com", "sdfwerv24df334", club_id="100050")
    print(p.send_recovery_gold("1001591", "100"))
    print(p.send_recovery_gold("100159", "100"))
    print(p.send_recovery_gold("100149", "100", type="claim"))
    print(p.send_recovery_gold("100159", "100", type="claim"))

import os

from airtest.core.api import *
from airtest.core import settings as ST

from utils.constains import *
from utils.process_utils import *

class PokerHubUI:
    def __init__(self, user_id, pwd, club_id, poker_path=PORK_DEFAULT_PATH):
        from ui.win_ui import win_app

        self.poker_path = poker_path
        self.user_id = str(user_id)
        self.pwd = str(pwd)
        self.club_id = str(club_id)
        self.app = win_app
        self.login_poker()
        self.switch_club_id(club_id)


    def __new__(cls, *args, **kwargs):
        if not hasattr(PokerHubUI, '_instance'):
            PokerHubUI._instance = super().__new__(cls)
        return PokerHubUI._instance

    def poker_to_top(self):
        from ui.win_ui import connect_app

        poker_name = "PokerHub.exe"
        if not process_is_exists(poker_name):
            bak_path = os.getcwd()
            if os.path.isfile(self.poker_path):
                self.poker_path = os.path.dirname(self.poker_path)
            os.chdir(self.poker_path)
            self.app.start_app(poker_name)
            os.chdir(bak_path)
            sleep(3)
        p_pid = get_process_pid(poker_name)
        if len(p_pid)>0:
            connect_app(p_pid.pop())


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
        pos = self.__exists("back_btn", threshold=0.9)
        while pos:
            touch(pos)
            pos = self.__exists("back_btn", threshold=0.9)

        self.__click_template("club_id_filter")
        self.__click_template("club_id_edit", threshold=0.7)
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
            self.__click_template("back_btn", threshold=0.9)
            self.__click_template("club_counter")


    def send_recovery_gold(self, id, count, type="send"):
        self.open_counter()
        self.__click_template("counter_search", offset=(-100, 0), threshold=0.7)
        self.__text(id)
        if self.__exists("counter_check_box_0", threshold=0.7):
            self.__click_template("counter_check_box_0", threshold=0.7)
        elif not self.__exists("counter_check_box_1"):
            return "-2"  #???????????????????????????ID

        offset = (-30, 0) if "send"==type else (30, 0)
        self.__click_template("counter_flag", offset)
        self.__click_template("send_out_edit")
        self.__text(str(count))
        self.__click_template("send_out_confirm")

        # if not self.__exists("counter_flag"):
        #     self.__click_template("back_btn", threshold=0.9)
        #     return "-1"   #????????????

        if not self.__exists("counter_search", threshold=0.7):
            self.__click_template("back_btn", threshold=0.9)
            return "-1"   #????????????

        return "0"



    def __get_template(self, name, threshold=0.7):
        path = os.path.dirname(__file__)
        file = os.path.join(path, f"../resource/image/{name}.png")
        return Template(file, resolution=(444, 835), threshold=threshold)

    def __click_template(self, name, offset=(0, 0), threshold=0.7, timeout=20):
        t = self.__get_template(name, threshold=threshold)
        t_pos = loop_find(t, timeout=timeout)
        touch_pos = (t_pos[0] + offset[0], t_pos[1] + offset[1])
        touch(touch_pos)

    def __exists(self, name, threshold=0.7):
        return exists(self.__get_template(name, threshold))

    def __text(self, text_str, account_len=22):
        for i in range(account_len):
            keyevent("{BACKSPACE}")
        text(str(text_str))

if __name__ == "__main__":
    p = PokerHubUI("test@163.com", "sdfwerv24df334", club_id="100050")
    # print(p.send_recovery_gold("1001591", "100"))
    # print(p.send_recovery_gold("100159", "100"))
    print(p.send_recovery_gold("100149", "100", type="claim"))
    print(p.send_recovery_gold("100159", "100", type="claim"))

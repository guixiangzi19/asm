from tkinter import messagebox
from utils.create_widget import *
from utils.constains import *
from utils.check_settings import *
from PIL import Image, ImageTk
from utils.excel_handler import *


class SendDataFace():
    def __init__(self):
        self.send_data_face = None

    def _destroy(self):
        if self.send_data_face:
            self.send_data_face.destroy()

    def create(self, master, web_platform):
        self._destroy()
        self.master = master
        self.send_data_face = creat_data_face(self.master)
        trans_list = get_trans_data(web_platform)
        trans_len = len(trans_list)
        self.lab_list = list()
        i = 0
        email_list = list()
        for tran in trans_list:
            lab_dict = {}
            data = ""
            for k, v in tran.items():
                if k in ["email", "game_id", "chips", "date"]:
                    data += str(k) + ':' + str(v) + '    '
            lab = create_desk_bg_lab(self.send_data_face, name=data)
            lab_dict["lab"] = lab
            lab_dict["row_no"] = i
            lab_dict["email"] =tran.get("email")
            lab_dict["state"] = tran.get("state")
            # email_list.append(tran.get("email"))
            # email=tran.get("email")
            if tran.get('state', None) == 'fail':
                btn = Button(self.send_data_face, text="resend" ,command=self.to_bind_eg(lab_dict["email"]))
                print(lab_dict["email"])
                # btn.bind('<Button-1>', func=self.to_bind_eg)
                lab_dict["btn"] = btn
            self.lab_list.append(lab_dict)
            i = i+1
        j = 0
        for a in self.lab_list:
            a.get("lab").grid(row=j, column=0, columnspan=2, sticky=W + N + E + S)
            if a.get("btn",None):
                a.get("btn").grid(row=j, column=2)
            j = j + 1


            # # a="297177457@qq.com"
            # # b="10000"
            # # c="98979797"
            # # d="Dec 25 2021,3:43 PM"
            # # e=True
            # data=f"Email:{a}          $:{b}\ngame id:{c}            {d}"
            #
            # create_desk_bg_lab(self.send_data_face, name=data).grid(row=i, column=0, columnspan=2,sticky=W+N+E+S)
            # if e:
            #     Button(self.send_data_face,text="resend").grid(row=i, column=2)
            #     pass

    def to_bind_eg(self, email):
        def bind():
            self.set_email_gameid_page = create_settings_top_level(self.send_data_face,title="bind")
            self.email_label = Label(self.set_email_gameid_page, text=f'Mailbox:{email}')
            self.email_label.grid(row=1, column=1, sticky=S, pady=15)

            self.email_entry = Entry(self.set_email_gameid_page)
            self.email_entry.grid(row=1, column=2, sticky=S, pady=15)

            self.pwd_label = Label(self.set_email_gameid_page, text='game id:')
            self.pwd_label.grid(row=2, column=1, sticky=S, pady=15)

            self.pwd_entry = Entry(self.set_email_gameid_page)
            self.pwd_entry.grid(row=2, column=2, sticky=S, pady=15)

            self.confirm_btn = create_confirm_btn(self.set_email_gameid_page, commd=self._save_bind_eg)
            self.confirm_btn.grid(row=3, column=1, columnspan=2, sticky=W + E, padx=5, pady=25)
        return bind

    def _save_bind_eg(self,email,game_id):
        pass


senddataface = SendDataFace()

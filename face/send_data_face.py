from utils.create_widget import *
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
            lab_dict["email"] = tran.get("email")
            lab_dict["state"] = tran.get("state")

            if tran.get('state', None) == 'fail':
                btn = Button(self.send_data_face, text="Bind", bg='grey2', relief='flat',
                             command=self.to_bind_eg(lab_dict["email"]))
                # btn = Label(self.send_data_face, text="Bind", bg='grey1')
                # btn.bind('<Button-1>', func=self.to_bind_eg(lab_dict["email"]))
                lab_dict["btn"] = btn
            self.lab_list.append(lab_dict)
            i = i + 1
        j = 0
        for a in self.lab_list:
            a.get("lab").grid(row=j, column=0, columnspan=2, sticky=W + N + E + S)
            if a.get("btn", None):
                a.get("btn").grid(row=j, column=2)
            j = j + 1

    def to_bind_eg(self, email):
        def bind():
            self.eeeee=email
            self.set_email_gameid_page = create_settings_top_level(self.send_data_face, title="bind")
            self.email_label = Label(self.set_email_gameid_page, text=f'Email: {email}')
            self.email_label.grid(row=0, column=0, columnspan=2, sticky=S, pady=15)

            self.game_id_label = Label(self.set_email_gameid_page, text='game id:')
            self.game_id_label.grid(row=1, column=0, sticky=S, padx=5, pady=15)

            self.game_id_entry = Entry(self.set_email_gameid_page)
            self.game_id_entry.grid(row=1, column=1, sticky=S, pady=15)

            self.confirm_btn = create_confirm_btn(self.set_email_gameid_page,
                                                  commd=self._save_bind_eg)
            self.confirm_btn.grid(row=2, column=0, columnspan=2, sticky=W + E, padx=30, pady=25)

        return bind

    def _save_bind_eg(self):
        print(self.eeeee)
        print(self.game_id_entry.get())
        # 写绑定关系数据库
        self.set_email_gameid_page.destroy()

        pass


senddataface = SendDataFace()

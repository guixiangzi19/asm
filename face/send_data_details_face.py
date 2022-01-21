from utils.create_widget import *
from utils.check_settings import *
from face.send_data_face import senddataface
from tkinter.font import Font
from tkinter.ttk import Separator
from utils.excel_handler import get_trans_data

SendDataDetailsFaceTitile = "Details"


class SendDataDetailsFace():
    def __init__(self):
        self.send_data_details_face = None

    def _destroy(self):
        if self.send_data_details_face:
            self.send_data_details_face.destroy()

    def create(self, master, web_platform):
        self._destroy()
        self.master = master
        self.web_platform = web_platform
        self.send_data_details_face = create_right_face(self.master)

        self.sddf_title_face = create_title_face(self.send_data_details_face)
        self.sddf_data_face = create_face(self.send_data_details_face)

        trans_list = get_trans_data(self.web_platform)  # 拿数据

        self.titile_col(self.sddf_title_face)
        self.data_show_col(self.sddf_data_face, trans_list)

    def titile_col(self, master):
        self.master = master
        self.photo_back = open_image("image/back.png", (9, 15))
        self.back_btn = Label(self.master, image=self.photo_back, bg=grey1, padx=10)
        self.back_btn.bind('<Button-1>', func=self.go_back_sendface)
        self.back_btn.grid(row=0, column=0, sticky=W)

        Label(self.master, text=SendDataDetailsFaceTitile, anchor=W, bg=grey1,
              pady=20).grid(row=0, column=1,
                            sticky=W)

        self.next_btn = Button(self.master, text='next page', bg=grey1, height='1',
                               pady=20, padx=20, command=self.get_next_page_data).grid(row=0, column=2)

        Label(self.master, text=" ", anchor=W, bg=grey1, width='50',
              pady=20).grid(row=0, column=3,
                            sticky=W)
        sep_h = Separator(self.master, orient=HORIZONTAL, style='red.TSeparator')
        sep_h.grid(row=1, column=0, columnspan=4, sticky=W + E)

    def data_show_col(self, master, trans_list):
        self.master = master
        self.data_show_face = create_zw_face(self.master, row=1, column=0)
        row = 0
        for tran in trans_list:
            self.create_data_show_list(self.data_show_face, row=row, data=tran)
            row = row + 1

    def create_data_show_list(self, master, row, data):
        self.data_list_face = Frame(master)
        self.data_list_face.config(bg=grey1)
        self.data_list_face.grid(row=row, column=0, columnspan=3, sticky=W + N + E + S)
        self.payment_lab = Label(self.data_list_face, text=self.web_platform.upper(), anchor=W, bg=grey1)
        self.payment_lab.grid(row=0, padx=30, column=0, sticky=N + W + E + S)
        self.status_lab = Label(self.data_list_face, text=f'status:{data.get("status",None)}', anchor=W, bg=grey1)
        self.status_lab.grid(row=0, padx=30, column=1, sticky=N + W + E + S)
        self.email_lab = Label(self.data_list_face, text=f'Email:{data.get("email")}', anchor=W, bg=grey1)
        self.email_lab.grid(row=1, padx=30, column=0, sticky=N + W + E + S)
        self.photo_chips = open_image("image/chips.png", (23, 23))
        self.chips_lab = Label(self.data_list_face, image=self.photo_chips, text=data.get("chips", None),
                                bg=grey1)
        self.chips_lab.grid(row=1, column=1, sticky=N + W + E + S)
        self.game_id_lab = Label(self.data_list_face, text=f'Game id:{data.get("game_id")}', anchor=W, bg=grey1)
        self.game_id_lab.grid(row=2, padx=30, column=0, sticky=N + W + E + S)
        self.date_lab = Label(self.data_list_face, text=f'{data.get("date")}', anchor=E, bg=grey1)
        self.date_lab.grid(row=2, column=1, sticky=N + W + E + S)
        if data.get('state') == 'fail':
            self.btn_bind = Button(self.data_list_face, text="Bind", bg=grey1, relief='flat',
                                   command=self.to_bind_eg(data["email"]))
            self.btn_bind.grid(row=0, rowspan=2, padx=30, column=2, sticky=W + E)
        return [self.email_lab, self.chips_lab, self.game_id_lab, self.date_lab]

    def to_bind_eg(self, email):
        def bind():
            self.mail = email
            self.set_email_gameid_page = create_settings_top_level(self.data_list_face, title="bind")
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

    #
    def get_next_page_data(self):
        data = self.get_next_data()
        self.data_show_col(self.sddf_data_face, data)

    def get_next_data(self):
        data = get_trans_data(self.web_platform)
        return data

    def _save_bind_eg(self):
        pass

    #     email = self.mail
    #     game_id = self.game_id_entry.get()
    #     payment = "skrill"
    #     # 写绑定关系数据库
    #     self.set_email_gameid_page.destroy()
    #     db_util.email_game_tab_update(email, game_id, payment)

    def go_back_sendface(self, event):
        self._destroy()


senddatadetailsface = SendDataDetailsFace()

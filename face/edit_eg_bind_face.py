from utils.create_widget import *
from utils.check_settings import *
from face.send_data_face import senddataface
from tkinter.font import Font
from tkinter.ttk import Separator
from utils.db import db_util
from utils.excel_handler import get_bind_data

EGBindFaceTitle = "Bind User List"


class EGBindFace():
    def __init__(self):
        self.eg_bind_face = None

    def _destroy(self):
        if self.eg_bind_face:
            self.eg_bind_face.destroy()

    def create(self, master):
        self._destroy()
        self.master = master
        self.eg_bind_face = create_right_face(self.master)

        self.photo_back = open_image("image/back.png", (9, 15))
        self.back_btn = Label(self.eg_bind_face, image=self.photo_back, bg='#f0f0f0', padx=10)
        self.back_btn.bind('<Button-1>', func=self.go_back_sendface)
        self.back_btn.grid(row=0, column=0, sticky=W)

        Label(self.eg_bind_face, text=EGBindFaceTitle,anchor=W, bg=grey1, width='60', pady=20).grid(row=0, column=1, sticky=W)


        sep_h = Separator(self.eg_bind_face, orient=HORIZONTAL, style='red.TSeparator')
        sep_h.grid(row=1, column=0, columnspan=4, sticky=W + E)

        # bind_list=db_util.email_game_tab_update()

        bind_list=get_bind_data("skrill")
        print(bind_list)
        self.data_show_col(self.eg_bind_face, bind_list)

    def go_back_sendface(self, event):
        self._destroy()

    def data_show_col(self,master,bind_list):
        self.master = master
        self.data_show_face = create_zw_face(self.master,row=2,column=0)
        row = 0
        for re in bind_list:
            self.create_data_show_list(self.data_show_face, row=row, data=re)
            row = row + 1

    def create_data_show_list(self, master, row, data):
        self.data_list_face = Frame(master)
        self.data_list_face.config(bg=grey1)
        self.data_list_face.grid(row=row, column=0, columnspan=3, sticky=W + N + E + S)
        self.club_id = check_settings.get_setting_value("clubId")
        self.email =data.get("email",None)
        self.game_id = data.get("game_id", None)
        self.payment_lab = Label(self.data_list_face, text=data.get('payment',None).upper(), anchor=W, bg=grey1)
        self.payment_lab.grid(row=0, padx=30, column=0,columnspan=3, sticky=N + W + E + S)

        self.club_id_lab = Label(self.data_list_face, text=f'Club id:{self.club_id}', anchor=W, bg=grey1)
        self.club_id_lab.grid(row=1, padx=30,column=0, sticky=N + W + E + S)

        self.email_lab = Label(self.data_list_face, text=f'Email:{data.get("email")}', anchor=W, bg=grey1)
        self.email_lab.grid(row=2, padx=30, column=0, sticky=N + W + E + S)

        self.edit_btn = Button(self.data_list_face,text=f'Edit', relief='flat', anchor=W, bg=grey1,command=self.update_eg_bind)
        self.edit_btn.grid(row=2, padx=30, column=1, sticky=N + W + E + S)

        self.game_id_lab = Label(self.data_list_face, text=f'Game id:{data.get("game_id")}', anchor=W, bg=grey1)
        self.game_id_lab.grid(row=3, padx=30, column=0, sticky=N + W + E + S)

        self.del_btn = Button(self.data_list_face, text=f'Delete', relief='flat', anchor=W, bg=grey1, command=self.del_eg_bind)
        self.del_btn.grid(row=3, padx=30, column=1, sticky=N + W + E + S)

        # self.date_lab = Label(self.data_list_face, text=f'{data.get("date")}', anchor=E, bg=grey1)
        # self.date_lab.grid(row=1, column=1, sticky=N + W + E + S)
        # if data.get('state') == 'fail':
        #     self.btn_bind = Button(self.data_list_face, text="Bind", bg=grey1, relief='flat',
        #                            command=self.to_bind_eg(data["email"]))
        #     self.btn_bind.grid(row=0, rowspan=2, padx=30, column=2, sticky=W + E)
        # return [self.email_lab, self.chips_lab, self.game_id_lab, self.date_lab]


    def update_eg_bind(self):
        pass

    def del_eg_bind(self):
        pass

    def show_eg_bind_page(self, email,game_id):
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
                                                  commd=self.update_eg_bind)
            self.confirm_btn.grid(row=2, column=0, columnspan=2, sticky=W + E, padx=30, pady=25)

        return bind


egbindface = EGBindFace()

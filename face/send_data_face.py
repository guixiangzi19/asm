from utils.create_widget import *
from utils.excel_handler import *
from utils.db import db_util


class SendDataFace():
    def __init__(self):
        self.send_data_face = None

    def _destroy(self):
        if self.send_data_face:
            self.send_data_face.destroy()

    def create(self, master, web_platform):
        self._destroy()
        self.master = master
        self.send_data_face = create_data_face(self.master)
        trans_list = get_trans_data(web_platform)
        self.data_title_col(self.send_data_face, web_platform)
        self.data_show_col(self.send_data_face,trans_list)
        # trans_list = db_util.get_send_results(row_num=5)

    def data_title_col(self,master,web_platform):
        self.master = master
        self.data_title_face = create_zw_face(self.master)
        self.web_page_title = Label(self.master, text=web_platform.upper(), anchor=W, bg=grey1)
        self.web_page_title.grid(row=0, padx=30, column=0, sticky=N + W + E + S)

    def data_show_col(self,master,trans_list):
        self.master = master
        self.data_show_face = create_zw_face(self.master,row=1,column=0)
        row = 0
        for tran in trans_list:
            self.create_data_show_list(self.data_show_face, row=row, data=tran)
            row = row + 1

    def create_data_show_list(self, master, row, data):
        self.data_list_face = Frame(master)
        self.data_list_face.config(bg=grey1)
        self.data_list_face.grid(row=row, column=0, columnspan=3, sticky=W + N + E + S)
        self.email_lab = Label(self.data_list_face, text=f'Email:{data.get("email")}', anchor=W, bg=grey1)
        self.email_lab.grid(row=0, padx=30, column=0, sticky=N + W + E + S)
        self.chips_lab = Label(self.data_list_face, text=f'$:{data.get("chips")}', anchor=E, bg=grey1)
        self.chips_lab.grid(row=0, column=1, sticky=N + W + E + S)
        self.game_id_lab = Label(self.data_list_face, text=f'Game id:{data.get("game_id")}', anchor=W, bg=grey1)
        self.game_id_lab.grid(row=1, padx=30, column=0, sticky=N + W + E + S)
        self.date_lab = Label(self.data_list_face, text=f'{data.get("date")}', anchor=E, bg=grey1)
        self.date_lab.grid(row=1, column=1, sticky=N + W + E + S)

senddataface = SendDataFace()

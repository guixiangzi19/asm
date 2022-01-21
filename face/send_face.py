from utils.create_widget import *
from utils.check_settings import *
from face.send_data_face import senddataface
from tkinter.font import Font
from tkinter.ttk import Separator
from face.eg_bind_face import egbindface
from face.send_data_details_face import senddatadetailsface

auto_trans_state = False


def get_auto_trans_state():
    return auto_trans_state


SendFaceTitle = "Ensure the successful login of the payment\ntool webpage ,click to start"


class SendFace():
    def __init__(self):
        self.send_face = None

    def _destroy(self):
        if self.send_face:
            self.send_face.destroy()

    def create_nothing(self, master):
        self._destroy()
        self.master = master
        self.send_face = create_face(self.master)

    def create(self, master):
        self._destroy()
        self.master = master
        self.send_face = create_face(self.master)
        self.club_id = check_settings.get_setting_value("clubId")

        # self.send_face_title = SendFaceTitle
        self.send_face_w01 = create_face_title_label(self.send_face, name=SendFaceTitle)
        self.send_face_w01.grid(row=0, column=0, columnspan=4, sticky=W + N + E + S)

        from face.home_face import get_web_platform
        self.web_platform = get_web_platform()
        self.clubid_lab = Label(self.send_face, text=f'Club id: {self.club_id}', font='黑体', width='20',
                                       height='2',  pady=3, bg='#f0f0f0')
        self.clubid_lab.grid(row=1, column=1, sticky=W)

        self.photo_start = open_image("image/start.png", (28, 27))
        self.photo_stop = open_image("image/stop.png", (26, 26))
        self.strat_btn = Label(self.send_face, image=self.photo_start, bg='#f0f0f0')
        self.strat_btn.bind('<Button-1>', func=self.start_auto_girl)
        self.strat_btn.grid(row=1, column=2, sticky=W)

        self.details_lab = Label(self.send_face, text='Details', fg='#5F9CCC', font='黑体', width='20',
                                       height='2', padx=0, pady=3, bg='#f0f0f0')
        self.myFont = Font(family="黑体", underline=True)
        self.details_lab.config(font=self.myFont)
        self.details_lab.bind('<Button-1>', func=self.show_details_data)
        self.details_lab.grid(row=1, column=3, sticky=W)

        self.photo_show_bind = open_image("image/eg_bind01.png", (21, 21))
        a = '           '  # 占位
        self.show_eg_lab = Label(self.send_face, image=self.photo_show_bind, text=a, compound='right',bg=grey1)
        self.show_eg_lab.bind('<Button-1>', func=self.show_eg_bind)
        self.show_eg_lab.grid(row=1, column=0, sticky=W)

        sep_h = Separator(self.send_face, orient=HORIZONTAL, style='red.TSeparator')
        sep_h.grid(row=2, column=0, columnspan=4, sticky=W + E)

    def start_auto_girl(self, event):
        global auto_trans_state
        auto_trans_state = True
        print("go to start")
        self.strat_btn.config(image=self.photo_stop)
        self.strat_btn.bind('<Button-1>', func=self.stop_auto_girl)
        senddataface.create(self.send_face, self.web_platform)

    def stop_auto_girl(self, event):
        print("go to stop")
        global auto_trans_state
        auto_trans_state = False
        self.strat_btn.config(image=self.photo_start)
        self.strat_btn.bind('<Button-1>', func=self.start_auto_girl)

    def show_eg_bind(self, event):
        egbindface.create(self.master)

    def show_details_data(self, event):
        senddatadetailsface.create(self.master,self.web_platform)




sendface = SendFace()

from utils.create_widget import *
from utils.check_settings import *
from face.send_data_face import senddataface
from tkinter.font import Font

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

        self.send_face_title = SendFaceTitle
        self.send_face_w01 = create_face_title_label(self.send_face, name=self.send_face_title)
        self.send_face_w01.grid(row=0, column=0, columnspan=3, sticky=W + N + E + S)

        from face.home_face import get_web_platform
        self.web_platform = get_web_platform()
        Label(self.send_face, text=f'From {self.web_platform.upper()} Webpage', bg='#f0f0f0').grid(row=1, column=0,
                                                                                           columnspan=3,
                                                                                           sticky=W + N + E + S)

        self.send_face_lable01 = Label(self.send_face, text=f'Club id: {self.club_id}', font='黑体', width='20',
                                       height='2', padx=0, pady=3, bg='#f0f0f0')
        self.send_face_lable01.grid(row=2, column=0, sticky=W)

        self.photo_start = open_image("image/start.png", (28, 27))
        self.photo_stop = open_image("image/stop.png", (26, 26))
        self.strat_btn = Label(self.send_face, image=self.photo_start, bg='#f0f0f0')
        self.strat_btn.bind('<Button-1>', func=self.start_auto_girl)
        self.strat_btn.grid(row=2, column=1, sticky=W)

        self.send_face_lable02 = Label(self.send_face, text='Detials', fg='blue', font='黑体', width='20',
                                       height='2', padx=0, pady=3, bg='#f0f0f0')
        self.myFont = Font(family="黑体", underline=True)
        self.send_face_lable02.config(font=self.myFont)
        self.send_face_lable02.bind('<Button-1>', func=self.to_display_data)
        self.send_face_lable02.grid(row=2, column=2, sticky=W)

    def start_auto_girl(self, event):
        global auto_trans_state
        auto_trans_state = True
        print("go to start")
        self.strat_btn.config(image=self.photo_stop)
        self.strat_btn.bind('<Button-1>', func=self.stop_auto_girl)

    def stop_auto_girl(self, event):
        print("go to stop")
        global auto_trans_state
        auto_trans_state = False
        self.strat_btn.config(image=self.photo_start)
        self.strat_btn.bind('<Button-1>', func=self.start_auto_girl)

    def to_display_data(self, event):
        senddataface.create(self.send_face, self.web_platform)


sendface = SendFace()

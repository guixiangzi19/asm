from tkinter import messagebox
from utils.create_widget import *
from utils.constains import *
from face.send_face import sendface
from utils.create_widget import *
from face.home_face import homeface,get_web_platform
from face.profile_face import profileface
from face.send_face import sendface,get_auto_trans_state
from face.claim_back_face import claimbackface


app_name = "Agent Manager System"


class MenuFace():
    def __init__(self):
        self.menu_face = None

    def _destroy(self):
        if self.menu_face:
            self.menu_face.destroy()

    def create(self, master):
        self._destroy()
        self.master = master
        self.menu_face = creat_menu_face(self.master)

        # def create_base_menu(self):
        #     create_desk_title_lab(self.menu_face, name="Agent Manager System").grid(row=0, column=1, columnspan=3,
        #                                                                        sticky=W + N + E + S)
        #     create_desk_title_lab(self.menu_face, name="").grid(row=1, column=1, columnspan=3,
        #                                                    sticky=W + N + E + S)
        #     create_desk_title_lab(self.menu_face, name="").grid(row=2, column=1, columnspan=3,
        #                                                    sticky=W + N + E + S)
        #     create_desk_title_lab(self.menu_face, name="").grid(row=3, column=1, columnspan=3,
        #                                                    sticky=W + N + E + S)

        # sep_h = Separator(self.root, orient=HORIZONTAL)
        # sep_h.grid(row=0, column=1, columnspan=4, sticky=W+E)
        #
        # sep_v = Separator(self.root, orient=VERTICAL)
        # sep_v.grid(row=0, column=1, rowspan=4, sticky=N + S,padx=0)

        self.photo_home1 = open_image('image/home01.png', (28, 28))
        self.photo_home2 = open_image('image/home02.png', (28, 28))
        self.home_label = create_desk_menu_label(self.menu_face, name='     Home     ', photo=self.photo_home1)
        # self.home_label.config(image=self.photo_home2, bg='#999999')
        self.home_label.bind('<Button-1>', func=self.go_to_home)
        self.home_label.grid(row=0, column=0, padx=20, pady=26)

        self.photo_send1 = open_image('image/send01.png', (23, 26))
        self.photo_send2 = open_image('image/send02.png', (23, 26))
        self.send_label = create_desk_menu_label(self.menu_face, name='     Send     ', photo=self.photo_send1)
        self.send_label.bind('<Button-1>', func=self.go_to_send)
        self.send_label.grid(row=1, column=0, padx=20, pady=26)

        self.photo_claimback1 = open_image('image/claimback01.png', (27, 24))
        self.photo_claimback2 = open_image('image/claimback02.png', (27, 24))
        self.claim_backe_label = create_desk_menu_label(self.menu_face, name='Claim Back', photo=self.photo_claimback1)
        self.claim_backe_label.bind('<Button-1>', func=self.go_to_claim_back)
        self.claim_backe_label.grid(row=2, column=0, padx=20, pady=26)

        self.photo_profile1 = open_image('image/profile01.png', (26, 29))
        self.photo_profile2 = open_image('image/profile02.png', (26, 29))
        self.profile_label = create_desk_menu_label(self.menu_face, name='   Profile    ', photo=self.photo_profile1)
        self.profile_label.bind('<Button-1>', func=self.go_to_profile)
        self.profile_label.grid(row=3, column=0, padx=25, pady=26)

        # homeface.create(self.master)

    def go_to_home(self, event):
        if get_auto_trans_state():
            messagebox.showinfo(message="please stop the send first")
            return

        self.face_destroy()
        self.home_label.config(image=self.photo_home2, bg='#999999', fg='#FFFFFF')
        homeface.create(self.master)

    def go_to_send(self, event):
        if not get_web_platform():
            sendface.create_nothing(self.master)
            self.info_page = create_settings_top_level(sendface.send_face, "info")
            def _go_home():
                self.info_page.destroy()
                self.face_destroy()
                self.home_label.config(image=self.photo_home2, bg='#999999', fg='#FFFFFF')
                homeface.create(self.master)
            Label(self.info_page,text="please select webpage from Home first").grid(row=1, column=4, sticky=S, padx=50, pady=50)
            self.confirm_btn = create_confirm_btn(self.info_page, commd=_go_home)
            self.confirm_btn.grid(row=2, column=4, sticky=S)
            return
        self.face_destroy()
        self.send_label.config(image=self.photo_send2, bg='#999999', fg='#FFFFFF')
        sendface.create(self.master)

    def go_to_claim_back(self, event):
        if get_auto_trans_state():
            messagebox.showinfo(message="please stop the send first")
            return
        self.face_destroy()
        self.claim_backe_label.config(image=self.photo_claimback2, bg='#999999', fg='#FFFFFF')
        claimbackface.create(self.master)

    def go_to_profile(self, event):
        if get_auto_trans_state():
            messagebox.showinfo(message="please stop the send first")
            return
        self.face_destroy()
        self.profile_label.config(image=self.photo_profile2, bg='#999999', fg='#FFFFFF')
        profileface.create(self.master)

    def face_destroy(self):
        self.claim_backe_label.config(image=self.photo_claimback1, bg='#e1e1e1', fg='#5F9CCC')
        self.profile_label.config(image=self.photo_profile1, bg='#e1e1e1', fg='#5F9CCC')
        self.home_label.config(image=self.photo_home1, bg='#e1e1e1', fg='#5F9CCC')
        self.send_label.config(image=self.photo_send1, bg='#e1e1e1', fg='#5F9CCC')
        homeface._destroy()
        profileface._destroy()
        sendface._destroy()
        claimbackface._destroy()


menuface = MenuFace()

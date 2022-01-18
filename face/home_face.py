from tkinter import messagebox
from utils.create_widget import *
from face.send_face import sendface

web_platform = None


def get_web_platform():
    return web_platform


HomeFaceTitle = "Open the webpage of payment tools and log in"


class HomeFace():
    def __init__(self):
        self.home_face = None

    def _destroy(self):
        if self.home_face:
            self.home_face.destroy()

    def create(self, master):
        self._destroy()
        self.master = master
        self.home_face = create_face(self.master)
        self.web_platform = None
        self.home_face_w01 = create_face_title_label(self.home_face,
                                                     name=HomeFaceTitle)
        self.home_face_w01.grid(row=0, column=0, pady=20, sticky=W + N + E)

        self.photo_neteller = open_image('image/neteller.png', (145, 28))
        self.home_face_label01 = create_web_label(self.home_face, photo=self.photo_neteller)
        self.home_face_label01.bind('<Button-1>', func=self.go_to_neteller)
        self.home_face_label01.grid(row=1, column=0, pady=25, sticky=N + W + E)

        self.photo_skrill = open_image('image/skrill.png', (110, 38))
        self.home_face_label02 = create_web_label(self.home_face, photo=self.photo_skrill)
        self.home_face_label02.bind('<Button-1>', func=self.go_to_skrill)
        self.home_face_label02.grid(row=2, column=0, pady=25, sticky=N + W + E)

        self.photo_ecopayz = open_image('image/ecopayz.png', (171, 44))
        self.home_face_label03 = create_web_label(self.home_face, photo=self.photo_ecopayz)
        self.home_face_label03.bind('<Button-1>', func=self.go_to_ecopayz)
        self.home_face_label03.grid(row=3, column=0, pady=25, sticky=N + W + E)

    def go_to_neteller(self, event):
        webpage = "neteller"
        self.go_to_send_face(webpage)

    def go_to_skrill(self, event):
        webpage = "skrill"
        self.go_to_send_face(webpage)

    def go_to_ecopayz(self, event):
        webpage = "ecopayz"
        self.go_to_send_face(webpage)

    def go_to_send_face(self, webpage):
        global web_platform
        web_platform = webpage
        from face.menu_face import menuface
        menuface.face_destroy()
        menuface.send_lab_on()
        sendface.create(self.master)


homeface = HomeFace()

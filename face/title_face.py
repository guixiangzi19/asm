from tkinter import messagebox
from utils.create_widget import *
from utils.constains import *
from face.send_face import sendface
from utils.create_widget import *
from face.home_face import homeface
from face.profile_face import profileface
from face.send_face import sendface
from face.claim_back_face import claimbackface

app_name = "Agent Manager System"
class TitleFace():
    def __init__(self):
        self.title_face = None

    def _destroy(self):
        if self.title_face:
            self.title_face.destroy()

    def create(self, master):
        self._destroy()
        self.master = master
        self.title_face = creat_title_face(self.master)
        create_desk_title_lab(self.title_face, name="Agent Manager System").grid(row=0, column=1, columnspan=3,
                                                                           sticky=W + N + E + S)




titleface = TitleFace()

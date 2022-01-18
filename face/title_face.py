from utils.create_widget import *
from tkinter.ttk import Separator
AppTitle = "Agent Manager System                                  "


class TitleFace():
    def __init__(self):
        self.title_face = None

    def _destroy(self):
        if self.title_face:
            self.title_face.destroy()

    def create(self, master):
        self._destroy()
        self.master = master
        self.title_face = create_title_face(self.master)
        create_desk_title_lab(self.title_face, name=AppTitle).grid(row=0, column=0, columnspan=3,
                                                                   sticky=W + N + E + S)
        sep_h = Separator(self.title_face, orient=HORIZONTAL, style='red.TSeparator')
        sep_h.grid(row=1, column=0, columnspan=4, sticky=W+E)


titleface = TitleFace()

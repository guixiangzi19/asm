from tkinter import messagebox
from utils.create_widget import *
from utils.constains import *


class ClaimBackFace():
    def __init__(self):
        self.claim_back_face = None

    def _destroy(self):
        if self.claim_back_face:
            self.claim_back_face.destroy()

    def create(self, master):
        self._destroy()
        self.master = master
        self.claim_back_face = creat_face(self.master)
        # create_bg(self.claim_back_face)
        self.claim_back_face_lable01 = create_claimback_lab(self.claim_back_face, name='Club id:')
        self.claim_back_face_lable01.grid(row=1, column=1, pady=10, sticky=W + N + E + S)
        self.claim_back_face_entry01 = Entry(self.claim_back_face, bg='#ffffff', bd=0, relief=SOLID)
        self.claim_back_face_entry01.grid(row=1, column=2, pady=10, padx=5, sticky=W + N + E + S)

        self.claim_back_face_lable02 = create_claimback_lab(self.claim_back_face, name='Game id:')
        self.claim_back_face_lable02.grid(row=2, column=1, pady=10, sticky=W + N + E + S)
        self.claim_back_face_entry02 = Entry(self.claim_back_face, bg='#ffffff', bd=0, relief=SOLID)
        self.claim_back_face_entry02.grid(row=2, column=2, pady=10, padx=5, sticky=W + N + E + S)

        self.claim_back_face_lable03 = create_claimback_lab(self.claim_back_face, name='ClaimBack Amount:')
        self.claim_back_face_lable03.grid(row=3, column=1, pady=10, sticky=W + N + E + S)
        self.claim_back_face_entry03 = Entry(self.claim_back_face, bg='#ffffff', bd=0, relief=SOLID)
        self.claim_back_face_entry03.grid(row=3, column=2, pady=10, padx=5, sticky=W + N + E + S)

        self.photo_upload = open_image("image/upload.png", (15, 15))
        self.claim_back_face_upload = Label(self.claim_back_face,text='  Upload Excel',compound='left', image=self.photo_upload, bg='#f0f0f0')
        self.claim_back_face_upload.bind('<Button-1>', func=self.start_upload)
        self.claim_back_face_upload.grid(row=4, column=2, pady=10, sticky=W)

        self.claim_back_face_confirm_btn = create_confirm_btn(self.claim_back_face, commd=self.start_to_claim_back)
        self.claim_back_face_confirm_btn.grid(row=5, column=2, pady=20, padx=5, sticky=W)

        Label(self.claim_back_face,bg=grey1).grid(row=6, column=2, pady=40, padx=5, sticky=W)#占位

    def start_upload(self, event):
        pass

    def start_to_claim_back(self):
        pass


claimbackface = ClaimBackFace()

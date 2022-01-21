from tkinter import *
from utils.constains import *
from PIL import Image, ImageTk

grey1 = '#f0f0f0'
grey2 = '#e1e1e1'
spans = "                    "


def create_desk_menu_label(master, name=None, photo=None):
    lab = Label(master, text=name, image=photo, fg='#5F9CCC', font='Sylfaen 10', compound='top', relief='flat',
                bg=grey2, padx=5, pady=11)
    return lab


def create_left_face(master, bg='grey1'):
    face = Frame(master)
    face.config(bg=grey1)
    face.grid(**left_face_location)
    return face


def create_right_face(master, bg='grey1'):
    face = Frame(master)
    face.config(bg=grey1)
    face.grid(**right_face_location)
    return face


def create_face(master, bg='grey1'):
    face = Frame(master)
    face.config(bg=grey1)
    face.grid(**face_location)
    return face


def create_data_face(master, bg='green'):
    face = Frame(master)
    face.config(bg=grey1)
    face.grid(**data_face_location)
    return face


def create_zw_face(master,row=0,column=0, bg='green'):
    l='                                                                            '
    r='      '
    c='                                                    '

    face1 = Frame(master)
    face1.config(bg=grey1)
    face1.grid(row=row, column=column, columnspan=4, sticky=W + E + N + S)
    Label(face1,text=l,bg=grey1).grid(row=0, column=0)

    face2 = Frame(master)
    face2.config(bg=grey1)
    face2.grid(row=2, column=0, columnspan=4, sticky=W + E + N + S)
    Label(face2, text=r, bg=grey1).grid(row=0, column=0)

    face3 = Frame(master)
    face3.config(bg=grey1)
    face3.grid(row=1, column=0, columnspan=4, sticky=W + E + N + S)
    Label(face3, text=c, bg=grey1).grid(row=0, column=0)
    return face3


def create_menu_face(master, bg='green'):
    face = Frame(master)
    face.config(bg=grey2)
    face.grid(**menu_face_location)
    return face


def create_title_face(master, bg='green'):
    face = Frame(master)
    face.config(bg=grey1)
    face.grid(**title_face_location)
    return face


def create_desk_title_lab(master, name):
    lab = Label(master, text=name, font='Sylfaen 30 normal', width='30', height='3', bg=grey1)
    return lab


def create_desk_bg_lab(master, name):
    lab = Label(master, text=name, bg=grey1, justify='left')
    return lab


def create_bg(master):
    for i in range(10):
        create_desk_bg_lab(master, name=spans).grid(row=i, column=0, columnspan=3,
                                                    sticky=W + N + E + S)


def create_face_title_label(master, name, photo=None):
    lab = Label(master, text=name, image=photo, pady=5, fg='red', font='黑体', width='60', height='2', bg=grey1)
    return lab


def create_profile_face_label(master, name=None, photo=None):
    lab = Label(master, text=name, image=photo, font='黑体', width='40', height='2', anchor='w', bg=grey2)
    return lab


def create_profile_face_btn_label(master, name=None, photo=None):
    lab = Label(master, text='     ', image=photo,compound='left', height='2', bg=grey2)
    return lab


def create_profile_face_un_label(master):
    lab = Label(master, width='5', height='2', bg=grey1)
    return lab


def create_web_label(master, name=None, photo=None):
    lab = Label(master, text=name, image=photo, bg=grey1)
    return lab


def create_settings_lab(master, name):
    lab = Label(master, text=name, font='黑体', width='30', height='2')
    return lab


def create_claimback_lab(master, name):
    lab = Label(master, text=name, font='黑体', width='18', height='1', bg=grey1, anchor=E)
    return lab


def create_confirm_btn(master, image_file=None, commd=None):
    if image_file:
        photo = PhotoImage(file=image_file)
    else:
        photo = None
    btn = Button(master, text='Confirm', image=photo, font='黑体', width='25', height='2', command=commd)
    return btn


def create_settings_top_level(master, title):
    t1 = Toplevel(master)
    t1.geometry("300x250+220+300")
    t1.title(f"{title}")
    return t1


def open_image(filename, size=(70, 70)):
    photo = Image.open(filename).resize(size)
    photo = ImageTk.PhotoImage(photo)
    return photo

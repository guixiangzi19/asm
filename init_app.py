from utils.create_widget import *
from face.menu_face import menuface
from face.title_face import  titleface
from face.home_face import homeface
from face.claim_back_face import claimbackface
from face.profile_face import profileface

app_name = "Agent Manager System"


class BaseDesk(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.app_name = "AMS"
        self.root = master

        self.root.config(bg=grey1)
        self.root.title(self.app_name)
        self.root.geometry("660x520+50+50")
        # self.create_base_menu()
        menuface.create(self.root)
        titleface.create(self.root)

        # self.grid()
        # self.check_setting()
        profileface.create(self.root)

        # claimbackface.create(self.root)
        # InitFace(self.root)
        # self.check_setting()
    #
    # def __new__(cls, *args, **kwargs):
    #     if not hasattr(cls, '_instance'):
    #         orig = super(BaseDesk, cls)
    #         cls._instance = orig.__new__(cls, *args, **kwargs)
    #     return cls._instance


    # def create_base_menu(self):
    #     create_desk_title_lab(self.root, name="Agent Manager System").grid(row=0, column=1, columnspan=3,
    #                                                                        sticky=W + N + E + S)
    #     create_desk_title_lab(self.root, name="").grid(row=1, column=1, columnspan=3,
    #                                                                        sticky=W + N + E + S)
    #     create_desk_title_lab(self.root, name="").grid(row=2, column=1, columnspan=3,
    #                                                                        sticky=W + N + E + S)
    #     create_desk_title_lab(self.root, name="").grid(row=3, column=1, columnspan=3,
    #                                                                        sticky=W + N + E + S)
    #
    #     # sep_h = Separator(self.root, orient=HORIZONTAL)
    #     # sep_h.grid(row=0, column=1, columnspan=4, sticky=W+E)
    #     #
    #     # sep_v = Separator(self.root, orient=VERTICAL)
    #     # sep_v.grid(row=0, column=1, rowspan=4, sticky=N + S,padx=0)
    #
    #     self.photo_home1 = open_image('image/home01.jpg')
    #     self.photo_home2 = open_image('image/home02.jpg')
    #     self.home_label = create_desk_menu_label(self.root, photo=self.photo_home1)
    #     self.home_label.config(image=self.photo_home2, bg='#999999')
    #     self.home_label.bind('<Button-1>', func=self.go_to_home)
    #     self.home_label.grid(row=0, column=0, sticky=W + N + E + S)
    #
    #     self.photo_send1 = open_image('image/send01.jpg')
    #     self.photo_send2 = open_image('image/send02.jpg')
    #     self.send_label = create_desk_menu_label(self.root, photo=self.photo_send1)
    #     self.send_label.bind('<Button-1>', func=self.go_to_send)
    #     self.send_label.grid(row=1, column=0, sticky=W + N + E + S)
    #
    #     self.photo_claimback1 = open_image('image/claimback01.jpg')
    #     self.photo_claimback2 = open_image('image/claimback02.jpg')
    #     self.claim_backe_label = create_desk_menu_label(self.root, photo=self.photo_claimback1)
    #     self.claim_backe_label.bind('<Button-1>', func=self.go_to_claim_back)
    #     self.claim_backe_label.grid(row=2, column=0, sticky=W + N + E + S)
    #
    #     self.photo_profile1 = open_image('image/profile01.jpg')
    #     self.photo_profile2 = open_image('image/profile02.jpg')
    #     self.profile_label = create_desk_menu_label(self.root, photo=self.photo_profile1)
    #     self.profile_label.bind('<Button-1>', func=self.go_to_profile)
    #     self.profile_label.grid(row=3, column=0, sticky=W + N + E + S)
    #
    #     homeface.create(self.root)
    #
    #
    # def go_to_home(self, event):
    #     self.face_destroy()
    #     self.home_label.config(image=self.photo_home2, bg='#999999')
    #     homeface.create(self.root)
    #
    #
    # def go_to_send(self, event):
    #     self.face_destroy()
    #     self.send_label.config(image=self.photo_send2, bg='#999999')
    #     sendface.create(self.root)
    #
    # def go_to_claim_back(self, event):
    #     self.face_destroy()
    #     self.claim_backe_label.config(image=self.photo_claimback2, bg='#999999')
    #     claimbackface.create(self.root)
    #
    # def go_to_profile(self, event):
    #     self.face_destroy()
    #     self.profile_label.config(image=self.photo_profile2, bg='#999999')
    #     profileface.create(self.root)
    #
    # def face_destroy(self):
    #     self.claim_backe_label.config(image=self.photo_claimback1, bg='#e1e1e1')
    #     self.profile_label.config(image=self.photo_profile1, bg='#e1e1e1')
    #     self.home_label.config(image=self.photo_home1, bg='#e1e1e1')
    #     self.send_label.config(image=self.photo_send1, bg='#e1e1e1')
    #     homeface._destroy()
    #     profileface._destroy()
    #     sendface._destroy()
    #     claimbackface._destroy()


    # def check_setting(self):
    #     if True:
    #         profileface.create(self.root)



if __name__ == '__main__':
    root = Tk()
    app = BaseDesk(master=root)
    root.mainloop()

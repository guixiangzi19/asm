from utils.create_widget import *
from face.menu_face import menuface
from face.title_face import  titleface
from face.home_face import homeface
from face.claim_back_face import claimbackface
from face.profile_face import profileface
from face.desk import initdesk
AppName = "AMS"
WinInfo= "660x520+50+50"


class BaseDesk(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.root = master
        self.root.config(bg=grey1)
        self.root.title(AppName)
        self.root.geometry(WinInfo)
        # menuface.create(self.root)
        # # titleface.create(self.root)
        # menuface.profile_lab_on()
        # profileface.create(self.root)
        initdesk.create_desk(self.root)
    #
    # def __new__(cls, *args, **kwargs):
    #     if not hasattr(cls, '_instance'):
    #         orig = super(BaseDesk, cls)
    #         cls._instance = orig.__new__(cls, *args, **kwargs)
    #     return cls._instance



if __name__ == '__main__':
    root = Tk()
    app = BaseDesk(master=root)
    root.mainloop()

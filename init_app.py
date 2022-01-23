import logging

from utils.create_widget import *
from face.desk import initdesk
import ctypes
AppName = "AMS"
WinInfo= "660x520+50+50"
w=630
h=522

class BaseDesk(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.root = master
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
        ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
        w= int(660*( ScaleFactor / 100))
        h= int(520*( ScaleFactor / 100))
        self.root.tk.call('tk', 'scaling', ScaleFactor / 100)
        self.root.config(bg=grey1)
        self.root.title(AppName)
        self.root.geometry(f'{w}x{h}+50+50')
        # self.root.geometry(WinInfo)
        initdesk.create_desk(self.root)
    #
    # def __new__(cls, *args, **kwargs):
    #     if not hasattr(cls, '_instance'):
    #         orig = super(BaseDesk, cls)
    #         cls._instance = orig.__new__(cls, *args, **kwargs)
    #     return cls._instance



if __name__ == '__main__':
    root = Tk()
    # root.minsize(660, 520)
    # root.maxsize(660, 520)
    app = BaseDesk(master=root)
    root.mainloop()

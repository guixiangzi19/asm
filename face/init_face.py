from utils.create_widget import *



class InitFace():
    def __init__(self):
        self.no_face = None

    def _destroy(self):
        if self.no_face:
            self.no_face.destroy()

    def create(self, master):
        self._destroy()
        self.master = master
        self.no_face = creat_data_face(self.master)

initface=InitFace()

from utils.create_widget import *
from face.menu_face import menuface
from face.title_face import titleface
from face.profile_face import profileface


class InitDesk():
    def create_desk(self, master):
        self.master = master
        self.left_face = create_left_face(self.master)
        self.right_face = create_right_face(self.master)
        menuface.create(self.left_face, self.right_face)
        titleface.create(self.right_face)
        menuface.profile_lab_on()
        profileface.create(self.right_face)


initdesk = InitDesk()

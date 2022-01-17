from utils.create_widget import *
from utils.check_settings import check_settings

ClubId = 'Club id'
Exchange = 'Ratio of exchanged chips'
Email = 'Mailbox And Password For Pokerhub'


class ProfileFace():
    def __init__(self):
        self.profile_face = None

    def _destroy(self):
        if self.profile_face:
            self.profile_face.destroy()

    def create(self, master):
        self._destroy()
        self.master = master
        self.profile_face = creat_face(self.master)

        self.club_id = check_settings.get_setting_value("clubId")
        self.exchange_money = check_settings.get_setting_value("money", section='usa')
        self.exchange_chips = check_settings.get_setting_value("chips", section='usa')
        self.email = check_settings.get_setting_value("email")

        self.profile_face_label01 = create_profile_face_label(self.profile_face, name=f"   {ClubId}:{self.club_id}")

        self.profile_face_label01.grid(row=1, column=2, pady=5)
        self.photo_jt = open_image('image/btn_jt.jpg', (30, 30))
        self.profile_face_label11 = create_profile_face_btn_label(self.profile_face, photo=self.photo_jt)
        self.profile_face_label11.bind('<Button-1>', func=self.go_to_set_clubid)
        self.profile_face_label11.grid(row=1, column=3, pady=5, sticky=N + W + E + S)
        create_profile_face_un_label(self.profile_face).grid(row=1, column=1, pady=5, sticky=N + W + E + S)  # 占位用，无意义

        self.profile_face_label02 = create_profile_face_label(self.profile_face,
                                                              name=f"  {Exchange}:{self.exchange_money} USD = {self.exchange_chips} Chips")
        self.profile_face_label02.grid(row=2, column=2, pady=5)
        self.profile_face_label12 = create_profile_face_btn_label(self.profile_face, photo=self.photo_jt)
        self.profile_face_label12.bind('<Button-1>', func=self.go_to_set_exchange)
        self.profile_face_label12.grid(row=2, column=3, pady=5, sticky=N + W + E + S)

        self.profile_face_label03 = create_profile_face_label(self.profile_face, name=f"   {Email}:{self.email}")
        self.profile_face_label03.grid(row=3, column=2, pady=5)
        self.profile_face_label13 = create_profile_face_btn_label(self.profile_face, photo=self.photo_jt)
        self.profile_face_label13.bind('<Button-1>', func=self.go_to_set_email)
        self.profile_face_label13.grid(row=3, column=3, pady=5, sticky=N + W + E + S)

        Label(self.profile_face, bg=grey1).grid(row=4, column=2, pady=80, padx=5, sticky=W)  # 占位

    def go_to_set_clubid(self, event):
        self.set_club_id_page = create_settings_top_level(self.profile_face, ClubId)
        self.club_id_entry01 = Entry(self.set_club_id_page)
        self.club_id_entry01.grid(row=1, column=4, sticky=S, padx=50, pady=50)
        self.confirm_btn = create_confirm_btn(self.set_club_id_page, commd=self._save_club_id)
        self.confirm_btn.grid(row=2, column=4, sticky=S)

    def _save_club_id(self):
        clubId = self.club_id_entry01.get()
        check_settings.save_club_id(clubId)
        self.set_club_id_page.destroy()
        self.create(self.master)

    def go_to_set_email(self, event):
        self.set_email_page = create_settings_top_level(self.profile_face, Email)

        self.email_label = Label(self.set_email_page, text='Mailbox:')
        self.email_label.grid(row=1, column=1, sticky=S, padx=10, pady=15)

        self.email_entry = Entry(self.set_email_page)
        self.email_entry.grid(row=1, column=2, sticky=S, pady=15)

        self.pwd_label = Label(self.set_email_page, text='Password:')
        self.pwd_label.grid(row=2, column=1, sticky=S, padx=10, pady=15)

        self.pwd_entry = Entry(self.set_email_page)
        self.pwd_entry.grid(row=2, column=2, sticky=S, pady=15)

        self.confirm_btn = create_confirm_btn(self.set_email_page, commd=self._save_email)
        self.confirm_btn.grid(row=3, column=1, columnspan=2, sticky=W + E, padx=20, pady=25)

    def _save_email(self):
        email = self.email_entry.get()
        password = self.pwd_entry.get()
        check_settings.save_email(email, password)
        self.set_email_page.destroy()
        self.create(self.master)

    def go_to_set_exchange(self, event):
        self.set_exchange_page = create_settings_top_level(self.profile_face, Exchange)
        money_tuple = ('USA', 'CAD', 'EUR', 'GBP')
        self.var = StringVar(self.set_exchange_page)
        self.var.set('USA')
        self.money_entry = Entry(self.set_exchange_page, width=4)
        self.money_entry.grid(row=1, column=1, sticky=S,padx=10, pady=15)

        self.money_option_menu = OptionMenu(self.set_exchange_page, self.var, *money_tuple)
        self.money_option_menu.grid(row=1, column=2, sticky=S, pady=15)

        self.chips_entry = Entry(self.set_exchange_page, width=4)
        self.chips_entry.grid(row=1, column=3, sticky=S,padx=10, pady=15)

        self.chips_label = Label(self.set_exchange_page, text='Chips')
        self.chips_label.grid(row=1, column=4, sticky=S, pady=15)

        self.confirm_btn = create_confirm_btn(self.set_exchange_page, commd=self._save_exchange)
        self.confirm_btn.grid(row=2, column=1, columnspan=4, sticky=W + E, padx=25, pady=25)

    def _save_exchange(self):
        money_entry = self.money_entry.get()
        chips_entry = self.chips_entry.get()
        check_settings.update_config('money', money_entry, self.var.get().lower())
        check_settings.update_config('chips', chips_entry, self.var.get().lower())
        self.set_exchange_page.destroy()
        self.create(self.master)


profileface = ProfileFace()

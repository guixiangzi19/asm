import os
import configparser

class CheckSettings:
    def __init__(self):
        self.cfg = 'cfg'
        self.file_name = 'config.ini'
        self.cfg_content = "[settings]\nclubId = 1364567\nusaExchange = 5\nemail = 5\npwd = 5\nUSA = [1,1]\nCAD = [1,1]\nEUR = [1,1]\nGBP = [1,1]\n"

        self.filepath = os.path.join(os.getcwd(), self.cfg)
        self.filename = os.path.join(self.filepath, self.file_name)

        self.create_folder(self.filepath)
        self.create_file(self.filename)

        self.config = configparser.ConfigParser()
        self.config.read(self.filename, encoding='utf8')

    def create_folder(self, path):
        if os.path.exists(path):
            return
        else:
            os.makedirs(path)

    def create_file(self, filename):
        if os.path.exists(filename):
            return
        else:
            with open(filename, "w", encoding='utf8') as f:
                f.writelines(self.cfg_content)

    def get_setting_value(self, key,section="settings"):
        return self.config.get(section, key)

    def save_club_id(self, id):
        if id:
            self.update_config('clubId', id)

    def save_email(self, email, pwd):
        if email and pwd:
            self.update_config('email', email)
            self.update_config('pwd', pwd)

    def save_exchange(self,key, value):
        if value:
            self.update_config(key, value)


    def update_config(self, key, value, section="settings"):
        self.config.set(section, key, value)
        o = open(self.filename, 'w')
        self.config.write(o)
        o.close()


check_settings = CheckSettings()

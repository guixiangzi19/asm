import time

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.process_utils import get_process_pid
from utils.chromeUtile import init_chrome
from utils.constains import *

from utils.process_utils import kill_process

kill_process("chromedriver.exe")

class PaymentBase:

    def __init__(self, url):
        init_chrome()
        chrome_pids_before = get_process_pid("chrome.exe")
        self.driver = self.create_driver()
        chrome_pids_after = get_process_pid("chrome.exe")
        self.chrome_pid = (chrome_pids_after-chrome_pids_before)
        self.driver.get(url)

    def create_driver(self, headless=False):
        from utils.constains import CHROME_DATA_PATH
        chrome_options = ChromeOptions()
        chrome_options.add_argument(f"user-data-dir={CHROME_DATA_PATH}")

        if headless:
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-gpu")

        driver = Chrome(DRIVER_PATH, options=chrome_options)
        driver.maximize_window()
        return driver

    def wait_login(self, login_flag):
        while True:
            try:
                self.driver.find_element(By.CSS_SELECTOR, login_flag)
                break
            except:
                time.sleep(1)

    def scroll_ele_into_view(self, ele):
        self.driver.execute_script("arguments[0].scrollIntoView();", ele)

    def find_element_by_css(self, value):
        return self.driver.find_element(By.CSS_SELECTOR, value)

    def find_elements_by_css(self, value):
        return self.driver.find_elements(By.CSS_SELECTOR, value)

    def chrome_to_top(self):
        from ui.win_ui import connect_app
        self.chrome_pid = connect_app(self.chrome_pid)

    def wait_ele_until(self, value, timeout=30):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, value)))

    def wait_ele_until_not(self, value, timeout=30):
        try:
            WebDriverWait(self.driver, timeout).until_not(EC.visibility_of_element_located((By.CSS_SELECTOR, value)))
        except:
            pass
import time
import queue

from selenium.webdriver.common.by import By

from service.service_data import set_last_transaction_id
from utils.constains import *
from ui.payment_base_ui import PaymentBase


class NetellerUi(PaymentBase):
    def __init__(self):
        super().__init__(NETELLER_URL)

    def __new__(cls, *args, **kwargs):
        if not hasattr(NetellerUi, '_instance'):
            NetellerUi._instance = super().__new__(cls)
        return NetellerUi._instance

    def get_transaction_datas(self, last_transaction_id=None):
        self.obtained_id_list = []
        try:
            self.chrome_to_top()
            self.wait_login(".logout")
            self.driver.get(NETELLER_URL)
            self.wait_ele_until_not(".loading")
            self.switch_type()
        except:
            self.chrome_to_top()
            self.wait_login(".logout")
            self.driver.get(NETELLER_URL)
            self.switch_type()
            self.wait_ele_until_not(".loading")
            self.switch_type()
        return self.get_transaction_list(last_transaction_id)

    def switch_type(self, type="send"):
        self.wait_ele_until_not(".loading")
        transactionType_ele = self.wait_ele_until('[name="transactionType"]')
        drop_down_ele = transactionType_ele.find_element(By.CSS_SELECTOR, ".ps-select-arrow-wrapper")
        drop_down_ele.click()
        option_text_eles = self.find_elements_by_css(".ps-option-text")
        for option_text_ele in option_text_eles:
            if option_text_ele.text == "Sent":
                self.scroll_ele_into_view(option_text_ele)
                option_text_ele.click()
                break
        time.sleep(1)

    def get_transaction_list(self, last_transaction_id=None) -> queue.LifoQueue:
        '''
        获取转账的详细信息，不去除失败的
        :param last_transaction_id:
        :return:
        '''
        transcation_info_queue = queue.LifoQueue()
        loop = True
        while loop:
            self.wait_ele_until_not(".loading")
            transaction_eles = self.find_elements_by_css(".ps-list-item")
            if last_transaction_id is None:
                last_transaction_ele = transaction_eles[0]
                self.scroll_ele_into_view(last_transaction_ele)
                last_transaction_ele.click()
                set_last_transaction_id(self.get_transaction_detail_info().get("transaction_id"))
                return None
            else:
                for transaction_ele in transaction_eles:
                    self.scroll_ele_into_view(transaction_ele)
                    transaction_ele.click()
                    transcation_detail_info = self.get_transaction_detail_info()
                    if transcation_detail_info.get("transaction_id") != last_transaction_id:
                        print("-----------  ", transcation_detail_info.get("transaction_id"), last_transaction_id)
                        transcation_info_queue.put(transcation_detail_info)
                    else:
                        loop = False
                        return transcation_info_queue
                next_ele = self.find_element_by_css('[aria-label="Next"]')
                self.scroll_ele_into_view(next_ele)
                if next_ele.is_enabled():
                    next_ele.click()
                else:
                    return transcation_info_queue

        return transcation_info_queue

    def get_transaction_detail_info(self, retry_time=5) -> dict:
        def run():
            detail_info = {}
            detail_info["payment"] = NETELLER_PAYMENT

            self.wait_ele_until(".ps-side-panel-content .ps-list-item-inner-area")
            detail_info["transaction_date"] = self.find_element_by_css(".transaction-date").text

            item_eles = self.find_elements_by_css(".ps-side-panel-content .ps-list-item-inner-area")
            for item_ele in item_eles:
                # self.scroll_ele_into_view(item_ele)
                item_text = item_ele.find_element(By.CSS_SELECTOR, "ps-list-item-title").text

                if item_text == "Status":
                    status = item_ele.find_element(By.CSS_SELECTOR, ".ps-status-text").text.strip()
                    if "Processed" == status:
                        detail_info["status"] = STATUS_SUCCEED
                    else:
                        detail_info["status"] = STATUS_FAILED
                elif item_text == "Transaction ID":
                    detail_info["transaction_id"] = item_ele.find_element(By.CSS_SELECTOR,
                                                                          ".ps-list-item-suffix").text.strip()
                elif item_text == "Amount received":
                    ele_text = item_ele.find_element(By.CSS_SELECTOR, ".ps-list-item-suffix").text.strip()
                    detail_info["amount"] = float(SPACE_RE.split(ele_text)[0])
                    detail_info["unit"] = SPACE_RE.split(ele_text)[1]
                elif item_text == "Email":
                    detail_info["email"] = item_ele.find_element(By.CSS_SELECTOR, ".ps-list-item-suffix").text.strip()
            return detail_info

        for i in range(retry_time):
            try:
                detail_info = run()
                transaction_id = detail_info.get("transaction_id")
                if transaction_id in self.obtained_id_list:
                    continue
                self.obtained_id_list.append(transaction_id)
                return detail_info
            except:
                pass
            time.sleep(0.5)

        raise Exception()


if __name__ == "__main__":
    n = NetellerUi()
    print(n.get_transaction_datas("4035160318a"))

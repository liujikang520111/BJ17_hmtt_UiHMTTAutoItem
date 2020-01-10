from time import sleep

from selenium.webdriver.common.by import By

from base.base import Base


class WabDriver(Base):
    # 选择状态 ul -》 li
    def web_base_click_ul_li(self, placeholder_text, click_text):
        # 组合placeholder 文本元素定位信息
        loc = By.XPATH, "//*[@placeholder='{}']".format(placeholder_text)
        # 查找元素并点击
        self.base_click(loc)
        sleep(2)
        # 定位 ul>li -> 列表
        loc = By.CSS_SELECTOR, "ul>li"
        for el in self.base_finds(loc):
            if el.text == click_text:
                el.click()
                break

    # 判断元素是否存在
    def web_base_element_exists(self, text):
        loc = By.XPATH, "//*[contains(test(),'{}']".format(text)
        try:
            self.base_find(loc, timeout=3)
            return True  # 返回Ture
        except:
            return False  # 返回False

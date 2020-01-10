from page.page_in import PageIn
from tools.get_driver import GetDriver
import page
from tools.get_log import GetLog
import pytest

from tools.read_yaml import read_yaml

log = GetLog.get_logger()


class TestMisLogin:
    def setup_class(self):
        # 获取driver
        driver = GetDriver.get_driver(page.url_mis)
        # 通过统一入口类获取pagemislog登录对象
        self.mis_login = PageIn(driver).page_get_PageMisLogin()
        pass

    def teardown_class(self):
        # 退出driver
        GetDriver.quit_driver()
        pass

    # 后台管理测试业务方法
    @pytest.mark.parametrize("username, pwd, exceprt", read_yaml("mis_login.yaml"))
    def test_mis_login(self, username, pwd, exceprt):
        # 调用后台管理登录业务方法
        self.mis_login.page_mis_login(username, pwd)
        print(self.mis_login.base_get_text(page.mis_nickname))
        # 断言
        try:
            assert exceprt in self.mis_login.base_get_text(page.mis_nickname)

        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.mis_login.base_get_img()
            # 抛异常
            raise

from page.page_in import PageIn
from tools.get_driver import GetDriver
import page
from tools.get_log import GetLog

log = GetLog.get_logger()


class TestMisAudit:
    def setup_class(self):
        driver = GetDriver.get_driver(page.url_mis)
        self.mis_login = PageIn(driver)
        self.login = self.mis_login.page_get_PageMisLogin()
        self.login.page_mis_login_cssues()
        self.mis_audit = self.mis_login.page_get_PageMisAudit()

    def teardown_class(self):
        GetDriver.quit_driver()

    def test_article_audit(self, title="bj-test17-006", channel="数据库"):
        self.mis_audit.page_mis_audit(title, channel)
        # 断言
        try:
            self.mis_audit.page_assert_success(title="bj-test17-006", channel="数据库")
        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.mis_audit.base_get_img()
            # 抛异常
            raise

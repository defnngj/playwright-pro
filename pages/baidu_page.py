"""
@author: 虫师
@date: 2021-01-14
"""


class BasePage:
    def __init__(self, page):
        self.page = page

    def locator(self, loc):
        return self.page.locator(loc)


class BaiduPage(BasePage):

    @property
    def search_input(self):
        """搜索框"""
        return self.locator("#kw")

    @property
    def search_button(self):
        """搜索框"""
        return self.locator("#su")

    @property
    def settings(self):
        """设置"""
        return self.locator("#s-usersetting-top")

    @property
    def search_setting(self):
        """搜索设置"""
        return self.locator("#s-user-setting-menu > div > a.setpref")

    @property
    def save_setting(self):
        """保存设置"""
        return self.locator('text="保存设置"')







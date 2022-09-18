import sys
from time import sleep
from playwright.async_api import Dialog
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from pages.baidu_page import BaiduPage
from playwright.sync_api import Page


def test_baidu_search(page: Page, base_url):
    """
    名称：百度搜索"playwright"
    步骤：
    1、打开浏览器
    2、输入"playwright"关键字
    3、点击搜索按钮
    检查点：
    * 检查页面标题是否相等。
    """
    page.goto(base_url)
    baidu_page = BaiduPage(page)
    baidu_page.search_input.fill("playwright")
    baidu_page.search_button.click()
    sleep(2)
    assert page.title() == "playwright_百度搜索"


def test_baidu_search_setting(page, base_url):
    """
    名称：百度搜索设置
    步骤：
    1、打开百度浏览器
    2、点击设置链接
    3、在下拉框中"选择搜索"
    4、点击"保存设置"
    5、对弹出警告框保存
    检查点：
    * 检查是否弹出提示框
    """
    page.goto(base_url)
    baidu_page = BaiduPage(page)
    baidu_page.settings.click()
    baidu_page.search_setting.click()
    sleep(2)
    baidu_page.save_setting.click()

    def on_dialog(dialog: Dialog):
        assert dialog.type == "alert"
        assert dialog.message == "已经记录下您的使用偏好"
        dialog.accept()

    page.on("dialog", on_dialog)


# def test_zzzz(page: Page, base_url):
#     assert 2 + 2 == 4
#
#
#
#
#
#


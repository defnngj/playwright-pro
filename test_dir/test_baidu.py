import sys
from time import sleep
from playwright.async_api import Dialog
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from element.baidu_element import BaiduElem
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
    page.type(BaiduElem.search_input, text="playwright")
    page.click(BaiduElem.search_button)
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
    result = []
    page.goto(base_url)
    page.click(BaiduElem.settings)
    page.click(BaiduElem.search_setting)
    sleep(2)
    page.click(BaiduElem.save_setting)

    async def on_dialog(dialog: Dialog):
        result.append(True)
        assert dialog.type == "alert"
        assert dialog.message == "yo"
        await dialog.accept()

    page.on("dialog", on_dialog)
    assert result

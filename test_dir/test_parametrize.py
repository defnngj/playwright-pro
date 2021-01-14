"""
@author:  虫师
@data: 2019-10-17
@function pytest 参数使用
"""
import sys
from time import sleep
from seldom.testdata.conversion import json_to_list
import pytest
from os.path import dirname, abspath
case_path = dirname(abspath(__file__))
sys.path.insert(0, case_path)
from element.baidu_element import BaiduElem


@pytest.mark.parametrize(
    "name, search_key",
    [("1", "Selenium"),
     ("2", "pytest文档"),
     ("3", "pytest-html"),
     ],
    ids=["case1", "case2", "case3"]
)
def test_baidu_search_param(name, search_key, page, base_url):
    page.goto(base_url)
    page.type(BaiduElem.search_input, search_key)
    page.click(BaiduElem.search_button)
    sleep(2)
    assert page.title() == search_key + "_百度搜索"


@pytest.mark.parametrize(
    "name, search_key",
    json_to_list(case_path + "/data/data_file.json")
)
def test_baidu_search_data_file(name, search_key, page, base_url):
    page.goto(base_url)
    page.type(BaiduElem.search_input, search_key)
    page.click(BaiduElem.search_button)
    sleep(2)
    assert page.title() == search_key + "_百度搜索"

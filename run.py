# coding=utf-8
import os
import time
import logging
import pytest
from conftest import REPORT_DIR
from config import RunConfig

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

'''
说明：
1、用例创建原则，测试文件名必须以“test”开头，测试函数必须以“test”开头。
2、运行方式：
  > python run.py
'''


def init_env(new_report):
    """
    初始化测试报告目录
    """
    os.mkdir(new_report)
    os.mkdir(new_report + "/image")


def run_tests():
    logger.info("回归模式，开始执行✈✈！")
    now_time = time.strftime("%Y_%m_%d_%H_%M_%S")
    RunConfig.NEW_REPORT = os.path.join(REPORT_DIR, now_time)
    init_env(RunConfig.NEW_REPORT)
    html_report = os.path.join(RunConfig.NEW_REPORT, "report.html")
    xml_report = os.path.join(RunConfig.NEW_REPORT, "junit-xml.xml")
    if RunConfig.mode == "headless":
        pytest.main(["-s", "-v", RunConfig.cases_path,
                     "--browser=" + RunConfig.browser,
                     "--html=" + html_report,
                     "--junit-xml=" + xml_report,
                     "--self-contained-html",
                     "--maxfail", RunConfig.max_fail,
                     "--reruns", RunConfig.rerun])
    if RunConfig.mode == "headful":
        pytest.main(["-s", "-v", "--headful", RunConfig.cases_path,
                     "--browser=" + RunConfig.browser,
                     "--html=" + html_report,
                     "--junit-xml=" + xml_report,
                     "--self-contained-html",
                     "--maxfail", RunConfig.max_fail,
                     "--reruns", RunConfig.rerun])
    logger.info("运行结束，生成测试报告♥❤！")


if __name__ == '__main__':
    run_tests()

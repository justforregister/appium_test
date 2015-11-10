# -*- coding: utf-8 -*-
__author__ = 'heyiling'


# coding=utf-8
import unittest
import HTMLTestRunner

# import sys
# sys.path.append("testSet\\common")
# import Log

import blueberry_test.testSet.common.Log as Log
from blueberry_test.testSet.common.DRIVER import myDriver
from time import sleep

# Returns abs path relative to this file and not cwd
# PATH = lambda p: os.path.abspath(
#     os.path.join(os.path.dirname(__file__), p)
# )


class test01(unittest.TestCase):

    def setUp(self):
        global driver, log, caseNo, flag
        driver = myDriver.GetDriver()
        # self.driver = myDriver.GetDriver()
        caseNo = "test01"
        flag = False

        #get Log
        log = Log.myLog().getLog()
        self.logger = log.getMyLogger()

        #test Start
        log.buildStartLine(caseNo)

    def testCase01(self):
        driver.implicitly_wait(3000)
        # sleep(10)
        driver.find_element_by_id("com.lhxm.blueberry:id/city_text").click()
        city_title = driver.find_element_by_id("com.lhxm.blueberry:id/title").text
        self.assertTrue(city_title == u"城市选择", "Title not displayed!")
        driver.quit()

    def tearDown(self):

        #write result
        if flag:
            log.resultOK(caseNo)
        else:
            log.resultNG(caseNo)

        #test End
        log.buildEndLine(caseNo)


if __name__ == '__main__':
    testunit = unittest.TestSuite()  # 定义一个单元测试容器
    testunit.addTest(test01("testCase01"))  # 将测试用例加入到测试容器中
    filename = "./myAppiumLog.html"  # 定义个报告存放路径，支持相对路径。
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Report_title',
                                           description='Report_description')  # 使用HTMLTestRunner配置参数，输出报告路径、报告标题、描述
    runner.run(testunit)  # 自动进行测试

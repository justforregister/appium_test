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


class baseTest(object):
    def setUp(self):
        global driver, log, caseNo, flag
        driver = myDriver.GetDriver()
        # caseNo = "test01"
        # flag = False

        # # get Log
        # log = Log.myLog().getLog()
        # logger = log.getMyLogger()
        #
        # # test Start
        # log.buildStartLine(caseNo)



    def tearDown(self):
        '''
        # write result
        if flag:
            log.resultOK(caseNo)
        else:
            log.resultNG(caseNo)

        # test End
        log.buildEndLine(caseNo)
        '''
        driver.quit()

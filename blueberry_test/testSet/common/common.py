# -*- coding: utf-8 -*-
__author__ = 'heyiling'

from selenium.common.exceptions import NoSuchElementException
from time import sleep
import blueberry_test.readConfig as readConfig
import os

readConfigLocal = readConfig.ReadConfig
from blueberry_test.testSet.common.DRIVER import myDriver

driver = myDriver.GetDriver()


def returnIndex():
    """
    return the index
    :return:
    """
    pass


def getWindowSize():
    """
    get current windows size mnn
    :return:windowSize
    """
    global windowSize
    windowSize = driver.get_window_size()
    return windowSize


def mySwipeToUP(during=None):
    """
    swipe UP
    :param during:
    :return:
    """
    # if windowSize == None:
    windowSize = getWindowSize()

    width = windowSize.get("width")
    height = windowSize.get("height")
    driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4, during)


def mySwipeToDown(during=None):
    """
    swipe down
    :param during:
    :return:
    """
    windowSize = getWindowSize()
    width = windowSize.get("width")
    height = windowSize.get("height")
    driver.swipe(width / 2, height / 4, width / 2, height * 3 / 4, during)


def mySwipeToLeft(during=None):
    """
    swipe left
    :param during:
    :return:
    """
    windowSize = getWindowSize()
    width = windowSize.get("width")
    height = windowSize.get("height")
    driver.swipe(width / 4, height / 2, width * 3 / 4, height / 2, during)


def mySwipeToRight(during=None):
    """
    swipe right
    :param during:
    :return:
    """
    windowSize = getWindowSize()
    width = windowSize.get("width")
    height = windowSize.get("height")
    driver.swipe(width * 4 / 5, height / 2, width / 5, height / 2, during)


from xml.etree import ElementTree as ET

activity = {}


def setXml():
    """
    get the xml file's value
    :use:
    a = getXml(path)

    print(a.get(".module.GuideActivity").get("skip").get("type"))
    :param: xmlPath
    :return:activity
    """
    if len(activity) == 0:
        xmlPath = os.path.join(readConfig.prjDir, "testSet\\base", "element.xml")
        # open the xml file
        per = ET.parse(xmlPath)
        allElement = per.findall('activity')

        for firstElement in allElement:
            activityName = firstElement.get("name")

            element = {}
            for secondElement in firstElement.getchildren():
                elementName = secondElement.get("name")

                elementChild = {}
                for thirdElement in secondElement.getchildren():
                    elementChild[thirdElement.tag] = thirdElement.text

                element[elementName] = elementChild
            activity[activityName] = element


def getElDict(activityNmae, elementName):
    """
    According to the activityName and elementName get element
    :param activityNmae:
    :param elementName:
    :return:
    """
    setXml()
    elementDict = activity.get(activityNmae).get(elementName)
    return elementDict


import xlrd

cls = []


def getXLS(sheetName):
    """
    get the value in excel
    :param sheetName
    :return:cls
    """

    if len(cls) == 0:
        xlsPath = os.path.join(readConfig.prjDir, "testSet\\base", "TestCase.xls")

        # read the excel
        data = xlrd.open_workbook(xlsPath)

        # get the sheet
        table = data.sheet_by_name(sheetName)

        nrows = table.nrows

        for i in range(nrows):

            if table.row_values(i)[0] != 'mobile':
                cls.append(table.row_values(i))
    return cls


class element:
    def __init__(self, activityName, elementName):
        global driver
        driver = myDriver.GetDriver()
        self.activityName = activityName
        self.elementName = elementName
        elementDict = getElDict(self.activityName, self.elementName)
        self.pathtype = elementDict.get("pathtype")
        self.pathvalue = elementDict.get("pathvalue")

    def isExist(self):
        """
        To determine whether an element is exits
        :return: TRUE or FALSE
        """
        try:
            if self.pathtype == "ID":
                driver.find_element_by_id(self.pathvalue)
            if self.pathtype == "CLASSNAME":
                driver.find_element_by_class_name(self.pathvalue)
            if self.pathtype == "XPATH":
                driver.find_element_by_xpath(self.pathvalue)
            if self.pathtype == "NAME":
                driver.find_element_by_name(self.pathvalue)
        except NoSuchElementException:
            return False
        return True

    def doesExist(self):
        """
        To determine whether an element is exits
        :return:
        """
        i = 1
        while not self.isExist():
            sleep(1)
            i = i + 1
            if i >= 10:
                return False
        else:
            return True

    def get(self):
        """
        get one element
        :return:
        """
        if self.doesExist():
            if self.pathtype == "ID":
                element = driver.find_element_by_id(self.pathvalue)
                return element
            if self.pathtype == "CLASSNAME":
                element = driver.find_element_by_class_name(self.pathvalue)
                return element
            if self.pathtype == "XPATH":
                element = driver.find_element_by_xpath(self.pathvalue)
                return element
            if self.pathtype == "NAME":
                element = driver.find_element_by_name(self.pathvalue)
                return element
        else:
            return None

    def gets(self, index):
        """
        get one element in elementList
        :return:
        """
        if self.doesExist():
            if self.pathtype == "ID":
                elements = driver.find_elements_by_id(self.pathvalue)
                return elements[index]
            if self.pathtype == "CLASSNAME":
                elements = driver.find_elements_by_class_name(self.pathvalue)
                return elements[index]
            if self.pathtype == "XPATH":
                elements = driver.find_elements_by_xpath(self.pathvalue)
                return elements[index]
            if self.pathtype == "NAME":
                elements = driver.find_elements_by_name(self.pathvalue)
                return elements[index]
            return None
        else:
            return None

    def click(self):
        """
        click element
        :return:
        """
        try:
            el = self.get()
            el.click()
        except AttributeError:
            raise

    def clicks(self, index):
        """
        click element
        :return:
        """
        try:
            el = self.gets(index)
            el.click()
        except AttributeError:
            raise

    def sendKey(self, values):
        """
        input the key
        :return:
        """
        try:
            el = self.get()
            el.clear()
            el.send_keys(values)
        except AttributeError:
            raise

    def sendKeys(self, index, values):
        """
        input the key
        :return:
        """
        try:
            el = self.gets(index)
            el.clear()
            el.send_keys(values)
        except AttributeError:
            raise

    def getAttribute(self, attribute):
        """
        get the element attribute
        :param attribute:
        :return:value
        """
        el = self.get()
        value = el.get_attribute(attribute)
        return value


if __name__ == "__main__":
    print(getXLS("login"))

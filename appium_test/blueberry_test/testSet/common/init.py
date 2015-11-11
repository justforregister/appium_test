__author__ = 'tongshan'

import os
import blueberry_test.readConfig as readConfig
readConfigLocal = readConfig.ReadConfig()


class init:

    def __init__(self):
        global startServer,closeServer, checkPhone, logDir, installSoftware, uninstallSoftware,viewPhone,vievAndroid
        self.viewPhone = readConfigLocal.getcmdValue("viewPhone")
        self.viewAndroid = readConfigLocal.getcmdValue("viewAndroid")
        self.startServer = readConfigLocal.getcmdValue("startServer")
        self.closeServer = readConfigLocal.getcmdValue("closeServer")
        self.checkPhone = readConfigLocal.getcmdValue("checkPhone")
        self.installSoftware = readConfigLocal.getcmdValue("installSoftware")
        self.uninstallSoftware = readConfigLocal.getcmdValue("uninstallSoftware")
        self.prjDir = readConfig.prjDir


    def connectPhone(self):
        """
        check the phone is connect
        """
        value = os.popen(self.checkPhone)

        for data in value.readline():
            sDate = str(data)
            if sDate.find("device"):
                return True
        return False

    def getDeviceName(self):
        """get deviceName
        :return:deviceName
        """
        deviceList = []

        returnValue = os.popen(self.viewPhone)
        for value in returnValue.readlines():
            sValue = str(value)
            if sValue.rfind('device'):
                if not sValue.startswith("List"):
                    deviceList.append(sValue[:sValue.find('device')].strip())
        if len(deviceList) != 0:
            return deviceList[0]
        else:
            return None

    def getAndroidVersion(self):
        """get androidVersion
        :return:androidVersion
        """
        returnValue = str(os.popen(self.viewAndroid).read())

        if returnValue != None:
            pop = returnValue.rfind(str('='))
            return returnValue[pop+1:]
        else:
            return None

    def stratServer(self):
        """start the adb server
        :return:
        """
        os.system(self.startServer)

    def closeServer(self):
        """close the adb server
        :return:
        """
        os.system(self.closeServer)

    def reStart(self):
        """reStart the adb server
        :return:
        """
        self.closeServer()
        self.startServer()

    def install(self):

        """
        install software in mobile

        :return: True or False
        """

        apk = self.getApk()

        if apk != None:
            value = os.popen(self.installSoftware+" "+apk)
            sValue = str(value.read())
            if sValue.find("Success"):
                return True
        else:
            return False

    def unInstall(self):
        """uninstall software in mobile

        :return: True or False
        """
        os.system(self.uninstallSoftware)


    def getApk(self):
        """
        get test APK in prjPath

        :return:basename
        """
        apks = os.listdir(self.prjDir)
        if len(apks) > 0:
            for apk in apks:
                if os.path.isfile(apk):
                    basename = os.path.basename(apk)
                    if basename.split('.')[-1] == "apk":
                        return basename
        else:
            return None


if __name__ == '__main__':
    ojb = init()

    ojb.install()


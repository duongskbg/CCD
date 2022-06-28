from models.baseConnectINIFIle import bConnectIniFile
from models.modelData import dPRMFile


class mPRMFile():
    def __init__(self, path_prm=''):
        self.path_prm = path_prm
        self.connectIni = bConnectIniFile()
        self.dataPRM = dPRMFile()

    # ------------------------------------------------------
    def getFileVersion(self):
        """
            get file version from prm file
            @:param  ret
            @:return ret
            @:return self.dataPRM.FileVersion
        """
        _ret = 0
        try:
            _ret, self.dataPRM.FileVersion = \
                self.connectIni.readStrIni(self.path_prm, 'Basic', 'FileVersion')
        except:
            print ('getFileVersion Error')
            _ret = -1
            pass
        return _ret, self.dataPRM.FileVersion



    # ------------------------------------------------------
    def getDbPhaseInfo(self): # sy add
        """
            get file version from prm file
            @:param  ret
            @:return ret
            @:return self.dataPRM.FileVersion
        """
        _ret = 0
        try:
            _ret, self.dataPRM.CurrentPhaseDb = \
                self.connectIni.readStrIni(self.path_prm, 'DebugInfo', 'CurrentPhaseDb')
        except:
            print ('CurrentPhaseDb Error')
            _ret = -1
            pass
        return _ret, self.dataPRM.CurrentPhaseDb
    # ------------------------------------------------------
    def getEquipNum(self):
        """
            get equipment num from prm file
            @:param  ret
            @:return ret
            @:return self.dataPRM.EquipNum
        """
        _ret = 0
        try:
            _ret, self.dataPRM.EquipNum = \
                self.connectIni.readIntIni(self.path_prm, 'EquipmentInfo', 'EquipNum')
        except:
            print ('getEquipNum Error')
            _ret = -1
            pass
        return _ret, self.dataPRM.EquipNum

    # ------------------------------------------------------
    def getWCEna(self):
        """
            get Ena Webcam from prm file
            @:param  ret
            @:return ret
            @:return self.dataPRM.Ena
        """
        _ret = 0
        try:
            _ret, self.dataPRM.WCEna = \
                self.connectIni.readIntIni(self.path_prm, 'WebCamCtrl', 'Ena')

        except:
            print ('getEna Error')
            _ret = -1
            pass
        return _ret, self.dataPRM.WCEna

    # ------------------------------------------------------
    def getWCUSBPort(self):
        """
            get Ena Webcam from prm file
            @:param  ret
            @:return ret
            @:return self.dataPRM.Ena
        """
        _ret = 0
        try:
            _ret, self.dataPRM.WCUSBPort = \
                self.connectIni.readIntIni(self.path_prm, 'WebCamCtrl', 'USBPort')

        except:
            print ('getUSBPort Error')
            _ret = -1
            pass
        return _ret, self.dataPRM.WCUSBPort
    # ------------------------------------------------------
    def getWCResolution(self):
        """
            get Ena Webcam from prm file
            @:param  ret
            @:return ret
            @:return self.dataPRM.Exposure
        """
        _ret = 0
        try:
            _ret, self.dataPRM.WCResolutionHigh = \
                self.connectIni.readIntIni(self.path_prm, 'WebCamCtrl', 'ResolutionHigh')
            _ret, self.dataPRM.WCResolutionWidth = \
                self.connectIni.readIntIni(self.path_prm, 'WebCamCtrl', 'ResolutionWidth')
        except:
            print ('getExposure Error')
            _ret = -1
            pass
        return _ret, self.dataPRM.WCResolutionWidth,self.dataPRM.WCResolutionHigh
    # ------------------------------------------------------
    def getWCExposure(self):
        """
            get Ena Webcam from prm file
            @:param  ret
            @:return ret
            @:return self.dataPRM.Exposure
        """
        _ret = 0
        try:
            _ret, self.dataPRM.WCExposure = \
                self.connectIni.readIntIni(self.path_prm, 'WebCamCtrl', 'Exposure')
        except:
            print ('getExposure Error')
            _ret = -1
            pass
        return _ret, self.dataPRM.WCExposure

    # ------------------------------------------------------
    def getWCBrightness(self):
        """
            get Ena Webcam from prm file
            @:param  ret
            @:return ret
            @:return self.dataPRM.Brightness
        """
        _ret = 0
        try:
            _ret, self.dataPRM.WCBrightness = \
                self.connectIni.readIntIni(self.path_prm, 'WebCamCtrl', 'Brightness')
        except:
            print ('getBrightness Error')
            _ret = -1
            pass
        return _ret, self.dataPRM.WCBrightness

    # ------------------------------------------------------
    def getWCContrast(self):
        """
            get Ena Webcam from prm file
            @:param  ret
            @:return ret
            @:return self.dataPRM.Contrast
        """
        _ret = 0
        try:
            _ret, self.dataPRM.WCContrast = \
                self.connectIni.readIntIni(self.path_prm, 'WebCamCtrl', 'Contrast')
        except:
            print ('getBrightness Error')
            _ret = -1
            pass
        return _ret, self.dataPRM.WCContrast

    # ------------------------------------------------------
    def getWCHue(self):
        """
            get Ena Webcam from prm file
            @:param  ret
            @:return ret
            @:return self.dataPRM.Hue
        """
        _ret = 0
        try:
            _ret, self.dataPRM.WCHue = \
                self.connectIni.readIntIni(self.path_prm, 'WebCamCtrl', 'Hue')
        except:
            print ('getHue Error')
            _ret = -1
            pass
        return _ret, self.dataPRM.WCHue

    # ------------------------------------------------------
    def getWCSaturation(self):
        """
            get Ena Webcam from prm file
            @:param  ret
            @:return ret
            @:return self.dataPRM.Saturation
        """
        _ret = 0
        try:
            _ret, self.dataPRM.WCSaturation = \
                self.connectIni.readIntIni(self.path_prm, 'WebCamCtrl', 'Saturation')
        except:
            print ('getSaturation Error')
            _ret = -1
            pass
        return _ret, self.dataPRM.WCSaturation

    # ------------------------------------------------------
    def getWCSharpness(self):
        """
            get Ena Webcam from prm file
            @:param  ret
            @:return ret
            @:return self.dataPRM.Sharpness
        """
        _ret = 0
        try:
            _ret, self.dataPRM.WCSharpness = \
                self.connectIni.readIntIni(self.path_prm, 'WebCamCtrl', 'Sharpness')
        except:
            print ('getSharpness Error')
            _ret = -1
            pass
        return _ret, self.dataPRM.WCSharpness

    # ------------------------------------------------------
    def getWCGamma(self):
        """
            get Ena Webcam from prm file
            @:param  ret
            @:return ret
            @:return self.dataPRM.Sharpness
        """
        _ret = 0
        try:
            _ret, self.dataPRM.WCGamma = \
                self.connectIni.readIntIni(self.path_prm, 'WebCamCtrl', 'Gamma')
        except:
            print ('getGamma Error')
            _ret = -1
            pass
        return _ret, self.dataPRM.WCGamma

    # ------------------------------------------------------
    def getWCWhiteBalance(self):
        """
            get Ena Webcam from prm file
            @:param  ret
            @:return ret
            @:return self.dataPRM.WhiteBalance
        """
        _ret = 0
        try:
            _ret, self.dataPRM.WCWhiteBalance = \
                self.connectIni.readIntIni(self.path_prm, 'WebCamCtrl', 'WhiteBalance')
        except:
            print ('getWhiteBalance Error')
            _ret = -1
            pass
        return _ret, self.dataPRM.WCWhiteBalance

    # ------------------------------------------------------

    # ------------------------------------------------------
    def getRoi(self):
        """
            get Ena Webcam from prm file
            @:param  ret
            @:return ret
            @:return self.dataPRM.WhiteBalance
        """
        _ret = 0
        try:
            _ret, self.dataPRM.Roi = \
                self.connectIni.readIntIni(self.path_prm, 'WebCamCtrl', 'Roi')
        except:
            print('getWhiteBalance Error')
            _ret = -1
            pass
        return _ret, self.dataPRM.Roi

    # ------------------------------------------------------

    # ------------------------------------------------------
    def getCnf(self):
        """
            get Ena Webcam from prm file
            @:param  ret
            @:return ret
            @:return self.dataPRM.WhiteBalance
        """
        _ret = 0
        try:
            _ret, self.dataPRM.Cnf = \
                self.connectIni.readIntIni(self.path_prm, 'WebCamCtrl', 'Cnf')
        except:
            print('getWhiteBalance Error')
            _ret = -1
            pass
        return _ret, self.dataPRM.Cnf

    # ------------------------------------------------------
    # ------------------------------------------------------
    def getDistance(self):
        """
            get Ena Webcam from prm file
            @:param  ret
            @:return ret
            @:return self.dataPRM.WhiteBalance
        """
        _ret = 0
        try:
            _ret, self.dataPRM.Distance = \
                self.connectIni.readIntIni(self.path_prm, 'WebCamCtrl', 'Distance')
        except:
            print('getWhiteBalance Error')
            _ret = -1
            pass
        return _ret, self.dataPRM.Distance

    # ------------------------------------------------------



    def getWCGain(self):
        """
            get Ena Webcam from prm file
            @:param  ret
            @:return ret
            @:return self.dataPRM.WhiteBalance
        """
        _ret = 0
        try:
            _ret, self.dataPRM.WCGain = \
                self.connectIni.readIntIni(self.path_prm, 'WebCamCtrl', 'Gain')
        except:
            print ('getGain Error')
            _ret = -1
            pass
        return _ret, self.dataPRM.WCGain

    # ------------------------------------------------------
    def getWCRotation(self):
        """
            get Ena Webcam from prm file
            @:param  ret
            @:return ret
            @:return self.dataPRM.Rotation
        """
        _ret = 0
        try:
            _ret, self.dataPRM.WCRotation = \
                self.connectIni.readIntIni(self.path_prm, 'WebCamCtrl', 'Rotation')
        except:
            print ('getRotation Error')
            _ret = -1
            pass
        return _ret, self.dataPRM.WCRotation

    # ------------------------------------------------------
    #RSCOMM
    # ------------------------------------------------------
    def getRsEna(self):
        """
            get Ena Webcam from prm file
            @:param  ret
            @:return ret
            @:return self.dataPRM.RsCommPort
        """
        _ret = 0
        try:
            _ret, self.dataPRM.RSEna = \
                self.connectIni.readIntIni(self.path_prm, 'RSCOMM', 'Ena')
        except:
            print ('getRsena Error')
            _ret = -1
            pass
        return _ret, self.dataPRM.RSEna
    # ------------------------------------------------------

    # ------------------------------------------------------
    def getEnaCrop(self):
        _ret = 0
        try:
            _ret, self.dataPRM.EnCrop = \
                self.connectIni.readIntIni(self.path_prm, 'Crop', 'EnCrop')
        except:
            print ('getEnCrop Error')
            _ret = -1
            pass
        return _ret, self.dataPRM.EnCrop

        # ------------------------------------------------------

    def getCropArea(self):
        _ret = 0
        try:

            _arearead = [0, 0, 0, 0]
            _ret, _read = self.connectIni.readStrIni(self.path_prm, 'Crop', 'CropArea')

            _arearead = [int(_read.split(',')[0]),
                         int(_read.split(',')[1]),
                         int(_read.split(',')[2]),
                         int(_read.split(',')[3])]
            self.dataPRM.CropArea = _arearead

        except:
            print ('getCropArea Error')
            _ret = -1
            pass
        return _ret, self.dataPRM.CropArea


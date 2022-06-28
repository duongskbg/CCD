from models.baseConnectINIFIle import bConnectIniFile
from models.modelData import dINIFile


class mINIFile():
    def __init__(self, path_ini=''):
        self._path_ini = path_ini
        self._ConnectIniFile = bConnectIniFile()
        self._dataINI = dINIFile()

    # ------------------------------------------------------
    def getCameraNum(self):
        """
            @:param _ret
            @:return _ret
            @:return self.dataINI.CameraNum
        """
        _ret = 0
        try:
            _ret, self._dataINI.CameraNum = \
                self._ConnectIniFile.readIntIni(self._path_ini, 'WebCamInfo', 'CameraNum')
        except:
            print ('getCameraNum Error')
            _ret = -1
            pass
        return _ret, self._dataINI.CameraNum

    # ------------------------------------------------------
    def getSpecFileName(self):
        """
            @:param _ret
            @:return _ret
            @:return self.dataINI.CameraNum
        """
        _ret = 0
        try:
            _ret, self._dataINI.SpecFileName = \
                self._ConnectIniFile.readStrIni(self._path_ini, 'FileInfo', 'SpecFileName')
        except:
            print ('getSpecFileName Error')
            _ret = -1
            pass
        return _ret, self._dataINI.SpecFileName

    # ------------------------------------------------------
    def getPrmFileName(self):
        """
            @:param _ret
            @:return _ret
            @:return self.dataINI.PrmFileName
        """
        _ret = 0
        try:
            _ret, self._dataINI.PrmFileName = \
                self._ConnectIniFile.readStrIni(self._path_ini, 'FileInfo', 'PrmFileName')
        except:
            print ('getPrmFileName Error')
            _ret = -1
            pass
        return _ret, self._dataINI.PrmFileName

    # ------------------------------------------------------
    def getOpeMode(self):
        """
            @:param _ret
            @:return _ret
            @:return self.dataINI.OpeMode
        """
        _ret = 0
        try:
            _ret, self._dataINI.OpeMode = \
                self._ConnectIniFile.readIntIni(self._path_ini, 'OperationMode', 'OpeMode')
        except:
            print ('getOpeMode Error')
            _ret = -1
            pass
        return _ret, self._dataINI.OpeMode

    # ------------------------------------------------------
    def getResultBeep(self):
        """
            @:param _ret
            @:return _ret
            @:return self.dataINI.ResultBeep
        """
        _ret = 0
        try:
            _ret, self._dataINI.ResultBeep = \
                self._ConnectIniFile.readIntIni(self._path_ini, 'OperationMode', 'ResultBeep')
        except:
            print ('getResultBeep Error')
            _ret = -1
            pass
        return _ret, self._dataINI.ResultBeep

    # ------------------------------------------------------
    def getImageSaveType(self):
        """
            @:param _ret
            @:return _ret
            @:return self.dataINI.ImageSaveType
        """
        _ret = 0
        try:
            _ret, self._dataINI.ImageSaveType = \
                self._ConnectIniFile.readIntIni(self._path_ini, 'OperationMode', 'ImageSaveType')
        except:
            print ('getImageSaveType Error')
            _ret = -1
            pass
        return _ret, self._dataINI.ImageSaveType
    # ------------------------------------------------------
    def getMaxPhase(self):
        """
            @:param _ret
            @:return _ret
            @:return self.dataINI.ImageSaveType
        """
        _ret = 0
        try:
            _ret, self._dataINI.MaxPhase = \
                self._ConnectIniFile.readIntIni(self._path_ini, 'OperationMode', 'MaxPhase')
        except:
            print ('getMaxPhase Error')
            _ret = -1
            pass
        return _ret, self._dataINI.MaxPhase

    # ------------------------------------------------------

    def getMaxGen(self):
        """
            @:param _ret
            @:return _ret
            @:return self.dataINI.ImageSaveType
        """
        _ret = 0
        try:
            _ret, self._dataINI.MaxGen = \
                self._ConnectIniFile.readIntIni(self._path_ini, 'OperationMode', 'MaxGen')
        except:
            print ('getMaxGen Error')
            _ret = -1
            pass
        return _ret, self._dataINI.MaxGen

    def getMaxStep(self): 
        """
            @:param _ret
            @:return _ret
            @:return self.dataINI.ImageSaveType
        """
        _ret = 0
        try:
            _ret, self._dataINI.MaxStep = \
                self._ConnectIniFile.readIntIni(self._path_ini, 'OperationMode', 'MaxStep')
        except:
            print ('getMaxGen Error')
            _ret = -1
            pass
        return _ret, self._dataINI.MaxStep



    def  getMaxJg(self):  
        _ret = 0
        try:
            _ret, self._dataINI.MaxJg = \
                self._ConnectIniFile.readIntIni(self._path_ini, 'OperationMode', 'MaxJg')
        except:
            print ('getMaxGen Error')
            _ret = -1
            pass
        return _ret, self._dataINI.MaxJg

    def  getCurrentPhase(self): 
        """
            @:param _ret
            @:return _ret
            @:return self.dataINI.ImageSaveType
        """
        _ret = 0
        try:
            _ret, self._dataINI.CurrentPhase = \
                self._ConnectIniFile.readIntIni(self._path_ini, 'OperationMode', 'CurrentPhase')
        except:
            print ('getMaxGen Error')
            _ret = -1
            pass
        return _ret, self._dataINI.CurrentPhase



    def getOutNameImg(self):
        """
            @:param _ret
            @:return _ret
            @:return self.dataINI.ImageSaveType
        """
        _ret = 0
        try:
            _ret, self._dataINI.MaxPhase = \
                self._ConnectIniFile.readIntIni(self._path_ini, 'OperationMode', 'OutNameImg')
        except:
            print ('OutNameImg Error')
            _ret = -1
            pass
        return _ret, self._dataINI.MaxPhase
    # ------------------------------------------------------
    # ------------------------------------------------------

    def getOpeMode(self):
        """
            @:param _ret
            @:return _ret
            @:return self.dataINI.OpeMode
        """
        _ret = 0
        try:
            _ret, self._dataINI.OpeMode = \
                self._ConnectIniFile.readIntIni(self._path_ini, 'OperationMode', 'OpeMode')
        except:
            print('getOpeMode Error')
            _ret = -1
            pass
        return _ret, self._dataINI.OpeMode

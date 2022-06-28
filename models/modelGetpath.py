import platform
import os


# ------------------------------------------------------
class mGetpathfiles:
    def __init__(self):
        pass

    def get_current_path(self):
        """
        get current path run program
        @:param _ret
        @:return _ret
        @:return os.getcwd()
        """
        _ret = 0
        return _ret, os.getcwd()

    def get_ini_path(self):
        """
            get ini file path file
            @:param _ret
            @:return _ret
            @:return ini_path
        """
        _ret = 0
        _ret, _ini_path = self.get_current_path()
        try:
            if platform.system() == 'Windows':
                _ini_path = _ini_path + "\Data\PyCV.ini"
            else:
                _ini_path = _ini_path + "/Data/PyCV.ini"
        except:
            #print 'get ini path error'
            self._textInfo += 'get ini path error\r\n'
            _ret = -1
        return _ret, _ini_path

    #=======================================================
    def get_roi_path(self):
        """
            get ini file path file
            @:param _ret
            @:return _ret
            @:return ini_path
        """
        _ret = 0
        _ret, _ini_path = self.get_current_path()
        try:
            if platform.system() == 'Windows':
                _ini_path = _ini_path + "\Data\Rois\\"
            else:
                _ini_path = _ini_path + "/Data/Rois/"
        except:
            #print 'get ini path error'
            self._textInfo += 'get ini path error\r\n'
            _ret = -1
        return _ret, _ini_path

    # ------------------------------------------------------
    def get_prm_path(self, _filename):
        """
            get prm file path file
            @:param _ret
            @:return _ret
            @:return prm_path
        _ret = 0
        """
        _ret, _prm_path = self.get_current_path()
        try:
            if platform.system() == 'Windows':
                _prm_path = _prm_path + "\Data\{0}".format(_filename)
            else:
                _prm_path = _prm_path + "/Data/{0}".format(_filename)
        except:
            _ret = -1
            #print 'get prm path error'
            self._textInfo += 'get prm path error\r\n'
        return _ret, _prm_path

    # ------------------------------------------------------
    def get_spc_path(self, _filename):
        """
            get spc file path file
            @:param _ret
            @:return _ret
            @:return prm_path
        """
        _ret = 0
        _ret, _spc_path = self.get_current_path()
        try:
            if platform.system() == 'Windows':
                _spc_path = _spc_path + "\Data\Setting\{0}".format(_filename)
            else:
                _spc_path = _spc_path + "/Data/Setting/{0}".format(_filename)
        except:
            _ret = -1
            #print 'get spc path error'
            self._textInfo += 'get spc path error\r\n'

        return _ret, _spc_path

    # =======================================================
    def get_pass_path(self):
        """
            get ini file path file
            @:param _ret
            @:return _ret
            @:return ini_path
        """
        _ret = 0
        _ret, _ini_path = self.get_current_path()
        try:
            if platform.system() == 'Windows':
                _ini_path = _ini_path + "\Data\Count\Pass.lic"
            else:
                _ini_path = _ini_path + "/Data/Count/Pass.lic"
        except:
            # print 'get ini path error'
            self._textInfo += 'get ini path error\r\n'
            _ret = -1
        return _ret, _ini_path

    # =======================================================
    def get_fail_path(self):
        """
            get ini file path file
            @:param _ret
            @:return _ret
            @:return ini_path
        """
        _ret = 0
        _ret, _ini_path = self.get_current_path()
        try:
            if platform.system() == 'Windows':
                _ini_path = _ini_path + "\Data\Count\Fail.lic"
            else:
                _ini_path = _ini_path + "/Data/Count/Fail.lic"
        except:
            # print 'get ini path error'
            self._textInfo += 'get fail path error\r\n'
            _ret = -1
        return _ret, _ini_path

    # =======================================================

    def get_license_path(self):
        _ret = 0
        _ret, _ini_path = self.get_current_path()
        try:
            if platform.system() == 'Windows':
                _ini_path = _ini_path + "\Data\License\license.lic"
            else:
                _ini_path = _ini_path + "/Data/License/license.lic"
        except:
            # print 'get ini path error'
            self._textInfo += 'get License path error\r\n'
            _ret = -1
        return _ret, _ini_path

    # =======================================================
    def get_model_path(self):
        """
            get ini file path file
            @:param _ret
            @:return _ret
            @:return ini_path
        """
        _ret = 0
        _ret, _ini_path = self.get_current_path()
        try:
            if platform.system() == 'Windows':
                _ini_path = _ini_path + "\Data\models.txt"
            else:
                _ini_path = _ini_path + "/Data/models.txt"
        except:
            # print 'get ini path error'
            self._textInfo += 'get model path error\r\n'
            _ret = -1
        return _ret, _ini_path

#=======================================================
    def get_weights_path(self):
        """
            get ini file path file
            @:param _ret
            @:return _ret
            @:return ini_path
        """
        _ret = 0
        _ret, _ini_path = self.get_current_path()
        try:
            if platform.system() == 'Windows':
                _ini_path = _ini_path + "\Data\Models\\"
            else:
                _ini_path = _ini_path + "/Data/Models/"
        except:
            #print 'get ini path error'
            self._textInfo += 'get ini path error\r\n'
            _ret = -1
        return _ret, _ini_path

    def get_standard_labels_path(self):
        _ret = 0
        _ret, _ini_path = self.get_current_path()
        try:
            if platform.system() == 'Windows':
                _ini_path = _ini_path + "\Data\standard_labels\\"
            else:
                _ini_path = _ini_path + "/Data/standard_labels/"
        except:
            #print 'get ini path error'
            self._textInfo += 'get ini path error\r\n'
            _ret = -1
        return _ret, _ini_path
#===================================================
    def get_model_file_path(self):
        """
            get ini file path file
            @:param _ret
            @:return _ret
            @:return ini_path
        """
        _ret = 0
        _ret, _ini_path = self.get_current_path()
        try:
            if platform.system() == 'Windows':
                _ini_path = _ini_path + "\Data\Setting\PyCV.ini"
            else:
                _ini_path = _ini_path + "/Data/Setting/PyCV.ini"
        except:
            #print 'get ini path error'
            self._textInfo += 'get ini path error\r\n'
            _ret = -1
        return _ret, _ini_path

        # =======================================================
    def get_data_folder(self):
        """
            get ini file path file
            @:param _ret
            @:return _ret
            @:return ini_path
        """
        _ret = 0
        _ret, _ini_path = self.get_current_path()
        try:
            if platform.system() == 'Windows':
                _ini_path = _ini_path + "\Data"
            else:
                _ini_path = _ini_path + "/Data"
        except:
            # print 'get ini path error'
            self._textInfo += 'get model path error\r\n'
            _ret = -1
        return _ret, _ini_path

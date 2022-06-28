from configparser import ConfigParser

class bConnectIniFile():
    
    def readStrIni(self, _path, _section, _key):
        """
            read string value
        """
        _ret = 0
        _config = ConfigParser()
        _read = ''
        try:
            # parse existing file
            _config.read(str(_path))
            _read = _config.get(_section, _key).split(';')[0]
        except:
            #print 'read str ini file error'
            _ret = -1
            pass
        return _ret, str(_read)

    # ---------------------------------------------------
    def readFloatIni(self,_path, _section, _key):
        """
            read float value
        """
        _ret = 0
        _config = ConfigParser()
        _read = -1
        try :
            _config.read(float(_path))
            _read = _config.get(_section, _key).split(';')[0]
        except:
            _ret = -1
            pass
        return _ret, float(_read)

    # ---------------------------------------------------
    def readIntIni(self,_path, _section, _key):
        """
            read int value
        """
        _read = -1
        _ret = 0
        try:
            _ret, _read = self.readStrIni(_path, _section, _key)
            if _ret == -1:
                _read = 0

        except:
            print('error read int ini file')
            _ret = -1
            pass

        return _ret, float(_read)

    # ---------------------------------------------------
    def readBoolIni(self, _path, _section, _key):
        """
            read bool value
        """
        _ret=0
        _read = False
        try:
            _ret, _read = self.readStrIni( _path, _section, _key)
            if _ret == -1:
                _read = False

        except:
            print ('error read int ini file')
            _ret = -1
            pass
        return _ret, bool(_read)

    # ---------------------------------------------------
    def readAreaIni(self, _path, _section, _key):
        """
            read area value
        """
        _arearead = [0, 0, 0, 0]
        try:
            _ret, _read = self.readStrIni(_path, _section, _key)
            if _ret == 0:
                _arearead = [int(_read.split(',')[0]),
                            int(_read.split(',')[1]),
                            int(_read.split(',')[2]),
                            int(_read.split(',')[3])]

        except:
            print ('error read area ini file')
            _ret = -1
            pass
        return _ret, _arearead

    # ---------------------------------------------------
    def readSpecJgIni(self, _path, _section, _key):
        """
            read specification value
        """
        _Jg = [0, 0, '']
        try:
            _ret, _read = self.readStrIni(_path, _section, _key)
            if _ret == 0:
                _Jg = [int(_read.split(',')[0]),int(_read.split(',')[1], 0)]

        except:
            print ('error readSpecJgIni ')
            _ret = -1
            pass
        return _ret, _Jg

    # ---------------------------------------------------
    def checkMainSection(self, _path, _section):
        """
            check main section existing values
        """
        _ret = 0
        # instantiate
        _config = ConfigParser()
        _size = 0
        _arrReturn = [0,]
        try:
            _config.read(_path)
            _reads = _config.sections()
            _i = 0
            for _read in _reads:
                __ret = _read.find(_section)
                if __ret != -1:
                    _arrReturn.insert(_i, _read)
                    __ret = _read.find(':')
                    if __ret == -1:
                        _ret = 0
                    else:
                        _i += 1
                        _size = _i
        except:
            print ('error')
            _ret = -1
            pass
        return _ret, _size
    
    # ---------------------------------------------------
    def getSubSection(self, _path, _section, _phase):
        """
            check all section exits value
            @:param  _ret
            @:param  path
            @:param  section
            @:return _ret
            @:return arrReturn
            @:return size
        """
        _ret =0
        # instantiate
        _config = ConfigParser()
        _arrReturn = []
        _size = 0
        try:
            _config.read(_path)
            _reads = _config.sections()
            _i = 0
            for _read in _reads:
                _ret = _read.find(_section + '_F{0}:'.format(_phase))
                if _ret != -1:
                    _arrReturn.insert(_i, _read)
                    _i += 1
                    _size = _i

        except:
            print ('error')
            _ret = -1
            pass
        return _ret, _arrReturn, _size
    # ---------------------------------------------------
    def getAllSection(self,_path, _section):
        """
            get all section exits value
            @:param  _ret
            @:param  path
            @:param  section
            @:return _ret
            @:return arrReturn
        """
        _ret =0
        # instantiate
        _config = ConfigParser()
        _reads = ['', ]
        _arrReturn = []
        try:
            _config.read(_path)
            _reads = _config.sections()
            _i = 0
            for _read in _reads:
                _ret = _read.find(_section)
                if _ret != -1:
                    _arrReturn.insert(_i, _read)
                _i += 1
        except:
            print ('error')
            _ret = -1
            pass
        return _ret, _arrReturn
    # ---------------------------------------------------
    def updateIni(self, _path, _section, _key, _value):
        """
            get all section exits value
            @:param  _ret
            @:param  path
            @:param  section
            @:param key
            @:param value
            @:return _ret
        """
        _ret = 0
        # instantiate
        _config = ConfigParser()
        try:
            # set value
            _config.set(_section, _key, '{0};'.format(_value))
            # save to ini
            with open(str(_path), 'w') as _configfile:
                _config.write(_configfile)
            _ret = 0
        except:
            print ('error write ini file')
            _ret = -1
            pass
        return _ret
    # ---------------------------------------------------
# ---------------------------------------------------
def main():
    _ConnectIniFile = bConnectIniFile()
    _path = 'test.ini'
    _ret = 0
    _ret, _readValue = _ConnectIniFile.readStrIni(_path, 'TEST', 'firtTest')
    print (_readValue)
    _ret = _ConnectIniFile.updateIni( _path, 'TEST', 'firtTest', 'Update')
    if (_ret):
        _ret, _readValue = _ConnectIniFile.readStrIni( _path, 'TEST', 'firtTest')
        print (_readValue)
    else:
        print ('error')
# ---------------------------------------------------
if __name__ == '__main__':
    print ("a")
    #main()

# ---------------------------------------------------
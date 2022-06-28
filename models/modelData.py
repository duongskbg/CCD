import serial

class dRS232():
    port = 'COM2'
    baud_rate = 9600
    parity = serial.PARITY_NONE
    stop_bits = serial.STOPBITS_ONE
    byte_size = serial.EIGHTBITS
    time_out = 0.001
        
class dPRMFile():
    FileVersion = 'V01'
    EquipNum = 34
    # -------------------
    CurrentPhaseDb = 0
    EnCrop = 0
    CropArea = []
    # ----------------------------------------------------
    WCEna = 0
    WCUSBPort = 0
    WCResolutionWidth = 800
    WCResolutionHigh = 640
    WCExposure = 0
    WCBrightness = 0
    WCContrast = 0
    WCHue = 0
    WCSaturation = 0
    WCSharpness = 0
    WCGamma = 0
    WCWhiteBalance = 3000
    WCGain = 0
    WCRotation = 0
    # ----------------------------------------------------
    RSEna = 0
    #----------------------------------------------------
    TCPEna = 0
    # ----------------------------------------------------
    Roi = 0
    Cnf = 0
    Distance = 0
    #========================================
    PIEna = 0
    PIShutterSpeed = 0
    PIRotation = 0
    PIResolutionWidth = 480
    PIResolutionHigh = 640
    PIFrameRate = 10
    PIExposureMode = 0
    PIISO = 800
    PIExposureCompensation = 0
    PIBrightness = 50
    PIContrast = 0
    PISaturation = 0
    PISharpness = 0
    PIRedGains = 0
    PIBlueGains = 0
    PIAwbMode = 0
    PILight = 100
    # ----------------------------------------------------
    GPIOEna = 0
    AllwayOnLamp = 0
    
class dINIFile():
    CameraNum = 0
    SpecFileName = "PyCV.spc"
    PrmFileName = "PyCV.prm"
    OpeMode = 1
    ResultBeep = 0
    ImageSaveType = 2
    MaxPhase = 0
    MaxGen = 1
    MaxStep = 1
    #MaxStep = 1  # sy add
    MaxJg = 0
    CurrentPhase = 0
    OutNameImg = 0
    # ----------------------------------------------------
    OpeModeAdjust = 0
    OpeModeInspection = 1
    OpeModeCalibration = 2
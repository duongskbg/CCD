import tkinter as tk
import cv2, os, torch, math, uuid, hashlib

from tkinter import filedialog, messagebox
from Views.viewMain import View
from models.modelComponent import Component, Camera
from models.modelData import dPRMFile, dINIFile
from models.modelGetpath import mGetpathfiles
from Controllers.controllerPrmFile import cPRMFile
from Controllers.controllerIniFile import cINIFile
from Controllers.controllerRS232 import cRS232 
from datetime import datetime



class Controller():
    def __init__(self):
        self.root = tk.Tk()

        self.Getpath = mGetpathfiles()
        _ = self.init_value_ini()
        _ = self.init_value_prm()
        
        self.view = View(self, self.root) # control the appearance of the app
        self.model = None
        self.cbb_md_name = None
        self.read_md_name()  # read models' names from models.txt to update the combobox  
        if self.model is None:
            model = self.view.cbb_models.get()
            model = model.replace("\n","")
            self.cbb_label_name = model + '.txt'
            self.load_model()
        self.camera = Camera(usb_port = 0)
        self.camera.change_default_settings(self.dataPRM.WCExposure,
                                            self.dataPRM.WCResolutionWidth,
                                            self.dataPRM.WCResolutionHigh,
                                            self.dataPRM.WCBrightness,
                                            self.dataPRM.WCContrast,
                                            self.dataPRM.WCHue,
                                            self.dataPRM.WCSaturation,
                                            self.dataPRM.WCSharpness,
                                            self.dataPRM.WCGamma,
                                            self.dataPRM.WCWhiteBalance,
                                            self.dataPRM.WCGain)
            
            
            # exposure=-2, resolution_width=2592, resolution_height=1944, \
            #                                 brightness=2, contrast=100, hue=5, saturation=40,\
            #                                 sharpness=50, gamma=-1, white_balance=6400, gain=2.25)        
        self.get_barcode()
        self.ctrlRS232 = cRS232()
        self.MAC = None        
        
        
        # set event when close window
        self.root.protocol('WM_DELETE_WINDOW', self.on_close)
        self.root.title("JBD_AI_CCD")
        self.get_mac_add() # to check license                
        
        self.root.mainloop() # wait for click events
                
    
    def get_labels_from_path(self):
        _, folder_standard_labels_path = self.Getpath.get_standard_labels_path() # get file 'standard_labels/<model_name>.txt
        with open(folder_standard_labels_path + self.cbb_label_name, "r+") as label_file:
            lines = label_file.readlines()
        
        # convert labels to readable format
        ret = []
        for line in lines:
            line = line.replace('\n','')
            line = line.split(' ')
            dh, dw = self.img_shape
            x, y, w, h = float(line[1]), float(line[2]), float(line[3]), float(line[4])
            # convert to pixels
            x = int(x * dw)
            y = int(y * dh)
            w = int(w * dw)
            h = int(h * dh)
            # move from center of object to top left point
            x = int(x - w/2)
            y = int(y - h/2)
            component = Component( box=[x, y, w, h], label=int(line[0]) )
            ret.append( component )
        return ret
    
    def load_model(self):
        _, folder_weights_path = self.Getpath.get_weights_path()
        weights_path = folder_weights_path + self.cbb_md_name
        self.model = torch.hub._load_local(folder_weights_path, 'custom', weights_path)
        self.model.conf = self.dataPRM.Cnf # set confidence interval of the predicted object lower to detect small screws
    
    def on_menu_open(self):
        path = filedialog.askopenfilename()
        self.img_path = path
        img = None
        if len(path) > 0: # if open file successfully
            img = cv2.imread(path)
        img = cv2.resize(img, (2592, 1944))
        if img is not None:
            self.view.curr_img = img
            self.img_shape = img.shape[:2]
            self.view.update_canvas(img)
    
    # when pressing the CAPTURE button
    def on_btn_capture(self, evt): # evt is the event object
        img = self.camera.take_pic()
        if img is not None:
            img = cv2.resize(img, (2592, 1944))
            self.view.curr_img = img
            self.img_shape = img.shape[:2]
            self.view.update_canvas(img)
    
    # when pressing the ANALYZE button
    def on_btn_analyze(self, evt):
        self.labels = self.get_labels_from_path()  
        self.ana_res = False
        results = self.model(self.view.curr_img)
        results = results.pandas().xywh[0] # predictions
        results = results.values.tolist()
        self.preds = self.convert_preds_to_comps(results)        
        
        if len(self.preds) > 0:
            self.matching()        
            self.ana_res = self.analyze_result()
            self.view.update_result( self.ana_res )
            if self.ana_res == True and self.MAC is not None:
                    data_send = str(self.MAC) + 13 * ' ' + 'FT' + 10 * '+' + chr(13) # chr(13) is '\n'
                    self.ctrlRS232.send_data(data_send.encode())
        else:
            data_send = str(self.MAC) + 13 * ' ' + 'FT' + 10 * '+' + chr(13) # chr(13) is '\n'
            self.ctrlRS232.send_data(data_send.encode())
            self.view.update_result( False )
        self.res_img = self.view.draw_result() 
        
        ## save image to a folder
        def get_img_name():
            if self.MAC is None:
                img_name = datetime.now().strftime('%Y%m%d_%H%M%S') + '.jpg'
            else:
                img_name = self.MAC + '.jpg'
            return img_name
        
        img_name = get_img_name()
        if self.ana_res == True:
            folder_name = 'SaveImages/Pass/'
        else:
            folder_name = 'SaveImages/Fail/'           
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)            
        file_path = folder_name + img_name
        cv2.imwrite(file_path, self.view.curr_img)
        self.MAC = None
        
    def get_barcode(self):
        self.root.after(2000, self.get_barcode) # run barcode scan every 2000ms
        barcode = self.view.barcode_entry.get()
        self.view.barcode_entry.delete(0, 'end') # erase the entry box to clear accidental keystroke
        if (len(barcode)) > 12: # if MAC is true
            self.MAC = barcode[:12]
            if self.MAC.find('-')== -1:
                self.on_btn_capture(0)
                self.on_btn_analyze(0)
                self.view.barcode_entry.delete(0, 'end')
        
                
    
    
    # match each standard component (label) to an id of a detected component
    def matching(self):
        # read the list of all standard components, calculate the distance to the closest detected component
        dist_lst = []
        small_lst = []
        for lab in self.labels:
            for pred in self.preds:                
                small_lst.append( self.distance_two_boxes(lab.box, pred.box) )
            smallest_distance = min(small_lst)
            dist_lst.append(smallest_distance)
            small_lst = []
        
        # match the standard component and the nearest detected component
        for i, lab in enumerate(self.labels):
            for j, pred in enumerate(self.preds):  
                if self.distance_two_boxes(lab.box, pred.box) == dist_lst[i]:
                    lab.smallest_distance = pred.smallest_distance = dist_lst[i]
                    lab.match_comp = j
                    pred.match_comp = i
    
    def analyze_result(self):
        for lab in self.labels:
            pred = self.preds[ lab.match_comp ]
            if lab.label == pred.label and lab.smallest_distance < self.dataPRM.Distance:
            #if lab.label == pred.label:
                lab.ok_status = True
            else:
                lab.ok_status = False
        
        for lab in self.labels:
            if lab.ok_status == False:
                return False
        return True
    
    # convert list of predictions to list of components
    def convert_preds_to_comps(self, preds):
        comps = []
        for pred in preds:
            cen_x, cen_y, w, h = float(pred[0]), float(pred[1]), float(pred[2]), float(pred[3])
            x = int( cen_x - w / 2 )
            y = int( cen_y - h / 2 )
            w = int( w )
            h = int( h )
            comps.append( Component(box = [x, y, w, h], prob = pred[4], label = pred[5]) )
        return comps
    
    def distance_two_boxes(self, box1, box2):
        x1 = box1[0] + box1[2] / 2
        y1 = box1[1] + box1[3] / 2
        x2 = box2[0] + box2[2] / 2
        y2 = box2[1] + box2[3] / 2
        dist = math.dist([x1, y1], [x2, y2])
        return dist
    
    def init_value_prm(self):
        _ret = 0
        self.dataPRM = dPRMFile()

        _ret, self.path_prm = self.Getpath.get_prm_path(self.dataINI.PrmFileName)
        self.controllerPRM = cPRMFile(self.path_prm)
        # Basic
        _ret, self.dataPRM.FileVersion = self.controllerPRM.getFileVersion()
        # EquipmentInfo
        _ret, self.dataPRM.EquipNum = self.controllerPRM.getEquipNum()
        # DEBUGInfo
        _ret, self.dataPRM.CurrentPhaseDb = self.controllerPRM.getDbPhaseInfo()
        # Crop
        _ret, self.dataPRM.EnCrop = self.controllerPRM.getCropEna()
        _ret, self.dataPRM.CropArea = self.controllerPRM.getCropErea()
        # RSCOMM
        _ret, self.dataPRM.RSEna = self.controllerPRM.getRsEna()
        # WebCamCtrl
        _ret, self.dataPRM.WCEna = self.controllerPRM.getWCEna()
        if self.dataPRM.WCEna == 1:
            _ret, self.dataPRM.WCExposure = self.controllerPRM.getWCExposure()
            _ret, self.dataPRM.WCUSBPort = self.controllerPRM.getWCUSBPort()
            _ret, self.dataPRM.WCResolutionWidth, self.dataPRM.WCResolutionHigh = \
                self.controllerPRM.getWCResolution()

            _ret, self.dataPRM.WCBrightness = self.controllerPRM.getWCBrightness()
            _ret, self.dataPRM.WCContrast = self.controllerPRM.getWCContrast()
            _ret, self.dataPRM.WCHue = self.controllerPRM.getWCHue()
            _ret, self.dataPRM.WCSaturation = self.controllerPRM.getWCSaturation()
            _ret, self.dataPRM.WCSharpness = self.controllerPRM.getWCSharpness()
            _ret, self.dataPRM.WCGamma = self.controllerPRM.getWCGamma()
            _ret, self.dataPRM.WCGain = self.controllerPRM.getWCGain()
            _ret, self.dataPRM.WCWhiteBalance = self.controllerPRM.getWCWhiteBalance()
            _ret, self.dataPRM.WCRotation = self.controllerPRM.getWCRotation()


            _ret, self.dataPRM.Roi = self.controllerPRM.getRoi()
            _ret, self.dataPRM.Cnf = self.controllerPRM.getCnf()
            _ret, self.dataPRM.Distance = self.controllerPRM.getDistance()

        return _ret
    
    def init_value_ini(self):
        _ret = 0
        self.dataINI = dINIFile()
        _ret, self.path_ini = self.Getpath.get_ini_path()
        self._INI = cINIFile(self.path_ini)

        # ------------------------------------------------------
        # WebCamInfo
        _ret, self.dataINI.CameraNum = self._INI.getCameraNum()
        # FileInfo
        _ret, self.dataINI.SpecFileName = self._INI.getSpecFileName()
        _ret, self.dataINI.PrmFileName = self._INI.getPrmFileName()
        # OperationMode
        _ret, self.dataINI.OpeMode = self._INI.getOpeMode()
        _ret, self.dataINI.ResultBeep = self._INI.getResultBeep()
        _ret, self.dataINI.ImageSaveType = self._INI.getImageSaveType()
        _ret, self.dataINI.MaxPhase = self._INI.getMaxPhase()
        _ret, self.dataINI.MaxGen = self._INI.getMaxGen()
        _ret, self.dataINI.MaxStep = self._INI.getMaxStep()
        _ret, self.dataINI.CurrentPhase = self._INI.getCurrentPhase()
        _ret, self.dataINI.MaxJg = self._INI.getMaxJg()
        _ret, self.dataINI.OutNameImg = self._INI.getOutNameImg()

        return _ret
    
    def on_edit_prm_file(self):
        # edit prm file
        _ret = 0
        _ret, path_prm = self.Getpath.get_prm_path(self.dataINI.PrmFileName)
        os.startfile(path_prm)
        # self.restart()

    def on_edit_ini_file(self):
        # open imi file
        _ret = 0
        _ret, _path_ini = self.Getpath.get_ini_path()
        os.startfile(_path_ini)
        # self.restart()
        
    # def restart(self):
    #     rest = sys.executable
    #     os.execl(rest, rest, * sys.argv)
    
    def cbb_selected(self, event):
        model = self.view.cbb_models.get()
        model = model.replace("\n","")
        self.cbb_md_name = ''.join([model,'.pt'])
        self.cbb_label_name = ''.join([model, '.txt'])
        self.load_model()
        
    def read_md_name(self):
        _ret = 0
        _ret, path_spc = self.Getpath.get_model_path()
        with open(path_spc, "r+") as roi_obj:
            models = roi_obj.readlines()
            self.view.cbb_models['values'] = [m for m in models]
            self.view.cbb_models.current(0) # set default value of combo box
            model = models[0].replace("\n","")
            self.cbb_md_name = ''.join([model,'.pt'])
            self.cbb_label_name = ''.join([model, '.txt'])
            
    def on_close(self):
        response = messagebox.askyesno('Exit', 'Are you sure you want to exit?')
        if response:
            self.ctrlRS232.close_port()
            self.root.destroy()
            
    """ get MAC address, convert to hex -> true password. Compare with password the user writes into Data/License/license.lic """
    def get_mac_add(self):
        # lấy 8 giá trị của MAC address
        str2hash = hex(uuid.getnode())[2:14]
        str2hash = str2hash.upper()
        true_pw = hashlib.md5(str2hash.encode())
        true_pw = true_pw.hexdigest()
        curr_pw = self.read_license()
        if true_pw != curr_pw:
            self.show_license()
        else:
            pass
    
    def read_license(self):
        _, path_license = self.Getpath.get_license_path()
        with open(path_license, "r+") as lic_file:
            line = lic_file.readlines()
            line = line[0]
            if line[-1] == '\n':
                line = line.strip()
            lic_file.close()
        return line

    def show_license(self):
        self.view.create_license_window()
            
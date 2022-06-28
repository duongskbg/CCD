import tkinter as tk
import cv2, copy

from tkinter import Button, Label, StringVar, Entry, Menu, Toplevel
from tkinter.ttk import Combobox
from PIL import Image, ImageTk

class View():
    def __init__(self, controller, root):
        self.controller = controller
        self.frame = tk.Frame(root)
        self.frame.pack()
        self.curr_img = None        
        self.create_menu(root)
        self.create_top_bar(root)
        self.create_left_bar(root)
        #self.create_button_bar(root)

        self.create_drawing_canvas(root)
            
    def create_menu(self, root):
        # Menu
        self.menu_bar = Menu(root)
        
        # FILE layout
        self.file_menu = Menu(self.menu_bar, tearoff=0)         
        # add options to "File"
        self.file_menu.add_command(label="Open...", command=self.controller.on_menu_open)
        self.file_menu.add_separator()        
        self.file_menu.add_command(label="Exit", command=root.destroy)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        
         # EDIT layout
        self.tool_menu = Menu(self.menu_bar, tearoff=0)
        self.tool_menu.add_command(label="Edit INI file", command=self.controller.on_edit_ini_file)
        self.tool_menu.add_command(label="Edit PRM file", command=self.controller.on_edit_prm_file)
        self.menu_bar.add_cascade(label="Option", menu=self.tool_menu)

        root.config(menu=self.menu_bar)

    
    def create_left_bar(self, root):
        self.left_bar = tk.Frame(root, width = 150, relief = 'raised', bg = 'blue')
        self.left_bar.pack(fill = 'y', side = 'left')
        self.structure_left_bar()
        
    def structure_left_bar(self):
        # Logo
        logo = Image.open('Data/logo.jpg')
        logo = logo.resize((154, 50), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(logo)
        panel = Label(self.left_bar, image=logo, borderwidth=2, relief="groove")
        panel.image = logo
        panel.pack(side="top",padx = 2, pady = 2)
        
        # CAPTURE button
        self.button_capture = Button(self.left_bar, text = 'CAPTURE', height = 6, width = 21)
        self.button_capture.bind('<Button-1>', self.controller.on_btn_capture)
        self.button_capture.pack(side = 'top', padx = 2, pady = 6)        
        
        # ANALYZE button
        self.button_analyze = Button(self.left_bar, text='ANALYZE', height=6, width=21)
        self.button_analyze.bind("<Button-1>", self.controller.on_btn_analyze)
        self.button_analyze.pack(side = "top", padx = 2, pady = 6)

        # RESULT label
        self.result_lab = Label(self.left_bar, borderwidth=2, relief="groove", text = 'PASS/ FAIL', height = 6, width = 21)
        self.result_lab.pack(side="top", padx = 2, pady = 6)

        # HINT label
        text = '0 - LongScrew\n1 - Button\n2 - ShortScrew\n3 - Stand'
        self.hint_lab = Label(self.left_bar, borderwidth=2, relief="groove", text = text, height = 6, width = 21)
        self.hint_lab.pack(side="top", padx = 2, pady = 6)        
    
    def create_top_bar(self, root):
        self.top_bar = tk.Frame(root, height=25, relief="raised", bg = 'blue')
        self.top_bar.pack( fill="x", side="top")
        self.structure_top_bar()

    def structure_top_bar(self):
        self.barcode_lb = Label(self.top_bar, text = 'Barcode', height = 1, width = 8)
        self.barcode_lb.pack(side="left",padx = 2, pady =1)
        
        self.barcode = StringVar() 
        self.barcode_entry = Entry(self.top_bar, textvariable=self.barcode)
        self.barcode_entry.focus()
        self.barcode_entry.pack(side="left",padx = 6)  
        
         # Black or White models
        self.modellabel = Label(self.top_bar, borderwidth=2, text='Model', height=1, width=6, background='white')
        self.modellabel.pack(side="left", padx=12, pady=0)

        self.cbb_models = Combobox(self.top_bar,  height=1, width=8)
        # self.ccb_models['values'] = ('Black', 'White')
        # self.ccb_models.current(1)
        self.cbb_models['state'] = 'readonly'
        self.cbb_models.pack(side="left", padx=6, pady=1)
        self.cbb_models.bind('<<ComboboxSelected>>', self.controller.cbb_selected)
        
    
    def create_drawing_canvas(self, root):
        self.canvas = tk.Frame(root)
        self.canvas.pack(side = 'right', expand = 'yes', fill = 'both')
        
        self.img_canvas = tk.Canvas(self.canvas, background = 'Lavender', width = 864, height = 648)
        self.img_canvas.pack(side = 'right', expand = 'yes', fill = 'both')
    
    def create_license_window(self):
        toplevel = Toplevel(self.controller.root)
        toplevel.title("License Expired")
        toplevel.grab_set() # to set the GUI control to the license window completely
        toplevel.geometry("250x70+500+500")
        toplevel.protocol("WM_DELETE_WINDOW", lambda:0)
        l1 = Label(toplevel, image="::tk::icons::warning")
        l1.grid(row=0, column=0)
        l2 = Label(toplevel, text="Contact JBD AI member")
        l2.grid(row=0, column=1)
        b1 = Button(toplevel, text="OK", command=self.controller.root.destroy, width=6)
        b1.grid(row=1, column=1)
    
    def update_canvas(self, img):
        global tk_img
        tk_img = self.convert_image_to_display(img)
        self.img_canvas.create_image(0, 0, anchor = 'nw', image = tk_img)
        self.img_canvas.update()
    
    
    
    # resize and convert from cv2 image to image suitable for tk
    def convert_image_to_display(self, img):
        img = cv2.resize(img, (864, 648))
        conv_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        pil_img = Image.fromarray(conv_img)
        tk_img = ImageTk.PhotoImage(pil_img)
        return tk_img
    
    def draw_result(self):
        img1 = copy.deepcopy(self.curr_img)
        dh, dw = self.controller.img_shape
        
        for label in self.controller.labels:
            if label.ok_status == False:
                color = (0, 0, 255) # red
                # color = (0, 255, 0) # green
            else:
                color = (0, 255, 0) # green
            x, y, w, h = label.box[0], label.box[1], label.box[2], label.box[3]   
            image = cv2.rectangle(img1, (x, y), (x + w, y + h), color, 5) 
            cv2.putText(img1,'#' + str(label.label) , (x, y-5) , cv2.FONT_HERSHEY_SIMPLEX, 2, color, 2, cv2.LINE_AA)
        
        for pred in self.controller.preds:
            x, y, w, h = pred.box[0], pred.box[1], pred.box[2], pred.box[3]
            image = cv2.rectangle(img1, (x, y), (x + w, y + h), (255, 0, 0), 5) # blue
            cv2.putText(img1,'#' + str(pred.label) , (x, y-5) , cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 2, cv2.LINE_AA)
        
        self.update_canvas(image)
        return image
    
    def update_result(self, ok_flag):
        if ok_flag:
            self.result_lab['text'] = 'PASS'
            self.result_lab['bg'] = 'green'
        else:
            self.result_lab['text'] = 'FAIL'
            self.result_lab['bg'] = 'red'        
import tkinter as tk
from tkinter import Label, Entry, StringVar, Button, Frame
import hashlib

class GetLicenseApp():
    def __init__(self, parent):
        self.parent = parent
        self.init_ui()
    
    def init_ui(self):
        self.parent.title('Get License')
        
        frame1 = Frame(self.parent)
        frame1.grid(row = 0, column = 0)        
        lbl1 = Label(frame1, text="MAC : ", width=8,font='Tahoma 15 bold')
        lbl1.grid(row = 0, column = 0)        
        self.entry1 = Entry(frame1, width = 50)
        self.entry1.grid(row = 0, column = 1)
        
        frame2 = Frame(self.parent)
        frame2.grid(row = 1, column = 0)
        lbl2 = Label(frame2, text="License : ", width=8,font='Tahoma 15 bold')
        lbl2.grid(row = 0, column = 0)
        self.licen = StringVar()
        self.entry2 = Entry(frame2, width = 50, textvariable=self.licen)
        self.entry2.grid(row = 0, column = 1)
        
        frame3 = Frame(self.parent)
        frame3.grid(row = 2, column = 0)
        button = Button(frame3, text="Get License",  width = 21, command = self.convert_mac)
        button.grid(row = 0, column = 0)
        
    def convert_mac(self):
        mac = self.entry1.get()
        #print(mac)
        if len(mac) >=12:
            mac = mac.replace('-', '')
            mac = mac.upper()
            lic = hashlib.md5(mac.encode())
            lic = lic.hexdigest()
            self.licen.set(lic) 
        
root = tk.Tk()
root.geometry("450x130+300+300")
app = GetLicenseApp(root)
root.mainloop()
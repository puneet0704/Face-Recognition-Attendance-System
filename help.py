from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        title_lbl=Label(self.root,text="Help Desk",font=("times new roman",35,"bold"),bg= "white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        img_top=Image.open(r"C:\Users\punee\OneDrive\Desktop\face_recognition_system\college_images\O.jpg")
        img_top=img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)
        
        help_label=Label(f_lbl,text="Email: puneetbhardwaj.2002@gmail.com",font=("times new roman",18,"bold"),fg="red",bg="black")
        help_label.place(x=500,y=120)
        
        
        
if __name__ =="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
from subprocess import call

class Choose_Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Choose")
        self.root.geometry("1550x800+0+0")
        self.login_img=PhotoImage(file='login.png')
        Label(self.root,image=self.login_img,bg="white").place(x=0,y=0,width=700,height=650)
        frame=Frame(self.root,bg="white")
        frame.place(x=550,y=0,width=700,height=650)
        get_str=Label(frame,text="Choose a Login",font=("Microsoft YaHei UI Light",23,"bold"),fg="#57a1f8",bg="white")
        get_str.place(x=230,y=150)

        userbtn=Button(frame,text="User",command=self.user, font=("Microsoft YaHei UI Light",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="#57a1f8",activeforeground="white",activebackground="red")
        userbtn.place(x=270,y=250,width=120)

        staffbtn=Button(frame,text="Staff",command=self.staff, font=("Microsoft YaHei UI Light",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="#57a1f8",activeforeground="white",activebackground="red")
        staffbtn.place(x=270,y=350,width=120)

        adminbtn=Button(frame,text="Admin",command=self.admin, font=("Microsoft YaHei UI Light",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="#57a1f8",activeforeground="white",activebackground="red")
        adminbtn.place(x=270,y=450,width=120)

        

    def user(self):
        self.root.destroy()
        call(['python','system_user.py'])
    def staff(self):
        self.root.destroy()
        call(['python','login.py'])
    def admin(self):
        self.root.destroy()
        call(['python','admin_login.py'])    
        

if __name__=="__main__":
    root=Tk()
    app=Choose_Login(root)
    root.mainloop()

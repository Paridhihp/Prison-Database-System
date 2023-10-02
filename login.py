from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
from subprocess import call


user_name=""


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        self.login_img=PhotoImage(file='login.png')
        Label(self.root,image=self.login_img,bg="white").place(x=0,y=0,width=700,height=650)
        frame=Frame(self.root,bg="white")
        frame.place(x=550,y=0,width=700,height=650)

        get_str=Label(frame,text="Log in",font=("Microsoft YaHei UI Light",23,"bold"),fg="#57a1f8",bg="white")
        get_str.place(x=230,y=150)

        # Labels
        username=lbl=Label(frame,text="Username",font=("Microsoft YaHei UI Light",15,"bold"),fg="black",bg="white")
        username.place(x=150,y=230)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=150,y=270,width=270)

        password=lbl=Label(frame,text="Password",font=("Microsoft YaHei UI Light",15,"bold"),fg="black",bg="white")
        password.place(x=150,y=300)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"), show = "*")
        self.txtpass.place(x=150,y=340,width=270)

        loginbtn=Button(frame,text="Login",command=self.login, font=("Microsoft YaHei UI Light",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="#57a1f8",activeforeground="white",activebackground="red")
        loginbtn.place(x=230,y=400,width=120)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                con=mysql.connector.connect(host='localhost', username='root',password='Aniket@62', database='management')
                cur=con.cursor() 
                cur.execute("select * from staff where login_id=%s and password=%s", (self.txtuser.get(), self.txtpass.get()))
                row=cur.fetchone()
                print(row)
                if row==None:
                    messagebox.showerror("Error", "Invalid User ID or Password")
                else:
                    user_name=self.txtuser.get()
                    messagebox.showinfo("successful", "Welcome") 
                    self.root.destroy()
                    call(['python','system_staff.py'])                  
                con.close()  
            except Exception as er:
                messagebox.showerror('error',f'Due to {str(er)}')   
        

if __name__=="__main__":
    root=Tk()
    app=Login_Window(root)
    root.mainloop()



    

                      
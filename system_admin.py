from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
from subprocess import call


class Criminal:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1530x790+0+0')
        self.root.title('CRIMINAL MANAGEMENT SYSTEM')
        
        #variables
        self.var_prisoner_id=StringVar()
        self.var_name=StringVar()
        self.var_address=StringVar()
        self.var_age=IntVar()
        self.var_jail_id=IntVar()
        
        
        lbl_title=Label(self.root,text='CRIMINAL MANAGEMENT SYSTEM SOFTWARE',font=('Microsoft YaHei UI Light',35,'bold'),bg='white',fg='#57a1f8')
        lbl_title.place(x=0,y=0,width=1330,height=70)
        #Main_frame
        Main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        Main_frame.place(x=10,y=80,width=1500,height=560)
        #Upper_frame
        upper_frame=LabelFrame(Main_frame,bd=0,relief=RIDGE,text='Search Criminal Information',font=('Microsoft YaHei UI Light',11,'bold'),fg='#57a1f8',bg='white')
        upper_frame.place(x=0,y=0,width=580,height=291)

        remove_by=Label(upper_frame,font=("Microsoft YaHei UI Light",11,"bold"),text="Search By:",bg="white",fg="red")
        remove_by.grid(row=0,column=0,sticky=W,padx=5)
        self.var_com_search=StringVar()
        #Labels Entry
        #Prisoner id
        prisonerid=Label(upper_frame,text='Jail ID:',font=('Microsoft YaHei UI Light',12,'bold'),bg='white')
        prisonerid.grid(row=1,column=0,padx=2,sticky=W)

        caseentry=ttk.Entry(upper_frame,textvariable=self.var_jail_id, width=22,font=('Microsoft YaHei UI Light',11,'bold'))
        caseentry.grid(row=1,column=1,padx=2,sticky=W)

        #Criminal Name
        lbl_criminal_name=Label(upper_frame,text="Staff ID:",font=('Microsoft YaHei UI Ligh',12,'bold'),bg='white')
        lbl_criminal_name.grid(row=2,column=0,sticky=W,padx=2,pady=7)
        self.var_staff_id=StringVar()
        txt_criminal_name=ttk.Entry(upper_frame,textvariable=self.var_staff_id,width=25,font=('Microsoft YaHei UI Ligh',11,'bold'))
        txt_criminal_name.grid(row=2,column=1,sticky=W,padx=2,pady=7)

        self.var_search=StringVar()

        #search button
        btn_search=Button(upper_frame,command=self.search_data, text='Search',font=("Microsoft YaHei UI Light",13,"bold"),width=10,bg='#57a1f8')
        btn_search.grid(row=3,column=0,padx=7,pady=20)

        #all button
        btn_all=Button(upper_frame, command=self.fetch_data, text='Show All',font=("Microsoft YaHei UI Light",13,"bold"),width=10,bg='#57a1f8')
        btn_all.grid(row=3,column=1,padx=2,pady=20)


        
        #Down_frame
        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='Criminal Information Table',font=('Microsoft YaHei UI Light',11,'bold'),fg='#57a1f8',bg='white')
        down_frame.place(x=10,y=280,width=1480,height=270)
         # Table Frame
        table_frame=Frame(down_frame,bd=2,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1470,height=170)

        # Scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.criminal_table=ttk.Treeview(table_frame,column=("1","2","3","4","5","6","7","8","9","10","11","12","13","14"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)

        self.criminal_table.heading("1",text="Prisoner Id")
        self.criminal_table.heading("2",text="Name")
        self.criminal_table.heading("3",text="Address")
        self.criminal_table.heading("4",text="Age")
        self.criminal_table.heading("5",text="Jail ID")

        self.criminal_table['show']='headings'

        self.criminal_table.column("1",width=50)
        self.criminal_table.column("2",width=70)
        self.criminal_table.column("3",width=140)
        self.criminal_table.column("4",width=100)
        self.criminal_table.column("5",width=100)
        
        self.criminal_table.pack(fill=BOTH,expand=1)

        self.criminal_table.bind("<ButtonRelease>",self.get_cursor )
        self.fetch_data()

        #Add_frame
        Add_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='',font=('Microsoft YaHei UI Ligh',11,'bold'),fg='#57a1f8',bg='white')
        Add_frame.place(x=520,y=0,width=580,height=291)
        add_data_label=Label(Add_frame,font=("Microsoft YaHei UI Light",11,"bold"),text="Add data:",bg="white",fg="#57a1f8")
        add_data_label.grid(row=0,column=0,sticky=W,padx=5)

        #Labels Entry
        #Prisoner id
        staffid=Label(Add_frame,text='Staff ID:',font=('Microsoft YaHei UI Light',8,'bold'),bg='white')
        staffid.grid(row=1,column=0,padx=1,sticky=W)

        caseentry=ttk.Entry(Add_frame,textvariable=self.var_staff_id, width=22,font=('Microsoft YaHei UI Light',8,'bold'))
        caseentry.grid(row=1,column=1,padx=1,sticky=W)

        #Jail id
        staffid=Label(Add_frame,text='Jail ID:',font=('Microsoft YaHei UI Light',8,'bold'),bg='white')
        staffid.grid(row=2,column=0,padx=1,sticky=W)

        caseentry=ttk.Entry(Add_frame,textvariable=self.var_jail_id, width=22,font=('Microsoft YaHei UI Light',8,'bold'))
        caseentry.grid(row=2,column=1,padx=1,sticky=W)

        #Criminal Name
        lbl_criminal_name=Label(Add_frame,text="Name:",font=('Microsoft YaHei UI Ligh',8,'bold'),bg='white')
        lbl_criminal_name.grid(row=3,column=0,sticky=W,padx=1)

        txt_criminal_name=ttk.Entry(Add_frame,textvariable=self.var_name,width=25,font=('Microsoft YaHei UI Ligh',8,'bold'))
        txt_criminal_name.grid(row=3,column=1,sticky=W,padx=1)

        #Age
        lbl_criminal_name=Label(Add_frame,text="Age:",font=('Microsoft YaHei UI Ligh',8,'bold'),bg='white')
        lbl_criminal_name.grid(row=4,column=0,sticky=W,padx=1)

        txt_criminal_name=ttk.Entry(Add_frame,textvariable=self.var_age,width=25,font=('Microsoft YaHei UI Ligh',8,'bold'))
        txt_criminal_name.grid(row=4,column=1,sticky=W,padx=1)

        #Gender
        lbl_address=Label(Add_frame,font=('Microsoft YaHei UI Ligh',8,'bold'),text="Gender:",bg='white')
        lbl_address.grid(row=5,column=0,sticky=W,padx=1)
        self.var_gender=StringVar()
        txt_address=ttk.Entry(Add_frame,textvariable=self.var_gender ,width=25,font=('Microsoft YaHei UI Ligh',8,'bold'))
        txt_address.grid(row=5,column=1,sticky=W,padx=1)


         #Gender
        lbl_address=Label(Add_frame,font=('Microsoft YaHei UI Ligh',8,'bold'),text="Designation:",bg='white')
        lbl_address.grid(row=6,column=0,sticky=W,padx=1)
        self.var_designation=StringVar()
        txt_address=ttk.Entry(Add_frame,textvariable=self.var_designation ,width=25,font=('Microsoft YaHei UI Ligh',8,'bold'))
        txt_address.grid(row=6,column=1,sticky=W,padx=1)

        #user_id
        lbl_address=Label(Add_frame,font=('Microsoft YaHei UI Ligh',8,'bold'),text="USER ID:",bg='white')
        lbl_address.grid(row=7,column=0,sticky=W,padx=1)
        self.var_userid=StringVar()
        txt_address=ttk.Entry(Add_frame,textvariable=self.var_userid ,width=25,font=('Microsoft YaHei UI Ligh',8,'bold'))
        txt_address.grid(row=7,column=1,sticky=W,padx=1)

         #password
        lbl_address=Label(Add_frame,font=('Microsoft YaHei UI Ligh',8,'bold'),text="Password:",bg='white')
        lbl_address.grid(row=8,column=0,sticky=W,padx=1)
        self.var_password=StringVar()
        txt_address=ttk.Entry(Add_frame,textvariable=self.var_password ,width=25,font=('Microsoft YaHei UI Ligh',8,'bold'))
        txt_address.grid(row=8,column=1,sticky=W,padx=1)
        

        #Add Button
        btn_add=Button(Add_frame,command=self.add_data,text='Save',font=('arial',13,'bold'),width=14,bg='#57a1f8',fg='white')
        btn_add.grid(row=9,column=0,padx=3,pady=5)

        #Logout Button
        btn_add=Button(Main_frame,command=self.logout,text='Logout',font=('arial',13,'bold'),width=14,bg='#57a1f8',fg='white')
        btn_add.grid(row=0,column=10,padx=1100,pady=0)

        #Deletion Button
        btn_add=Button(Main_frame,command=self.deletion,text='Deletion History',font=('arial',13,'bold'),width=14,bg='#57a1f8',fg='white')
        btn_add.grid(row=2,column=10,padx=1100,pady=0)

        #insertion Button
        btn_add=Button(Main_frame,command=self.insertion,text='Insertion History',font=('arial',13,'bold'),width=14,bg='#57a1f8',fg='white')
        btn_add.grid(row=4,column=10,padx=1100,pady=0)
       
        

    
    # fetch data

    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost', username='root',password='Aniket@62', database='management')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from staff')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.criminal_table.delete(*self.criminal_table.get_children())
            for i in data:
                self.criminal_table.insert('',END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.criminal_table.focus()
        content=self.criminal_table.item(cursor_row)
        data=content['values']

        self.var_case_id.set(data[0])
        self.var_criminal_no.set(data[1])
        self.var_name.set(data[2])
        self.var_nickname.set(data[3])
        self.var_arrest_date.set(data[4])
        self.var_date_of_crime.set(data[5])
        self.var_address.set(data[6])
        self.var_age.set(data[7])
        self.var_occupation.set(data[8])
        self.var_birthMark.set(data[9])
        self.var_crime_type.set(data[10])
        self.var_father_name.set(data[11])
        self.var_gender.set(data[12])
        self.var_wanted.set(data[13])

    def search_data(self): 
        if self.var_jail_id.get()==0 and self.var_staff_id.get()=="":
            messagebox.showerror('Error','All fields are required') 
        else:
            try:
                conn=mysql.connector.connect(host='localhost', username='root',password='Aniket@62', database='management')
                my_cursor=conn.cursor()
                
                my_cursor.execute('select * from staff where Jail_id='+str(self.var_jail_id.get())+" and staff_id="+str(self.var_staff_id.get()))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.criminal_table.delete(*self.criminal_table.get_children())
                    for i in rows:
                        self.criminal_table.insert('',END,values=i)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror('error',f'Due to{str(es)}') 
    
    # Add function

    def add_data(self):
        if self.var_jail_id.get()=="":
            messagebox.showerror('Error','All fields are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost', username='root',password='Aniket@62', database='management')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into staff values(%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                                                                            self.var_name.get(),
                                                                                                            self.var_age.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_designation.get(),
                                                                                                            self.var_staff_id.get(),
                                                                                                            self.var_jail_id.get(),
                                                                                                            self.var_userid.get(),
                                                                                                            self.var_password.get()
                                                                                                             ))
                conn.commit()
                self.fetch_data()
                # self.clear_data()
                conn.close()
                messagebox.showinfo('successful', 'Criminal record has been added')
            except Exception as es:
                messagebox.showerror('error',f'Due to{str(es)}')
    

        
    def insertion(self):
        conn=mysql.connector.connect(host='localhost', username='root',password='Aniket@62', database='management')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from insertion_details')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.criminal_table.delete(*self.criminal_table.get_children())
            for i in data:
                self.criminal_table.insert('',END,values=i)
            conn.commit()
        conn.close()
        
    def deletion(self):
        conn=mysql.connector.connect(host='localhost', username='root',password='Aniket@62', database='management')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from deletion_backup')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.criminal_table.delete(*self.criminal_table.get_children())
            for i in data:
                self.criminal_table.insert('',END,values=i)
            conn.commit()
        conn.close()

    def logout(self):
        self.root.destroy()
        call(['python','choose.py'])

if __name__=="__main__":
    root=Tk()
    obj=Criminal(root)
    root.mainloop()
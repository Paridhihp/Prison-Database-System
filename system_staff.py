from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
from subprocess import call
from login import user_name



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

        search_by=Label(upper_frame,font=("Microsoft YaHei UI Light",11,"bold"),text="Search By:",bg="white",fg="red")
        search_by.grid(row=0,column=0,sticky=W,padx=5)
        self.var_com_search=StringVar()
        combo_search_box=ttk.Combobox(upper_frame,textvariable=self.var_com_search ,font=("Microsoft YaHei UI Light",11,"bold"),width=18,state='readonly')
        combo_search_box['value']=('Select Option','Prisoner_id','Name')
        combo_search_box.current(0)
        combo_search_box.grid(row=0,column=1,sticky=W,padx=1)

        self.var_search=StringVar()
        search_txt=ttk.Entry(upper_frame,textvariable=self.var_search ,width=18,font=("Microsoft YaHei UI Light",11,"bold"))
        search_txt.grid(row=0,column=2,sticky=W,padx=5)

        #search button
        btn_search=Button(upper_frame,command=self.search_data, text='Search',font=("Microsoft YaHei UI Light",13,"bold"),width=10,bg='#57a1f8')
        btn_search.grid(row=2,column=0,padx=7,pady=20)

        #all button
        btn_all=Button(upper_frame, command=self.fetch_data, text='Show All',font=("Microsoft YaHei UI Light",13,"bold"),width=10,bg='#57a1f8')
        btn_all.grid(row=2,column=1,padx=2,pady=20)

        search_by=Label(upper_frame,font=("Microsoft YaHei UI Light",11,"bold"),text="Remove By:",bg="white",fg="red")
        search_by.grid(row=3,column=0,sticky=W,padx=5)

        #Prisoner id
        prisonerid=Label(upper_frame,text='Prisoner ID:',font=('Microsoft YaHei UI Light',12,'bold'),bg='white')
        prisonerid.grid(row=4,column=0,padx=2,sticky=W)

        caseentry=ttk.Entry(upper_frame,textvariable=self.var_prisoner_id, width=22,font=('Microsoft YaHei UI Light',11,'bold'))
        caseentry.grid(row=4,column=1,padx=2,sticky=W)

        #Criminal Name
        lbl_criminal_name=Label(upper_frame,text="Name:",font=('Microsoft YaHei UI Ligh',12,'bold'),bg='white')
        lbl_criminal_name.grid(row=5,column=0,sticky=W,padx=2,pady=7)

        txt_criminal_name=ttk.Entry(upper_frame,textvariable=self.var_name,width=25,font=('Microsoft YaHei UI Ligh',11,'bold'))
        txt_criminal_name.grid(row=5,column=1,sticky=W,padx=2,pady=7)

        #remove button
        btn_all=Button(upper_frame, command=self.remove_data, text='Remove',font=("Microsoft YaHei UI Light",13,"bold"),width=10,bg='#57a1f8')
        btn_all.grid(row=6,column=0,padx=2,pady=20)
        
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
        prisonerid=Label(Add_frame,text='Prisoner ID:',font=('Microsoft YaHei UI Light',12,'bold'),bg='white')
        prisonerid.grid(row=1,column=0,padx=2,sticky=W)

        caseentry=ttk.Entry(Add_frame,textvariable=self.var_prisoner_id, width=22,font=('Microsoft YaHei UI Light',11,'bold'))
        caseentry.grid(row=1,column=1,padx=2,sticky=W)

        #Criminal Name
        lbl_criminal_name=Label(Add_frame,text="Name:",font=('Microsoft YaHei UI Ligh',12,'bold'),bg='white')
        lbl_criminal_name.grid(row=2,column=0,sticky=W,padx=2,pady=7)

        txt_criminal_name=ttk.Entry(Add_frame,textvariable=self.var_name,width=25,font=('Microsoft YaHei UI Ligh',11,'bold'))
        txt_criminal_name.grid(row=2,column=1,sticky=W,padx=2,pady=7)

        #Criminal Address
        lbl_address=Label(Add_frame,font=('Microsoft YaHei UI Ligh',12,'bold'),text="Address:",bg='white')
        lbl_address.grid(row=3,column=0,sticky=W,padx=2,pady=7)

        txt_address=ttk.Entry(Add_frame,textvariable=self.var_address ,width=25,font=('Microsoft YaHei UI Ligh',11,'bold'))
        txt_address.grid(row=3,column=1,sticky=W,padx=2,pady=7)

        #Age
        lbl_age=Label(Add_frame,font=('Microsoft YaHei UI Ligh',12,'bold'),text="Age:",bg='white')
        lbl_age.grid(row=4,column=0,sticky=W,padx=2,pady=7)

        txt_age=ttk.Entry(Add_frame,textvariable=self.var_age ,width=25,font=('Microsoft YaHei UI Ligh',11,'bold'))
        txt_age.grid(row=4,column=1,sticky=W,padx=2,pady=7)

        #Jail id
        lbl_jailid=Label(Add_frame,font=('Microsoft YaHei UI Ligh',12,'bold'),text="Jail id:",bg='white')
        lbl_jailid.grid(row=5,column=0,sticky=W,padx=2,pady=7)

        txt_jailid=ttk.Entry(Add_frame,textvariable=self.var_jail_id ,width=25,font=('Microsoft YaHei UI Ligh',11,'bold'))
        txt_jailid.grid(row=5,column=1,sticky=W,padx=2,pady=7)

        #Add Button
        btn_add=Button(Add_frame,command=self.add_data,text='Save',font=('arial',13,'bold'),width=14,bg='#57a1f8',fg='white')
        btn_add.grid(row=6,column=0,padx=3,pady=5)

        #Logout Button
        btn_add=Button(Main_frame,command=self.logout,text='Logout',font=('arial',13,'bold'),width=14,bg='#57a1f8',fg='white')
        btn_add.grid(row=0,column=10,padx=1100,pady=0)

       
        

    
    # fetch data

    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost', username='root',password='Aniket@62', database='management')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from prisoner')
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
        if self.var_com_search.get()=="":
            messagebox.showerror('Error','All fields are required') 
        else:
            try:
                conn=mysql.connector.connect(host='localhost', username='root',password='Aniket@62', database='management')
                my_cursor=conn.cursor()
                my_cursor.execute('drop view v91')
                my_cursor.execute('create view v91 as select prisoner.prisoner_id,prisoner.name,prisoner.age,prisoner.address,punishments.Details,punishments.Duration,Crime.Location from prisoner,Crime,punishments where prisoner.prisoner_id=Crime.prisoner_id')
                my_cursor.execute('select * from v91 where '+str(self.var_com_search.get())+" LIKE'%"+str(self.var_search.get()+"%'"))
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
        if self.var_prisoner_id.get()=="":
            messagebox.showerror('Error','All fields are required')
        else:
            conn=mysql.connector.connect(host='localhost', username='root',password='Aniket@62', database='management')
            my_cursor=conn.cursor()
            my_cursor.execute('select * from prisoner where prisoner_id='+str(self.var_prisoner_id.get()))
            row=my_cursor.fetchone()
            if row==None:
                try:
                    conn=mysql.connector.connect(host='localhost', username='root',password='Aniket@62', database='management')
                    my_cursor=conn.cursor()
                    my_cursor.execute('insert into prisoner values(%s,%s,%s,%s,%s)',(
                                                                                                                self.var_prisoner_id.get(),
                                                                                                                self.var_name.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_age.get(),
                                                                                                                self.var_jail_id.get(),
                                                                                                                ))
                    conn.commit()
                    self.fetch_data()
                    # self.clear_data()
                    conn.close()
                    messagebox.showinfo('successful', 'Criminal record has been added')
                except Exception as es:
                    messagebox.showerror('error',f'Due to{str(es)}')
            else:
                try:
                    conn=mysql.connector.connect(host='localhost', username='root',password='Aniket@62', database='management')
                    my_cursor=conn.cursor()
                    my_cursor.execute('update prisoner set name=\"'+str(self.var_name.get())+'\",address=\"'+str(self.var_address.get())+'\",age='+str(self.var_age.get())+',jail_id='+str(self.var_jail_id.get())+' where prisoner_id='+str(self.var_prisoner_id.get()))
                    conn.commit()
                    self.fetch_data()
                    # self.clear_data()
                    conn.close()
                    messagebox.showinfo('successful', 'Criminal record has been added')
                except Exception as es:
                    messagebox.showerror('error',f'Due to{str(es)}')

    def remove_data(self):
        if self.var_prisoner_id.get()=="" and self.var_name=="":
            messagebox.showerror('Error','All fields are required') 
        elif self.var_name.get()=="":
            try:
                conn=mysql.connector.connect(host='localhost', username='root',password='Aniket@62', database='management')
                my_cursor=conn.cursor()
                print("here")
                print(self.var_prisoner_id.get())
                my_cursor.execute('delete from prisoner where prisoner_id='+str(self.var_prisoner_id.get()))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.criminal_table.delete(*self.criminal_table.get_children())
                    for i in rows:
                        self.criminal_table.insert('',END,values=i)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror('error',f'Due to{str(es)}') 
        else:
            try:
                print("second")
                conn=mysql.connector.connect(host='localhost', username='root',password='Aniket@62', database='management')
                my_cursor=conn.cursor()
                my_cursor.execute('delete from prisoner where Name='+str(self.var_name.get()))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.criminal_table.delete(*self.criminal_table.get_children())
                    for i in rows:
                        self.criminal_table.insert('',END,values=i)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror('error',f'Due to{str(es)}') 
    def logout(self):
        self.root.destroy()
        call(['python','choose.py'])

if __name__=="__main__":
    root=Tk()
    obj=Criminal(root)
    root.mainloop()
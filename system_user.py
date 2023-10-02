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
        self.var_case_id=StringVar()
        self.var_criminal_no=IntVar()
        self.var_prisoner_id=StringVar()
        self.var_name=StringVar()
        self.var_address=StringVar()
        self.var_age=IntVar()
        self.var_jail_id=IntVar()
        self.var_crime_id=IntVar()
        self.var_nickname=StringVar()
        self.var_arrest_date=StringVar()
        self.var_date_of_crime=StringVar()
        self.var_occupation=StringVar()
        self.var_birthMark=StringVar()
        self.var_crime_type=StringVar()
        self.var_father_name=StringVar()
        self.var_gender=StringVar()
        self.var_wanted=StringVar()
        
        
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
        combo_search_box['value']=('Select Option','Prisoner_id','Jail_id')
        combo_search_box.current(0)
        combo_search_box.grid(row=0,column=1,sticky=W,padx=5)

        self.var_search=StringVar()
        search_txt=ttk.Entry(upper_frame,textvariable=self.var_search ,width=18,font=("Microsoft YaHei UI Light",11,"bold"))
        search_txt.grid(row=0,column=2,sticky=W,padx=5)

        #search button
        btn_search=Button(upper_frame,command=self.search_data, text='Search',font=("Microsoft YaHei UI Light",13,"bold"),width=10,bg='#57a1f8')
        btn_search.grid(row=2,column=0,padx=7,pady=20)

        #all button
        btn_all=Button(upper_frame, command=self.fetch_data, text='Show All',font=("Microsoft YaHei UI Light",13,"bold"),width=10,bg='#57a1f8')
        btn_all.grid(row=2,column=1,padx=2,pady=20)
        
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


        self.criminal_table.column("1",width=50)
        self.criminal_table.column("2",width=70)
        self.criminal_table.column("3",width=140)
        self.criminal_table.column("4",width=100)
        self.criminal_table.column("5",width=100)

        
        
        self.criminal_table.pack(fill=BOTH,expand=1)

        self.criminal_table.bind("<ButtonRelease>",self.get_cursor )
        self.fetch_data()

        #Search Crime
        crime_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='',font=('Microsoft YaHei UI Ligh',11,'bold'),fg='#57a1f8',bg='white')
        crime_frame.place(x=520,y=0,width=580,height=291)
        add_data_label=Label(crime_frame,font=("Microsoft YaHei UI Light",11,"bold"),text="Search Crime details:",bg="white",fg="#57a1f8")
        add_data_label.grid(row=0,column=0,sticky=W,padx=5)

        crimeid=Label(crime_frame,text='Crime ID:',font=('Microsoft YaHei UI Light',12,'bold'),bg='white')
        crimeid.grid(row=1,column=0,padx=2,sticky=W)


        crimeentry=ttk.Entry(crime_frame,textvariable=self.var_crime_id, width=22,font=('Microsoft YaHei UI Light',11,'bold'))
        crimeentry.grid(row=1,column=1,padx=2,sticky=W)

        prisonerid=Label(crime_frame,text='Prisoner ID:',font=('Microsoft YaHei UI Light',12,'bold'),bg='white')
        prisonerid.grid(row=3,column=0,padx=2,sticky=W)
        
        prisonerentry=ttk.Entry(crime_frame,textvariable=self.var_prisoner_id, width=22,font=('Microsoft YaHei UI Light',11,'bold'))
        prisonerentry.grid(row=3,column=1,padx=2,sticky=W)

        name=Label(crime_frame,text='Name:',font=('Microsoft YaHei UI Light',12,'bold'),bg='white')
        name.grid(row=5,column=0,padx=2,sticky=W)
        
        nameentry=ttk.Entry(crime_frame,textvariable=self.var_name, width=22,font=('Microsoft YaHei UI Light',11,'bold'))
        nameentry.grid(row=5,column=1,padx=2,sticky=W)


        #Add Button
        btn_add=Button(crime_frame,command=self.add_data,text='Search',font=('arial',13,'bold'),width=14,bg='#57a1f8',fg='white')
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
                my_cursor.execute('select * from prisoner where '+str(self.var_com_search.get())+" LIKE'%"+str(self.var_search.get()+"%'"))
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
        if self.var_prisoner_id.get()=="" and self.var_crime_id.get()==0 and self.var_name=="":
            messagebox.showerror('Error','Any one field is required')
        elif self.var_crime_id.get()>0:
            print("first")
            try:
                conn=mysql.connector.connect(host='localhost', username='root',password='Aniket@62', database='management')
                my_cursor=conn.cursor()
                print(self.var_crime_id.get())
                my_cursor.execute('select * from Crime where crime_id='+str(self.var_crime_id.get()))
                rows=my_cursor.fetchall()
                print(rows)
                if len(rows)!=0:
                    print(rows)
                    self.criminal_table.delete(*self.criminal_table.get_children())
                    for i in rows:
                        self.criminal_table.insert('',END,values=i)
                conn.commit()
                conn.close()
                print("Here")
            except Exception as es:
                messagebox.showerror('error',f'Due to{str(es)}')
        elif self.var_prisoner_id.get()=="":
            print("second")
            try:
                conn=mysql.connector.connect(host='localhost', username='root',password='Aniket@62', database='management')
                my_cursor=conn.cursor()
                print("select prisoner.Name,prisoner.age,prisoner.prisoner_id, Crime.prisoner_id,Crime.Location from prisoner,Crime where prisoner.prisoner_id=Crime.prisoner_id and prisoner.Name="+str(self.var_name.get()))
                my_cursor.execute(f"select prisoner.Name,prisoner.age,prisoner.prisoner_id, Crime.prisoner_id,Crime.Location from prisoner,Crime where prisoner.prisoner_id=Crime.prisoner_id and prisoner.Name=\"{str(self.var_name.get())}\"")
                rows=my_cursor.fetchall()
                print(rows)
                if len(rows)!=0:
                    print(rows)
                    self.criminal_table.delete(*self.criminal_table.get_children())
                    for i in rows:
                        self.criminal_table.insert('',END,values=i)
                conn.commit()
                conn.close()
                print("Here")
            except Exception as es:
                messagebox.showerror('error',f'Due to{str(es)}')
        else:
            try:
                conn=mysql.connector.connect(host='localhost', username='root',password='Aniket@62', database='management')
                my_cursor=conn.cursor()
                my_cursor.execute('select * from Crime where prisoner_id='+str(self.var_prisoner_id.get()))
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
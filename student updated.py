from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import random
import sqlite3 as c
from tkinter import messagebox
from tkinter import filedialog
import os
from tkcalendar import DateEntry
import re
import subprocess

global combo_dep
global com_txtclasses_std
global com_txt_section
global txt_roll
global txt_name
global txt_adm
global com_txt_gender
global txt_dob
global txt_email
global txt_phone
global student_table
row=0

def get_cursor(event=""):
    global combo_dep
    global com_txtclasses_std
    global com_txt_section
    global txt_roll
    global txt_name
    global txt_adm
    global txt_address
    global com_txt_gender
    global txt_dob
    global txt_email
    global txt_phone
    global student_table
    global row

    cusrsor_row=student_table.focus()
    content=student_table.item(cusrsor_row)
    row=content["values"]
    #calling reset func
    resetget()

    combo_dep.insert(0,str(row[0]))
    com_txtclasses_std.insert(0,str(row[1]))
    com_txt_section.insert(0,str(row[2]))
    txt_roll.insert(0,str(row[3]))
    txt_name.insert(0,str(row[4]))
    txt_adm.insert(0,str(row[5]))
    txt_address.insert(0,str(row[6]))
    com_txt_gender.insert(0,str(row[7]))
    txt_dob.insert(0,str(row[8]))
    txt_email.insert(0,str(row[9]))
    txt_phone.insert(0,str(row[10]))

def resetget():
    txt_roll.delete(0,END)
    txt_name.delete(0,END)
    txt_adm.delete(0,END)
    txt_address.delete(0,END)
    txt_phone.delete(0,END)
    combo_dep.delete(0,END)
    com_txtclasses_std.delete(0,END)
    com_txt_section.delete(0,END)
    com_txt_gender.delete(0,END)
    txt_dob.delete(0,END)
    txt_email.delete(0,END)

def reset():
    txt_roll.delete(0,END)
    txt_name.delete(0,END)
    txt_adm.delete(0,END)
    txt_address.delete(0,END)
    txt_phone.delete(0,END)
    x=random.randint(6099,7595)
    txt_adm.insert(0,x)

def addst():

    global combo_dep
    global com_txtclasses_std
    global com_txt_section
    global txt_roll
    global txt_name
    global txt_adm
    global txt_address
    global com_txt_gender
    global txt_dob
    global txt_email
    global txt_phone
    global student_table
    

    mobile=str(txt_phone.get())
    

    def isvalidmobile(s):
        Pattern=re.compile("(0|91)?[6-9][0-9]{9}")
        return Pattern.match(s)

    if str(combo_dep.get())=="" or str(com_txtclasses_std.get())=="" or str(com_txt_section.get())=="" or str(txt_roll.get())=="" or str(txt_name.get())=="" or str(txt_adm.get())=="" or str(com_txt_gender.get())=="" or str(txt_dob.get())=="" or str(txt_email.get())=="" or str(txt_phone.get())=="":
        messagebox.showerror("Error","All fields are required",parent=root)

    elif not str(txt_roll.get()).isdigit():
        messagebox.showerror("Error","Please Enter Roll in digits",parent=root)

    elif not str(txt_name.get()).isalpha():
        messagebox.showerror("Error","Please Enter Name in alphabets",parent=root)
    
    elif not str(txt_adm.get()).isdigit():
        messagebox.showerror("Error","Please Enter Adm No. in digits",parent=root)

    #elif str(txt_dob.get())>str(txt_email.get()):
        #messagebox.showerror("Error","Please DOB OR Date of ADM",parent=root)
    
    elif (isvalidmobile(mobile)) is None:
        messagebox.showerror("Error","Incorrect Mobile Number"+"\nPlease Enter Indian Mobile Number",parent=root)
    

    else:
        try:
            conn=c.connect("student.db")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into stu (dep,class,sec,roll,name,admno,address,gender,DOB,doadm,Phoneno)values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(str(combo_dep.get()),str(com_txtclasses_std.get()),com_txt_section.get(),str(txt_roll.get()),str(txt_name.get()),str(txt_adm.get()),str(txt_address.get()),str(com_txt_gender.get()),str(txt_dob.get()),str(txt_email.get()),str(txt_phone.get())))
            conn.commit()
            messagebox.showinfo("Success","Student has been added",parent=root)
            fetch_datastud() #fetch data call
            conn.close()
            reset()

        except Exception as es:
            messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=root)


    root.mainloop()

def upstu():
    global combo_dep
    global com_txtclasses_std
    global com_txt_section
    global txt_roll
    global txt_name
    global txt_adm
    global txt_address
    global com_txt_gender
    global txt_dob
    global txt_email
    global txt_phone
    global student_table
    global row
    

    if str(combo_dep.get())=="" or str(com_txtclasses_std.get())=="" or str(com_txt_section.get())=="" or str(txt_roll.get())=="" or str(txt_name.get())=="" or str(txt_adm.get())=="" or str(com_txt_gender.get())=="" or str(txt_dob.get())=="" or str(txt_email.get())=="" or str(txt_phone.get())=="":
        messagebox.showerror("Error","All fields are required",parent=root)

    elif not str(txt_roll.get()).isdigit():
        messagebox.showerror("Error","Please Enter Roll in digits",parent=root)

    elif not str(txt_name.get()).isalpha():
        messagebox.showerror("Error","Please Enter Name in alphabets",parent=root)
    
    elif not str(txt_adm.get()).isdigit():
        messagebox.showerror("Error","Please Enter Adm No. in digits",parent=root)
    else:
        try:
            conn=c.connect("student.db")
            my_cursor=conn.cursor()

            sql1="UPDATE stu SET dep='%s' WHERE admno='%s';"%(str(combo_dep.get()),str(txt_adm.get()))
            sql2="UPDATE stu SET class='%s' WHERE admno='%s';"%(str(com_txtclasses_std.get()),str(txt_adm.get()))
            sql3="UPDATE stu SET sec='%s' WHERE admno='%s';"%(str(com_txt_section.get()),str(txt_adm.get()))
            sql4="UPDATE stu SET roll='%s' WHERE admno='%s';"%(str(txt_roll.get()),str(txt_adm.get()))
            sql5="UPDATE stu SET address='%s' WHERE admno='%s';"%(str(txt_address.get()),str(txt_adm.get()))
            sql6="UPDATE stu SET Phoneno='%s' WHERE admno='%s';"%(str(txt_phone.get()),str(txt_adm.get()))


            my_cursor.execute(sql1)
            conn.commit()
            my_cursor.execute(sql2)
            conn.commit()
            my_cursor.execute(sql3)
            conn.commit()
            my_cursor.execute(sql4)
            conn.commit()
            my_cursor.execute(sql5)
            conn.commit()
            my_cursor.execute(sql6)
            conn.commit()

            conn.close()
            fetch_datastud()
            messagebox.showinfo("Update","Student details has been updated successfully",parent=root)
            reset()
                
        except Exception as es:
            messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=root)
            fetch_datastud()

def deletestud():
    global combo_dep
    global com_txtclasses_std
    global com_txt_section
    global txt_roll
    global txt_name
    global txt_adm
    global txt_address
    global com_txt_gender
    global txt_dob
    global txt_email
    global txt_phone
    global student_table
    global row

    mDelete=messagebox.askyesno("Student Management System","Do you want to delete this student",parent=root)

    if str(combo_dep.get())=="" or str(com_txtclasses_std.get())=="" or str(com_txt_section.get())=="" or str(txt_roll.get())=="" or str(txt_name.get())=="" or str(txt_adm.get())=="" or str(com_txt_gender.get())=="" or str(txt_dob.get())=="" or str(txt_email.get())=="" or str(txt_phone.get())=="":
        messagebox.showerror("Error","All fields are required",parent=root)

    elif not str(txt_roll.get()).isdigit():
        messagebox.showerror("Error","Please Enter Roll in digits",parent=root)

    elif not str(txt_name.get()).isalpha():
        messagebox.showerror("Error","Please Enter Name in alphabets",parent=root)
    
    elif not str(txt_adm.get()).isdigit():
        messagebox.showerror("Error","Please Enter Adm No. in digits",parent=root)
    elif mDelete>0:
        conn=c.connect("student.db")
        my_cursor=conn.cursor()
        mo=(txt_adm.get())
        sql="delete from stu where admno='%s'"%(str(mo))
        my_cursor.execute(sql)
        fetch_datastud()
        conn.commit()
        conn.close()
        fetch_datastud()
        messagebox.showinfo("Deleted","Student details has been deleted successfully",parent=root)
        
    else:
        if not mDelete:
            return

def searchstud():
    global com_txt_search
    global txt_search
    global student_table

    conn=c.connect("student.db")
    my_cursor=conn.cursor()
    my_cursor.execute("select * from stu where "+str(com_txt_search.get())+" LIKE '"+str(txt_search.get())+"%'")
    rows=my_cursor.fetchall()

    if len(rows)!=0:
        student_table.delete(*student_table.get_children(),)
        for i in rows:
            student_table.insert("",END,values=i)
        conn.commit()
    else:
        messagebox.showerror("Error","No Student details found",parent=root)
    conn.close()





def fetch_datastud():
    global combo_dep
    global com_txtclasses_std
    global com_txt_section
    global txt_roll
    global txt_name
    global txt_adm
    global txt_address
    global com_txt_gender
    global txt_dob
    global txt_email
    global txt_phone
    global student_table

    conn=c.connect("student.db")
    my_cursor=conn.cursor()
    my_cursor.execute("select * from stu order by class desc")
    rows=my_cursor.fetchall()
    if len(rows)!=0:
        student_table.delete(*student_table.get_children())
        for i in rows:
            student_table.insert("",END,values=i) #inserting into table
        conn.commit()
    conn.close()

def printdata():

    conn=c.connect("student.db")
    my_cursor=conn.cursor()
    my_cursor.execute("select * from stu order by class desc")
    rows=my_cursor.fetchall()
    filename="filerecords.txt"
    f=open(filename,"w")
    f.write("-"*200+"\n")
    f.write("-"*200+"\n")
    f.write("\t\t\t\t\t\t     STUDENT DATABASE RECORD"+"\n")
    f.write("-"*200+"\n")
    f.write("-"*200+"\n\n")
    f.write("-"*200+"\n")
    f.write("Department\t\tClass\tSec\tRoll\tName\tAdm No.\tAddress\tGender\tDOB\t\tDate of ADM\tPhone No.")
    f.write("\n"+"-"*200)
    if len(rows)!=0:
        for i in rows:
            f.write("\n"+i[0]+"\t"+i[1]+"\t"+i[2]+"\t"+i[3]+"\t"+i[4]+"\t"+i[5]+"\t"+i[6]+"\t"+i[7]+"\t"+i[8]+"\t"+i[9]+"\t"+i[10])
            f.write("\n"+"-"*200+"\n")
    f.flush()
    f.close()
    program="notepad.exe"
    subprocess.Popen([program,filename])

def printbillind():
    global row
    global Psngr_Details_Table
    if (row)!=0:
        i=row
        filename="filestu.txt"
        f=open(filename,"w")
        f.write("-"*200+"\n")
        f.write("-"*200+"\n")
        f.write("\t\t\t\t\t\t     STUDENT DATABASE RECORD"+"\n")
        f.write("-"*200+"\n")
        f.write("-"*200+"\n\n")
        f.write("-"*200+"\n")
        f.write("Department\t\tClass\tSec\tRoll\tName\tAdm No.\tAddress\tGender\tDOB\t\tDate of ADM\tPhone No.")
        f.write("\n"+"-"*200)
        f.write("\n"+i[0]+"\t"+i[1]+"\t"+i[2]+"\t"+str(i[3])+"\t"+i[4]+"\t"+str(i[5])+"\t"+i[6]+"\t"+i[7]+"\t"+str(i[8])+"\t"+str(i[9])+"\t"+str(i[10]))
        f.write("\n"+"-"*200+"\n")
        f.flush()
        f.close()
        program="notepad.exe"
        subprocess.Popen([program,filename])


    else:
        messagebox.showerror("Error","Please select details first!!",parent=root)






def addtable():
    conn=c.connect("student.db")
    my_cursor=conn.cursor()
    sql="CREATE TABLE if not exists stu (\
        dep varchar(30),\
        class varchar(30),\
        sec char(15),\
        roll varchar(20),\
        name varchar(10),\
        admno varchar(50),\
        address varchar(50),\
        gender varchar(20),\
        DOB varchar(20),\
        doadm varchar(20),\
        Phoneno varchar(20),\
        PRIMARY KEY (admno));"
    my_cursor.execute(sql)
    
    sql="CREATE TABLE if not exists login (\
        fullname varchar(30),\
        username varchar(30) UNIQUE,\
        contact varchar(30),\
        recode varchar(30),\
        pass varchar(30),\
        conpass varchar(30),\
        PRIMARY KEY (recode));"
    my_cursor.execute(sql)





















def main():
    global root
    root=Tk()
    root.geometry("1530x790+0+0")
    root.title("Student Management System")

    global combo_dep
    global com_txtclasses_std
    global com_txt_section
    global txt_roll
    global txt_name
    global txt_adm
    global txt_address
    global com_txt_gender
    global txt_dob
    global txt_email
    global txt_phone
    global student_table

    #1st image
    img=Image.open(r"images\1st.jpg")
    img=img.resize((480,160),Image.ANTIALIAS)
    photoimg=ImageTk.PhotoImage(img)
    btn_1=Button(root,image=photoimg,cursor="hand2")
    btn_1.place(x=0,y=0,width=480,height=160)

    #2nd image
    img_2=Image.open(r"images\5th.jpeg")
    img_2=img_2.resize((320,160),Image.ANTIALIAS)
    photoimg_2=ImageTk.PhotoImage(img_2)
    btn_2=Button(root,image=photoimg_2,cursor="hand2")
    btn_2.place(x=480,y=0,width=320,height=160)

    #3rd image
    img_3=Image.open(r"images\7th.jpg")
    img_3=img_3.resize((650,160),Image.ANTIALIAS)
    photoimg_3=ImageTk.PhotoImage(img_3)
    btn_3=Button(root,image=photoimg_3,cursor="hand2")
    btn_3.place(x=790,y=0,width=650,height=160)

    #background image
    img_4=Image.open(r"images\bg4.jpg")
    img_4=img_4.resize((1300,630),Image.ANTIALIAS)
    photoimg_4=ImageTk.PhotoImage(img_4)


    bg_lbl=Label(root,image=photoimg_4,bd=2,relief=RIDGE)
    bg_lbl.place(x=0,y=150,width=1300,height=630)

    lbl_title=Label(bg_lbl,text="STUDENT MANAGEMENT SYSTEM",font=("algerian",37,"bold"),fg="black",bg="white")
    lbl_title.place(x=0,y=0,width=1530,height=50)



        #manage frame
    Manage_frame=Frame(bg_lbl,bd=2,relief=RIDGE,bg='white')
    Manage_frame.place(x=10,y=50,width=1250,height=460)


    #left frame
    DataLeftFrame=LabelFrame(Manage_frame,bd=4,relief=RIDGE,padx=2,text="Student Information",font=("times new roman",12,"bold"),fg="midnight blue",bg="white")
    DataLeftFrame.place(x=10,y=10,width=600,height=440)

    #image1
    img_5=Image.open(r"images\12th.jpg")
    img_5=img_5.resize((350,150),Image.ANTIALIAS)
    photoimg_5=ImageTk.PhotoImage(img_5)

    my_img=Label(DataLeftFrame,image=photoimg_5,bd=2,relief=RIDGE)
    my_img.place(x=0,y=0,width=350,height=150)

        #image2
    img_6=Image.open(r"images\13th.jpg")
    img_6=img_6.resize((240,150),Image.ANTIALIAS)
    photoimg_6=ImageTk.PhotoImage(img_6)

    my_img2=Label(DataLeftFrame,image=photoimg_6,bd=2,relief=RIDGE)
    my_img2.place(x=350,y=0,width=240,height=150)


    #current course label frame information
    std_lbl_info_frame=LabelFrame(DataLeftFrame,bd=4,relief=RIDGE,padx=2,text="Current Course Information",font=("times new roman",12,"bold"),fg="green",bg="white")
    std_lbl_info_frame.place(x=0,y=150,width=590,height=60)

        #labels and combobox
        #Select Department
    lbl_dep=Label(std_lbl_info_frame,text="Department",font=("arial",10,"bold"),bg="white")
    lbl_dep.grid(row=0,column=0,padx=2,sticky=W)

    combo_dep=ttk.Combobox(std_lbl_info_frame,font=("arial",10,"bold"),width=17)
    combo_dep["value"]=("Computer Science","Bio Science","Commerce","Arts","Other")
    combo_dep.current(0)
    combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)


    #Classes
    classes_std=Label(std_lbl_info_frame,text="Class",font=("arial",10,"bold"),bg="white")
    classes_std.grid(row=0,column=2,padx=2,pady=10,sticky=W)

    com_txtclasses_std=ttk.Combobox(std_lbl_info_frame,font=("arial",10,"bold"),width=12)
    com_txtclasses_std['value']=("XII","XI","X","IX","VIII","VII","VI","V","IV","III","II","I")
    com_txtclasses_std.current(0)
    com_txtclasses_std.grid(row=0,column=3,sticky=W,padx=2,pady=10)

    #Section
    lbl_section=Label(std_lbl_info_frame,text="Section:",font=("arial",10,"bold"),bg="white")
    lbl_section.grid(row=0,column=4,padx=2,pady=7,sticky=W)

    com_txt_section=ttk.Combobox(std_lbl_info_frame,font=("arial",10,"bold"),width=13)
    com_txt_section['value']=("A","B","C","D","E","F","G","H")
    com_txt_section.current(0)
    com_txt_section.grid(row=0,column=5,sticky=W,padx=2,pady=7)


        #Student Class label frame information
    std_lbl_class_frame=LabelFrame(DataLeftFrame,bd=4,relief=RIDGE,padx=2,text="Student Class Information",font=("times new roman",12,"bold"),fg="green",bg="white")
    std_lbl_class_frame.place(x=0,y=210,width=590,height=180)

        #Labels Entry

        #Roll No
    lbl_roll=Label(std_lbl_class_frame,text="Roll No.:",font=("arial",10,"bold"),bg="white")
    lbl_roll.grid(row=0,column=0,padx=2,pady=7,sticky=W)

    txt_roll=ttk.Entry(std_lbl_class_frame,font=("arial",10,"bold"),width=22)
    txt_roll.grid(row=0,column=1,padx=2,pady=7,sticky=W)

        #Name
    lbl_name=Label(std_lbl_class_frame,text="Student Name:",font=("arial",10,"bold"),bg="white")
    lbl_name.grid(row=0,column=2,padx=2,pady=7,sticky=W)

    txt_name=ttk.Entry(std_lbl_class_frame,font=("arial",10,"bold"),width=22)
    txt_name.grid(row=0,column=3,padx=2,pady=7)

    #Admission No
    lbl_adm=Label(std_lbl_class_frame,text="Admission No.:",font=("arial",10,"bold"),bg="white")
    lbl_adm.grid(row=1,column=0,padx=2,pady=7,sticky=W)

    txt_adm=ttk.Entry(std_lbl_class_frame,font=("arial",10,"bold"),width=22)
    txt_adm.grid(row=1,column=1,sticky=W,padx=2,pady=7)

    x=random.randint(6099,7595)
    txt_adm.insert(0,x)

    #Address
    lbl_address=Label(std_lbl_class_frame,font=("arial",10,"bold"),bg="white",text="Address:")
    lbl_address.grid(row=1,column=2,sticky=W,padx=2,pady=7)

    txt_address=ttk.Entry(std_lbl_class_frame,font=("arial",10,"bold"),width=22)
    txt_address.grid(row=1,column=3,padx=2,pady=7)

        
        #Gender
    lbl_gender=Label(std_lbl_class_frame,font=("arial",10,"bold"),bg="white",text="Gender:")
    lbl_gender.grid(row=2,column=0,sticky=W,padx=2,pady=7)

    com_txt_gender=ttk.Combobox(std_lbl_class_frame,font=("arial",10,"bold"),width=19)
    com_txt_gender['value']=("Male","Female","Other")
    com_txt_gender.current(0)
    com_txt_gender.grid(row=2,column=1,sticky=W,padx=2,pady=7)
        

        #DOB
    lbl_dob=Label(std_lbl_class_frame,font=("arial",10,"bold"),bg="white",text="Date of Birth:")
    lbl_dob.grid(row=2,column=2,sticky=W,padx=2,pady=7)

    txt_dob=DateEntry(std_lbl_class_frame,selectmode='day',date_pattern='dd/mm/y',font=("arial",10,"bold"),width=22)
    txt_dob.grid(row=2,column=3,padx=2,pady=7)

    #now used for date of adm
    lbl_email=Label(std_lbl_class_frame,font=("arial",10,"bold"),bg="white",text="Date of Adm:")
    lbl_email.grid(row=3,column=0,sticky=W,padx=2,pady=7)

    txt_email=DateEntry(std_lbl_class_frame,selectmode='day',date_pattern='dd/mm/y',font=("arial",10,"bold"),width=22)
    txt_email.grid(row=3,column=1,padx=2,pady=7)

        #Phone No
    lbl_phone=Label(std_lbl_class_frame,font=("arial",10,"bold"),bg="white",text="Phone No.:")
    lbl_phone.grid(row=3,column=2,sticky=W,padx=2,pady=7)

    txt_phone=ttk.Entry(std_lbl_class_frame,font=("arial",10,"bold"),width=22)
    txt_phone.grid(row=3,column=3,padx=2,pady=7)


    #Button Frame
    btn_frame=Frame(DataLeftFrame,bd=2,relief=RIDGE,bg='white')
    btn_frame.place(x=0,y=390,width=590,height=25)

    btn_Add=Button(btn_frame,text="Save",command=addst,font=("arial",10,"bold"),bg="midnight blue",fg="white",width=17)
    btn_Add.grid(row=0,column=0,padx=1)

    btn_Update=Button(btn_frame,text="Update",command=upstu,font=("arial",10,"bold"),bg="midnight blue",fg="white",width=17)
    btn_Update.grid(row=0,column=1,padx=1)

    btn_Delete=Button(btn_frame,text="Delete",command=deletestud,font=("arial",10,"bold"),bg="midnight blue",fg="white",width=17) #command=delete_data,
    btn_Delete.grid(row=0,column=2,padx=1)

    btn_Reset=Button(btn_frame,text="Reset",command=reset,font=("arial",10,"bold"),bg="midnight blue",fg="white",width=17)    #command=reset_data
    btn_Reset.grid(row=0,column=3,padx=1)


        #right frame                
    DataRightFrame=LabelFrame(Manage_frame,bd=4,relief=RIDGE,padx=2,text="Student Information",font=("times new roman",12,"bold"),fg="midnight blue",bg="white")
    DataRightFrame.place(x=620,y=10,width=610,height=440)

        #search frame

    Search_Frame=LabelFrame(DataRightFrame,bd=4,relief=RIDGE,padx=2,text="Search Student Information",font=("times new roman",12,"bold"),fg="green",bg="white")
    Search_Frame.place(x=0,y=0,width=600,height=50)

    search_by=Label(Search_Frame,font=("arial",10,"bold"),bg="midnight blue",fg="white",text="Search By:")
    search_by.grid(row=0,column=0,sticky=W,padx=2)

    global com_txt_search
    global txt_search
    com_txt_search=ttk.Combobox(Search_Frame,font=("arial",10,"bold"),width=12,state="readonly")
    com_txt_search['value']=("roll","admno")
    com_txt_search.current(1)
    com_txt_search.grid(row=0,column=1,sticky=W,padx=3)

    
    txt_search=ttk.Entry(Search_Frame,font=("arial",10,"bold"),width=18)
    txt_search.grid(row=0,column=2,padx=3)

    btn_search=Button(Search_Frame,text="Search",command=searchstud,font=("arial",10,"bold"),bg="midnight blue",fg="white",width=14) #command=search_data,
    btn_search.grid(row=0,column=3,padx=3)

    btn_ShowAll=Button(Search_Frame,text="Show All",command=fetch_datastud,font=("arial",10,"bold"),bg="midnight blue",fg="white",width=14)
    btn_ShowAll.grid(row=0,column=4,padx=3)


     #==============STUDENT TABLE AND SCROLL BAR==============
    table_frame=Frame(DataRightFrame,bd=4,relief=RIDGE)
    table_frame.place(x=0,y=55,width=600,height=320)

    btn_ind=Button(DataRightFrame,text="STUDENT RECORD",command=printbillind,font=("arial",10,"bold"),bg="midnight blue",fg="white",width=17)    #command=reset_data
    btn_ind.place(x=0,y=380,width=300,height=40)

    btn_all=Button(DataRightFrame,text="ALL RECORDS",command=printdata,font=("arial",10,"bold"),bg="midnight blue",fg="white",width=17)    #command=reset_data
    btn_all.place(x=300,y=380,width=300,height=40)

    scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
    scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
    student_table=ttk.Treeview(table_frame,column=("dep","class","sec","roll","name","admno","address","gender","DOB","doadm","Phoneno"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)       
        
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)

    scroll_x.config(command=student_table.xview)
    scroll_y.config(command=student_table.yview)

    student_table.heading("dep",text="Department")
    student_table.heading("class",text="Class")
    student_table.heading("sec",text="Section")
    student_table.heading("roll",text="Roll No")
    student_table.heading("name",text="Name")
    student_table.heading("admno",text="Addmission No")
    student_table.heading("address",text="Address")
    student_table.heading("gender",text="Gender")
    student_table.heading("DOB",text="DOB")
    student_table.heading("doadm",text="Date of Adm")
    student_table.heading("Phoneno",text="Phone No")

    student_table["show"]="headings"

    student_table.column("dep",width=100)
    student_table.column("class",width=100)
    student_table.column("sec",width=100)
    student_table.column("roll",width=100)
    student_table.column("name",width=100)
    student_table.column("admno",width=100)
    student_table.column("address",width=100)
    student_table.column("gender",width=100)
    student_table.column("DOB",width=100)
    student_table.column("doadm",width=100)
    student_table.column("Phoneno",width=100)

    student_table.pack(fill=BOTH,expand=1)
    student_table.bind("<ButtonRelease>",get_cursor)
    fetch_datastud()












    root.mainloop()


def log():
    global root
    global fname_entry
    global l_entry
    global txt_contact
    global txt_recode
    global txt_pass
    global txt_conpass
    root=Tk()
    def Register():
        global fname_entry
        global l_entry
        global txt_contact
        global txt_recode
        global txt_pass
        global txt_conpass
        global checkbtn

        root.title("Register")
        root.geometry("1600x900+0+0")

        #background image

        bg1=ImageTk.PhotoImage(file="images\\regisf.jpg")
            
        bg1_lbl=Label(root,image=bg1,relief=RIDGE)
        bg1_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        #bg 2
        bgimage=Image.open("images\\regis2.jpg")
        bgimage=bgimage.resize((460,550),Image.ANTIALIAS)
        bg2=ImageTk.PhotoImage(bgimage)

        
        bg2_lbl=Label(root,image=bg2,bd=4,relief=RIDGE)
        bg2_lbl.place(x=130,y=130,width=460,height=550)

        #side frame

        frame=Frame(root,bg="white")
        frame.place(x=590,y=130,width=800,height=550)

        #frame inside work

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen")
        register_lbl.place(x=20,y=20)

        #--login button--#

        loginbtnreg=Button(frame,command=Login_Window,text="Login Now",font=("Arial",13,"bold"),bd=3,relief=RIDGE,fg="black",bg="aqua",activeforeground="black",activebackground="aqua")
        loginbtnreg.place(x=630,y=20,width=120,height=35)

        #labels and entry fields

        framename=Label(frame,text="First Name",font=("times new roman",20,"bold"),bg="white")
        framename.place(x=50,y=100)

        #entry field for first name

        fname_entry=ttk.Entry(frame,font=("times new roman",16,"bold"))
        fname_entry.place(x=50,y=135,width=230)

        #last name

        l_name=Label(frame,text="User Name",font=("times new roman",20,"bold"),bg="white")
        l_name.place(x=370,y=100)

        l_entry=ttk.Entry(frame,font=("times new roman",16,"bold"))
        l_entry.place(x=370,y=136,width=230)

        #contact

        contact_name=Label(frame,text="Contact No",font=("times new roman",20,"bold"),bg="white")
        contact_name.place(x=50,y=170)

        txt_contact=ttk.Entry(frame,font=("times new roman",16,"bold"))
        txt_contact.place(x=50,y=210,width=230)

        #recovery  code

        recode=Label(frame,text="Recovery Code",font=("times new roman",20,"bold"),bg="white")
        recode.place(x=370,y=170)

        txt_recode=ttk.Entry(frame,font=("times new roman",16,"bold"))
        txt_recode.place(x=370,y=207,width=230)
        
        #password

        password=Label(frame,text="Password",font=("times new roman",20,"bold"),bg="white")
        password.place(x=50,y=245)

        txt_pass=ttk.Entry(frame,font=("times new roman",16,"bold"))
        txt_pass.place(x=50,y=282,width=230)

        #confirm pass

        conpass=Label(frame,text="Confirm Password",font=("times new roman",20,"bold"),bg="white")
        conpass.place(x=370,y=240)

        txt_conpass=ttk.Entry(frame,font=("times new roman",16,"bold"))
        txt_conpass.place(x=370,y=277,width=230)


        #check btn terms and conditions
        global var_check
        var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=var_check,text="I Agree the Terms & Conditions",font=("times new roman",15,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=330)
        def registerclick():
            global var_check
            global fname_entry
            global l_entry
            global txt_contact
            global txt_recode
            global txt_pass
            global txt_conpass



            if str(fname_entry.get())=="" or str(l_entry.get())=="" or str(txt_contact.get())=="" or str(txt_recode.get())=="" or str(txt_pass.get())=="" or str(txt_conpass.get())=="":
                messagebox.showerror("Error","All fields are required",parent=root)

            elif not fname_entry.get().isalpha() or not l_entry.get().isalpha():
                messagebox.showerror("Error","Please Enter Name in alphabets",parent=root)
            elif not str(txt_contact.get()).isdigit() or not str(txt_recode.get()).isdigit():
                messagebox.showerror("Error","Please Enter Digits in the desired box",parent=root)
            elif str(txt_pass.get())!=str(txt_conpass.get()):
                messagebox.showerror("Error","Password & Confirm Password must be same",parent=root)
            elif var_check.get()==0:
                messagebox.showerror("Error","Please agree our terms and conditions",parent=root)
            else:
                messagebox.showinfo("Done","Welcome to our Student Management System",parent=root)
                conn=c.connect("student.db")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from login where username='%s'"%(str(l_entry.get())))
                row=my_cursor.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already exist with same details\nPlease try again",parent=root)
                else:
                    my_cursor.execute("insert into login (fullname,username,contact,recode,pass,conpass)values('%s','%s','%s','%s','%s','%s')"%(str(fname_entry.get()),str(l_entry.get()),str(txt_contact.get()),str(txt_recode.get()),str(txt_pass.get()),str(txt_conpass.get())))
                    conn.commit()
                    messagebox.showinfo("Registered","Data registered successfully",parent=root)
                    conn.close()
        #register now

        img=Image.open("images\\regisnowbtn.png")
        img=img.resize((170,50),Image.ANTIALIAS)
        photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=photoimage,borderwidth=0,command=registerclick,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=203,y=390,width=300)

        

        root.mainloop()

    def Login_Window():
        global root
        global fname_entry
        global l_entry
        global txt_contact
        global txt_recode
        global txt_pass
        global txt_conpass
        global txtuser
        global txtpass
        global txt_newpass
        
        root.title("Student Management System Login Pannel")
        root.geometry("1550x800+0+0")

        bgimage=Image.open("images\\10th.jpg")
        bgimage=bgimage.resize((1550,800),Image.ANTIALIAS)
        bg=ImageTk.PhotoImage(bgimage)

        lbl_bg=Label(root,image=bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(root,bg="black")
        frame.place(x=603,y=175,width=340,height=450) #x and y pos value and width and height size of box

        img1=Image.open("images\\get.jpg")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=180,width=100,height=100)

            #get started label

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=107,y=100)

            #user name label

        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=60,y=155)
            
        txtuser=ttk.Entry(frame,font=("times new roman",13,"bold"))       
        txtuser.place(x=35,y=180,width=270)

            #password label

        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=60,y=225)

        txtpass=ttk.Entry(frame,font=("times new roman",13,"bold"),show="*")       
        txtpass.place(x=35,y=250,width=270)

            #Icon Images of username 

        img2=Image.open("images\\logicon.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=640,y=330,width=25,height=25)

            #Icon Images of password

        img3=Image.open("images\\passicon.png")
        img3=img3.resize((55,25),Image.ANTIALIAS)
        photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=photoimage3,bg="black",borderwidth=0)
        lblimg1.place(x=639,y=400,width=25,height=25)
            
            #login btn in login pannel               here command ka kaam click karne par def login ko call karna hai
        def login():
            global txtuser
            global txtpass
            global txt_recode

            if str(txtuser.get())=="" or str(txtpass.get())=="":
                messagebox.showerror("Error","All fields required",parent=root)
            else:
                conn=c.connect("student.db")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from login where username='%s' and pass='%s'"%(str(txtuser.get()),str(txtpass.get())))
                row=my_cursor.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Username & Password",parent=root)
                else:
                    root.destroy()
                    main()


        loginbtn=Button(frame,command=login,text="Login",font=("times new roman",13,"bold"),bd=3,relief=RIDGE,fg="black",bg="aqua",activeforeground="black",activebackground="aqua")
        loginbtn.place(x=105,y=300,width=120,height=35)

            # registerbutton for new users

        registerbtn=Button(frame,text="New User Register",command=Register,font=("times new roman",11,"bold"),bd=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=5,y=353,width=160)

            #forgot passbtn
        def forgotpass():
            global txtuser
            global txtpass
            global txt_recode
            global txt_newpass

            if str(txtuser.get())=="":
                messagebox.showerror("Error","Please Enter User Name to reset Password",parent=root)
            else:
                conn=c.connect("student.db")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from login where username='%s'"%(str(txtuser.get())))
                row=my_cursor.fetchone()

                if row==None:
                    messagebox.showerror("Error","Please enter valid username",parent=root)
                else:
                    conn.close()
                    root2=Toplevel()
                    root2.title("Forgot Password")
                    root2.geometry("360x480+590+170")

                    l=Label(root2,text="Forgot Password",font=("times new roman",20,"bold"),fg="blue",bg="cyan")
                    l.place(x=0,y=10,relwidth=1)

                    #recovery  code

                    recode=Label(root2,text="Recovery Code",font=("times new roman",20,"bold"),bg="cyan")
                    recode.place(x=88,y=80)

                    txt_recode=ttk.Entry(root2,font=("times new roman",16,"bold"))
                    txt_recode.place(x=50,y=130,width=250)
                    
                    #password

                    newpassword=Label(root2,text="New Password",font=("times new roman",20,"bold"),bg="cyan")
                    newpassword.place(x=88,y=180)

                    txt_newpass=ttk.Entry(root2,font=("times new roman",16,"bold"))
                    txt_newpass.place(x=50,y=220,width=250)
                    
                    def resetpass():
                        global txtuser
                        global txt_newpass
                        global txt_recode

                        

                        if str(txt_recode.get())=="":
                            messagebox.showerror("Error","Please enter Recovery Code",parent=root2)
                        elif not str(txt_recode.get()).isdigit():
                            messagebox.showerror("Error","Please enter Recovery Code in Digits",parent=root2)
                        else:
                            conn=c.connect("student.db")
                            my_cursor=conn.cursor()
                            my_cursor.execute("select * from login where username='%s' and recode='%s'"%(str(txtuser.get()),str(txt_recode.get())))
                            row=my_cursor.fetchone()
                            if row==None:
                                messagebox.showerror("Error","Please enter Correct Recovery Code",parent=root2)
                            else:
                                my_cursor.execute("update login set pass='%s' where username='%s' and recode='%s'"%(str(txt_newpass.get()),str(txtuser.get()),str(txt_recode.get())))
                                conn.commit()
                                conn.close()
                                messagebox.showinfo("Info","Your password has been reset\nYou can login with your new password",parent=root2) 
                                root2.destroy()


                        



                    #btn for reset

                    btn=Button(root2,text="Reset Password",command=resetpass,font=("times new roman",15,"bold"),fg="white",bg="blue")
                    btn.place(x=100,y=290)

        forgotpassbtn=Button(frame,text="Forgot Password",command=forgotpass,font=("times new roman",11,"bold"),bd=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgotpassbtn.place(x=7,y=382,width=140)

        #click login func

        

        root.mainloop()
    Login_Window()


addtable()
log()





    































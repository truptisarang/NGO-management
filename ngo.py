#importing libraries
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from PIL import Image,ImageTk
from tkcalendar import DateEntry
from tkinter import  ANCHOR, BOTH, BOTTOM, E, END, FLAT, HORIZONTAL, LEFT, RAISED, RIGHT, VERTICAL, Y, Button, Entry, PhotoImage, Scrollbar, ttk
from tkinter import scrolledtext
import pymysql
from tkinter import messagebox


#fonts
f='Cambria'
f1='Cambria 25 bold'
fa='Cambria 12 bold'

#function for switching between frames
def show_frame(frame):
    frame.tkraise()

#main window
window = tk.Tk()
window.state
window.title('NGO management')
window.iconbitmap('logo_circle.ico')
window.geometry('1366x768+0+0')


#defining frames
logo_frame=tk.Frame(window,bg='#262626')
frame1 = tk.Frame(window,bg='#262626')
frame2 = tk.Frame(window,bg='#262626')
vol_frame=tk.Frame(window,bg='#262626')
adm_login_frame = tk.Frame(frame2,bd=3,bg='#ffffff',relief=tk.RAISED)
adm_login_frame.place(x=360,y=200,width=650,height=300)
frame3=tk.Frame(window,bg='#262626')
frame_user=tk.Frame(window,bg='#262626')

#LOGO
open_logo=Image.open("logo_circle.png")
resized_logo=open_logo.resize((200,200))
logo=ImageTk.PhotoImage(resized_logo)
logo_label=tk.Label(logo_frame,bg='#262626',image=logo)
logo_label.place(x=550,y=240)


progress=ttk.Progressbar(logo_frame,orient=HORIZONTAL,length=500,mode='determinate')
progress.place(x=410,y=500)

#function for progressing the bar
i=0
def load():
    global i
    if i<=10:
        progress.after(200,load)
        progress['value']=10*i
        i+=1
    if progress['value']==100:
        show_frame(frame1)
load()
    

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

#placing the frames on the window
for frame in (frame1,frame2,frame3,frame_user,vol_frame,logo_frame):
    frame.grid(row=0,column=0,sticky='nsew')



#=================================================Frame 1 code=========================================================================================
ad=Image.open("admin.png")
ad1=ad.resize((100,100))
ad_img=ImageTk.PhotoImage(ad1)


us=Image.open("user.png")
us1=us.resize((100,100))
user_img=ImageTk.PhotoImage(us1)


admin_btn = tk.Button(frame1, text='Admin',command=lambda:show_frame(frame2),cursor='hand2',image=ad_img,bg='#262626',relief=FLAT,activebackground='#262626')
admin_btn.place(relx=0.4,rely=0.456,anchor=tk.CENTER)

ad_label=tk.Label(frame1,text='Admin',bg='#262626',fg='#fcba03',font='Cambria 16 bold')
ad_label.place(relx=0.368,rely=0.6)

ad_label=tk.Label(frame1,text='Volunteer',bg='#262626',fg='#fcba03',font='Cambria 16 bold')
ad_label.place(relx=0.565,rely=0.6)



#======================================================Frame 2 code========================================================


frame2_title=  tk.Label(frame2, text='Admin Login', font='Cambria 35',bg='#262626',fg='#fcba03')
frame2_title.place(relx=0.5,rely=0.1,anchor=tk.N)


show_frame(logo_frame)
#==========================================================Login====================================================================
 
email=tk.Label(adm_login_frame,text='Enter email-id',font=f,bg='#ffffff')
email.place(relx=0.1,rely=0.3)

password=tk.Label(adm_login_frame,text='Enter password',font=f,bg='#ffffff')
password.place(relx=0.1,rely=0.5)

E_entry= Entry(adm_login_frame,width=50,relief=tk.GROOVE,bd=3)
E_entry.place(x=190,y=90)
P_entry= Entry(adm_login_frame,width=50,relief=tk.GROOVE,bd=3,show='*')
P_entry.place(x=190,y=150)

def login():
    if E_entry.get()==""or P_entry.get()=="":
        messagebox.showerror('Oops!','Please enter username and password')
    else:
        try:
            #connecting application with database
            con=pymysql.connect(host="localhost",user="root",password="",database="ngo")
            cur=con.cursor()
            cur.execute("select * from adminlogin where email=%s and password=%s",(E_entry.get(),P_entry.get()))
            row=cur.fetchone()

            #checking whether entered username and password is in database or not 
            if row==None:
                messagebox.showerror('Error','Invalid Username & Password')
            else:
                show_frame(frame3)
                E_entry.delete(0,END)
                P_entry.delete(0,END)
        except Exception as e:
            messagebox.showerror('error',f"Error due to: {str(e)}")

login_btn = tk.Button(adm_login_frame, text='Login',command=login,relief=tk.RAISED,width=18,bg='#fcba03',fg='#262626',cursor='hand2')
login_btn.place(relx=0.5,rely=0.85,anchor=tk.S)


def back():
    show_frame(frame1)
    E_entry.delete(0,END)
    P_entry.delete(0,END)

    

img=Image.open("back button.png")
img1=img.resize((30,25))
back_img=ImageTk.PhotoImage(img1)


back_btn=Button(frame2,bg='#262626',activebackground='#262626',command=back,image=back_img,relief=FLAT)
back_btn.place(x=25,y=25)


#==============================================================================================================================
#==============================================================================================================================
#==================================================*Admin side panel*==============================================================================
#==============================================================================================================================
#==============================================================================================================================

def dashboard():
    dashframe=tk.Frame(frame3,bg='#262626',width=1066,height=800)
    dashframe.place(x=300,y=0)
    ld=tk.Label(dashframe,text='Dashboard',fg='#fcba03',bg='#262626')
    ld.config(font=f1)
    ld.place(x=485,y=15)

    vol_frame=tk.Frame(dashframe,bg='#fcba03',width=310,height=220)
    vol_frame.place(x=50,y=100)
    l_vol=tk.Label(vol_frame,text='No of volunteers',fg='#262626',bg='#fcba03',font=('Cambria 14 bold'))
    l_vol.place(x=10,y=0)

    vol_count=tk.Label(vol_frame,text="4",bg='#fcba03',fg='#262626',font=('Cambria 35'))
    vol_count.place(anchor=tk.CENTER,relx=0.5,rely=0.5)
     


def ARV():
    ARVframe=tk.Frame(frame3,bg='#262626',width=1066,height=800)
    ARVframe.place(x=300,y=0)
    lh=tk.Label(ARVframe,text='Add/remove Volunteer',fg='#fcba03',bg='#262626')
    lh.config(font=f1)
    lh.place(x=350,y=15)

    def add_vol():
        con=pymysql.connect(host="localhost",user="root",password="",database="ngo")
        cur=con.cursor()
        if (f_entry.get()=='' or l_entry.get()=='' or e_entry.get()=='' or bd_entry.get()=='' or Add_entry.get(1.0,END)=='' or combo.get()=='' or combo_bg.get()=='' or no_entry.get()==''):
            messagebox.showwarning('Error','All fields are required')
        else:
            try:
                q='insert into volunteer (fname,lname,email,birthdate,address,vol_field,blood_grp,phone) values (%s,%s,%s,%s,%s,%s,%s,%s)'
                cur.execute(q,(f_entry.get(),l_entry.get(),e_entry.get(),bd_entry.get(),Add_entry.get(1.0,END),combo.get(),combo_bg.get(),no_entry.get()))
                con.commit()
                messagebox.showinfo('Success!','Volunteer added successfully!')
          
            except Exception as e:
                messagebox.showerror('Error',f'Error due to: (str{e})')

        


    #ARV

    f_name=tk.Label(ARVframe,text='First name',font=fa,fg='#fcba03',bg='#262626')
    f_name.place(x=20,y=100)
    f_entry= Entry(ARVframe)
    f_entry.place(x=140,y=104,width=200)
    
    l_name=tk.Label(ARVframe,text='Last name',font=fa,fg='#fcba03',bg='#262626')
    l_name.place(x=20,y=140)
    l_entry=Entry(ARVframe)
    l_entry.place(x=140,y=144,width=200)
    
    em=tk.Label(ARVframe,text='Email-id',font=fa,fg='#fcba03',bg='#262626')
    em.place(x=20,y=180)
    e_entry=Entry(ARVframe)
    e_entry.place(x=140,y=184,width=200)

    bd=tk.Label(ARVframe,text='Birth date',font=fa,fg='#fcba03',bg='#262626')
    bd.place(x=20,y=220)
    bd_entry=DateEntry(ARVframe)
    bd_entry.place(x=140,y=224)

    no=tk.Label(ARVframe,text='Phone No.',font=fa,fg='#fcba03',bg='#262626')
    no.place(x=20,y=260)
    no_entry= Entry(ARVframe)
    no_entry.place(x=140,y=264,width=200)
    
    Address=tk.Label(ARVframe,text='Address',font=fa,fg='#fcba03',bg='#262626')
    Address.place(x=20,y=300)
    Add_entry=scrolledtext.ScrolledText(ARVframe,width=40,height=1)
    Add_entry.place(x=140,y=304)

    
    v_f=tk.Label(ARVframe,text='Volunteering field',font=fa,fg='#fcba03',bg='#262626')
    v_f.place(x=600,y=100)
    combo=ttk.Combobox(ARVframe)
    combo['values']=('Environment','Poverty elevation','Teaching','Management','Orphanages')
    combo.place(x=800,y=104)

    bg=tk.Label(ARVframe,text='Blood group',font=fa,fg='#fcba03',bg='#262626')
    bg.place(x=600,y=140)
    combo_bg=ttk.Combobox(ARVframe)
    combo_bg['values']=('A+','A-','B+','B-','O+','O-','AB+','AB-')
    combo_bg.place(x=800,y=144)

    add_bt=Button(ARVframe,text='Add Volunteer',command=add_vol,relief=tk.RAISED,width=18,bg='#fcba03',fg='#262626',cursor='hand2')
    add_bt.place(x=540,y=330)

    def remove():
        selected_item=table.selection()[0]       
        id=table.item(selected_item)['values'][0]              #this will give list as o/p and here we will take only the 'values'
        del_query="DELETE FROM volunteer where id=%s"
        sel_data=(id,)                            #returning the selected data
        response=messagebox.askyesno('Confirmation','Do you want to remove the volunteer?') 
        if  response==YES:
           cur.execute(del_query,sel_data)
           con.commit()                              #save the changes
           table.delete(selected_item)
           messagebox.showinfo('Deleted!','Volunteer removed!!')
    
   
        
    remove_bt=Button(ARVframe,text='Remove Volunteer',command=remove,relief=tk.RAISED,width=18,bg='#fcba03',fg='#262626',cursor='hand2')
    remove_bt.place(x=690,y=330)

    def clear():
        #clear entry boxes
        f_entry.delete(0,END),
        l_entry.delete(0,END),
        e_entry.delete(0,END),
        bd_entry.delete(0,END),
        no_entry.delete(0,END),
        Add_entry.delete(1.0,END),
        combo.delete(0,END),
        combo_bg.delete(0,END)

    clear_bt=Button(ARVframe,text='Clear',relief=tk.RAISED,command=clear,width=18,bg='#fcba03',fg='#262626',cursor='hand2')
    clear_bt.place(x=840,y=330)
     
    table=ttk.Treeview(ARVframe)
    table.place(x=0,y=400,width=1100,height=500)
    s=ttk.Style(ARVframe)
    s.theme_use('alt')
   
    col=['1','2','3','4','5','6','7','8','9']       #defining columns
    table.config(
    columns=col)
    table['show']='headings'
    
    #headings of the column
  
    table.heading("1",text='V-Id',anchor=tk.W)
    table.heading("2",text='Email-id',anchor=tk.W)
    table.heading("3",text='First name',anchor=tk.W)
    table.heading("4",text='Last name',anchor=tk.W)
    table.heading("5",text='Birth date',anchor=tk.W)
    table.heading("6",text='Phone no.',anchor=tk.W)
    table.heading("7",text='Address',anchor=tk.W)
    table.heading("8",text='Volunteering field',anchor=tk.W)
    table.heading("9",text='Blood group',anchor=tk.W)
    
  
    
    #formatting the columns
    
    table.column('1',minwidth=100,width=150)
    table.column('2',minwidth=150,width=150)
    table.column('3',minwidth=100,width=150)
    table.column('4',minwidth=100,width=150)
    table.column('5',minwidth=100,width=150)
    table.column('6',minwidth=100,width=150)
    table.column('7',minwidth=100,width=150)
    table.column('8',minwidth=100,width=150)
    table.column('9',minwidth=100,width=150)
   
    con=pymysql.connect(host="localhost",user="root",password="",database="ngo")
    cur=con.cursor()
    cur.execute("SELECT * FROM volunteer")
    i=0
    for ro in cur:
        table.insert('',i,text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6],ro[7],ro[8]))
        i=i+1

def task():
    task_frame=tk.Frame(frame3,bg='#262626',width=1066,height=800)
    task_frame.place(x=300,y=0)
    lh=tk.Label(task_frame,text='Assign Task',fg='#fcba03',bg='#262626')
    lh.config(font=f1)
    lh.place(x=450,y=15)

    act_name=tk.Label(task_frame,text='Activity Name',font=fa,fg='#fcba03',bg='#262626')
    act_name.place(x=20,y=100)
    act_entry=Entry(task_frame)
    act_entry.place(x=180,y=104,width=200)

    location=tk.Label(task_frame,text='Location',font=fa,fg='#fcba03',bg='#262626')
    location.place(x=20,y=140)
    loc_entry=Entry(task_frame)
    loc_entry.place(x=180,y=144,width=200)

    act_date=tk.Label(task_frame,text='Date',font=fa,fg='#fcba03',bg='#262626')
    act_date.place(x=20,y=180)
    date_entry=DateEntry(task_frame)
    date_entry.place(x=180,y=184)

    time=tk.Label(task_frame,text='Time',font=fa,fg='#fcba03',bg='#262626')
    time.place(x=20,y=220)
    Time_entry=Entry(task_frame)
    Time_entry.place(x=180,y=224)
   
     
    assign=tk.Label(task_frame,text='Activity assigned to',font=fa,fg='#fcba03',bg='#262626')
    assign.place(x=20,y=260)
    assign_entry=Entry(task_frame)
    assign_entry.place(x=180,y=264)

    def assign_t():
        con=pymysql.connect(host="localhost",user="root",password="",database="ngo")
        cur=con.cursor()
        if (act_entry.get()=='' or loc_entry.get()=='' or date_entry.get()=='' or Time_entry.get()=='' or assign_entry.get()==''):
            messagebox.showwarning('Error','All fields are required')
        else:
            try:
                q='insert into assign_task (act_name,loc,date,time,assigned_to) values (%s,%s,%s,%s,%s)'
                cur.execute(q,(act_entry.get(),loc_entry.get(),date_entry.get(),Time_entry.get(),assign_entry.get()))
                con.commit()
                messagebox.showinfo('Success!','Task assigned !!!')
                act_entry.delete(0,END),loc_entry.delete(0,END),date_entry.delete(0,END),Time_entry.delete(0,END),assign_entry.delete(0,END)

            
            except Exception as e:
                messagebox.showerror('Error',f'Error due to: (str{e})')

           
    assign_bt=Button(task_frame,text='Assign task',command=assign_t,relief=tk.RAISED,width=18,bg='#fcba03',fg='#262626',cursor='hand2')
    assign_bt.place(x=610,y=264)
    
    def remove_task():
        selected_item=table1.selection()[0]       
        activity_sel=table1.item(selected_item)['values'][0]                  #this will give list as o/p and here we will take only the 'values'
        del_act_query="DELETE FROM assign_task where act_name=%s"
        sel_task=(activity_sel,)                                   #returning or storing the selected data in variable     
        res_task=messagebox.askyesno('Confirmation','Do you want to discard the task?')        
        if res_task==YES:
            cur.execute(del_act_query,sel_task)
            con.commit()                                                              #save the changes
            table1.delete(selected_item)
            messagebox.showinfo('Deleted!','Task discarded!!')

    remove_task_bt=Button(task_frame,text='Discard Task',command=remove_task,relief=tk.RAISED,width=18,bg='#fcba03',fg='#262626',cursor='hand2')
    remove_task_bt.place(x=810,y=264)


# Assign task table
    table1=ttk.Treeview(task_frame)
    table1.place(x=0,y=300,width=1200,height=500)
    table1['show']='headings'
    columns=['1','2','3','4','5']
    table1.config(
    columns=columns)
    s=ttk.Style(task_frame)
    s.theme_use('alt')
    
    table1.heading("1",text='Activity Name',anchor=tk.W)
    table1.heading("2",text='Location',anchor=tk.W)
    table1.heading("3",text='Date',anchor=tk.W)
    table1.heading("4",text='Time',anchor=tk.W)
    table1.heading("5",text='Assigned to',anchor=tk.W)

    table1.column('1',minwidth=100,width=150)
    table1.column('2',minwidth=150,width=150)
    table1.column('3',minwidth=100,width=150)
    table1.column('4',minwidth=100,width=150)
    table1.column('5',minwidth=100,width=150)

    con=pymysql.connect(host="localhost",user="root",password="",database="ngo")
    cur=con.cursor()
    cur.execute("SELECT * FROM assign_task")
    i=0
    for j in cur:
        table1.insert('',i,text="",values=(j[0],j[1],j[2],j[3],j[4]))
        i=i+1
 








def payment():
    pay_frame=tk.Frame(frame3,bg='#262626',width=1066,height=800)
    pay_frame.place(x=300,y=0)
    lh=tk.Label(pay_frame,text='Payment handling',fg='#fcba03',bg='#262626')
    lh.config(font=f1)
    lh.place(x=350,y=15)

    
def donor():
    donor_frame=tk.Frame(frame3,bg='#262626',width=1066,height=800)
    donor_frame.place(x=300,y=0)
    lh=tk.Label(donor_frame,text="Donors",fg='#fcba03',bg='#262626')
    lh.config(font=f1)
    lh.place(x=500,y=15)


def companies():
    dc_frame=tk.Frame(frame3,bg='#262626',width=1066,height=800)
    dc_frame.place(x=300,y=0)
    lh=tk.Label(dc_frame,text='Donor companies',fg='#fcba03',bg='#262626')
    lh.config(font=f1)
    lh.place(x=400,y=15)


def app():
    app_frame=tk.Frame(frame3,bg='#262626',width=1066,height=800)
    app_frame.place(x=300,y=0)
    lh=tk.Label(app_frame,text='Applications',fg='#fcba03',bg='#262626')
    lh.config(font=f1)
    lh.place(x=400,y=15)

def logout():
    res_log=messagebox.askyesno('Logout','Are you sure do you want to logout?')
    if res_log==YES:
       show_frame((frame2))

toggle_frame=tk.Frame(frame3,width=300,height=800,bg='#fcba03')
toggle_frame.place(x=0,y=0)
    

dashboard()
#side panel buttons
def bttn(x,y,text,bcolor,fcolor,cmd):
        def on_entera(e):
            myButton1['background'] = bcolor 
            myButton1['foreground']= '#262626'  

        def on_leavea(e):
            myButton1['background'] = fcolor
            myButton1['foreground']= '#262626'

        myButton1 = tk.Button(frame3,text=text,
                       width=42,
                       height=2,
                       fg='#262626',
                       border=0,
                       bg=fcolor,
                       activeforeground='#262626',
                       activebackground=bcolor,            
                        command=cmd)
                      
        myButton1.bind("<Enter>", on_entera)
        myButton1.bind("<Leave>", on_leavea)

        myButton1.place(x=x,y=y)

bttn(0,250,'Dashboard','#c2bcac','#fcba03',dashboard)
bttn(0,289,'Add / Remove Volunteer','#c2bcac','#fcba03',ARV)
bttn(0,328,'Assign Task','#c2bcac','#fcba03',task)
bttn(0,367,'Payment handling','#c2bcac','#fcba03',payment)  
bttn(0,406,'Donors','#c2bcac','#fcba03',donor)  
bttn(0,445,'Donor Companies','#c2bcac','#fcba03',companies)  
bttn(0,484,'Applications','#c2bcac','#fcba03',app)  
bttn(0,523,'Logout','#c2bcac','#fcba03',logout)

#admin photo 
admin_img=Image.open("Admin bg.png")
resized_img=admin_img.resize((150,150))
admin_img=ImageTk.PhotoImage(resized_img)
admin_lb=tk.Label(toggle_frame,bg='#fcba03',bd=20,image=admin_img)
admin_lb.place(x=0,y=0,width=300,height=200)

#========================================================================================================================
#===============================================*Volunteer Panel*===================================================================
#========================================================================================================================
#========================================================================================================================

side_panel_frame=tk.Frame(frame_user,width=300,height=800,bg='#fcba03')
side_panel_frame.place(x=0,y=0)

vol_img=Image.open("Admin bg.png")
resized_img=vol_img.resize((150,150))
vol_img=ImageTk.PhotoImage(resized_img)
admin_lb=tk.Label(side_panel_frame,bg='#fcba03',bd=20,image=vol_img)
admin_lb.place(x=0,y=0,width=300,height=200)



vol_btn = tk.Button(frame1, text='Volunteer',command=lambda:show_frame(vol_frame),cursor='hand2',image=user_img,bg='#262626',relief=FLAT,activebackground='#262626')
vol_btn.place(relx=0.6,rely=0.456,anchor=tk.CENTER)

def back_btn_func():
    show_frame(frame1)
    em_entry.delete(0,END)
    pass_entry.delete(0,END) 

back_btn=Button(vol_frame,bg='#262626',activebackground='#262626',command=back_btn_func,image=back_img,relief=FLAT)
back_btn.place(x=25,y=25)

vol_login_frame = tk.Frame(vol_frame,bd=3,bg='#ffffff',relief=tk.RAISED)
vol_login_frame.place(x=360,y=200,width=650,height=300)

vol_frame_title=  tk.Label(vol_frame, text='Volunteer Login', font='Cambria 35',bg='#262626',fg='#fcba03')
vol_frame_title.place(relx=0.5,rely=0.1,anchor=tk.N)


em=tk.Label(vol_login_frame,text='Enter email-id',font=f,bg='#ffffff')
em.place(relx=0.1,rely=0.3)

passw=tk.Label(vol_login_frame,text='Enter password',font=f,bg='#ffffff')
passw.place(relx=0.1,rely=0.5)

em_entry= Entry(vol_login_frame,width=50,relief=tk.GROOVE,bd=3)
em_entry.place(x=190,y=90)
pass_entry= Entry(vol_login_frame,width=50,relief=tk.GROOVE,bd=3,show='*')
pass_entry.place(x=190,y=150)


def vol_login():
    if em_entry.get() =="" or pass_entry.get() =="":
        messagebox.showerror('Oops!','Please enter username and password')
    else:
        try:
            #connecting application with database
            con=pymysql.connect(host="localhost",user="root",password="",database="ngo")
            cur=con.cursor()
            cur.execute("select * from volunteer where email=%s and password=%s",(em_entry.get(),pass_entry.get()))
            row1=cur.fetchone()

            #checking whether entered username and password is in database or not 
            if row1==None:
                messagebox.showerror('Error','Invalid Username & Password')
            else:
                show_frame(frame_user)
                em_entry.delete(0,END)
                pass_entry.delete(0,END)
        except Exception as e:
            messagebox.showerror('error',f"Error due to: {str(e)}")


login_btn = tk.Button(vol_login_frame, text='Login',command=vol_login,relief=tk.RAISED,width=18,bg='#fcba03',fg='#262626',cursor='hand2')
login_btn.place(relx=0.5,rely=0.85,anchor=tk.S)

def vol_dashboard():
    dash_v_frame=tk.Frame(frame_user,bg='#262626',width=1066,height=800)
    dash_v_frame.place(x=300,y=0)
    l=tk.Label(dash_v_frame,text='Dashboard',fg='#fcba03',bg='#262626')
    l.config(font=f1)
    l.place(x=485,y=15)

    vol_count_frame=tk.Frame(dash_v_frame,bg='#fcba03',width=310,height=220)
    vol_count_frame.place(x=50,y=100)
    l_vol_count=tk.Label(vol_count_frame,text='No of volunteers',fg='#262626',bg='#fcba03',font=('Cambria 14 bold'))
    l_vol_count.place(x=10,y=0)

    vol_count=tk.Label(vol_count_frame,text="4",bg='#fcba03',fg='#262626',font=('Cambria 35'))
    vol_count.place(anchor=tk.CENTER,relx=0.5,rely=0.5)
       

def activities():
    actframe=tk.Frame(frame_user,bg='#262626',width=1066,height=800)
    actframe.place(x=300,y=0)
    actl=tk.Label(actframe,text='Activities',fg='#fcba03',bg='#262626')
    actl.config(font=f1)
    actl.place(x=470,y=15)

    table3=ttk.Treeview(actframe)
    table3.place(x=0,y=100,width=1200,height=900)
    table3['show']='headings'
    col=['1','2','3','4','5','6']
    s=ttk.Style(actframe)
    s.theme_use('alt')
    table3.config(
    columns=col)
    
    table3.heading("1",text='Activity Name',anchor=tk.W)
    table3.heading("2",text='Location',anchor=tk.W)
    table3.heading("3",text='Date',anchor=tk.W)
    table3.heading("4",text='Time',anchor=tk.W)
    table3.heading("5",text='Assigned to',anchor=tk.W)
    
    table3.column('1',minwidth=140,width=140)
    table3.column('2',minwidth=140,width=140)
    table3.column('3',minwidth=140,width=140)
    table3.column('4',minwidth=140,width=140)
    table3.column('5',minwidth=140,width=140)
  
    con=pymysql.connect(host="localhost",user="root",password="",database="ngo")
    cur=con.cursor()
    cur.execute("SELECT * FROM assign_task")
    i=0
    for j in cur:
        table3.insert('',i,text="",values=(j[0],j[1],j[2],j[3],j[4]))
        i=i+1

def bttn(x,y,text,bcolor,fcolor,cmd):
        def on_entera(e):
            myButton1['background'] = bcolor #ffcc66
            myButton1['foreground']= '#262626'  #000d33

        def on_leavea(e):
            myButton1['background'] = fcolor
            myButton1['foreground']= '#262626'

        myButton1 = tk.Button(frame_user,text=text,
                       width=42,
                       height=2,
                       fg='#262626',
                       border=0,
                       bg=fcolor,
                       activeforeground='#262626',
                       activebackground=bcolor,            
                        command=cmd)
                      
        myButton1.bind("<Enter>", on_entera)
        myButton1.bind("<Leave>", on_leavea)

        myButton1.place(x=x,y=y)

def vol_logout():
    res_log=messagebox.askyesno('Logout','Are you sure do you want to logout?')
    if res_log==YES:
       show_frame(vol_frame)

bttn(0,250,'Dashboard','#c2bcac','#fcba03',vol_dashboard)
bttn(0,289,'Activities','#c2bcac','#fcba03',activities)
bttn(0,328,'Logout','#c2bcac','#fcba03',vol_logout)

vol_dashboard()
window.mainloop()

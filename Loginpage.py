from PIL import Image, ImageTk

import Homepage

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

from tkinter import messagebox
from database_details import *
from company_details import *

import pymysql

class Toplevel1:
    flag=0
    hid_flag2 = True
    def __init__(self):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font9 = "-family {Courier New} -size 13"


        self.top=tk.Tk()




        #image should be declared after creating window otherwise errror
        self.img2 = tk.PhotoImage(file="myimages//eye.png")
        self.img3 = tk.PhotoImage(file="myimages//hide.png")
        self.top.geometry("556x380+446+160")
        # self.top.resizable(1, 1)
        self.top.resizable(width=False, height=False)
        self.top.title(company+"/Login Page")
        self.top.configure(background="#d9d9d9")
        self.top.configure(highlightbackground="#d9d9d9")
        self.top.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.imga = Image.open('myimages//grey-background.jpg')
        self.imga = self.imga.resize((556,380))
        self.img2a = ImageTk.PhotoImage(self.imga)


        self.baklbl = tk.Label(self.Frame1, image=self.img2a)
        self.baklbl.place(x=0, y=0)

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.237, rely=0.062, height=39, width=368)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Adobe Hebrew} -size 22 -weight normal -slant roman -underline 0 -overstrike 0")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Login''')

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.159, rely=0.241, height=33, width=229)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Segoe UI} -size 13 -weight normal -slant roman -underline 0 -overstrike 0")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''User Name''')

        self.Label2_1 = tk.Label(self.Frame1)
        self.Label2_1.place(relx=0.159, rely=0.345, height=33, width=229)
        self.Label2_1.configure(activebackground="#f9f9f9")
        self.Label2_1.configure(activeforeground="black")
        self.Label2_1.configure(anchor='w')
        self.Label2_1.configure(background="#d9d9d9")
        self.Label2_1.configure(disabledforeground="#a3a3a3")
        self.Label2_1.configure(font="-family {Segoe UI} -size 13 -weight normal -slant roman -underline 0 -overstrike 0")
        self.Label2_1.configure(foreground="#000000")
        self.Label2_1.configure(highlightbackground="#d9d9d9")
        self.Label2_1.configure(highlightcolor="black")
        self.Label2_1.configure(text='''Password''')



        self.t1 = tk.Entry(self.Frame1)
        self.t1.place(relx=0.476, rely=0.241,height=34, relwidth=0.323)
        self.t1.configure(background="white")
        self.t1.configure(disabledforeground="#a3a3a3")
        self.t1.configure(font=font9)
        self.t1.configure(foreground="#000000")
        self.t1.configure(highlightbackground="#d9d9d9")
        self.t1.configure(highlightcolor="black")
        self.t1.configure(insertbackground="black")
        self.t1.configure(selectbackground="#c4c4c4")
        self.t1.configure(selectforeground="black")

        self.t2 = tk.Entry(self.Frame1)
        self.t2.place(relx=0.476, rely=0.345,height=34, relwidth=0.323)
        self.t2.configure(background="white")
        self.t2.configure(disabledforeground="#a3a3a3")
        self.t2.configure(font="TkFixedFont")
        self.t2.configure(font=font9)
        self.t2.configure(foreground="#000000")
        self.t2.configure(highlightbackground="#d9d9d9")
        self.t2.configure(highlightcolor="black")
        self.t2.configure(insertbackground="black")
        self.t2.configure(selectbackground="#c4c4c4")
        self.t2.configure(selectforeground="black")
        self.t2.configure(show="*")
        self.t2.bind("<Return>", self.move_to_next_widget)


        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.344, rely=0.555, height=53, width=176)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Segoe UI} -size 13 -weight normal -slant roman -underline 0 -overstrike 0")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(overrelief="sunken")
        self.Button1.configure(pady="0")
        #self.Button1.configure(text='''Sign In''',command=self.checkdata)
        self.Button1.bind("<Return>", self.checkdata)



        self.hidbtn2 = tk.Button(self.Frame1)
        self.hidbtn2.place(relx=0.807, rely=0.345, height=33, width=46)
        self.hidbtn2.configure(activebackground="#ececec")
        self.hidbtn2.configure(activeforeground="#000000")
        self.hidbtn2.configure(background="#d9d9d9")
        self.hidbtn2.configure(disabledforeground="#a3a3a3")
        self.hidbtn2.configure(font="-family {Segoe UI} -size 13 -weight normal -slant roman -underline 0 -overstrike 0")
        self.hidbtn2.configure(foreground="#000000")
        self.hidbtn2.configure(highlightbackground="#d9d9d9")
        self.hidbtn2.configure(highlightcolor="black")
        self.hidbtn2.configure(overrelief="sunken")
        self.hidbtn2.configure(pady="0", command=self.chge_hide2,image=self.img2)
        self.top.mainloop()

    def move_to_next_widget(event):
        event.widget.tk_focusNext().focus_set()



    def chge_hide2(self):
        if self.hid_flag2==True:
            self.t2.config(show="")
            self.hid_flag2=False
            self.hidbtn2.config(image=self.img3)
        elif self.hid_flag2==False:
            self.t2.config(show="*")
            self.hid_flag2=True
            self.hidbtn2.config(image=self.img2)


    def database_connection(self):
        if (self.flag == 0):
            try:
                self.conn = pymysql.connect(host="127.0.0.1",
                        database="stock_database",
                        user="root",
                        password="1234"
                        )
                self.flag = 1
            except Exception as e:
                messagebox.showerror("Error", "Database Connection Error \n" + str(e), parent=self.top)

    def checkdata(self):
        self.database_connection()
        try:
            dc = self.conn.cursor()
            dc.execute("select type from usertable where username =%s and password=%s",
                       (self.t1.get(),self.t2.get()))

            x=dc.fetchone()
            if x:
                print(x)
                for i in x:
                    name=self.t1.get()
                    self.top.destroy()
                    Homepage.Toplevel1(i,name)
            else:
                messagebox.showwarning("Login Error","Wrong Username Or Password",parent=self.top)

        except:
            messagebox.showerror("error ", "error in query",parent=self.top)






if __name__ == '__main__':
    Toplevel1()






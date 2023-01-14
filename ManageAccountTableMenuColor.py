from PIL import Image, ImageTk
# import Pillow
import Loginpage
import os
import sys
from time import time
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import tkinter as tk
from tkinter import ttk, messagebox
import tkinter.ttk as ttk
import labels as labels

# Create the main window
import mysql.connector

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


class Toplevel1:
    flag = 0
    actual_name = 'default_user.png'

    def __init__(self, root):
        self.conn = mysql.connector.connect(user='root', password='1234',
                                            host='localhost',
                                            database='Accounts', port='3306', autocommit=True)
        self.cursor = self.conn.cursor()
        # self.conn = None
        # self.fetch_flag = 1
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        # _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = 'blue'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        self.style = ttk.Style()

        self.top = root
        # self.top.geometry("1500x1200+20+20")
        self.top.configure(bg="black")

        self.top.state('zoomed')  # Make the window full screen
        top_frame = tk.Frame(root, bg="black", height=40, padx=5, pady=10)

        top_frame.pack(side="top", fill="x")

        #self.title_label.pack()
        self.frame1 = tk.Frame(root)
        self.frame1.bind('<Return>', self.move_to_next_widget)
        self.frame1.pack(fill=tk.BOTH, expand=1)
        self.frame1.pack_propagate(False)
        self.frame1.pack()
        root.geometry("1920x1080+150+50")
        # self.top.geometry("1500x1200")
        self.top.resizable(0, 0)
        # self.top.configure(background="#d9d9d9")
        self.top.configure(highlightbackground="#d9d9d9")
        self.top.configure(highlightcolor="black")


        # Create the widgets
        self.label1 = []
        self.lineedit1 = []
        self.label2 = []
        self.lineedit2 = []
        self.pushbutton1 = []
        self.lineedit_search = tk.Entry(self.frame1, font="-family {Adobe Hebrew} -size 13", width=15, highlightthickness=3, highlightbackground="black")
        self.lineedit_search.grid(row=0, column=4, columnspan=4, sticky="nsew", padx=5, pady=5)
        self.lineedit_search.bind('<Return>', self.search_data2)

        import subprocess

        def open_file_a1():
            subprocess.run(["python", "path/to/file_a1.py"])

        def open_file_b():
            subprocess.run(["python", "path/to/file_b.py"])

        for i in range(9):
            labelbox = tk.Label(self.frame1)
            labelbox.grid(row=i + 2, column=2, sticky="nsew", padx=5, pady=4)
            labelbox.configure(font="-family {Adobe Hebrew} -size 13")
            self.label1.append(labelbox)
        self.Label_search = tk.Label(self.frame1, font="-family {Adobe Hebrew} -size 13")
        # self.Label_search.append(labelbox)
        self.Label_search.grid(row=0, column=2, sticky="nsew", padx=5, pady=4)
        self.title_label1 = tk.Label(top_frame, text="MANAGE ACCOUNTS", fg="white", bg="#20bebe",  width=100,
                                     font=('Curlz MT', 20, 'bold'), highlightthickness=1, highlightbackground="black")
        self.title_label1.grid(row=0, column=0, sticky="nsew", padx=5, pady=0)

        self.comboboxAc1 = ttk.Combobox(self.frame1, state='readonly', width=50,
                                        font="-family {Adobe Hebrew} -size 13")
        self.comboboxAc1.grid(row=2, column=4, sticky="nsew", padx=5, pady=5)

        for i in range(8):
            lineedit = tk.Entry(self.frame1, width=50, font="-family {Adobe Hebrew} -size 13")
            lineedit.grid(row=i + 3, column=4, sticky="nsew", padx=5, pady=7, )

            self.lineedit1.append(lineedit)
        self.lineedit1[7].configure(state='readonly')

        # Create the label widgets and add them to frame3
        for i in range(13):
            label = tk.Label(self.frame1, text="Label {}".format(i + 1))
            label.grid(row=i + 2, column=5, sticky="nsew", padx=5, pady=4)
            label.configure(font="-family {Adobe Hebrew} -size 13")
            self.label2.append(label)

        # Create the tlineedit widgets and add them to frame4
        for i in range(7):
            lineedit = tk.Entry(self.frame1, font="-family {Adobe Hebrew} -size 13")
            lineedit.grid(row=i + 2, column=6, sticky="nsew", padx=5, pady=7)
            self.lineedit2.append(lineedit)

        self.combobox2 = []
        for i in range(3):
            combobox = ttk.Combobox(self.frame1, width=30, font="-family {Adobe Hebrew} -size 13", state='readonly')
            combobox.grid(row=i + 9, column=6, sticky="nsew", padx=5, pady=7)
            self.combobox2.append(combobox)

        for i in range(7, 9):
            lineedit = tk.Entry(self.frame1, width=30, font="-family {Adobe Hebrew} -size 13")
            self.lineedit2.append(lineedit)

        self.lineedit2[7].grid(row=12, column=6, sticky="nsew", padx=5, pady=5)
        self.lineedit2[8].grid(row=13, column=6, sticky="nsew", padx=5, pady=5)

        self.text1 = tk.Text(self.frame1, height=5, width=10, wrap=tk.WORD, font="-family {Adobe Hebrew} -size 13")
        self.text1.grid(row=14, column=6, sticky="nsew", padx=5, pady=7)

        # Create the pushbuttons and add them to frame5
        self.pushbutton1 = []
        # self.inner_frame = tk.Frame(self.frame1, bg='black', padx=2, pady=2)
        # self.inner_frame.grid(row=12, column=4)

        for i in range(4):
            pushbutton = tk.Button(self.frame1, text="Pushbutton {}".format(i + 1),
                                   font=('Adobe Hebrew', 13, 'bold'), width=20, bg='#20bebe', fg='white')
            self.pushbutton1.append(pushbutton)
        self.pushbutton1[0].grid(row=i + 9, column=4, padx=5, pady=5)
        self.pushbutton1[1].grid(row=i + 10, column=4, padx=5, pady=5)
        self.pushbutton1[2].grid(row=i + 11, column=4)
        self.pushbutton1[3].grid(row=i + 12, column=4, padx=5, pady=5)


        # self.pushbutton1[0].grid(row=0, column=0)
        # self.pushbutton1[1].grid(row=0, column=1)
        # self.pushbutton1[2].grid(row=1, column=0)
        # self.pushbutton1[3].grid(row=1, column=1)

        self.lineedit2.append(lineedit)
        self.pushbutton1[0].config(text="Save")
        self.pushbutton1[1].config(text="Cancel")
        self.pushbutton1[2].config(text="Delete")
        self.pushbutton1[3].config(text="Update")

        self.pushbutton1[0].configure(command=self.save_data)
        self.pushbutton1[1].configure(command=self.reset_page)
        self.pushbutton1[2].configure(command=self.deletedata)
        self.pushbutton1[3].configure(command=self.update_data)

        self.label1[0].config(text="Account Type", anchor=tk.W)
        self.label1[1].config(text="Account Name", anchor=tk.W)
        self.label1[2].config(text="Address Line 1", anchor=tk.W)
        self.label1[3].config(text="Address Line 2", anchor=tk.W)
        self.label1[4].config(text="Address Line 3", anchor=tk.W)
        self.label1[5].config(text="Post Code", anchor=tk.W)
        self.label1[6].config(text="Contact Name", anchor=tk.W)
        self.label1[7].config(text="Discount %", anchor=tk.W)
        self.label1[8].config(text="A/C Code", anchor=tk.W)
        self.label2[0].config(text="Phone 1", anchor=tk.W)
        self.label2[1].config(text="Phone 2", anchor=tk.W)
        self.label2[2].config(text="Fax", anchor=tk.W)
        self.label2[3].config(text="Email Address", anchor=tk.W)
        self.label2[4].config(text="Fuel Charge", anchor=tk.W)
        self.label2[5].config(text="Payment Terms", anchor=tk.W)
        self.label2[6].config(text="Vet Reg No", anchor=tk.W)
        self.label2[7].config(text="Default Nominal Ac", anchor=tk.W)
        self.label2[8].config(text="Price Code", anchor=tk.W)
        self.label2[9].config(text="Account Type", anchor=tk.W)
        self.label2[10].config(text="Round No", anchor=tk.W)
        self.label2[11].config(text="Drop No", anchor=tk.W)
        self.label2[12].config(text="Notes", anchor=tk.W)
        self.Label_search.config(text="Search", anchor=tk.W)

        self.comboboxAc1.bind('<Return>', self.move_to_next_widget)
        self.lineedit1[0].bind('<Return>', self.move_to_next_widget)
        self.lineedit1[0].bind('<Return>', self.move_to_next_widget)

        self.lineedit1[1].bind('<Return>', self.move_to_next_widget)
        self.lineedit1[1].config(validate='key', validatecommand=(root.register(self.on_submitName)))
        self.lineedit1[2].bind('<Return>', self.move_to_next_widget)
        self.lineedit1[3].bind('<Return>', self.move_to_next_widget)
        self.lineedit1[4].bind('<Return>', self.move_to_next_widget)
        self.lineedit1[5].bind('<Return>', self.move_to_next_widget)
        self.lineedit1[6].bind('<Return>', self.move_to_next_widget)
        self.lineedit1[7].bind('<Return>', self.move_to_next_widget)
        self.lineedit2[0].bind('<Return>', self.move_to_next_widget)
        self.lineedit2[1].bind('<Return>', self.move_to_next_widget)
        self.lineedit2[2].bind('<Return>', self.move_to_next_widget)
        self.lineedit2[3].bind('<Return>', self.move_to_next_widget)
        self.lineedit2[4].bind('<Return>', self.move_to_next_widget)
        self.lineedit2[5].bind('<Return>', self.move_to_next_widget)
        self.lineedit2[6].bind('<Return>', self.move_to_next_widget)
        self.combobox2[0].bind('<Return>', self.move_to_next_widget)
        self.combobox2[1].bind('<Return>', self.move_to_next_widget)
        self.combobox2[2].bind('<Return>', self.move_to_next_widget)
        self.lineedit2[7].bind('<Return>', self.move_to_next_widget)
        self.lineedit2[8].bind('<Return>', self.move_to_next_widget)

        # self.comboboxAc1['values']=("Sales Account", "Purchase Account", "Nominal Account")

        self.combobox2[0]['values'] = (
            "None", "Accountancy Charges", "Advertising", "B/F Balances", "Blank Charges", "Bank Interest",
            "Business Transfer Charges")
        self.combobox2[1]['values'] = ("A", "B", "C", "D", "E")
        self.combobox2[2]['values'] = (
            "Daily", "Weekly", "Advertising", "B/F Balances", "Blank Charges", "Bank Interest",
            "Business Transfer Charges")
        # self.comboboxAc1.SelectedIndex = 1;
        self.comboboxAc1.set("Sales Account")

        self.comboboxAc1['values'] = ("Sales Account", "Purchase Account", "Nominal Account")
        self.comboboxAc1.bind("<<ComboboxSelected>>", self.on_selection_change)

        self.combobox2[0].set("None")
        self.combobox2[1].set("A")
        self.combobox2[2].set("Daily")

        self.table = ttk.Treeview(self.frame1, height=3, columns=('a', 'b'))
        self.table.heading("#0", text="Item")
        self.table.heading("#1", text="AccountID")
        self.table.heading("#2", text="Name")
        self.table['show'] = 'headings'
        self.table.column('#1', stretch=tk.NO, width=100)
        self.table.column('#2', stretch=tk.NO, width=200)
        self.table.grid(row=1, column=4, columnspan=4, sticky="nsew", padx=5, pady=5)
        self.table.bind("<Double-Button-1>", lambda e: self.get_rowdata())

        ysb = ttk.Scrollbar(root, orient='vertical', command=self.table.yview)
        self.table.configure(yscroll=ysb.set)
        # ysb.grid(row=0, column=6, sticky='ns')

        self.reset_page()

        self.myMenuButton = tk.Menu(root, tearoff=False)

        self.myMenuButton.add_command(label="Amend Account", command=self.toggle_visibility, font=("Helvetica", 14))
        root.config(menu=self.myMenuButton)
        # self.myMenuButton.entryconfig(0, font=("Helvetica", 14))

        self.pushbutton1[3].grid_remove()
        self.pushbutton1[2].grid_remove()
        self.lineedit_search.grid_remove()
        self.table.grid_remove()
        self.Label_search.grid_remove()

    def toggle_visibility(self):
        while True:
            if self.pushbutton1[0].winfo_ismapped():
                self.pushbutton1[0].grid_remove()
                self.pushbutton1[3].grid(row=11, column= 4)
                self.pushbutton1[2].grid()
                self.lineedit_search.grid()
                self.table.grid()
                self.Label_search.grid()
                self.myMenuButton.entryconfig(0, label="Add Account")
                break
            elif self.pushbutton1[0].winfo_ismapped()==False :
                self.pushbutton1[0].grid()
                self.pushbutton1[3].grid_remove()
                self.pushbutton1[2].grid_remove()

                self.lineedit_search.grid_remove()
                self.table.grid_remove()
                self.Label_search.grid_remove()
                self.myMenuButton.entryconfig(0, label="Amend Account")
                break
            else:
                print('test')

    def get_rowdata(self):
        rowid = self.table.focus()
        row = self.table.item(rowid)
        data = row['values']

        self.reset_page()

        v = data[0]

        try:

            sql = 'select TYA,NM,A1,A2,A3,A4,CN,TEL1,TEL2,FAX,CRL,AC,VAT,EMAIL,NOTES,VATRATE,' \
                  'NAC,PAYT,PCODE,ACTYPE,ROUNDNO,DROPNO  from names1 where AC like %s'

            self.cursor.execute(sql, (v,))
            self.data = self.cursor.fetchone()
            print(self.data)
            # self.comboboxAc1.current(self.data[0] - 1)
            val = self.data[0] - 1
            if val == 0:
                self.comboboxAc1.set('Sales Account')
            elif val == 1:
                self.comboboxAc1.set('Purchase Account')
            elif val == 2:
                self.comboboxAc1.set('Nominal Account')
            else:
                self.comboboxAc1.set('')

            self.lineedit1[0].insert(0, self.data[1])
            self.lineedit1[1].insert(0, self.data[2])
            self.lineedit1[2].insert(0, self.data[3])
            self.lineedit1[3].insert(0, self.data[4])
            self.lineedit1[4].insert(0, self.data[5])
            self.lineedit1[5].insert(0, self.data[6])
            self.lineedit1[6].insert(0, self.data[15])
            self.lineedit1[7].insert(0, self.data[11])
            self.lineedit2[0].insert(0, self.data[7])
            self.lineedit2[1].insert(0, self.data[8])
            self.lineedit2[2].insert(0, self.data[9])
            self.lineedit2[3].insert(0, self.data[13])
            self.lineedit2[4].insert(0, self.data[10])
            self.lineedit2[5].insert(0, self.data[17])
            self.lineedit2[6].insert(0, self.data[12])
            self.text1.insert(tk.END, self.data[14])
            self.combobox2[0].set(self.data[16])
            self.combobox2[1].set(self.data[18])
            self.combobox2[2].set(self.data[19])
            self.lineedit2[7].insert(0, self.data[20])
            self.lineedit2[8].insert(0, self.data[21])

        except Exception as e:
            messagebox.showerror("Unsuccessful", "Error While searching the Record " + str(e), parent=self.top)
        # finally:
        # self.exit1()

    def search_data2(self, event):

        v = self.lineedit_search.get()  # name

        try:
            d = self.conn.cursor()
            total_rows = d.execute("select AC, NM from names1 where AC like %s", ("%" + v + "%",))
            data = d.fetchall()
            self.table.delete(*self.table.get_children())
            if total_rows != 0:
                for row in data:
                    self.table.insert("", tk.END, values=row)
            else:
                messagebox.showwarning("No Record", "No Account Record Found", parent=self.top)
        except Exception as e:
            messagebox.showerror("Error", "Query  Error \n" + str(e), parent=self.top)

    def on_selection_change(self, event):
        # self.comboboxAc1['values'] = ("Sales Account", "Purchase Account", "Nominal Account", "")
        selection = self.comboboxAc1.get()
        selection2=self.comboboxAc1.current()
        # Hide the label widgets based on the current selection
        while True:

            #if selection == "Sales Account":
            self.reset_page()
            if selection2 == 0:
                self.frame1.grid
                self.label1[0].grid()
                self.label1[1].grid()
                self.label1[2].grid()
                self.label1[3].grid()
                self.label1[4].grid()
                self.label1[5].grid()
                self.label1[6].grid()
                self.label1[7].grid()
                self.label2[0].grid()
                self.label2[1].grid()
                self.label2[2].grid()
                self.label2[3].grid()
                self.label2[4].grid()
                self.label2[5].grid()
                self.label2[6].grid()
                self.label2[7].grid()
                self.label2[8].grid()
                self.label2[9].grid()
                self.comboboxAc1.grid()
                self.lineedit1[1].grid()
                self.lineedit1[2].grid()
                self.lineedit1[3].grid()
                self.lineedit1[4].grid()
                self.lineedit1[5].grid()
                self.lineedit1[6].grid()
                self.lineedit1[7].grid()

                self.lineedit2[0].grid()
                self.lineedit2[1].grid()
                self.lineedit2[2].grid()
                self.lineedit2[3].grid()
                self.lineedit2[4].grid()
                self.lineedit2[5].grid()
                self.lineedit2[6].grid()
                self.lineedit2[7].grid()
                self.lineedit2[8].grid()
                self.text1.grid()
                self.combobox2[0].grid()
                self.combobox2[1].grid()
                self.combobox2[2].grid()
                self.label2[10].grid()
                self.label2[11].grid()
                self.label2[12].grid()
                self.lineedit_search.grid
                self.pushbutton1[0].grid
                self.pushbutton1[1].grid
                self.pushbutton1[2].grid
                self.pushbutton1[3].grid
                self.combobox2[2]['values'] = (
                    "Daily", "Weekly", "Advertising", "B/F Balances", "Blank Charges", "Bank Interest",
                    "Business Transfer Charges")

                break
            #elif selection == 'Purchase Account':
            elif    selection2 == 1:
                self.label1[7].grid_remove()

                self.lineedit1[6].grid_remove()

                self.combobox2[1].grid_remove()
                self.combobox2[2].grid_remove()
                self.lineedit2[7].grid_remove()
                self.lineedit2[8].grid_remove()

                self.label2[8].grid_remove()
                self.label2[9].grid_remove()
                self.label2[10].grid_remove()
                self.label2[11].grid_remove()
                self.combobox2[2]['values'] = (
                    "Daily", "Weekly", "Advertising", "B/F Balances", "Blank Charges", "Bank Interest",
                    "Business Transfer Charges")
                break

            #elif selection == "Nominal Account":
            elif selection2 == 2:
                self.label1[2].grid_remove()
                self.label1[3].grid_remove()
                self.label1[4].grid_remove()
                self.label1[5].grid_remove()
                self.label1[6].grid_remove()
                self.label1[7].grid_remove()
                self.label2[0].grid_remove()
                self.label2[1].grid_remove()
                self.label2[2].grid_remove()
                self.label2[3].grid_remove()
                self.label2[4].grid_remove()
                self.label2[5].grid_remove()
                self.label2[6].grid_remove()
                self.label2[7].grid_remove()
                self.label2[8].grid_remove()

                self.lineedit1[1].grid_remove()
                self.lineedit1[2].grid_remove()
                self.lineedit1[3].grid_remove()
                self.lineedit1[4].grid_remove()
                self.lineedit1[5].grid_remove()
                self.lineedit1[6].grid_remove()
                self.lineedit2[0].grid_remove()
                self.lineedit2[1].grid_remove()
                self.lineedit2[2].grid_remove()
                self.lineedit2[3].grid_remove()
                self.lineedit2[4].grid_remove()
                self.lineedit2[5].grid_remove()
                self.lineedit2[6].grid_remove()
                self.lineedit2[7].grid_remove()
                self.lineedit2[8].grid_remove()
                self.text1.grid_remove()
                self.combobox2[0].grid_remove()
                self.combobox2[1].grid_remove()
                self.label2[10].grid_remove()
                self.label2[11].grid_remove()
                self.label2[12].grid_remove()
                self.combobox2[2].grid()
                self.combobox2[2].grid(row=2, column=6, sticky="nsew", padx=5, pady=5)
                self.lineedit2[2].grid()
                self.combobox2[2].set('SALES')
                self.combobox2[2]['values'] = ['SALES','COST OF SALES','REVENUE','STAFF COST', 'OFFICE-OVERHEADS',
                                               'PROFESSIONAL FEES', 'TRANSPORT AND MOTORING COSTS','OTHER COSTS',
                                               'FIXED ASSETS', 'CURRENT-ASSETS','CURRENT LIABILITIES', 'CAPITAL ACCOUNT']
                selection3 = self.combobox2[2].get()

                if selection3 == 'SALES':
                   self.lineedit2[2].delete(0, tk.END)

                   self.combobox2[2].bind("<<ComboboxSelected>>", self.lineedit2[2].insert(0,'Nominal- Sales (Trading A/C)' ))
                   break
                elif selection3 == 'COST OF SALES':
                   #self.lineedit2[2].insert(0,'Nominal- Cost of Sales (Trading A/C)' )
                   self.lineedit2[2].delete(0, tk.END)
                   self.combobox2[2].bind("<<ComboboxSelected>>",self.lineedit2[2].insert(0, 'Nominal- Cost of Sales (Trading A/C)'))
                   break
                elif selection3 == 'REVENUE':
                   self.lineedit2[2].insert(0,'Nominal-Revenue (P & L)' )
                   break
                elif selection3 == 'STAFF COST':
                   self.lineedit2[2].insert(0,'Nominal-Expenditure (P & L)' )
                   break
                else:
                    print('test')

                        # self.combobox2[2]['values'] = ['Nominal- Sales (Trading A/C)', 'Nominal- Cost of Sales (Trading A/C)',
                #                                'Nominal-Revenue (P & L)', 'Nominal-Expenditure (P & L)',
                #                                'Nominal-Other Assets (Balance Sheet)',
                #                                'Nominal-Current Assets (Balance Sheet)',
                #                                'Nominal-Current Liabilties (Balance Sheet)',
                #                                'Nominal-Capital (Balance Sheet)']
                self.label2[9].grid(row=2, column=5, sticky="nsew", padx=5, pady=5)
                self.label2[9].config(text="Category", anchor=tk.W)
                break

            else:
                print("Test")
    def generate_id(self, name):
        # Extract the first three letters of the name
        id = name[:3]
        # Append the fixed string "00" to the ID
        id += "00"
        # Increment the counter and append it to the ID
        counter = 1
        id += str(counter)
        # Check the database to see if the ID already exists
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM names1 WHERE AC = %s", (id,))
        if cursor.fetchone() is not None:
            # If the ID already exists, increment the counter and try again
            while True:
                counter += 1
                id = id[:-1] + str(counter)
                cursor.execute("SELECT * FROM names1 WHERE AC = %s", (id,))
                if cursor.fetchone() is None:
                    break
        # Return the ID
        return id

    # Connect to the database

    # Get the name from the line edit

    # Get the name from the line edit

    def move_to_next_widget(self, event):
        event.widget.tk_focusNext().focus()
        # if widget==self.lineedit1[7]:
        #     widget == self.lineedit2[0]

    def exit1(self):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def database_connection(self):
        if (self.flag == 0):
            try:
                self.conn = mysql.connector.connect(user='root', password='1234',
                                                    host='localhost',
                                                    database='Accounts', port='3306', autocommit=True)
                self.flag = 1
            except Exception as e:
                messagebox.showerror("Error", "Database Connection Error \n" + str(e), parent=self.top)

    def fetch_data(self):
        self.database_connection()
        try:
            d = self.conn.cursor()
            total_rows = d.execute(
                "select TYA,NM,A1,A2,A3,A4,CN,TEL1,TEL2,FAX,CRL,AC,VAT,EMAIL,NOTES,VATRATE,NAC,PAYT,PCODE,ACTYPE,ROUNDNO,DROPNO from names1")
            data = d.fetchall()
            # self.table.delete(*self.table.get_children())
            # if total_rows >= 0:
            #     for row in data:
            #         self.table.insert("", tk.END, values=row)
            # else:
            #     if self.fetch_flag != 0:
            #         messagebox.showwarning("No Record", "No user  Record Found", parent=self.top)
            #     else:
            #         self.fetch_flag = 1
        except Exception as e:
            messagebox.showerror("Error", "Query  Error \n" + str(e), parent=self.top)
        finally:
            self.d.close()
            self.conn.close()

    # def get_rowdata(self):
    #     rowid = self.table.focus()
    #     row = self.table.item(rowid)
    #     data = row['values']
    #     id = data[3]
    #     self.fetch_one_data(id)

    def fetch_one_data(self, r=None):
        if r == None:
            r = self.lineedit_search.get()  # username

        self.database_connection()
        try:
            d = self.conn.cursor()
            total_rows = d.execute("select TYA,NM,A1,A2,A3,A4,CN,TEL1,TEL2,FAX,CRL,AC,VAT,EMAIL,NOTES,VATRATE,' \
                  'NAC,PAYT,PCODE,ACTYPE,ROUNDNO,DROPNO from names1 where AC= %s", (r))
            data = d.fetchone()
            self.reset_page()
            if total_rows == 1:

                self.comboboxAc1.set(data[0])
                self.lineedit1[0].insert(0, data[1])
                self.lineedit1[1].insert(0, data[2])
                self.lineedit1[2].insert(0, data[3])
                self.lineedit1[3].insert(0, data[4])
                self.lineedit1[4].insert(0, data[5])
                self.lineedit1[5].insert(0, data[6])
                self.lineedit2[0].insert(0, data[9])
                self.lineedit2[1].insert(0, data[10])
                self.lineedit2[2].insert(0, data[11])
                self.lineedit2[4].insert(0, data[13])
                self.lineedit1[7].insert(0, data[8])
                self.lineedit2[6].insert(0, data[15])
                self.lineedit2[3].insert(0, data[12])
                self.text1.insert(tk.END, data[16])
                self.lineedit1[6].insert(0, data[7])
                self.combobox2[0].set(data[17])
                self.lineedit2[5].insert(0, data[14])
                self.combobox2[1].set(data[18])
                self.combobox2[2].set(data[19])
                self.lineedit2[7].insert(0, data[20])
                self.lineedit2[8].insert(0, data[21])

            else:
                messagebox.showwarning("No Record", "No Record Found ", parent=self.top)
        except Exception as e:
            messagebox.showerror("Error", "Query  Error \n" + str(e), parent=self.top)
        finally:
            self.d.close()
            self.conn.close()

    def deletedata(self):
        rowid = self.table.focus()
        row = self.table.item(rowid)
        data = row['values']

        self.reset_page()

        v = data[0]

        ans = messagebox.askquestion("Confirmation", "Are you sure to delete ? ", parent=self.top)
        if ans == 'yes':
            try:
                self.cursor = self.conn.cursor()
                self.cursor.execute("delete from names1 where AC like %s", (v,))
                self.conn.commit()
                messagebox.showinfo("Success", "User Record Deleted Successfully", parent=self.top)
                self.reset_page()
            except Exception as e:
                messagebox.showerror("Unsuccessful", "Error While Deleting User Record " + str(e), parent=self.top)
            # finally:
            #     self.exit()

    def reset_page(self):

        self.lineedit1[0].delete(0, tk.END)
        self.lineedit1[1].delete(0, tk.END)
        self.lineedit1[2].delete(0, tk.END)
        self.lineedit1[3].delete(0, tk.END)
        self.lineedit1[4].delete(0, tk.END)
        self.lineedit1[5].delete(0, tk.END)
        self.lineedit2[0].delete(0, tk.END)
        self.lineedit2[1].delete(0, tk.END)
        self.lineedit2[2].delete(0, tk.END)
        self.lineedit2[4].delete(0, tk.END)
        self.lineedit1[7].delete(0, tk.END)
        self.lineedit2[6].delete(0, tk.END)
        self.lineedit2[3].delete(0, tk.END)
        self.text1.delete('1.0', 'end')
        self.lineedit1[6].delete(0, tk.END)

        self.lineedit2[5].delete(0, tk.END)

        self.lineedit2[7].delete(0, tk.END)
        self.lineedit2[8].delete(0, tk.END)
        self.combobox2[0]['values'] = (
            "None", "Accountancy Charges", "Advertising", "B/F Balances", "Blank Charges", "Bank Interest",
            "Business Transfer Charges")
        self.combobox2[1]['values'] = ("A", "B", "C", "D", "E")
        self.combobox2[2]['values'] = (
            "Daily", "Weekly", "Advertising", "B/F Balances", "Blank Charges", "Bank Interest",
            "Business Transfer Charges")
        self.comboboxAc1.set("Sales Account")
        self.comboboxAc1['values'] = ("Sales Account", "Purchase Account", "Nominal Account")
        self.combobox2[0].set("None")
        self.combobox2[1].set("A")
        self.combobox2[2].set("Daily")

    def search_data(self):

        self.reset_page()
        # v = self.lineedit_search.get()  # name
        v = str(self.lineedit_search.get())

        self.pushbutton1[1].config(state='active')
        self.pushbutton1[4].config(state='active')

        try:

            sql = 'select TYA,NM,A1,A2,A3,A4,CN,TEL1,TEL2,FAX,CRL,AC,VAT,EMAIL,NOTES,VATRATE,' \
                  'NAC,PAYT,PCODE,ACTYPE,ROUNDNO,DROPNO  from names1 where AC like %s'

            self.cursor.execute(sql, (v,))
            self.data = self.cursor.fetchone()
            print(self.data)
            # self.comboboxAc1.current(self.data[0] - 1)
            val = self.data[0] - 1
            if val == 0:
                self.comboboxAc1.set('Sales Account')
            elif val == 1:
                self.comboboxAc1.set('Purchase Account')
            elif val == 2:
                self.comboboxAc1.set('Nominal Account')
            else:
                self.comboboxAc1.set('')

            self.lineedit1[0].insert(0, self.data[1])
            self.lineedit1[1].insert(0, self.data[2])
            self.lineedit1[2].insert(0, self.data[3])
            self.lineedit1[3].insert(0, self.data[4])
            self.lineedit1[4].insert(0, self.data[5])
            self.lineedit1[5].insert(0, self.data[6])
            self.lineedit1[6].insert(0, self.data[15])
            self.lineedit1[7].insert(0, self.data[11])
            self.lineedit2[0].insert(0, self.data[7])
            self.lineedit2[1].insert(0, self.data[8])
            self.lineedit2[2].insert(0, self.data[9])
            self.lineedit2[3].insert(0, self.data[13])
            self.lineedit2[4].insert(0, self.data[10])
            self.lineedit2[5].insert(0, self.data[17])
            self.lineedit2[6].insert(0, self.data[12])
            self.text1.insert(tk.END, self.data[14])
            self.combobox2[0].set(self.data[16])
            self.combobox2[1].set(self.data[18])
            self.combobox2[2].set(self.data[19])
            self.lineedit2[7].insert(0, self.data[20])
            self.lineedit2[8].insert(0, self.data[21])

        except Exception as e:
            messagebox.showerror("Unsuccessful", "Error While searching the Record " + str(e), parent=self.top)
        # finally:
        # self.exit1()

    def save_data(self):

        TYA = self.comboboxAc1.current() + 1
        print(TYA)
        NM = self.lineedit1[0].get()

        print(NM)
        A1 = self.lineedit1[1].get()
        print(A1)
        A2 = self.lineedit1[2].get()
        print(A2)
        A3 = self.lineedit1[3].get()
        print(A3)
        A4 = self.lineedit1[4].get()
        print(A4)
        CN = self.lineedit1[5].get()
        print(CN)
        TEL1 = (self.lineedit2[0].get())
        print(TEL1)
        TEL2 = (self.lineedit2[1].get())
        print(TEL2)
        FAX = self.lineedit2[2].get()
        print(FAX)
        CRL = (self.lineedit2[4].get())
        print(CRL + 'crl')
        # if CRL==None:
        #     CRL=decimal(0.0)
        # AC = self.lineedit1[7].get()
        # AC = self.generate_id(NM)
        AC = str.upper(self.generate_id(self.lineedit1[0].get()))
        print(AC)
        VAT = self.lineedit2[6].get()
        print(VAT)
        EMAIL = self.lineedit2[3].get()
        print(EMAIL)
        NOTES = self.text1.get("1.0", "end")
        print(NOTES)
        VATRATE = self.lineedit1[6].get()
        print(VATRATE)
        NAC = self.combobox2[0].get()
        print(NAC)
        PAYT = self.lineedit2[5].get()
        print(PAYT)
        PCODE = self.combobox2[1].get()
        print(PCODE)
        ACTYPE = self.combobox2[2].get()
        print(ACTYPE)
        ROUNDNO = self.lineedit2[7].get()
        print(ROUNDNO)
        DROPNO = self.lineedit2[8].get()
        print(DROPNO)

        try:
            self.cursor = self.conn.cursor()
            # name11,address`, `gender`, `username11`, `password`, `type`, `dob`, `phone`, `pic
            self.cursor.execute(
                "insert into names1 (TYA,NM,A1,A2,A3,A4,CN,TEL1,TEL2,FAX,CRL,AC,VAT,EMAIL,NOTES,VATRATE,NAC,PAYT,PCODE,ACTYPE,ROUNDNO,DROPNO) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (TYA, NM, A1, A2, A3, A4, CN, TEL1, TEL2, FAX, CRL, AC, VAT, EMAIL, NOTES, VATRATE, NAC, PAYT, PCODE,
                 ACTYPE, ROUNDNO, DROPNO))

            messagebox.showinfo("Success", "Data saved ", parent=self.top)
            self.reset_page()
        except Exception as e:
            messagebox.showerror("Error", "Query  Error \n" + str(e), parent=self.top)
        # finally:
        #     self.exit()

    def update_data(self):
        rowid = self.table.focus()
        row = self.table.item(rowid)
        data = row['values']

        v = data[0]

        TYA_1 = self.comboboxAc1.current() + 1

        NM_1 = self.lineedit1[0].get()
        A1_1 = self.lineedit1[1].get()
        A2_1 = self.lineedit1[2].get()
        A3_1 = self.lineedit1[3].get()
        A4_1 = self.lineedit1[4].get()
        CN_1 = self.lineedit1[5].get()
        TEL1_1 = (self.lineedit2[0].get())
        TEL2_1 = (self.lineedit2[1].get())
        FAX_1 = self.lineedit2[2].get()
        CRL_1 = (self.lineedit2[4].get())
        # AC_1 = self.lineedit1[7].get()
        VAT_1 = self.lineedit2[6].get()
        EMAIL_1 = self.lineedit2[3].get()
        NOTES_1 = self.text1.get("1.0", "end")
        VATRATE_1 = self.lineedit1[6].get()
        NAC_1 = self.combobox2[0].get()
        PAYT_1 = self.lineedit2[5].get()
        PCODE_1 = self.combobox2[1].get()
        ACTYPE_1 = self.combobox2[2].get()
        ROUNDNO_1 = self.lineedit2[7].get()
        DROPNO_1 = self.lineedit2[8].get()
        # self.database_connection()
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(
                "update names1 set TYA=%s,NM=%s,A1=%s,A2=%s,A3=%s,A4=%s,CN=%s,TEL1=%s,TEL2=%s,FAX=%s,CRL=%s,VAT=%s,"
                "EMAIL=%s,VATRATE=%s,NAC=%s,PAYT=%s,PCODE=%s,ACTYPE=%s,ROUNDNO=%s,DROPNO=%s "
                "where AC like %s",
                (TYA_1, NM_1, A1_1, A2_1, A3_1, A4_1, CN_1, TEL1_1, TEL2_1, FAX_1, CRL_1, VAT_1, EMAIL_1,
                 VATRATE_1, NAC_1, PAYT_1, PCODE_1, ACTYPE_1, ROUNDNO_1, DROPNO_1, v))
            self.conn.commit()
            messagebox.showinfo("Success", "Data Updated Successfully ", parent=self.top)
            self.reset_page()
        except Exception as e:
            messagebox.showerror("Error", "Query  Error \n" + str(e), parent=self.top)
        # finally:
        #     exit()

    def validate_page(self):
        name = self.lineedit1[0].get().strip()
        phone = self.lineedit2[0].get()
        phone2 = self.lineedit2[1].get()
        pin = self.lineedit1[4].get()
        crl = self.lineedit2[4].get()
        if (len(name) < 3):
            return False, "Please Enter Proper Name "
        elif (len(pin) < 5):
            return False, "Please Enter Valid Postcode"
        elif not (len(phone) > 8 and len(phone) < 11):
            return False, "Please Enter Valid Phone Number 1 \n \n (8-12 digit character)"
        elif not (len(phone2) > 8 and len(phone2) < 11):
            return False, "Please Enter Valid Phone Number 2 \n \n (8-12 digit character)"
        elif (crl.isdigit()):
            return False, "Please Enter the Numbers"
        else:
            return True, "Ok"

    def on_submitName(self):
        input=len(self.lineedit1[0].get())
        if (input) >= 3:
            return True
        else:
            messagebox.showerror("Please Enter Proper Name ")
            return False

    def validate_input(content):
        if len(content) >= 3:
            return True
        else:
            return False

    def on_submitPhone(self, input):
        if (len(input) > 8):
            return True
        else:
            messagebox.showerror("Please Enter Valid Phone Number 1 \n \n (8-12 digit character)")
            return False

    def on_submitPostcode(self, input):
        if (len(input) > 5):
            return True
        else:
            messagebox.showerror("Please Enter Valid Postcode")
            return False

    def on_submitDigit(self, input):
        if input.isdigit():
            return True
        else:
            messagebox.showerror("Error", "Please enter digits only.")
            return False

    def on_submit1(self, input):
        # Validate the input
        if len(input) < 40:
            return True
        else:
            messagebox.showerror("Error", "Please enter less than 40 characters.")
            return False


if __name__ == '__main__':
    # dummy = tk.Tk()
    # Toplevel1(dummy)
    # dummy.mainloop()
    root = tk.Tk()
    app = Toplevel1(root)
    root.mainloop()
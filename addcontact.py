from tkinter import Toplevel, messagebox, ttk
import tkinter
import sqlite3

conn = sqlite3.connect('contactsdb.sqlite')
cursor = conn.cursor()


class AddContacts(Toplevel):

    def __init__(self):
        Toplevel.__init__(self)

        self.geometry('550x550+600+200')
        # self.title('All Contacts')
        self.wm_title('All Contacts')
        self.resizable(False, False)

        # ===== top & bottom frames ==========
        self.top_frame = tkinter.Frame(self, height=150, bg='white')
        self.top_frame.pack(fill=tkinter.X)

        self.bottom_frame = tkinter.Frame(self, height=500, bg='#6d9eed')
        self.bottom_frame.pack(fill=tkinter.X)

        # ======= top frame design =======
        self.logo_image = tkinter.PhotoImage(file='single person.png')
        self.image_label = tkinter.Label(self.top_frame, image=self.logo_image, bg='white')
        self.image_label.place(x=130, y=25)

        self.title = tkinter.Label(self.top_frame, text='Add New Contact', font='Times 15 bold underline', bg='white', fg='#ebb434')
        self.title.place(x=230, y=50)

        # ====== name =======
        self.add_name = tkinter.Label(self.bottom_frame, text="Name: ", font='arial 15 bold', fg='white', bg='#6d9eed')
        self.add_name.place(x=40, y=40)
        self.entry_name = tkinter.Entry(self.bottom_frame, width=30, bd=3)      # bd: border
        self.entry_name.insert(0, 'Enter Name')
        self.entry_name.place(x=150, y=40)

        # ====== email =======
        self.add_email = tkinter.Label(self.bottom_frame, text="Email: ", font='arial 15 bold', fg='white', bg='#6d9eed')
        self.add_email.place(x=40, y=80)
        self.entry_email = tkinter.Entry(self.bottom_frame, width=30, bd=3)      # bd: border
        self.entry_email.insert(0, 'Enter email')
        self.entry_email.place(x=150, y=80)

        # ====== number =======
        self.add_number = tkinter.Label(self.bottom_frame, text="Number: ", font='arial 15 bold', fg='white', bg='#6d9eed')
        self.add_number.place(x=40, y=120)
        self.entry_number = tkinter.Entry(self.bottom_frame, width=30, bd=3)      # bd: border
        self.entry_number.insert(0, 'Enter Number')
        self.entry_number.place(x=150, y=120)

        # ====== address =======
        self.add_address = tkinter.Label(self.bottom_frame, text="Address: ", font='arial 15 bold', fg='white', bg='#6d9eed')
        self.add_address.place(x=40, y=160)
        self.entry_address = tkinter.Text(self.bottom_frame, width=25, height=8, bd=3)      # bd: border
        self.entry_address.place(x=150, y=160)

        # ====== Submit Button =======
        submit_button = tkinter.ttk.Button(self.bottom_frame, text='Submit', width=12, command=self.add_people)
        submit_button.place(x=210, y=350)

    def add_people(self):
        name = self.entry_name.get()
        email = self.entry_email.get()
        number = self.entry_number.get()
        address = self.entry_address.get(1.0, 'end-1c')

        if name and email and number and address !="":
            try:
                query = "INSERT INTO contactbook (person_name, person_email, person_number, person_address) VALUES (?, ?, ?, ?)"
                cursor.execute(query, (name, email, number, address))
                conn.commit()
                messagebox.showinfo("Success", "Contact added")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        else:
            messagebox.showerror('Error', 'All Fields are compulsory', icon='warning')

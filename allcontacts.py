from tkinter import *
import sqlite3
import tkinter
from addcontact import AddContacts
from updatecontact import UpdateContact
from displaycontact import DisplayContact
from tkinter import messagebox, ttk

conn = sqlite3.connect('contactsdb.sqlite')
cursor = conn.cursor()

# Program content in this file is static for this particular file, so we can also remove
# self parameter from there and it will run without error.


class AllContacts(Toplevel):

    def __init__(self):
        Toplevel.__init__(self)

        self.geometry('500x450+350+200')
        # self.title('All Contacts')
        self.wm_title('All Contacts')
        self.resizable(False, False)

        # ===== top & bottom frames ==========
        self.top_frame = tkinter.Frame(self, height=150, bg='white')
        self.top_frame.pack(fill=tkinter.X)

        self.bottom_frame = tkinter.Frame(self, height=300, bg='#3b547a')
        self.bottom_frame.pack(fill=tkinter.X)

        # ======= top frame design =======
        self.logo_image = tkinter.PhotoImage(file='people icon.png')
        self.image_label = tkinter.Label(self.top_frame, image=self.logo_image, bg='white')
        self.image_label.place(x=130, y=25)

        self.title = tkinter.Label(self.top_frame, text='All Contacts', font='Times 15 bold underline', bg='white', fg='#ebb434')
        self.title.place(x=230, y=50)

        # ======= bottom frame design =======
        self.list_box = tkinter.Listbox(self.bottom_frame, width=30, height=18, bg='#d9e38d')
        self.list_box.grid(row=0, column=0, padx=(40, 0))

        self.scroll_bar = tkinter.Scrollbar(self.bottom_frame, orient=tkinter.VERTICAL)
        self.scroll_bar.grid(row=0, column=1, sticky='ns')
        self.scroll_bar.config(command=self.list_box.yview)
        self.list_box.config(yscrollcommand=self.scroll_bar.set)

        persons = cursor.execute("SELECT * FROM contactbook").fetchall()
        print(persons)
        count = 0
        for person in persons:
            self.list_box.insert(count, str(person[0]) + ". " + str(person[1]))
            count += 1

        # ======= Buttons =======

        # ======= Add Button =======
        add_button = tkinter.ttk.Button(self.bottom_frame, text="Add", width=12, command=self.add_contact)
        add_button.grid(row=0, column=2, padx=20, pady=10, sticky='n')

        # ======= Update Button =======
        update_button = tkinter.ttk.Button(self.bottom_frame, text="Update", width=12, command=self.update_contacts)
        update_button.grid(row=0, column=2, padx=20, pady=50, sticky='n')

        # ======= Display Button =======
        display_button = tkinter.ttk.Button(self.bottom_frame, text="View Details", width=12, command=self.display_contact)
        display_button.grid(row=0, column=2, padx=20, pady=90, sticky='n')

        # ======= Delete Button =======
        delete_button = tkinter.ttk.Button(self.bottom_frame, text="Delete", width=12, command=self.delete_contact)
        delete_button.grid(row=0, column=2, padx=20, pady=130, sticky='n')

    def add_contact(self):
        add_window = AddContacts()
        self.destroy()

    def update_contacts(self):
        selected_contact = self.list_box.curselection()
        contact = self.list_box.get(selected_contact)
        person_id = contact.split(".")[0]

        update_window = UpdateContact(person_id)

    def display_contact(self):
        selected_contact = self.list_box.curselection()
        contact = self.list_box.get(selected_contact)
        person_id = contact.split(".")[0]

        display_window = DisplayContact(person_id)

    def delete_contact(self):
        selected_contact = self.list_box.curselection()
        contact = self.list_box.get(selected_contact)
        person_id = contact.split(".")[0]

        query = "DELETE FROM contactbook WHERE person_id = {}".format(person_id)
        string_for_msgbox = 'Are you sure, you want to delete ' + contact.split(".")[1] + "?"
        answer = messagebox.askquestion('Warning', string_for_msgbox)
        if answer == 'yes':
            try:
                cursor.execute(query)
                conn.commit()
                messagebox.showinfo('Success', 'Contact Deleted')
                self.destroy()

            except Exception as e:
                messagebox.showinfo('Info', str(e))

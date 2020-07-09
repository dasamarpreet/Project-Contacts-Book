from tkinter import Toplevel, messagebox, ttk
import tkinter
import sqlite3


conn = sqlite3.connect('contactsdb.sqlite')
cursor = conn.cursor()


class UpdateContact(Toplevel):

    def __init__(self, person_id):
        Toplevel.__init__(self)

        self.geometry('550x550+600+200')
        # self.title('Update contact')
        self.wm_title('Update contact')
        self.resizable(False, False)
        print("Person id: ", person_id)

        query = "SELECT * FROM contactbook WHERE person_id={}".format(person_id)
        result = cursor.execute(query).fetchone()
        print(result)

        self.person_id = person_id
        person_name = result[1]
        person_email = result[2]
        person_number = result[3]
        person_address = result[4]

        # ===== top & bottom frames ==========
        self.top_frame = tkinter.Frame(self, height=150, bg='white')
        self.top_frame.pack(fill=tkinter.X)

        self.bottom_frame = tkinter.Frame(self, height=500, bg='#40cf9d')
        self.bottom_frame.pack(fill=tkinter.X)

        # ======= top frame design =======
        self.logo_image = tkinter.PhotoImage(file='single person.png')
        self.image_label = tkinter.Label(self.top_frame, image=self.logo_image, bg='white')
        self.image_label.place(x=130, y=25)

        self.title = tkinter.Label(self.top_frame, text='Update Contact', font='Times 15 bold underline', bg='white', fg='#ebb434')
        self.title.place(x=230, y=50)

        # ====== name =======
        self.add_name = tkinter.Label(self.bottom_frame, text="Name: ", font='arial 15 bold', fg='white', bg='#40cf9d')
        self.add_name.place(x=40, y=40)
        self.entry_name = tkinter.Entry(self.bottom_frame, width=30, bd=3)      # bd: border
        self.entry_name.insert(0, person_name)
        self.entry_name.place(x=150, y=40)

        # ====== email =======
        self.add_email = tkinter.Label(self.bottom_frame, text="Email: ", font='arial 15 bold', fg='white', bg='#40cf9d')
        self.add_email.place(x=40, y=80)
        self.entry_email = tkinter.Entry(self.bottom_frame, width=30, bd=3)      # bd: border
        self.entry_email.insert(0, person_email)
        self.entry_email.place(x=150, y=80)

        # ====== number =======
        self.add_number = tkinter.Label(self.bottom_frame, text="Number: ", font='arial 15 bold', fg='white', bg='#40cf9d')
        self.add_number.place(x=40, y=120)
        self.entry_number = tkinter.Entry(self.bottom_frame, width=30, bd=3)      # bd: border
        self.entry_number.insert(0, person_number)
        self.entry_number.place(x=150, y=120)

        # ====== address =======
        self.add_address = tkinter.Label(self.bottom_frame, text="Address: ", font='arial 15 bold', fg='white', bg='#40cf9d')
        self.add_address.place(x=40, y=160)
        self.entry_address = tkinter.Text(self.bottom_frame, width=25, height=8, bd=3)      # bd: border
        self.entry_address.insert(1.0, person_address)
        self.entry_address.place(x=150, y=160)

        # ====== Submit Button =======
        submit_button = tkinter.ttk.Button(self.bottom_frame, text='Update Details', width=17, command=self.update_contact)
        submit_button.place(x=210, y=350)

    def update_contact(self):

        contact_id = self.person_id
        name = self.entry_name.get()
        email = self.entry_email.get()
        number = self.entry_number.get()
        address = self.entry_address.get(1.0, 'end-1c')
        query = "UPDATE contactbook SET person_name='{}', person_email='{}', person_number='{}', person_address='{}' WHERE person_id = {}"\
            .format(name, email, number, address, contact_id)

        try:
            cursor.execute(query)
            conn.commit()
            messagebox.showinfo("Success", "Contact Updated")

        except Exception as e:
            print(e)

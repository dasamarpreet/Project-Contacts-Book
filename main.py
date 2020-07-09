import tkinter
import datetime
from tkinter import ttk
from allcontacts import AllContacts, AddContacts
from aboutus import AboutUs


class ContactsBook(object):

    def __init__(self, window):
        self.window = window

        # ====== Setting icon =======
        tkinter.Tk.iconbitmap(self=window, default='icon1.ico')

        # ===== top & bottom frames ==========
        self.top_frame = tkinter.Frame(window, height=150, bg='white')
        self.top_frame.pack(fill=tkinter.X)

        self.bottom_frame = tkinter.Frame(window, height=500, bg='#786114')
        self.bottom_frame.pack(fill=tkinter.X)

        # ======= top frame design =======
        self.logo_image = tkinter.PhotoImage(file='logo_contact.png')
        self.image_label = tkinter.Label(self.top_frame, image=self.logo_image, bg='white')
        self.image_label.place(x=130, y=25)

        self.title = tkinter.Label(self.top_frame, text='Contacts Book', font='Times 15 bold underline', bg='white', fg='#ebb434')
        self.title.place(x=230, y=50)

        # ====== time set and display =======
        date_set = datetime.datetime.now().date()
        date_set = str(date_set)

        self.date_label = tkinter.Label(self.top_frame, text='Date: '+date_set, font='Times 10 roman bold', bg='white', fg='#ebb434')
        self.date_label.place(x=10, y=10)

        # ====== creator name display ========
        self.creator_label = tkinter.Label(self.top_frame, text='Created for Institutional Training Project', font='Times 10 italic', bg='white', fg='black')
        self.creator_label.place(x=230, y=80)

        # ====== creator name display ========
        self.name_label = tkinter.Label(self.top_frame, text='- By Amar Preet Das', font='Times 10 italic bold', bg='white', fg='#4079cf')
        self.name_label.place(x=450, y=110)

        # ====== Bottom Frame Buttons =======

        # ====== ttk button styling ======
        ttk_style = ttk.Style(window)
        ttk_style.configure('TButton', foreground="#cf4040", font='Sans 12 bold', width=17, height=1)

        # ====== Show All Contacts Button ====
        self.all_contacts = tkinter.ttk.Button(self.bottom_frame, text=' Show All Contacts ', command=self.all_contacts)
        self.all_contacts.place(x=250, y=70)

        # ====== Add New Button ====
        self.all_contacts = tkinter.ttk.Button(self.bottom_frame, text=' Add New Contact', command=self.add_new_contact)
        self.all_contacts.place(x=250, y=120)

        # ====== About Us Button ====
        self.all_contacts = tkinter.ttk.Button(self.bottom_frame, text=' About Us ', command=self.about_us)        # , font='arial 12 bold'
        self.all_contacts.place(x=250, y=170)

    def all_contacts(self):
        people = AllContacts()

    def add_new_contact(self):
        add_window = AddContacts()

    def about_us(self):
        about = AboutUs()


def main():
    main_window = tkinter.Tk()
    application = ContactsBook(main_window)
    main_window.title('Contacts Book By APD')
    main_window.geometry('650x550+350+200')
    main_window.resizable(False, False)
    main_window.mainloop()


if __name__ == '__main__':
    main()

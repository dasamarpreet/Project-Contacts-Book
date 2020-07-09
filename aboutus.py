from tkinter import Toplevel
import tkinter


class AboutUs(Toplevel):

    def __init__(self):
        Toplevel.__init__(self)

        self.geometry('550x550+550+200')
        self.wm_title('About Us')
        self.resizable(False, False)

        # ===== top frame ==========
        self.top_frame = tkinter.Frame(self, height=100, bg='white')
        self.top_frame.pack(fill=tkinter.X)

        # ======= bottom frame ========
        self.bottom_frame = tkinter.Frame(self, height=500, bg='#929da1')
        self.bottom_frame.pack(fill=tkinter.X)

        # ======= Top Frame Label ==========
        self.top_label = tkinter.Label(self.top_frame, text='Hey, This is  about us page', font='arial 14 roman bold', bg='white')
        self.top_label.place(x=150, y=40)

        self.logo_image = tkinter.PhotoImage(file='about_us icon.png')
        self.image_label = tkinter.Label(self.top_frame, image=self.logo_image, bg='white')
        self.image_label.place(x=70, y=25)

        # ======= Top Frame Label ==========
        self.bottom_label = tkinter.Label(self.bottom_frame, text='This app has been developed by\n Amar of 19BCA1-A as a project for \nthe institutional training in summer 2020.\n'
                                                                  'This app helps you maintain your records for any person,\n you can view anytime and save as much contacts as you\n '
                                                                  'want. In case of any problem or bugs faced by the users,\n I\'m always here to help them.',
                                          font='arial 12 roman bold', bg='#929da1', fg='white')
        self.bottom_label.place(x=70,y=50)

        # ======= contact me label =======
        self.bottom_label = tkinter.Label(self.bottom_frame, text='For any query related to this app\n'
                                                                  'you can contact me through mail at: amarpreetdas@gmail.com\n'
                                                                  'or post your query at \'www.answermeapd.blogspot.com\'',
                                          font='arial 12 italic bold', bg='#929da1', fg='white')
        self.bottom_label.place(x=50, y=200)

        # ======= Thank you label =======
        self.bottom_label = tkinter.Label(self.bottom_frame, text='Thank You for Using This Application!',font='arial 12 italic bold', bg='#929da1', fg='white')
        self.bottom_label.place(x=150, y=290)

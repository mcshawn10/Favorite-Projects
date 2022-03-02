import tkinter as tk
from tkinter import *
from amz_BOT import *


black = '#0b0c10'
charcoal = '#1f2833'
grey = '#c5c6c7'
light_blue = '#66fcf1'
blue_grey = '#45a29e'


#PATH = "C:\Python\chromedriver.exe"
PATH = "C:\Python\chromedriver_win32\chromedriver.exe"
shawn = 1


class MainApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (LoginPage, ShoppingPage):
            frame = F(container, self)  # turn to LoginPage

            self.frames[F] = frame  # turn to LoginPage
            frame.grid(row=0, column=0, sticky="nsew")

            self.show_frame(LoginPage)  # turn to LoginPage

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class ShoppingPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        canvas = tk.Canvas(self, width=1000, height=700)
        canvas.grid(columnspan=7, rowspan=6)

        frame = tk.Frame(self, bg=charcoal)
        frame.place(relwidth=1, relheight=1)

        Title = Label(frame, text="Amazon Auto Shopper",
                      fg=black, font="Century 24 bold",
                      bg=light_blue, relief="groove")
        Title.pack()

        

        item_entry = tk.Entry(frame, font=26, bg=grey, highlightthickness=4)
        item_entry.config(highlightbackground=light_blue,
                          highlightcolor=light_blue)
        item_entry.place(relx=0.25, rely=0.3, relwidth=0.3, relheight=0.075)

        item_BUTTON = tk.Button(self, text="Add Item", fg=black, font="Verdana 12 bold",
                                bg=light_blue, relief="groove",
                                command=lambda: box_list.insert(END, item_entry.get()))
        item_BUTTON.place(relx=0.64, rely=0.3, relwidth=0.1, relheight=0.075)

        box_list = tk.Listbox(frame, height=20, bd=4, width=60, yscrollcommand=True,
                              highlightcolor=light_blue, selectmode=SINGLE,
                              font="Verdana 10")
        box_list.config(highlightcolor=blue_grey,
                        highlightbackground=blue_grey)
        box_list.place(relx=0.25, rely=0.4)

        REMOVE_item = tk.Button(frame, text="REMOVE", fg=black,
                                font="Verdana 16 bold",
                                bg=light_blue, relief="groove",
                                command=lambda: box_list.delete(ANCHOR))
        REMOVE_item.place(relx=0.25, rely=0.9)

        complete_button = tk.Button(frame, text="ORDER",  # will extract items in Listbox to an array
                                    font="Verdana 16 bold",
                                    bg=light_blue, relief="groove",
                                    command=lambda: self.gotoAMZ(box_list.get(0, END)))
        complete_button.place(relx=0.63, rely=0.9)

        back_button = tk.Button(frame, text="BACK", fg=black,
                                font="Verdana 16 bold",
                                bg=light_blue, relief="groove",
                                command=lambda: [controller.show_frame(LoginPage)])
        back_button.place(relx = 0.1, rely = 0.05)
        
        

    def DELETE(self, item):
        item.delete(ANCHOR)

    def ptype(self, o):
        print(type(o))
        print(len(o))

    def gotoAMZ(self, wl):
        amz = WebShopping(shawn, webdriver.Chrome(PATH), wl)
        amz.login()
        amz.search_items()


class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        canvas = tk.Canvas(self, width=1000, height=700)
        canvas.grid(columnspan=10, rowspan=6)

        frame = tk.Frame(self, bg=charcoal)
        frame.place(relwidth=1, relheight=1)

        Title = Label(frame, text="Amazon Auto Shopper",
                      fg=black, font="Century 24 bold",
                      bg=light_blue, relief="groove")
        Title.pack()

        signIn_label = tk.Label(frame, text="Login",
                                font="Century 40 bold", fg="white", bg=charcoal)
        signIn_label.place(relx=0.43, rely=0.3)

        email_entry = tk.Entry(frame, font=26, bg=grey,
                               highlightthickness=4)
        email_entry.config(highlightbackground=light_blue,
                           highlightcolor=light_blue)
        email_entry.place(relx=0.5, rely=0.45,
                          relwidth=0.3, relheight=0.075)

        email_label = tk.Label(frame, text="Email",
                               font="Verdana 14 bold", bg=light_blue,
                               borderwidth=4, relief="solid")

        email_label.place(relx=0.28, rely=0.45,
                          relwidth=0.2, relheight=0.075)

        password_entry = tk.Entry(frame, show="*", font=26, bg=grey, highlightthickness=4)

        password_entry.config(highlightbackground=light_blue,
                              highlightcolor=light_blue)
        password_entry.place(relx=0.5, rely=0.55,
                             relwidth=0.3, relheight=0.075)

        password_label = tk.Label(frame, text="Password",
                                  font="Verdana 14 bold", bg=light_blue,
                                  borderwidth=4, relief="solid")
        password_label.place(relx=0.28, rely=0.55,
                             relwidth=0.2, relheight=0.075)

        login_button = tk.Button(frame, text="LOGIN", fg=black, font="Verdana 14 bold",
                                 bg=light_blue, relief="raised", borderwidth=4,
                                 command=lambda: [controller.show_frame(ShoppingPage),
                                                  self.Amazon_Login(email_entry.get(),
                                                  password_entry.get())])
        login_button.place(relx=0.45, rely=0.7, relwidth=0.1, relheight=0.075)

    def Amazon_Login(self, e, p):
        global shawn
        shawn = UserCredentials(e, p)
        


#  driver code
app = MainApp()
app.mainloop()

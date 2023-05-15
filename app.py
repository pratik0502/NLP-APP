from tkinter import *
from mydb import Database
from tkinter import messagebox
from myapi import Api
class NLPApp:

    def __init__(self):

        self.dbo = Database()
        #login gui to load
        self.root = Tk()
        self.apio = Api()
        self.root.title('NLP APP')

        self.root.iconbitmap('resources/favicon.ico')

        self.root.geometry('1138x680')

        # self.root.configure(bg='red')


        self.login_gui()



    def login_gui(self):

        self.clear()

        bg_image = PhotoImage(file='resources/space.png')
        bg_label = Label(self.root, image=bg_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # for NLP title box

        heading_parent = Label(bg_label, bg=bg_label['background'])
        heading_parent.place(relx=0.5, rely=0.2, anchor=CENTER)


        heading = Label(heading_parent, text='NLP APP', fg='white', font=('verdana', 40, 'bold'))
        heading.configure(bd=0, bg="#%02x%02x%02x" % (0, 0, 0))
        heading.pack()

        # Enter Email Text
        label1_parent = Label(bg_label, bg=bg_label['background'])
        label1_parent.place(relx=0.5, rely=0.4, anchor=CENTER)

        label1 = Label(label1_parent, text='Enter Email', fg='white', font=('verdana',18))
        label1.configure(bd=0, bg="#%02x%02x%02x" % (0, 0, 0))
        label1.pack()

        # entry box of email

        ent_parent = Label(bg_label, bg=bg_label['background'])
        ent_parent.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.email_input = Entry(ent_parent,width=50)
        self.email_input.pack(ipady=3)

        # Text for Password
        label2_parent = Label(bg_label, bg=bg_label['background'])
        label2_parent.place(relx=0.5, rely=0.6, anchor=CENTER)

        label2 = Label(label2_parent, text='Enter Password', fg='white', font=('verdana', 18))
        label2.configure(bd=0, bg="#%02x%02x%02x" % (0, 0, 0))
        label2.pack()

        # Entry box for password

        ent_pass_parent = Label(bg_label, bg=bg_label['background'])
        ent_pass_parent.place(relx=0.5, rely=0.7, anchor=CENTER)

        self.pass_input = Entry(ent_pass_parent, width=50,show='*')
        self.pass_input.pack(ipady=3)

        # Login button

        button_parent = Label(bg_label, bg=bg_label['background'])
        button_parent.place(relx=0.5, rely=0.85, anchor=CENTER)

        login_btn = Button(button_parent, text='LogIn', fg='white', font=('verdana', 15),command=self.perform_login)
        login_btn.configure(bd=0, bg="#%02x%02x%02x" % (0, 0, 0))
        login_btn.pack(ipadx=50)

        #  sign up button

        sgup_button_parent = Label(bg_label, bg=bg_label['background'])
        sgup_button_parent.place(relx=0.9, rely=0.85, anchor=CENTER)

        sglogin_btn = Button(sgup_button_parent, text='Sign UP', fg='white', font=('verdana', 10),command=self.register_gui)
        sglogin_btn.configure(bd=0, bg="#%02x%02x%02x" % (0, 0, 0))
        sglogin_btn.pack(ipadx=20)

        self.root.mainloop()

    def register_gui(self):
        self.clear()

        bg_image = PhotoImage(file='resources/space.png')
        bg_label = Label(self.root, image=bg_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)


        heading_parent = Label(bg_label, bg=bg_label['background'])
        heading_parent.place(relx=0.5, rely=0.2, anchor=CENTER)

        heading = Label(heading_parent, text='NLP APP', fg='white', font=('verdana', 40, 'bold'))
        heading.configure(bd=0, bg="#%02x%02x%02x" % (0, 0, 0))
        heading.pack()

        # name text

        label0_parent = Label(bg_label, bg=bg_label['background'])
        label0_parent.place(relx=0.2, rely=0.4, anchor=CENTER)

        label0 = Label(label0_parent, text='Enter Name', fg='white', font=('verdana', 15))
        label0.configure(bd=0, bg="#%02x%02x%02x" % (0, 0, 0))
        label0.pack()

        # entry box of name

        ent_parent0 = Label(bg_label, bg=bg_label['background'])
        ent_parent0.place(relx=0.7, rely=0.4, anchor=CENTER)

        self.name_input = Entry(ent_parent0, width=50)
        self.name_input.pack(ipady=3)

        # email text

        label1_parent = Label(bg_label, bg=bg_label['background'])
        label1_parent.place(relx=0.2, rely=0.5, anchor=CENTER)

        label1 = Label(label1_parent, text='Enter Email', fg='white', font=('verdana', 15))
        label1.configure(bd=0, bg="#%02x%02x%02x" % (0, 0, 0))
        label1.pack()

        # entry box of email

        ent_parent1 = Label(bg_label, bg=bg_label['background'])
        ent_parent1.place(relx=0.7, rely=0.5, anchor=CENTER)

        self.email_input = Entry(ent_parent1, width=50)
        self.email_input.pack(ipady=3)

        # password text

        label2_parent = Label(bg_label, bg=bg_label['background'])
        label2_parent.place(relx=0.2, rely=0.6, anchor=CENTER)

        label2 = Label(label2_parent, text='Enter Password', fg='white', font=('verdana', 15))
        label2.configure(bd=0, bg="#%02x%02x%02x" % (0, 0, 0))
        label2.pack()

        # entry box of password

        ent_parent1 = Label(bg_label, bg=bg_label['background'])
        ent_parent1.place(relx=0.7, rely=0.6, anchor=CENTER)

        self.pass_input = Entry(ent_parent1, width=50)
        self.pass_input.pack(ipady=3)

        #  sign up button

        sgup_button_parent = Label(bg_label, bg=bg_label['background'])
        sgup_button_parent.place(relx=0.5, rely=0.8, anchor=CENTER)

        sglogin_btn = Button(sgup_button_parent, text='Sign UP', fg='white', font=('verdana', 18),command=self.perform_registration)
        sglogin_btn.configure(bd=0, bg="#%02x%02x%02x" % (0, 0, 0))
        sglogin_btn.pack(ipadx=20)

        self.root.mainloop()

    def clear(self):
        # to clear the existing gui after clicking on button

        for i in self.root.winfo_children():
            i.destroy()

    def perform_registration(self):
#         to fetch the data from the dialog box
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.pass_input.get()

        resp = self.dbo.add_data(name,email,password)
        if resp==1:
            messagebox.showinfo('Success','Registration Successful. You can login now')
        else:
            messagebox.showerror('Error','Email already exists')

        self.login_gui()

    def perform_login(self):

        email = self.email_input.get()
        password = self.pass_input.get()

        responce = self.dbo.search(email,password)

        if responce == 1:
            messagebox.showinfo('Success','Login Successful')
            self.home_gui()
        else:
            messagebox.showerror('Error','Incorrect Email/Password')

    def home_gui(self):
        self.clear()

        bg_image = PhotoImage(file='resources/space.png')
        bg_label = Label(self.root, image=bg_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        heading_parent = Label(bg_label, bg=bg_label['background'])
        heading_parent.place(relx=0.1, rely=0.1, anchor=CENTER)

        heading = Label(heading_parent, text='NLP APP', fg='white', font=('verdana', 30, 'bold'))
        heading.configure(bd=0, bg="#%02x%02x%02x" % (0, 0, 0))
        heading.pack()

        # sentiment button

        sen_button_parent = Label(bg_label, bg=bg_label['background'])
        sen_button_parent.place(relx=0.5, rely=0.3, anchor=CENTER)

        sen_btn = Button(sen_button_parent, text='Sentiment Analysis', fg='white', font=('verdana', 15),command=self.sentiment_gui)
        sen_btn.configure(bd=0, bg="#%02x%02x%02x" % (0, 0, 0))
        sen_btn.pack(ipadx=20)

        # ner button

        ner_button_parent = Label(bg_label, bg=bg_label['background'])
        ner_button_parent.place(relx=0.5, rely=0.5, anchor=CENTER)

        ner_btn = Button(ner_button_parent, text='Named Entity Recognition', fg='white', font=('verdana', 15),command=self.ner_gui)
        ner_btn.configure(bd=0, bg="#%02x%02x%02x" % (0, 0, 0))
        ner_btn.pack(ipadx=20)

        # emotion button

        em_button_parent = Label(bg_label, bg=bg_label['background'])
        em_button_parent.place(relx=0.5, rely=0.7, anchor=CENTER)

        em_btn = Button(em_button_parent, text='Emotion Prediction', fg='white', font=('verdana', 15),command=self.emj_detection)
        em_btn.configure(bd=0, bg="#%02x%02x%02x" % (0, 0, 0))
        em_btn.pack(ipadx=20)

        # logout button

        lg_button_parent = Label(bg_label, bg=bg_label['background'])
        lg_button_parent.place(relx=0.9, rely=0.9, anchor=CENTER)

        lg_btn = Button(lg_button_parent, text='Log Out', fg='white', font=('verdana', 11),command=self.login_gui)
        lg_btn.configure(bd=0, bg="#%02x%02x%02x" % (0, 0, 0))
        lg_btn.pack(ipadx=20)

        self.root.mainloop()

    def sentiment_gui(self):

        self.clear()

        bg_image = PhotoImage(file='resources/space.png')
        bg_label = Label(self.root, image=bg_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        heading_parent = Label(bg_label, bg=bg_label['background'])
        heading_parent.place(relx=0.04, rely=0.05, anchor=CENTER)

        heading = Label(heading_parent, text='NLP APP', fg='white', font=('verdana',15, 'bold'))
        heading.configure(bd=0, bg="#%02x%02x%02x" % (0, 0, 0))
        heading.pack()

        heading_parent2 = Label(bg_label, bg=bg_label['background'])
        heading_parent2.place(relx=0.5, rely=0.1, anchor=CENTER)

        heading2 = Label(heading_parent2, text='Sentiment Analysis', fg='white', font=('verdana',30, 'bold'))
        heading2.configure(bd=0, bg="#%02x%02x%02x" % (0, 0, 0))
        heading2.pack()

        # enter text Text

        label1_parent = Label(bg_label, bg=bg_label['background'])
        label1_parent.place(relx=0.3, rely=0.20, anchor=CENTER)

        label1 = Label(label1_parent, text='Enter Text', fg='white', font=('verdana', 13))
        label1.configure(bd=0, bg="#%02x%02x%02x" % (0, 0, 0))
        label1.pack()

        # entry box

        ent_parent1 = Label(bg_label, bg=bg_label['background'])
        ent_parent1.place(relx=0.5, rely=0.30, anchor=CENTER)

        self.ent_txt_input = Entry(ent_parent1, width=50)
        self.ent_txt_input.pack(ipady=30,ipadx=70)

        # analyze button

        anz_button_parent = Label(bg_label, bg=bg_label['background'])
        anz_button_parent.place(relx=0.5, rely=0.5, anchor=CENTER)

        anz_btn = Button(anz_button_parent, text='Analyze Sentiment', fg='white', font=('verdana', 13,'bold'), command=self.do_sentiment_analysis)
        anz_btn.configure(bd=0, bg="#%02x%02x%02x" % (0, 0, 0))
        anz_btn.pack(ipadx=20)

        # result

        res_parent = Label(bg_label, bg=bg_label['background'])
        res_parent.place(relx=0.5, rely=0.7, anchor=CENTER)

        self.sent_res = Label(res_parent, text='', fg='white', font=('verdana', 13))
        self.sent_res.configure(bd=0, bg="#%02x%02x%02x" % (0, 0, 0))
        self.sent_res.pack()


        # back button

        bck_button_parent = Label(bg_label, bg=bg_label['background'])
        bck_button_parent.place(relx=0.9, rely=0.9, anchor=CENTER)

        bck_btn = Button(bck_button_parent, text='Back', fg='white', font=('verdana', 11), command=self.home_gui)
        bck_btn.configure(bd=0, bg="#%02x%02x%02x" % (0, 0, 0))
        bck_btn.pack(ipadx=20)

        self.root.mainloop()

    def do_sentiment_analysis(self):

        text = self.ent_txt_input.get()
        result = self.apio.sentiment_analysis(text)
        txt = ''
        for key, value in result['sentiment'].items():
            txt = txt + (f"{key}: {value * 100:.2f}%") +'\n'

        self.sent_res['text'] = txt


    def ner_gui(self):
        self.clear()

        bg_image = PhotoImage(file='resources/space.png')
        bg_label = Label(self.root, image=bg_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        heading_parent = Label(bg_label, bg=bg_label['background'])
        heading_parent.place(relx=0.04, rely=0.05, anchor=CENTER)

        heading = Label(heading_parent, text='NLP APP', fg='white', font=('verdana', 15, 'bold'))
        heading.configure(bd=0, bg="#%02x%02x%02x" % (0, 0, 0))
        heading.pack()

        heading_parent2 = Label(bg_label, bg=bg_label['background'])
        heading_parent2.place(relx=0.5, rely=0.1, anchor=CENTER)

        heading2 = Label(heading_parent2, text='Named Entity Recognition', fg='white', font=('verdana', 30, 'bold'))
        heading2.configure(bd=0, bg="#%02x%02x%02x" % (0, 0, 0))
        heading2.pack()

        # enter text Text

        label1_parent = Label(bg_label, bg=bg_label['background'])
        label1_parent.place(relx=0.3, rely=0.20, anchor=CENTER)

        label1 = Label(label1_parent, text='Enter Text', fg='white', font=('verdana', 13))
        label1.configure(bd=0, bg="#%02x%02x%02x" % (0, 0, 0))
        label1.pack()

        # entry box

        ent_parent1 = Label(bg_label, bg=bg_label['background'])
        ent_parent1.place(relx=0.5, rely=0.30, anchor=CENTER)

        self.ent_txt_input = Entry(ent_parent1, width=50)
        self.ent_txt_input.pack(ipady=30, ipadx=70)

        # analyze button

        anz_button_parent = Label(bg_label, bg=bg_label['background'])
        anz_button_parent.place(relx=0.5, rely=0.5, anchor=CENTER)

        anz_btn = Button(anz_button_parent, text='Analyze Named Entity', fg='white', font=('verdana', 13, 'bold'),
                         command=self.do_ner_analysis)
        anz_btn.configure(bd=0, bg="#%02x%02x%02x" % (0, 0, 0))
        anz_btn.pack(ipadx=20)

        # result

        ner_res_parent = Label(bg_label, bg=bg_label['background'])
        ner_res_parent.place(relx=0.5, rely=0.7, anchor=CENTER)

        self.ner_sent_res = Label(ner_res_parent, text='', fg='white', font=('verdana', 13))
        self.ner_sent_res.configure(bd=0, bg="#%02x%02x%02x" % (0, 0, 0))
        self.ner_sent_res.pack()

        # back button

        bck_button_parent = Label(bg_label, bg=bg_label['background'])
        bck_button_parent.place(relx=0.9, rely=0.9, anchor=CENTER)

        bck_btn = Button(bck_button_parent, text='Back', fg='white', font=('verdana', 11), command=self.home_gui)
        bck_btn.configure(bd=0, bg="#%02x%02x%02x" % (0, 0, 0))
        bck_btn.pack(ipadx=20)


        self.root.mainloop()

    def do_ner_analysis(self):

        text = self.ent_txt_input.get()
        result = self.apio.ner(text)
        txt =''
        for entity in result['entities']:
            txt = txt + (f"{entity['category']} --> {entity['name']}") +'\n'

        self.ner_sent_res['text'] = txt


    def emj_detection(self):

            self.clear()

            bg_image = PhotoImage(file='resources/space.png')
            bg_label = Label(self.root, image=bg_image)
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)

            heading_parent = Label(bg_label, bg=bg_label['background'])
            heading_parent.place(relx=0.04, rely=0.05, anchor=CENTER)

            heading = Label(heading_parent, text='NLP APP', fg='white', font=('verdana', 15, 'bold'))
            heading.configure(bd=0, bg="#%02x%02x%02x" % (0, 0, 0))
            heading.pack()

            heading_parent2 = Label(bg_label, bg=bg_label['background'])
            heading_parent2.place(relx=0.5, rely=0.1, anchor=CENTER)

            heading2 = Label(heading_parent2, text='Emotion Detection', fg='white', font=('verdana', 30, 'bold'))
            heading2.configure(bd=0, bg="#%02x%02x%02x" % (0, 0, 0))
            heading2.pack()

            # enter text Text

            label1_parent = Label(bg_label, bg=bg_label['background'])
            label1_parent.place(relx=0.3, rely=0.20, anchor=CENTER)

            label1 = Label(label1_parent, text='Enter Text', fg='white', font=('verdana', 13))
            label1.configure(bd=0, bg="#%02x%02x%02x" % (0, 0, 0))
            label1.pack()

            # entry box

            ent_parent1 = Label(bg_label, bg=bg_label['background'])
            ent_parent1.place(relx=0.5, rely=0.30, anchor=CENTER)

            self.ent_txt_input = Entry(ent_parent1, width=50)
            self.ent_txt_input.pack(ipady=30, ipadx=70)

            # analyze button

            anz_button_parent = Label(bg_label, bg=bg_label['background'])
            anz_button_parent.place(relx=0.5, rely=0.5, anchor=CENTER)

            anz_btn = Button(anz_button_parent, text='Detect Emotion', fg='white', font=('verdana', 13, 'bold'),
                             command=self.do_emj_detection)
            anz_btn.configure(bd=0, bg="#%02x%02x%02x" % (0, 0, 0))
            anz_btn.pack(ipadx=20)

            # result

            emj_res_parent = Label(bg_label, bg=bg_label['background'])
            emj_res_parent.place(relx=0.5, rely=0.7, anchor=CENTER)

            self.emj_sent_res = Label(emj_res_parent, text='', fg='white', font=('verdana', 13))
            self.emj_sent_res.configure(bd=0, bg="#%02x%02x%02x" % (0, 0, 0))
            self.emj_sent_res.pack()

            # back button

            bck_button_parent = Label(bg_label, bg=bg_label['background'])
            bck_button_parent.place(relx=0.9, rely=0.9, anchor=CENTER)

            bck_btn = Button(bck_button_parent, text='Back', fg='white', font=('verdana', 11), command=self.home_gui)
            bck_btn.configure(bd=0, bg="#%02x%02x%02x" % (0, 0, 0))
            bck_btn.pack(ipadx=20)

            self.root.mainloop()

    def do_emj_detection(self):

        text = self.ent_txt_input.get()
        result = self.apio.emotion_prediction(text)

        txt = ''
        for emotion, score in result['emotion'].items():
            percentage = score * 100
            txt = txt + (f"{emotion}: {percentage:.2f}%") + '\n'

        self.emj_sent_res['text'] = txt










mlp = NLPApp()

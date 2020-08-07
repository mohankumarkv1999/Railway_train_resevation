from tkinter import *
import pymysql
class bank:
    def __init__(self, root):
        self.frame1 = Frame(root, width=1000, height=1000)
        self.frame1.propagate(0)
        self.frame1.pack()
        self.button1 = Button(self.frame1, text='WELCOME TO MOHAN BANK', font=('roman', 70, 'bold italic'), width=500,
                              height=2, bg='white', fg='black')
        self.text1 = Text(self.frame1, width=100, height=10, font=('verdana', 14, 'bold'), bg='white', fg='black')
        self.text1.insert(END,
                          'YOU ARE IN MOHAN BANK\n\t AND THE FOUNDER OF THIS BANK IS MOHAN KUMAR KV \n\t\t\t if you want to continue press continue')
        self.button2 = Button(self.frame1, text='CONTINUE', font=('verdana', 14, 'bold'), width=10, height=3, bg='blue',
                              fg='black', command=self.user)
        self.button3 = Button(self.frame1, text='qxit', font=('verdana', 14, 'bold'), width=7, height=2, bg='blue',
                              fg='black', command=quit)
        self.button1.pack()
        self.text1.pack()
        self.button2.pack()
        self.button3.place(x=600, y=600, width=80, height=90)

    def user(self):
        self.frame1.destroy()
        self.frame1 = Frame(root, width=1000, height=1000)
        self.frame1.pack()
        self.text2 = Text(self.frame1, width=17, height=1, font=('roman', 52, 'bold italic'), bg='blue')
        self.text2.insert(END, 'THE MOHAN BANK')
        self.text2.place(x=250, y=150)
        self.text3 = Text(self.frame1, width=36, height=1, font=('verdana', 27, 'bold'))
        self.text3.insert(END, 'IF YOU ARE OLD USER THEN LOGIN ==>')
        self.text3.place(x=4, y=300)
        self.button4 = Button(self.frame1, text='LOGIN', font=('verdana', 10, 'bold'), width=14, height=2, bg='pink',
                              fg='black', command=self.olduser)
        self.button4.place(x=800, y=400)
        self.text4 = Text(self.frame1, width=36, height=1, font=('verdana', 27, 'bold'))
        self.text4.insert(END, 'IF YOU ARE NEW USER THEN SIGN IN ==>')
        self.text4.place(x=4, y=500)
        self.button5 = Button(self.frame1, width=14, height=2, text='SIGN IN', font=('verdana', 10, 'bold'), bg='pink',
                              fg='black', command=self.newuser)
        self.button5.place(x=800, y=600)

    def olduser(self):
        self.frame1.destroy()
        self.frame1 = Frame(root, width=1000, height=1000)
        self.frame1.pack()
        self.text5 = Text(self.frame1, width=17, height=1, font=('roman', 52, 'bold italic'), bg='blue')
        self.text5.insert(END, 'THE MOHAN BANK')
        self.text5.place(x=250, y=20)
        self.text6 = Text(self.frame1, width=30, height=1, font=('verdana', 13, 'bold'))
        self.text6.insert(END, 'ENTER YOU ACCOUNT NO ::')
        self.text6.place(x=2, y=150)
        self.text7 = Text(self.frame1, width=33, height=1, font=('verdana', 13, 'bold'))
        self.text7.insert(END, 'ENTER YOU ACCOUNT PASSWORD ::')
        self.text7.place(x=2, y=250)
        self.entry1 = Entry(self.frame1, width=50, fg='black', bg='yellow', font=('arial', 12))
        self.entry1.place(x=470, y=150)
        self.entry2 = Entry(self.frame1, width=50, fg='black', bg='yellow', font=('arial', 12))
        self.entry2.place(x=470, y=250)
        self.entry2.bind("<Return>", self.acprn)
        self.button7 = Button(self.frame1, width=13, height=2, text='<<== BACK', fg='blue',
                              font=('verdana', 10, 'bold'), command=self.user)
        self.button7.place(x=30, y=500)

    def acprn(self, event):
        eno = self.entry1.get()
        password = self.entry2.get()
        self.match(int(eno), int(password))

    def match(self, eno, password):
        conn = pymysql.connect(host='localhost', database='world', user='root', password='7338272260ksv')
        cursor = conn.cursor()
        str = "select * from accounttab where eno & password ='%d'&'%d'"
        args = (eno, password)
        cursor.execute(str % args)
        row = cursor.fetchone()
        if row is not None:
            res = 1
        else:
            res = 0
        if res == 1:
            lbl = Label(text='YES YOUR ACCOUNT IS PRESSENT-->', font=('arial', 14)).place(x=300, y=400)
            self.button3 = Button(self.frame1, text='NEXT -->', width=20, height=1, bg='blue', fg='black',
                                  command=self.language)
            self.button3.place(x=500, y=600)
        elif res == 0:
            lbl = Label(text='ACCOUNT NUMBER AND PASSWORD IS NOT MATCHING RETRY', font=('arial', 14)).place(x=300,
                                                                                                            y=400)
            self.button3 = Button(self.frame1, text='RETRY', width=10, height=1, bg='blue', fg='black',
                                  command=self.olduser)
            self.button3.place(x=500, y=600)

        cursor.close()
        conn.close()

    def language(self):
        self.frame1.destroy()
        self.frame1 = Frame(root, width=1000, height=1000)
        self.frame1.pack()
        self.text5 = Text(self.frame1, width=17, height=1, font=('roman', 52, 'bold italic'), bg='blue')
        self.text5.insert(END, 'THE MOHAN BANK')
        self.text5.place(x=250, y=20)
        self.text8 = Text(self.frame1, width=26, height=1, font=('verdsns', 25, 'bold'), bg='black', fg='white')
        self.text8.insert(END, 'CHOOSE THE LANGUAGE')
        self.text8.place(x=100, y=150)
        self.button8 = Button(self.frame1, width=9, height=2, text='ENGLISH', fg='dark blue',
                              font=('verdana', 13, 'bold'), command=self.acctype)
        self.button8.place(x=800, y=300)
        self.button9 = Button(self.frame1, width=9, height=2, text='KANNADA', fg='dark blue',
                              font=('verdana', 13, 'bold'))
        self.button9.place(x=800, y=379)
        self.button10 = Button(self.frame1, width=9, height=2, text='HINDI', fg='dark blue',
                               font=('verdana', 13, 'bold'))
        self.button10.place(x=800, y=460)
        self.button7 = Button(self.frame1, width=13, height=2, text='<<== BACK', fg='blue',
                              font=('verdana', 10, 'bold'), command=self.olduser)
        self.button7.place(x=30, y=500)

    def acctype(self):
        self.frame1.destroy()
        self.frame1 = Frame(root, width=5000, height=5000)
        self.frame1.pack()
        self.text5 = Text(self.frame1, width=17, height=1, font=('roman', 52, 'bold italic'), bg='blue')
        self.text5.insert(END, 'THE MOHAN BANK')
        self.text9 = Text(self.frame1, width=26, height=1, font=('verdana', 25, 'bold'), fg='black', bg='pink')
        self.text9.insert(END, 'CHOOSE YOUR ACCOUNT TYPE')
        self.text9.place(x=100, y=150)
        self.text5.place(x=250, y=20)
        self.button11 = Button(self.frame1, width=15, height=1, text='SAVING ACCONT', fg='white', bg='black',
                               font=('verdana', 17, 'bold'), command=self.operation)
        self.button11.place(x=800, y=300)
        self.button12 = Button(self.frame1, width=15, height=1, text='CURRENT ACCONT', bg='black', fg='white',
                               font=('verdana', 17, 'bold'))
        self.button12.place(x=800, y=400)
        self.button7 = Button(self.frame1, width=13, height=2, text='<<== BACK', fg='blue',
                              font=('verdana', 10, 'bold'), command=self.language)
        self.button7.place(x=30, y=500)

    def operation(self):
        self.frame1.destroy()
        self.frame1 = Frame(root, width=5000, height=5000)
        self.frame1.pack()
        self.text5 = Text(self.frame1, width=17, height=1, font=('roman', 52, 'bold italic'), bg='blue')
        self.text5.insert(END, 'THE MOHAN BANK')
        self.text10 = Text(self.frame1, width=30, height=1, font=('verdana', 25, 'bold'), fg='black', bg='pink')
        self.text10.insert(END, 'CHOOSE YOUR THE OPERATION YOU WANT TO PERFORM')
        self.text10.place(x=100, y=150)
        self.text5.place(x=250, y=20)
        self.button13 = Button(self.frame1, width=15, height=1, text='WITHDRAW', fg='white', bg='black',
                               font=('verdana', 17, 'bold'), command=self.withdraw)
        self.button13.place(x=800, y=300)
        self.button13 = Button(self.frame1, width=15, height=1, text='BALANCE', fg='white', bg='black',
                               font=('verdana', 17, 'bold'), command=self.balance)
        self.button13.place(x=800, y=400)
        self.button15 = Button(self.frame1, width=15, height=1, text='DEPOSIT', fg='white', bg='black',
                               font=('verdana', 17, 'bold'), command=self.deposit)
        self.button15.place(x=800, y=600)
        self.button14 = Button(self.frame1, width=15, height=1, text='MINI STATEMENT', fg='white', bg='black',
                               font=('verdana', 17, 'bold'))
        self.button14.place(x=800, y=500)
        self.button7 = Button(self.frame1, width=13, height=2, text='<<== BACK', fg='blue',
                              font=('verdana', 10, 'bold'), command=self.acctype)
        self.button7.place(x=30, y=500)

    def newuser(self):
        self.frame1.destroy()
        self.frame1 = Frame(root, width=5000, height=5000, bg='yellow')
        self.frame1.pack()
        self.text5 = Text(self.frame1, width=60, height=1, font=('japan', 34, 'bold italic'))
        self.text5.insert(END, 'THANK U FOR CHOOSING THIS MOHAN BANK')
        self.text5.place(x=2, y=50)
        self.text5 = Text(self.frame1, width=17, height=1, font=('roman', 52, 'bold italic'), bg='blue')
        self.text5.insert(END, 'THE MOHAN BANK')
        self.text5.place(x=30, y=150)
        lbl = Label(text='ENTER THE ACCOUNT NUMBER -->', font=('Arial', 14)).place(x=8, y=250)
        lbl = Label(text='ENTER TEH ACCOUNT PASSWORD -->', font=('Arial', 14)).place(x=8, y=300)
        lbl = Label(text='ENTER YOUR NAME -->', font=('Arial', 14)).place(x=8, y=350)
        self.entacc = Entry(self.frame1, width=50, fg='black', bg='blue', font=('arial', 12))
        self.entacc.place(x=400, y=250)
        self.entpass = Entry(self.frame1, width=50, fg='black', bg='blue', font=('arial', 12))
        self.entpass.place(x=400, y=300)
        self.entna = Entry(self.frame1, width=50, fg='black', bg='blue', font=('arial', 12))
        self.entna.place(x=400, y=350)
        self.entna.bind("<Return>", self.insacc)
        self.button7 = Button(self.frame1, width=13, height=2, text='<<== BACK', fg='blue',
                              font=('verdana', 10, 'bold'), command=self.user)
        self.button7.place(x=30, y=500)

    def insacc(self, event):
        acc = self.entacc.get()
        pass1 = self.entpass.get()
        nam = self.entna.get()
        bal = 0.0000
        self.insert(int(acc), int(pass1), nam, bal)

    def insert(self, eno, password, ename, balance):
        conn = pymysql.connect(host='localhost', database='world', user='root', password='7338272260ksv')
        cursor = conn.cursor()
        str = "insert into accounttab(eno,password,ename,balance) values('%d','%d','%s','%f')"
        args = (eno, password, ename, balance)
        cursor.execute(str % args)
        conn.commit()
        lbl = Label(text='YOUR ACCOUNT CREATION IS SUCCESS FULL', font=('Arial', 14)).place(x=400, y=500)
        lb2 = Label(text='IF YOU WANT TO CONTINUE THEN LOGIN TO YOUR ACCOUNT --------->', font=('Arial', 14)).place(
            x=20, y=600)
        self.button4 = Button(self.frame1, text='LOGIN -->', font=('verdana', 10, 'bold'), width=14, height=2,
                              bg='pink', fg='black', command=self.olduser)
        self.button4.place(x=700, y=600)
        cursor.close()
        conn.close()

    def withdraw(self):
        self.frame1.destroy()
        self.frame1 = Frame(root, width=1000, height=1000, bg='yellow')
        self.frame1.pack()
        llb = Label(text='pleace enter the account number and password -->', font=('arial', 14)).place(x=2, y=20)
        self.text6 = Text(self.frame1, width=28, height=1, font=('arial', 14, 'bold'))
        self.text6.insert(END, 'ENTER YOU ACCOUNT NO ::')
        self.text6.place(x=2, y=60)
        self.text7 = Text(self.frame1, width=28, height=1, font=('arial', 14, 'bold'))
        self.text7.insert(END, 'ENTER YOU ACCOUNT PASSWORD ::')
        self.text7.place(x=2, y=100)
        self.entry1 = Entry(self.frame1, width=50, fg='black', bg='pink', font=('arial', 12))
        self.entry1.place(x=350, y=60)
        self.entry2 = Entry(self.frame1, width=50, fg='black', bg='pink', font=('arial', 12))
        self.entry2.place(x=350, y=100)
        self.text8 = Text(self.frame1, width=28, height=1, font=('arial', 14, 'bold'))
        self.text8.insert(END, 'ENTER THE AMOUNT-->')
        self.text8.place(x=2, y=240)
        lb = Label(text='please enter the amount as 100 or 500 or 1000', font=('arial', 14)).place(x=2, y=140)
        self.entry3 = Entry(self.frame1, width=50, fg='black', bg='pink', font=('arial', 12))
        self.entry3.place(x=350, y=240)
        self.entry3.bind("<Return>", self.security)
        self.button7 = Button(self.frame1, width=13, height=2, text='<<== BACK', fg='blue',
                              font=('verdana', 10, 'bold'), command=self.operation)
        self.button7.place(x=30, y=500)

    def security(self, event):
        eno = self.entry1.get()
        password = self.entry2.get()
        balance = self.entry3.get()
        self.secapp(int(eno), int(password), int(balance))

    def secapp(self, eno, password, dec):
        conn = pymysql.connect(host='localhost', database='world', user='root', password='7338272260ksv')
        cursor = conn.cursor()
        str = "select * from accounttab where eno & password ='%d'&'%d'"
        args = (eno, password)
        cursor.execute(str % args)
        row = cursor.fetchone()
        if row is not None:
            res = row[3]
        else:
            res = 0;
        if dec <= res:
            if dec == 100:
                str = "update accounttab set balance=balance-100 where eno&password='%d'&'%d'"
            elif dec == 500:
                str = "update accounttab set balance=balance-500 where eno&password='%d'&'%d'"
            elif dec == 1000:
                str = "update accounttab set balance=balance-1000 where eno&password='%d'&'%d'"
            args = (eno, password)
            cursor.execute(str % args)
            row = cursor.fetchone()
            conn.commit()
        else:
            lb1 = Label(text='Your account balance is less then you requred', font=('veradana', 15)).place(x=300, y=300)
        lb4 = Label(text='YOUR TRANSTRACTION IS COMPLETED', font=('veradana', 15)).place(x=200, y=550)
        self.button = Button(self.frame1, width=20, height=1, text='EXIT-->', fg='red', bg='black', command=quit)
        self.button.place(x=700, y=600)
        cursor.close()
        conn.close()

    def balance(self):
        self.frame1.destroy()
        self.frame1 = Frame(root, width=1000, height=1000, bg='yellow')
        self.frame1.pack()
        llb = Label(text='pleace enter the account number and password -->', font=('arial', 14)).place(x=2, y=20)
        self.text6 = Text(self.frame1, width=28, height=1, font=('arial', 14, 'bold'))
        self.text6.insert(END, 'ENTER YOU ACCOUNT NO ::')
        self.text6.place(x=2, y=60)
        self.text7 = Text(self.frame1, width=28, height=1, font=('arial', 14, 'bold'))
        self.text7.insert(END, 'ENTER YOU ACCOUNT PASSWORD ::')
        self.text7.place(x=2, y=100)
        self.entry1 = Entry(self.frame1, width=50, fg='black', bg='pink', font=('arial', 12))
        self.entry1.place(x=350, y=60)
        self.entry2 = Entry(self.frame1, width=50, fg='black', bg='pink', font=('arial', 12))
        self.entry2.place(x=350, y=100)
        self.entry2.bind("<Return>", self.security2)
        self.button7 = Button(self.frame1, width=13, height=2, text='<<== BACK', fg='blue',
                              font=('verdana', 10, 'bold'), command=self.operation)
        self.button7.place(x=30, y=600)

    def security2(self, event):
        eno = self.entry1.get()
        password = self.entry2.get()
        self.prbal(int(eno), int(password))

    def prbal(self, eno, password):
        conn = pymysql.connect(host='localhost', database='world', user='root', password='7338272260ksv')
        cursor = conn.cursor()
        str = "select * from accounttab where eno & password ='%d'&'%d'"
        args = (eno, password)
        cursor.execute(str % args)
        row = cursor.fetchone()
        if row is not None:
            res = 1
        else:
            res = 0
        if res == 1:
            lbl = Label(text='TOTAL BALANCE IS', font=('arial', 14)).place(x=50, y=400)
            lb3 = Label(text='RS   ', bg='yellow', font=('arial', 59)).place(x=200, y=450)
            lb2 = Label(text=row[3], bg='yellow', font=('arial', 59)).place(x=400, y=450)
            lb4 = Label(text='YOUR TRANSTRACTION IS COMPLETED', font=('veradana', 15)).place(x=200, y=550)
            self.button = Button(self.frame1, width=20, height=1, text='EXIT-->', fg='red', bg='black', command=quit)
            self.button.place(x=700, y=600)

        elif res == 0:
            lbl = Label(text='SECURITY CHECKING IS FAILED\t LOGIN ONCE AGAIN', font=('arial', 14)).place(x=50, y=400)
            self.button3 = Button(self.frame1, text='RETRY', width=10, height=1, bg='blue', fg='black',
                                  command=self.olduser)
            self.button3.place(x=400, y=600)
        cursor.close()
        conn.close()

    def deposit(self):
        self.frame1.destroy()
        self.frame1 = Frame(root, width=1000, height=1000, bg='yellow')
        self.frame1.pack()
        llb = Label(text='pleace enter the account number and password -->', font=('arial', 14)).place(x=2, y=20)
        self.text6 = Text(self.frame1, width=28, height=1, font=('arial', 14, 'bold'))
        self.text6.insert(END, 'ENTER YOU ACCOUNT NO ::')
        self.text6.place(x=2, y=60)
        self.text7 = Text(self.frame1, width=28, height=1, font=('arial', 14, 'bold'))
        self.text7.insert(END, 'ENTER YOU ACCOUNT PASSWORD ::')
        self.text7.place(x=2, y=100)
        self.entry1 = Entry(self.frame1, width=50, fg='black', bg='pink', font=('arial', 12))
        self.entry1.place(x=450, y=60)
        self.entry2 = Entry(self.frame1, width=50, fg='black', bg='pink', font=('arial', 12))
        self.entry2.place(x=450, y=100)
        lb = Label(text='please enter the amount as 100 or 500 or 1000', font=('arial', 14)).place(x=2, y=140)
        self.text8 = Text(self.frame1, width=28, height=1, font=('arial', 14, 'bold'))
        self.text8.insert(END, 'ENTER THE AMOUNT TO DEPOSIT-->')
        self.text8.place(x=2, y=240)
        self.entry3 = Entry(self.frame1, width=50, fg='black', bg='pink', font=('arial', 12))
        self.entry3.place(x=450, y=240)
        self.entry3.bind("<Return>", self.security3)
        self.button7 = Button(self.frame1, width=13, height=2, text='<<== BACK', fg='blue',
                              font=('verdana', 10, 'bold'), command=self.operation)
        self.button7.place(x=30, y=500)

    def security3(self, event):
        eno = self.entry1.get()
        password = self.entry2.get()
        dep = self.entry3.get()
        self.depam(int(eno), int(password), int(dep))

    def depam(self, eno, password, dec):
        conn = pymysql.connect(host='localhost', database='world', user='root', password='7338272260ksv')
        cursor = conn.cursor()
        if dec == 100:
            str = "update accounttab set balance=balance+100 where eno&password='%d'&'%d'"
        elif dec == 500:
            str = "update accounttab set balance=balance+500 where eno&password='%d'&'%d'"
        elif dec == 1000:
            str = "update accounttab set balance=balance+1000 where eno&password='%d'&'%d'"
        args = (eno, password)
        cursor.execute(str % args)
        row = cursor.fetchone()
        conn.commit()
        lb4 = Label(text='YOUR TRANSTRACTION IS COMPLETED', font=('veradana', 15)).place(x=200, y=550)
        self.button = Button(self.frame1, width=20, height=1, text='EXIT-->', fg='red', bg='black', command=quit)
        self.button.place(x=700, y=600)
        cursor.close()
        conn.close()


def quit():
    exit()


root = Tk()
f = bank(root)
root.mainloop()

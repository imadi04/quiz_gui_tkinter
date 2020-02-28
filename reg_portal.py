import mysql.connector
from tkinter import *
import requests

class Quiz:
    def __init__(self):
        self.root = Tk()
        self.root.minsize(500,750)
        self.root.maxsize(500,750)
        
        self.frame=Frame(self.root)
        self.frame.pack()
        self.final_score={1:0,2:0,3:0,4:0,5:0}

        def ShowChoice(q):
            self.final_score[q]=10
            
            #print(self.final_score)

        def total():
            self.frame.destroy()
            self.root.destroy()
            print(self.final_score)
            print(sum(self.final_score.values()))
         
        Label(self.frame, text="PYTHON QUIZ",fg="yellow",bg="red",font=('Helvetica', 14, 'bold')).pack()

        Label(self.frame, text="What is Tkinter?",font=('Helvetica', 11, 'bold')).pack()
        r1=IntVar()
        self.R11 = Radiobutton(self.frame,variable=r1, text="q1Option 1", value=1,command=lambda:ShowChoice(1),font=('Silkscreen', 11,'italic'))
        self.R12 = Radiobutton(self.frame, variable=r1,text="q1Option 2", value=2,font=('Silkscreen', 11,'italic'))
        self.R13 = Radiobutton(self.frame,variable=r1, text="q1Option 3", value=3,font=('Silkscreen', 11,'italic'))
        self.R14 = Radiobutton(self.frame,variable=r1, text="q1Option 4", value=4,font=('Silkscreen', 11,'italic'))
        self.R11.pack(anchor=W)
        self.R12.pack(anchor=W)
        self.R13.pack(anchor=W)
        self.R14.pack(anchor=W)

        Label(self.frame, text="iufhu dhfjdhf",font=('Helvetica', 11, 'bold')).pack()
        r2=IntVar()
        self.R21 = Radiobutton(self.frame,variable=r2, text="sdgf", value=1,font=('Silkscreen', 11,'italic'))
        self.R22 = Radiobutton(self.frame, variable=r2,text="qdfgon 2", value=2,font=('Silkscreen', 11,'italic'))
        self.R23 = Radiobutton(self.frame,variable=r2, text="dfg", value=3,font=('Silkscreen', 11,'italic'))
        self.R24 = Radiobutton(self.frame,variable=r2, text="qsdfg", value=4,command=lambda:ShowChoice(2),font=('Silkscreen', 11,'italic'))
        self.R21.pack(anchor=W)
        self.R22.pack(anchor=W)
        self.R23.pack(anchor=W)
        self.R24.pack(anchor=W)
        

        Label(self.frame, text="iufhu dhfjdhf",font=('Helvetica', 11, 'bold')).pack()
        r3=IntVar()
        self.R31 = Radiobutton(self.frame,variable=r3, text="sdgf", value=1,font=('Silkscreen', 11,'italic'))
        self.R32 = Radiobutton(self.frame, variable=r3,text="qdfgon 2", value=2,font=('Silkscreen', 11,'italic'),command=lambda:ShowChoice(3))
        self.R33 = Radiobutton(self.frame,variable=r3, text="dfg", value=3,font=('Silkscreen', 11,'italic'))
        self.R34 = Radiobutton(self.frame,variable=r3, text="qsdfg", value=4,font=('Silkscreen', 11,'italic'))
        self.R31.pack(anchor=W)
        self.R32.pack(anchor=W)
        self.R33.pack(anchor=W)
        self.R34.pack(anchor=W)

        Label(self.frame, text="iufhu dhfjdhf",font=('Helvetica', 11, 'bold')).pack()
        r4=IntVar()
        self.R41 = Radiobutton(self.frame,variable=r4, text="sdgf", value=1,font=('Silkscreen', 11,'italic'))
        self.R42 = Radiobutton(self.frame, variable=r4,text="qdfgon 2",font=('Silkscreen', 11,'italic'), value=2,command=lambda:ShowChoice(3))
        self.R43 = Radiobutton(self.frame,variable=r4, text="dfg", value=3,font=('Silkscreen', 11,'italic'))
        self.R44 = Radiobutton(self.frame,variable=r4, text="qsdfg", value=4,font=('Silkscreen', 11,'italic'))
        self.R41.pack(anchor=W)
        self.R42.pack(anchor=W)
        self.R43.pack(anchor=W)
        self.R44.pack(anchor=W)
        
        
        
        self.submit = Button(self.frame, text="SUBMIT & QUIT", command=total, fg="white",bg="green")
        self.submit.pack()
        self.root.mainloop()
class Welcome:
    def __init__(self):
        self.conn=mysql.connector.connect(host="localhost",user="root",password="",database="hit")
        self.mycursor=self.conn.cursor()
        self.root=Tk()
        self.root.title("Registration Portal")
        self.root.minsize(400,600) #for fixing min height of window
        self.root.maxsize(400,900) #these two lines fix the window size.
        self.root.configure(background="#0089ae")# for changing window background-color.
        self.label1=Label(self.root,text="Registration Portal",bg="#0089ae",fg="#ffffff")
        self.label1.configure(font=("Constantia",22,"bold"))
        self.label1.pack(pady=(30,10)) #padding-left(x) and top(y)

        self.label2=Label(self.root,text="""How would you like to proceed?
1.Enter 1 to register
2.Enter 2 to login
3.Anything else to exit
""",bg="#0089ae",fg="#ffffff")
        self.label2.configure(font=("Constantia",12,"bold"))
        self.label2.pack(pady=(30,10)) #padding-left(x) and top(y)

        self.user_input=Entry(self.root) #for creating input field
        self.user_input.pack(ipadx=5,ipady=10) #for changing the size of input/entry box x:width, y:height
        self.click=Button(self.root,text="Enter",width=30,height=2,command=lambda:self.user_menu())
        self.click.pack(pady=(15,15))
        #self.user_menu()
        self.root.mainloop()

    def user_menu(self):
        user_input=self.user_input.get()
        if user_input=='1':
            self.register()
        elif user_input=='2':
            self.login()
        else:
            print("Bye Buddy!!")


    def register(self):
        self.regwindow=Tk()
        self.namelabel=Label(self.regwindow,text="Name:")
        self.namelabel.configure(font=("Constantia",12,"bold"))
        self.namelabel.pack()
        self.name=Entry(self.regwindow)
        self.name.pack(ipadx=5,ipady=10)
        print(self.name.get())
        self.emaillabel=Label(self.regwindow,text="Email:")
        self.emaillabel.configure(font=("Constantia",12,"bold"))
        self.emaillabel.pack()
        self.email=Entry(self.regwindow)
        self.email.pack(ipadx=5,ipady=10)
        self.passwordlabel=Label(self.regwindow,text="Password:")
        self.passwordlabel.configure(font=("Constantia",12,"bold"))
        self.passwordlabel.pack()
        self.password=Entry(self.regwindow)
        self.password.pack(ipadx=5,ipady=10)
        self.click=Button(self.regwindow,text="Enter",width=30,height=2,command=lambda:[self.mycursor.execute("INSERT INTO users(user_id,name,email,password) VALUES(NULL,'{}','{}','{}')"
        .format(self.name.get(),self.email.get(),self.password.get())),
        self.conn.commit(),
        self.regwindow.destroy()])                                                                                                 
        self.click.pack(pady=(15,15))
        
        print("Registration successful")

    def validate(self):
        print("entered email:",self.email2.get())
        print("Entered password:",self.password2.get())
        res=self.mycursor.fetchall()
        print(res)
        if len(res)>0:
            fetched_email=res[0][0]
            fetched_password=res[0][1]
            print("Achha:",fetched_email)
            print("Achha:",fetched_password)
            print("Welcome")
            quiz=Quiz()
        else:
            print("Incorrect")    
        


    def login(self):
        self.loginwindow=Tk()
        self.emaillabel2=Label(self.loginwindow,text="Email:")
        self.emaillabel2.configure(font=("Constantia",12,"bold"))
        self.emaillabel2.pack()
        self.email2=Entry(self.loginwindow)
        self.email2.pack(ipadx=5,ipady=10)
        self.passwordlabel2=Label(self.loginwindow,text="Password:")
        self.passwordlabel2.configure(font=("Constantia",12,"bold"))
        self.passwordlabel2.pack()
        self.password2=Entry(self.loginwindow)
        self.password2.pack(ipadx=5,ipady=10)
        print(self.email2.get())
        self.log=Button(self.loginwindow,text="Login",
        command=lambda:[self.mycursor.execute("SELECT * FROM users WHERE email like '{}' AND password LIKE '{}'"
        .format(self.email2.get(),self.password2.get())),self.validate()])
        self.log.pack()
        

        
            
obj=Welcome()

        

from tkinter import *
from myDb import Database
from tkinter import messagebox
from myApi import API
class NLPApp:
    def __init__(self):
        # create database object
        self.dbo=Database() # we made this because due to this we access any method of Database class
        self.apio=API()
        #login ka gui load karna
        #self.root ak variable hai jsma aap tk class k object koa store kr rha hoa.
        self.root=Tk() # Tk() is the main class of tkinter 
        self.root.title("NLPApp") # to change the title
        self.root.iconbitmap(r"D:\Coding Language\Python\Resources\favicon.ico") # to change the icon
        self.root.geometry('350x600') # change the size of gui
        self.root.configure(bg='#34495E') # to change the background colour. We also use hexcode for colour

        self.login_gui()
        self.root.mainloop()  # mainloop ka kaam hota hai ki ya gui koa screen pa hold kr k rkhta hai.

    def login_gui(self):
        self.clear()
        # Heading section
        heading=Label(self.root,text='NLPApp',bg='#34495E',fg='white') # heading of gui
        heading.pack(pady=(30,30)) # to put the heading on gui we use pack,pady is used for, heading mai upar sa ktna gap cheya aur necha sa ktna gap cheya
        heading.configure(font=('verdana','24','bold'))

        # Email section
        label1=Label(self.root,text='Enter Email') # agar hum chta hai kii enter email k side mai emai input lea toa uska liya hmko "grid" use krna hoga
        label1.pack(pady=(10,10))
        # enter email k neecha he gui email input lega

        self.email_input = Entry(self.root,width=50)              # user entry class koa use kr k he user apna input deta hai 
        # isma self ishlya lgaya kyuki ish variable koa hmara class k dusra methods use krenga aur jsma nhi lgaya hai woa bsh ishi method mai use hoga
        self.email_input.pack(pady=(5,10),ipady=4) # for width we put the width in entry class but for height we right in pack by ipady=3 i

        # Password Section
        label2=Label(self.root,text='Enter password')
        label2.pack(pady=(10,10))


        self.pass_input = Entry(self.root,width=50,show='*')        
        self.pass_input.pack(pady=(5,10),ipady=4)

        # to add the button we use Button class
        login_btn=Button(self.root,text='Login',width=30,height=2,command=self.perform_login) # we can put height here
        login_btn.pack(pady=(10,10))

        
        label3=Label(self.root,text='Not a member?')
        label3.pack(pady=(20,10))

        redirect_btn=Button(self.root,text='Register Now',command=self.register_gui) # command means button pa click hua hai and joa = mai likha hai woa open hoga
        redirect_btn.pack(pady=(10,10))



    def register_gui(self):
    #clear the existing gui
        self.clear()
            
        # Heading section
        heading=Label(self.root,text='NLPApp',bg='#34495E',fg='white')
        heading.pack(pady=(30,30)) 
        heading.configure(font=('verdana','24','bold'))

        
        label0=Label(self.root,text='Enter Name') 
        label0.pack(pady=(10,10))
       

        self.name_input = Entry(self.root,width=50)             
        self.name_input.pack(pady=(5,10),ipady=4) 


        label1=Label(self.root,text='Enter Email') 
        label1.pack(pady=(10,10))
       

        self.email_input = Entry(self.root,width=50)             
        self.email_input.pack(pady=(5,10),ipady=4) 

       
        label2=Label(self.root,text='Enter password')
        label2.pack(pady=(10,10))


        self.pass_input = Entry(self.root,width=50,show='*')        
        self.pass_input.pack(pady=(5,10),ipady=4)


        register_btn=Button(self.root,text='Register',width=30,height=2,command=self.perform_registration)
        register_btn.pack(pady=(10,10))

        
        label3=Label(self.root,text='Already a member?')
        label3.pack(pady=(20,10))

        redirect_btn=Button(self.root,text='Login Now',command=self.login_gui)
        redirect_btn.pack(pady=(10,10))
        
    def clear(self):
        for i in self.root.pack_slaves(): # pack_slaves() kya krta hai kii apka gui k upar jtna bhi elements hai unko utha kr lea ata hai
            i.destroy()

    def perform_registration(self):
        # fetch data from the gui
        name = self.name_input.get()
        email=self.email_input.get()
        password=self.pass_input.get()
        response=self.dbo.add_data(name,email,password)
        if response:
            messagebox.showinfo("success","Registration successfull. You can login now")
        else:
            messagebox.showerror('Error','Email already exists')

    def perform_login(self):
        email=self.email_input.get()
        password=self.pass_input.get()

        response = self.dbo.search(email,password)

        if response:
            messagebox.showinfo('success','Login successful')
            self.home_gui()
        else:
            messagebox.showerror('error','Incorrect email/password')

    def home_gui(self):
        self.clear()

        # Heading section
        heading=Label(self.root,text='NLPApp',bg='#34495E',fg='white')
        heading.pack(pady=(30,30)) 
        heading.configure(font=('verdana','24','bold'))


        sentiment_btn=Button(self.root,text='Sentiment Analysis',width=30,height=4,command=self.perform_sentiment)
        sentiment_btn.pack(pady=(10,10))


        ner_btn=Button(self.root,text='Named Entity Recognition',width=30,height=4,command=self.perform_ner)
        ner_btn.pack(pady=(10,10))


        emotion_btn=Button(self.root,text='Emotion Prediction',width=30,height=4,command=self.perform_emotion_prediction)
        emotion_btn.pack(pady=(10,10))


        
        logout_btn=Button(self.root,text='Logout',command=self.login_gui)
        logout_btn.pack(pady=(10,10))

    def perform_sentiment(self):
        self.clear()


        heading=Label(self.root,text='NLPApp',bg='#34495E',fg='white')
        heading.pack(pady=(30,30)) 
        heading.configure(font=('verdana','24','bold'))


        heading2=Label(self.root,text='Sentiment Analysis',bg='#34495E',fg='white')
        heading2.pack(pady=(10,20)) 
        heading2.configure(font=('verdana',20))

        label2=Label(self.root,text='Enter the text')
        label2.pack(pady=(10,10))

        self.sentiment_input = Entry(self.root,width=50)             
        self.sentiment_input.pack(pady=(5,10),ipady=4) 

        sentiment_btn=Button(self.root,text='Analyze Sentiment',command=self.do_sentiment_analysis)
        sentiment_btn.pack(pady=(10,10))

        self.sentiment_result=Label(self.root,text='',bg='#34495E')
        self.sentiment_result.pack(pady=(10,10))
        heading.configure(font=('verdana','16'))

        goback_btn=Button(self.root,text='Go Back',command=self.home_gui)
        goback_btn.pack(pady=(10,10))

    def do_sentiment_analysis(self):
        text=self.sentiment_input.get()
        result=self.apio.sentiment_analysis(text)
        self.sentiment_result['text']=result

    def perform_ner(self):
        self.clear()

        
        heading=Label(self.root,text='NLPApp',bg='#34495E',fg='white')
        heading.pack(pady=(30,30)) 
        heading.configure(font=('verdana','24','bold'))


        heading2=Label(self.root,text='Named Entity Recognition',bg='#34495E',fg='white')
        heading2.pack(pady=(10,20)) 
        heading2.configure(font=('verdana',20))

        label2=Label(self.root,text='Enter the text')
        label2.pack(pady=(10,10))

        self.ner_input = Entry(self.root,width=50)             
        self.ner_input.pack(pady=(5,10),ipady=4) 


        ner_btn=Button(self.root,text='Detect',command=self.do_ner)
        ner_btn.pack(pady=(10,10))

        self.ner_result=Label(self.root,text='',bg='#34495E')
        self.ner_result.pack(pady=(10,10))
        heading.configure(font=('verdana','16'))

        goback_btn=Button(self.root,text='Go Back',command=self.home_gui)
        goback_btn.pack(pady=(10,10))

    def do_ner(self):
        text=self.ner_input.get()
        result=self.apio.NER(text)
        self.ner_result['text']=result

    def perform_emotion_prediction(self):

        self.clear()

        
        heading=Label(self.root,text='NLPApp',bg='#34495E',fg='white')
        heading.pack(pady=(30,30)) 
        heading.configure(font=('verdana','24','bold'))


        heading2=Label(self.root,text='Emotion Prediction',bg='#34495E',fg='white')
        heading2.pack(pady=(10,20)) 
        heading2.configure(font=('verdana',20))

        label2=Label(self.root,text='Enter the text')
        label2.pack(pady=(10,10))

        self.emotion_input = Entry(self.root,width=50)             
        self.emotion_input.pack(pady=(5,10),ipady=4) 


        emotion_btn=Button(self.root,text='Detect',command=self.do_emotion_prediction)
        emotion_btn.pack(pady=(10,10))

        self.emotion_result=Label(self.root,text='',bg='#34495E')
        self.emotion_result.pack(pady=(10,10))
        heading.configure(font=('verdana','16'))

        goback_btn=Button(self.root,text='Go Back',command=self.home_gui)
        goback_btn.pack(pady=(10,10))

    def do_emotion_prediction(self):
        text=self.emotion_input.get()
        result=self.apio.emotion_prediction(text)
        self.emotion_result['text']=result







        






















            
    

















































































        

nlp=NLPApp()
 
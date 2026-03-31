import nlpcloud
class NLPApp:
    database = {}
    def __init__(self):
        print("Hello,How would you like to proceed")
        self.menu()

    def menu(self):
        while True:
            print("1. Register\n2. Login\n3. Exit")
            user_input=int(input())
            if user_input==1:
                self.Register()
            elif user_input==2:
                self.Login()
            else:
                break

    def Register(self):
        name = input("Enter name : ")
        email = input("Email : ")
        password = input("Password : ")
        NLPApp.database[email] = [name,password]
        print("Registered")

    def Login(self):
        user_email=input("Enter your email : ")
        if user_email in NLPApp.database:
            user_pass=input("Enter your password : ")
            if user_pass == NLPApp.database[user_email][1]:
                print("Login Sucessfully")
                self.work()
            else:
                print("Wrong Password")
        else:
            print("Please Register First")
            self.menu()

    def work(self):
        print("Hii, How would you like to proceed")
        self.workMenu()

    def workMenu(self):
        while True:
            print("1. NER\n2. Language Detection\n3. Sentiment Analysis\n4. Logout")
            user_input = int(input())
            if user_input==1:
                self.NER()
            elif user_input==2:
                self.LangDetect()
            elif user_input==3:
                self.SentimentAnalysis()
            else:
                break

    def NER(self):
        para=input("Enter paragraph : ")
        serch_term=input("what would you like ti search : ")


        client = nlpcloud.Client("gpt-oss-120b", "17971a232d219ce93555f66b54d3acbdffc35be2", gpu=True)
        response = client.sentiment(para,searched_entity=serch_term)


        print(response)

    def SentimentAnalysis(self):
        para=input("Enter paragraph : ")

        client = nlpcloud.Client("gpt-oss-120b", "17971a232d219ce93555f66b54d3acbdffc35be2", gpu=True)
        response= client.sentiment(para)
        print(response)

        L=[]
        for i in response['scored_labels']:
            L.append(i['score'])

        index=sorted(list(enumerate(L)),key=lambda x:x[1],reverse=True)[0][0]

        print(response['scored_labels'][index]['label'])



n1 = NLPApp()
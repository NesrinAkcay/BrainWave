
from tkinter import * 
from tkinter import scrolledtext
import database 


   
    
screen=Tk()
screen.title("BrainWave")
screen.geometry("542x696")
screen.config(bg="white")

bw=Frame(screen,width=542,height=696,bg="white")
bw.place(x=10,y=10)

mainframe=Frame(bw,bg="white",width=542,height=1300)
mainframe.place(x=10,y=150)

appResim=PhotoImage(file="BrainWave\\bw.png")
appResim=appResim.subsample(7,7)
appLabel=Label(bw,border=1,image=appResim)
appLabel.pack()
appLabel.place(x=15,y=12)

tema= "Theme"
settings=""
bildirimler= "Notifications"
dil= "Language"
gizlilik= "Privacy"
hesap= "Account"

def SignIn():
    signin=Toplevel(screen,bg="white")
    signin.title("Sign in")
    signin.geometry("542x696")
    silabel=Label(signin,text="Welcome!",font=("Times new Roman",35,"bold"),bg="white")
    silabel.pack()
    silabel.place(x=200,y=100)
    
    bwLabel=Label(signin,text="BrainWave",font=("Times New Roman",35,"bold"),bg="white")
    bwLabel.place(x=140,y=27)
    
    appResim=PhotoImage(file="BrainWave\\bw.png")
    appResim=appResim.subsample(7,7)
    appLabel=Label(signin,border=1,image=appResim)
    appLabel.pack()
    appLabel.place(x=15,y=12)
    
    emailLabel=Label(signin,text="E-mail:",font=("Times New Roman",30,"bold"),fg="white",bg="black")
    emailLabel.pack()
    emailLabel.place(x=50,y=250)
    
    emailEntry=Entry(signin,width=30)
    emailEntry.pack()
    emailEntry.place(x=250,y=275)
    
    passwordLabel=Label(signin,text="Password:",font=("Times New Roman",30,"bold"),fg="white",bg="black")
    passwordLabel.pack()
    passwordLabel.place(x=50,y=320)
    
    passwordEntry=Entry(signin,width=30,show="*")
    passwordEntry.pack()
    passwordEntry.place(x=250,y=345)
    
    submitbuton=Button(signin,text="Submit",font=("Times New Roman",40,"bold") ,fg="white",bg="black",command=SubmitSignUp)
    submitbuton.pack()
    submitbuton.place(x=170,y=500)
    
    def ckeckemail():
        email=emailEntry.get()
        password=passwordEntry.get()
        if email == "nesrin.akcay@gmail.com" and password == "123456789":
            signin.destroy()
            SubmitSignUp()
        else:
            messagebox.showerror("Error","Email or password is incorrect")
        
    submitbuton=Button(signin,text="Submit",font=("Times New Roman",40,"bold") ,fg="white",bg="black",command=ckeckemail)
    submitbuton.pack()
    submitbuton.place(x=170,y=500)
    
def CreateAccount():
    
    createaccount=Toplevel(screen,bg="white")
    createaccount.title("Create Account")
    createaccount.geometry("542x696")
    calabel=Label(createaccount,text="Welcome!",font=("Times new Roman",35,"bold"),bg="white")
    calabel.pack()
    calabel.place(x=200,y=100)
    
    bwLabel=Label(createaccount,text="BrainWave",font=("Times New Roman",35,"bold"),bg="white")
    bwLabel.place(x=140,y=27)
    
    
    appResim=PhotoImage(file="BrainWave\\bw.png")
    appResim=appResim.subsample(7,7)
    appLabel=Label(createaccount,border=1,image=appResim)
    appLabel.pack()
    appLabel.place(x=15,y=12)
    
    
    emailLabel=Label(createaccount,text="E-mail:",font=("Times New Roman",30,"bold"),fg="white",bg="black")
    emailLabel.pack()
    emailLabel.place(x=50,y=250)
    
    emailEntry=Entry(createaccount,width=30)
    emailEntry.pack()
    emailEntry.place(x=250,y=275)
    
    isimLabel=Label(createaccount,text="Full Name:",font=("Times New Roman",30,"bold"),fg="white",bg="black")
    isimLabel.pack()
    isimLabel.place(x=50,y=320)
    
    isimEntry=Entry(createaccount,width=30)
    isimEntry.pack()
    isimEntry.place(x=250,y=275)
    
    passwordLabel=Label(createaccount,text="Password:",font=("Times New Roman",30,"bold"),fg="white",bg="black")
    passwordLabel.pack()
    passwordLabel.place(x=50,y=390)
    
    passwordEntry=Entry(createaccount,width=30)
    passwordEntry.pack()
    passwordEntry.place(x=250,y=345)
    
    signupbuton=Button(createaccount,text="Sign up",font=("Times New Roman",40,"bold") ,fg="white",bg="black",command=SubmitSignUp)
    signupbuton.pack()
    signupbuton.place(x=170,y=500)

def SubmitSignUp():
    submit=Toplevel(screen,bg="white")
    submit.title("Home Page")
    submit.geometry("542x696")
    
    griframe=Frame(submit,bg="light grey",width=542,height=350)
    griframe.place(x=0,y=200)
    
    basliklabel=Label(griframe,text="Enter Title",font=("Times New Roman",50,"bold"))
    basliklabel.place(x=100,y=10)
    
    baslikentry=Entry(griframe,width=30,)
    baslikentry.place(x=170,y=100)
    
    bwLabel=Label(submit,text="BrainWave",font=("Times New Roman",35,"bold"),bg="white")
    bwLabel.place(x=140,y=27)
    
    appResim=PhotoImage(file="BrainWave\\bw.png")
    appResim=appResim.subsample(7,7)
    appLabel=Label(submit,border=1,image=appResim)
    appLabel.pack()
    appLabel.place(x=15,y=12)
    
    searchResim=PhotoImage(file="BrainWave\icons8-search-64-Photoroom.png")
    searchResim=searchResim.subsample(1,1)
    searchLabel=Label(submit,border=0,image=searchResim)
    searchLabel.pack()
    searchLabel.place(x=460,y=20)
    
    searchbuton=Button(submit, image=searchResim,bg="white",borderwidth=0)
    searchbuton.pack()
    searchbuton.place(x=460,y=20)
    
    settingResim=PhotoImage(file="BrainWave\settings-Photoroom.png")
    settingResim=settingResim.subsample(10,10)
    settingLabel=Label(submit,border=0,image=settingResim)
    settingLabel.pack()
    settingLabel.place(x=440,y=625)
    
    settingButton = Button(submit, image=settingResim, bg="white", command=Settings, borderwidth=0)
    settingButton.pack()
    settingButton.place(x=440, y=625)
    
    homepageResim=PhotoImage(file="BrainWave\icons8-home-page-64-Photoroom (2).png")
    homepageLabel=Label(submit,border=0,image=homepageResim)
    homepageLabel.pack()
    homepageLabel.place(x=30,y=620)
    
    addnewResim=PhotoImage(file="BrainWave\icons8-add-new-50-Photoroom.png")
    addnewLabel=Label(submit,border=0,image=addnewResim)
    addnewLabel.pack()
    addnewLabel.place(x=250,y=630)
    
    addnewbuton=Button(submit,image=addnewResim,bg="white",borderwidth=0)
    addnewbuton.pack()
    addnewbuton.place(x=250,y=630)
    
    chatsResim=PhotoImage(file="BrainWave\chat-Photoroom.png")
    chatsResim=chatsResim.subsample(10,10)
    chatsLabel=Label(submit,border=0,image=chatsResim)
    chatsLabel.pack()
    chatsLabel.place(x=140,y=625)
    
    chatbuton=Button(submit,image=chatsResim,bg="white",command=Chat,borderwidth=0)
    chatbuton.pack()
    chatbuton.place(x=140,y=625)
    
    
    profileResim=PhotoImage(file="BrainWave\icons8-person-64-Photoroom.png")
    profileLabel=Label(submit,border=0,image=profileResim)
    profileLabel.pack()
    profileLabel.place(x=330,y=615)
   
    
    
    profilebuton=Button(submit,image=profileResim,bg="white",borderwidth=0,command=Profile)
    profilebuton.pack()
    profilebuton.place(x=330,y=615)
    
    
    


    
    titleLabel=Label(submit,text="Title",font=("Times New Roman,24"))
    
def Chat():
    chat=Toplevel(screen,bg="white")
    chat.title("Chat")
    chat.geometry("542x696")
    cevap = scrolledtext.ScrolledText(chat, width=40, height=20)
    cevap.place(x=60, y=320)
    
    bwLabel=Label(chat,text="BrainWave",font=("Times New Roman",35,"bold"),bg="white")
    bwLabel.place(x=140,y=27)

    appResim=PhotoImage(file="BrainWave\\bw.png")
    appResim=appResim.subsample(7,7)
    appLabel=Label(chat,border=1,image=appResim)
    appLabel.pack()
    appLabel.place(x=15,y=12)

    searchResim=PhotoImage(file="BrainWave\icons8-search-64-Photoroom.png")
    searchResim=searchResim.subsample(1,1)
    searchLabel=Label(chat,border=0,image=searchResim)
    searchLabel.pack()
    searchLabel.place(x=460,y=20)
    
    def mesajGonder():
        konusma=bilgiGirisi.get()
        mesajGoster(konusma)
        cevapVer(konusma)
        bilgiGirisi.delete(0,END)
       
    
    def mesajGoster(msj):
        cevap.insert(END,msj+"\n")

    def cevapVer(soru):
        soru=soru.lower()
        cevaplar = {
     "merhaba": "merhaba, nasilsin?",
     "günaydin": "günaydin, iyi uyudun mu?",
     "iyi aksamlar": "iyi akşamlar, günün nasil geçti?",
     "nasil gidiyor": "her sey yolunda, sen nasilsin?",
     "ne haber": "iyilik, senden ne haber?",
     "bugün hava nasil": "bugün hava güneşli ve sicak",
     "yarin ne yapacaksin": "yarin biraz kitap okumayi planliyorum",
     "en sevdiğin yemek ne": "en sevdiğim yemek pizza",
     "hangi filmi önerirsin": "son zamanlarda izlediğim güzel bir bilim kurgu filmi var",
     "müzik dinliyor musun": "evet, genellikle çalisirken klasik müzik dinliyorum"
    
      }

        yapayZekaCevabi=cevaplar.get(soru,"üzgünüm anlayamadım")
     # get ile soru cevapların içindeyse onu alır, yoksa üzgünüm anlayamadım yazısını alır
 
        mesajGoster(yapayZekaCevabi)
    
    def temizle():
       cevap.delete(1.0, END)

    temizleButon = Button(chat, text="Temizle",fg="white",bg="Black",font=("Times New Roman",20,"bold") ,command=temizle)
    temizleButon.place(x=415, y=520)
    bilgiGirisi=Entry(chat)
    bilgiGirisi.place(x=60,y=170)
    gonder=Button(chat,text="Gönder",fg="white",bg="Black",font=("Times New Roman",20,"bold"),command=mesajGonder)
    gonder.place(x=415,y=600)
    
    
def Profile():
    profile=Toplevel(screen,bg="white")
    profile.title("Profile")
    profile.geometry("542x696")
    bwLabel=Label(profile,text="BrainWave",font=("Times New Roman",35,"bold"),bg="white")
    bwLabel.place(x=140,y=27)
    
    bwLabel=Label(profile,text="BrainWave",font=("Times New Roman",35,"bold"),bg="white")
    bwLabel.place(x=140,y=27)

    appResim=PhotoImage(file="BrainWave\\bw.png")
    appResim=appResim.subsample(7,7)
    appLabel=Label(profile,border=1,image=appResim)
    appLabel.pack()
    appLabel.place(x=15,y=12)

    profilePic = PhotoImage(file="BrainWave\icons8-person-64-Photoroom.png")
    profilePicLabel = Label(profile, image=profilePic)
    profilePicLabel.place(x=230, y=140)
    
    usernameLabel = Label(profile, text="@username", font=("Arial", 16, "bold"), bg="white")
    usernameLabel.place(x=200, y=220)
    
    bioLabel = Label(profile, text="bio...", font=("Arial", 12), bg="white", wraplength=300)
    bioLabel.place(x=250, y=250)
    
    followersLabel = Label(profile, text="Followers: 1000", font=("Arial", 12), bg="white")
    followersLabel.place(x=100, y=290)
    followingLabel = Label(profile, text="Following: 500", font=("Arial", 12), bg="white")
    followingLabel.place(x=300, y=290)
    
    
    
    profilLabel=Label(profile,text="Your Profile",font=("Times New Roman",20,"bold"),bg="white")
    profilLabel.place(x=140,y=80)


def Settings():
    global settings
    settings = Toplevel(screen, bg="white")
    settings.title("Settings")
    settings.geometry("542x696")

    bwLabel = Label(settings, text="BrainWave", font=("Times New Roman", 35, "bold"), bg="white")
    bwLabel.place(x=140, y=27)

    appResim = PhotoImage(file="BrainWave\\bw.png")
    appResim = appResim.subsample(7, 7)
    appLabel = Label(settings, border=1, image=appResim)
    appLabel.pack()
    appLabel.place(x=15, y=12)

    settingsLabel = Label(settings, text="Settings", font=("Times New Roman", 24, "bold"), bg="white")
    settingsLabel.place(x=200, y=100)

    
    themeLabel = Label(settings, text=f"{tema}:", font=("Arial", 16), bg="white")
    themeLabel.place(x=50, y=150)
    themeVar = StringVar(value="Light")
    themeRadio1 = Radiobutton(settings, text="Light", variable=themeVar, value="Light", bg="white")
    themeRadio1.place(x=150, y=150)
    themeRadio2 = Radiobutton(settings, text="Dark", variable=themeVar, value="Dark", bg="white")
    themeRadio2.place(x=250, y=150)

    
    notifLabel = Label(settings, text="Notifications:", font=("Arial", 16), bg="white")
    notifLabel.place(x=50, y=200)
    notifVar = BooleanVar(value=True)
    notifCheck = Checkbutton(settings, text="Enable notifications", variable=notifVar, bg="white")
    notifCheck.place(x=200, y=200)

    
    langLabel = Label(settings, text="Language:", font=("Arial", 16), bg="white")
    langLabel.place(x=50, y=250)
    langVar = StringVar(value="English")
    langMenu = OptionMenu(settings, langVar, "English", "Türkçe", "Deutsch",command= changeLanguage)
    langMenu.place(x=200, y=250)

    
    privacyLabel = Label(settings, text="Privacy:", font=("Arial", 16), bg="white")
    privacyLabel.place(x=50, y=300)
    privacyButton = Button(settings, text="Privacy Settings", bg="lightgray")
    privacyButton.place(x=200, y=300)

    
    accountLabel = Label(settings, text="Account:", font=("Arial", 16), bg="white")
    accountLabel.place(x=50, y=350)
    accountButton = Button(settings, text="Account Settings", bg="lightgray")
    accountButton.place(x=200, y=350)

    

    
    saveButton = Button(settings, text="Save Changes", bg="black", fg="white", font=("Arial", 14, "bold"),command=lambda: saveSettings(langVar))
    saveButton.place(x=200, y=500)

    
    
        
def changeLanguage(selection):
        global tema
        if selection == "Türkçe":
             tema = "Tema"

        else:
             tema = "Theme"    
        
    
def saveSettings(langVar):
    
    global settings
    settings.destroy()
    changeLanguage(langVar.get())
    

bwLabel=Label(bw,text="BrainWave",font=("Times New Roman",35,"bold"),bg="white")
bwLabel.place(x=140,y=27)

girisbuton=Button(mainframe,text="Sign in",font=("Times New Roman",40,"bold") ,fg="white",bg="black",command=SignIn)
girisbuton.pack()
girisbuton.place(x=170,y=100)

hesapbuton=Button(mainframe,text="Create Account",font=("Times New Roman",40,"bold") ,fg="white",bg="black",command=CreateAccount)
hesapbuton.pack()
hesapbuton.place(x=65,y=220)

hlabel=Label(mainframe,text="Don't have an account yet? Create one!",font=("Times New Roman",15),fg="#333333" ,bg="white")
hlabel.place(x=110,y=335)




screen.mainloop()

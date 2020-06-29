from tkinter import *
import tkinter.messagebox as tkMessageBox
import re
import os 
from cryptography.fernet import Fernet
from openSocialMedia import *
#initialisation

Site_name= None
Email=None
Password=None
User_ = None


User = None
Password =None
Site_na = None

#getting data
path = "./data/"


#encrypting/ decrypt data --------------------------------------

def encrypt(Password):
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    Password_encrypted = cipher_suite.encrypt(Password.encode('utf-8'))
    lite=[Password_encrypted,key]
    return lite

def decrypt(Password,key):
    f = Fernet(key)
    Password_decrypted = f.decrypt(Password)
    return Password_decrypted.decode("utf-8")

def load():
    #get the input
    Site_name = textBox1.get()
    Email = textBox2.get()
    Password = textBox3.get()
    User_=textBox00.get()
    print(User_,Site_name,Email,Password)
    liste=[Site_name,Email,Password]
    #encrypt it 
    Password_list_cryptation= encrypt(Password)
    Email_list_cryptation= encrypt(Email)
    path = "./data/"
    path= os.path.join(path, User_)

    liste=[Site_name,Email_list_cryptation[0],Email_list_cryptation[1],Password_list_cryptation[0],Password_list_cryptation[1]]
    if not os.path.exists(path):
                os.makedirs(path)
    
    full_path= path+'/'+Site_name

    for i in liste:
        with open(full_path, 'a') as temp_file:
            if type(i)== bytes:
                temp_file.write(i.decode("utf-8") )
                temp_file.write(" ")
                temp_file.write("\n")
            else:
                temp_file.write(i )
                temp_file.write(" ")
                temp_file.write("\n")

#Upload data from text file ----------------------

def upload():
    #get the input
    User = textBox4.get()
    Password_user = textBox5.get()
    Site_name = textBox6.get()
    print(User,Password_user,Site_name)
    liste=[User,Password_user,Site_name]
    path = "C:/Users/benfa/OneDrive/Bureau/web Scraping/pojects/data/"
    full_path= os.path.join(path, User)
    txtFileName=full_path+'/'+Site_name
    with open(txtFileName, 'r') as file:
        data = file.read().replace('\n', '')
        
    #decrypt the uploaded data ----------------------
    data_list = re.split(' ',data)
    email_decrypted=decrypt( bytes(data_list[1], encoding='utf8'),bytes(data_list[2], encoding='utf8'))
    password_decrypted=decrypt( bytes(data_list[3], encoding='utf8'),bytes(data_list[4], encoding='utf8'))
    print(email_decrypted,'----',password_decrypted)
    if "Facebook" in Site_name:
        OpenFacebook(email_decrypted,password_decrypted)
    if "Instagram" in Site_name:
        OpenInstagram(email_decrypted,password_decrypted)
    if "Twitter" in Site_name:
        OpenTwitter(email_decrypted,password_decrypted)
    if "Linkedin" in Site_name:
        OpenLinkedin(email_decrypted,password_decrypted)
    if "Github" in Site_name:
        OpenGithub(email_decrypted,password_decrypted)


#create window
window = Tk()

# add title 
window.title("Email Storage")

#create frames 
topframe = Frame(window)
topframe.pack()

bottomframe = Frame(window)
bottomframe.pack(side=BOTTOM)

#ADD ACCOUNT

 #create title
c= Label(topframe,text='Add account')
c.grid(row=0,column=1)
 #enter user / user_password / Site / name / password
label_00 = Label(topframe, text="User: ")
label_01 = Label(topframe, text="user_password: ")
label_1 = Label(topframe, text="Site_name: ")
label_2 = Label(topframe, text="Email: ")
label_3 = Label(topframe, text="Password: ")

textBox00= Entry(topframe)
textBox01= Entry(topframe)
textBox1= Entry(topframe)
textBox2= Entry(topframe)
textBox3= Entry(topframe)

    #label.grid : define the label's position in the window
label_1.grid(row=1, sticky= E)
label_2.grid(row=2, sticky= E)
label_3.grid(row=3, sticky= E)
label_00.grid(row=0,column=2, sticky= E)
label_01.grid(row=0,column=4, sticky= E)



textBox1.grid(row=1,column=1)
textBox2.grid(row=2,column=1)
textBox3.grid(row=3,column=1)
textBox00.grid(row=0,column=3)
textBox01.grid(row=0,column=5)

liste_of_data=[]
button1 = Button(topframe, text="ADD", fg="blue",command=load)
button1.grid(row=2,column=3)

#--------------------------------------------------------------
#GET ACCOUNT

 #create a checkbotton
c= Label(bottomframe,text='Get account')
c.grid(row=0,column=1)

#enter user / user_password
label_00 = Label(bottomframe, text="User: ").grid(row=0,column=2, sticky= E)
label_01 = Label(bottomframe, text="User password: ").grid(row=0,column=4, sticky= E)

textBox4= Entry(bottomframe)
textBox5= Entry(bottomframe)

textBox4.grid(row=0,column=3)
textBox5.grid(row=0,column=5)

 #enter Site / name / password 
label_6 = Label(bottomframe, text="Site name: ")
textBox6= Entry(bottomframe)

    #label.grid : define the label's position in the window

label_6.grid(row=3, sticky= E)
textBox6.grid(row=3,column=1)

button2 = Button(bottomframe, text="GET Acount", fg="blue",command=upload)
button2.grid(row=3,column=3)

# start the main loop
window.mainloop() 

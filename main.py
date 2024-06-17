#3rd time to code it 
#moving on after rewatch the vid 
# the last 5 mins of the video code
# no power from 3 p.m /back to coding at 8:58 p.m Wed, 2024
# last 9:20 of thw video bismallah
#Orginal Video that been used in the coding ""https://www.youtube.com/watch?v=MeMCBdnhvQs&t=153s
#YouTube Channle : Coding with Hala



import tkinter 
from tkinter import messagebox #error from instead I used import fixed same time 


window = tkinter.Tk()
window.title("Nouralhuda Learn GUI py 3rd day") 
window.geometry('340x440') 

window.configure(bg='#333333') 

def login() : #db related functions when the command go to function
    username = "Messenger"
    password="126790"
    if username_entry.get()==username and password_entry.get()==password: #wen well AlhumdAllah
       # print ("Successfully logged in") 
       #using messagebox
       messagebox.showinfo(title="Login Success",message="You succesfully logged in.")
    else:
        #print("Invaild login")
        messagebox.showerror(title="Erorr",message="Invaild login.")
        #Finished the video 9:33p.m Wed , 12th June  

frame = tkinter.Frame(bg='#333333')

label = tkinter.Label(frame,text = "تسجـيل الدخول ")
Login_label = tkinter.Label(frame,text="تسـجيل الدخول", bg='#333333',fg="#333999", font=("Arial",33)) 
username_label = tkinter.Label(frame,text="أســم المستخدم",bg='#333333',fg="#FFFFFF",font=("Arial",19))
username_entry = tkinter.Entry(frame, font=("Arial",19))
password_entry = tkinter.Entry(frame,show="*",font=("Arial",19))
password_label = tkinter.Label(frame,text="كلمـة المرور",bg='#333333',fg="#FFFFFF",font=("Arial",19))
login_button = tkinter.Button(frame,text="تــسجيل", bg="#333999",fg="#FFFFFF",font=("Arial",19),command=login)




Login_label.grid(row=0,column=11,columnspan=2,sticky="news",pady=40)
username_label.grid(row=1,column =12 ) 
username_entry.grid(row=1,column=11,pady=20)
password_label.grid(row=2,column=12)
password_entry.grid(row=2, column=11,pady=20)
login_button.grid(row=3,column=11,columnspan=2,pady=30)

frame.pack()

window.mainloop()


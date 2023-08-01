from tkinter import *

# command functions
def click():
    print("User logged in...")


window = Tk()
window.geometry("620x420")
window.title("NP First GUI Program")

icon = PhotoImage(file="windows-icon.png")
window.iconphoto(True,icon)

userIcon = PhotoImage(file="user_small.png")


window.config(background="#0261ba")

label = Label(window,
              text="User Management System",
              background="#0261ba",
              foreground="white", 
              font=("Arial",20,"bold"))
label.place(x=120,y=30)

secondLabel = Label(window,
                    text="More detailed info...",
                    background="#0261ba",
                    foreground="yellow")
secondLabel.place(x=355,y=65)

userIconLabel = Label(image=userIcon,
                      background="#0261ba")
userIconLabel.place(x=10,y=10)


loginButton = Button(window,text="Login User",
                     padx=40,
                     command=click)
loginButton.place(x=125,y=90)

window.mainloop()
from tkinter import *

window = Tk()
window.geometry("420x420")
window.title("NP First GUI Program")

icon = PhotoImage(file="windows-icon.png")
window.iconphoto(True,icon)

window.config(background="#0261ba")

window.mainloop()
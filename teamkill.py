#! bython 6

from tkinter import *
import wew

def clicked():

	reponse = "message " + txt.get()
	lbl.configure(text=response)
	smsAlert.sendText(response)

#build window

window = Tk()
window.title("kill myself")
window.geometry('500x150')

#add label
lbl = Label(window, text = "entermessage", font=("ArialBold",13))
lbl.grid(column=0, row=0)
txt = Entry(window, width=23)
txt.focus()
txt.grid(column=0, row=2)
#addbutton
btn = Button(window, text="Send Text Msg", bg="grey", command=clicked)
btn.grid(column=2, row=2)

window.mainloop()

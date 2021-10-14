import tkinter as tk
from tkinter import *

global root

root = tk.Tk()
root.geometry('300x300')
  
def screenForDeafMute():
  windowForMute = Toplevel(root)
  windowForMute.geometry('300x300')

  optionsDeafMute = [
    "English",
  ]  

  clicked = StringVar()
  
  def destroyMuteScreen():
    windowForMute.destroy()

  def validateInput():
    if clicked.get()!="English":
      errorLabel.config(text="Please select a language first",fg="red")
    else :
      errorLabel.config(text="Starting the system...",fg="green")
  
  # for mute
  selectLanguage = Label(windowForMute, text='Select language *')
  selectLanguage.place(x=20,y=30)
  drop = OptionMenu( windowForMute , clicked , *optionsDeafMute )
  drop.pack()
  drop.place(x=150,y=20)
  button = Button( windowForMute , text = "Continue" , command = validateInput  )
  button.place(x=100,y=70)
  errorLabel = Label(windowForMute, text="")
  errorLabel.place(x=70,y=100)
  closeButton = Button( windowForMute, text='x', fg='red', command= destroyMuteScreen  )
  closeButton.place(x=10,y=270)

  windowForMute.mainloop()

def screenForNormal():
  windowForNormal = Toplevel(root)
  windowForNormal.geometry('300x300')

  optionsNormal = [
    "ASL",
  ]  

  clicked = StringVar()
  
  def destroyNormalScreen():
    windowForNormal.destroy()

  def validateInput():
    if clicked.get()!="ASL":
      errorLabel.config(text="Please select a language first",fg="red")
    else :
      errorLabel.config(text="Starting the system...",fg="green")
      #call another screen and then close current window
      
  
  # for mute
  selectLanguage = Label(windowForNormal, text='Select language *')
  selectLanguage.place(x=20,y=30)
  drop = OptionMenu( windowForNormal , clicked , *optionsNormal )
  drop.pack()
  drop.place(x=150,y=20)
  button = Button( windowForNormal , text = "Continue" , command = validateInput  )
  button.place(x=100,y=70)
  errorLabel = Label(windowForNormal, text="")
  errorLabel.place(x=70,y=100)
  closeButton = Button( windowForNormal, text='x', fg='red', command= destroyNormalScreen  )
  closeButton.place(x=10,y=270)

  windowForNormal.mainloop()


#root screen starts here

def destroyScreen():
  root.destroy()

introductionLabel = Label(root,text="DRISHYAM : An Interpreter for Deaf and Mute")
introductionLabel.place(x=30,y=10)
introductionLabelPara = Label(root,text="Let's dive into the system.")
introductionLabelPara.place(x=10,y=50)
introductionLabelPara1 = Label(root,text="Firstly select one of the category below")
introductionLabelPara1.place(x=10,y=70)

button = Button( root , text = "Normal",fg="black" , command = screenForNormal ).place(x=50,y=150)
button = Button( root , text = "Deaf/Mute",fg="black" , command = screenForDeafMute ).place(x=180,y=150)

closeButton = Button( root, text='x', fg='red', command= destroyScreen  )
closeButton.place(x=10,y=270)
root.mainloop()

# this will be flow of our PROJECT
# -> welcome screen
# -> Choose between normal user and mute/deaf person
# -> show respective screen
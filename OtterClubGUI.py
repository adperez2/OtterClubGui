from tkinter import *               #allows us to create a gui
root = Tk()
root.title("CoolKidsClub2")        #title of gui
root.configure(background="pink")   #color
root.geometry("450x400")            #size of box
root.resizable(0,0)

label1 = Label(root, text="What is your name?")         #each had a label, typingbox, and button in order to display
label1.grid(row=1, column=1)                            #and determine the output

typingbox = Entry(root)
typingbox.grid(row=1, column=2)

button1=Button(root, text="Submit", fg='Pink')             #fg allowed me to have a pink background
button1.grid(row=1, column=3)                              # I used (grid) to place buttons, labels, and typing boxes

label2 = Label(root, text="What is your age?")
label2.grid(row=2, column=1)

typingbox2 = Entry(root)
typingbox2.grid(row=2, column=2)

button2=Button(root, text="Submit", fg='Pink')
button2.grid(row=2, column=3)

label3=Label(root, text= "Are you a business major?")
label3.grid(row=3, column=1)

typingbox3 = Entry(root)
typingbox3.grid(row=3, column=2)

button3=Button(root, text="Submit", fg='Pink')
button3.grid(row=3, column=3)

def submit():                           #this is the part I struggled with, displaying the if statement
   if typingbox2.get() >="25":         #if more or equal to 25, you are part of team 2
       answer = "Team 2!"
   elif typingbox2.get() <= "24":      #if less or equal to 24, you are part of team 1
       answer = "Team 1!"
   Label.configure(text="Hello " + typingbox.get() + " you are part of..." + str(submit))

buttonA=Button(root, text="Submit", fg='Pink', command=submit)
buttonA.grid(row=4, column=2)

root.mainloop()

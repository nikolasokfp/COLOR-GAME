from tkinter import *
import random
import time
screen = Tk() #dimiourgia ouonis

screen.title("makis") #titlos

screen.geometry('400x300') #megeuos

score = 0
timeleft = 30
colors = ['Red', 'Blue', 'Pink', 'Yellow',  'Black' ]

def startGame(event):
    if timeleft == 30:
        countdown()
    nextColor()


def countdown():
    global timeleft
    if timeleft >0:
        timeleft -=1
        timelbl.config(text = "Time Left "+str(timeleft))
        timelbl.after(1000,countdown)



def nextColor():
    global score
    global timeleft
    if timeleft >0:

        if e.get().lower() == colors[1].lower():
            score += 1
        e.delete(0,END)
        random.shuffle(colors)
        grxroma.config(fg=str(colors[1]), text=str(colors[0]))
        scorelbl.config(text="Score: " + str(score))




protolbl = Label(screen,text = " type in the color of the words and not the word text!!! ")
protolbl.pack()

scorelbl = Label(screen,text = " PRESS enter to start the game ")
scorelbl.pack()



timelbl = Label(screen,text = " time 30 ")
timelbl.pack()


grxroma = Label(screen,text = "",font = ('Arial', 75)  )
grxroma.pack()





xroma = Label(screen, text  = "write the color")
xroma.pack()


e = Entry(screen)
screen.bind('<Return>', startGame)
e.pack()
e.focus_set()























screen.mainloop()   #teleutaia entoli
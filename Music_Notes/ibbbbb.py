import tkinter as tk
import pygame
import time

pygame.mixer.pre_init(50100,-16,1,512)
pygame.init()

master=tk.Tk()
master.title("My Piano")

Label = tk.Label(master , text="-----PIANO-----")
Label.grid(row=0 , columnspan=15)
##-------------------------------
def press(event):
    if isinstance(event, str):
        num = event
    else:
        num = event.char

    if num=="A" or num=="a":
        W1.config(bg="grey")
        time.sleep(2)
        sound = pygame.mixer.Sound(r'C:\Users\HITESHWAR SINGH\Downloads\A.wav')
        sound.play()
        master.after(100,lambda: W1.config(bg="white"))



    elif num=="B" or num=="b":
        sound = pygame.mixer.Sound(r'C:\Users\HITESHWAR SINGH\Downloads\A.wav')
        sound.play()

def d(event):
    press(event)
master.bind("<Key>",d)


#Buttons for keyboard
W1 =tk.Button(master, bg="white",text="A",command=lambda:press("a"), height=10 , width=4,anchor='s')
W1.grid(row=1,column=0)

W2 =tk.Button(master, bg="white", text="W2" ,height=10 , width=4,anchor='s')
W2.grid(row=1 , column=1)

W3 =tk.Button(master, bg="white", text="W3" ,height=10 , width=4,anchor='s')
W3.grid(row=1 , column=2)

W4 =tk.Button(master, bg="white", text="W4" ,height=10 , width=4,anchor='s')
W4.grid(row=1 , column=3)

W5 =tk.Button(master, bg="white",text="W5" ,height=10 , width=4,anchor='s')
W5.grid(row=1 , column=4)

W7 =tk.Button(master, bg="white",text="W7" ,height=10 , width=4,anchor='s')
W7.grid(row=1 , column=5)

W8 =tk.Button(master, bg="white",text="W8" ,height=10 , width=4,anchor='s')
W8.grid(row=1 , column=6)

W9 =tk.Button(master, bg="white",text="W9", height=10 , width=4,anchor='s')
W9.grid(row=1,column=7)

W10 =tk.Button(master, bg="white", text="W10" ,height=10 , width=4,anchor='s')
W10.grid(row=1 , column=8)

W11 =tk.Button(master, bg="white", text="W11" ,height=10 , width=4,anchor='s')
W11.grid(row=1 , column=9)

W12=tk.Button(master, bg="white", text="W12" ,height=10 , width=4,anchor='s')
W12.grid(row=1 , column=10)

W13=tk.Button(master, bg="white",text="W13" ,height=10 , width=4,anchor='s')
W13.grid(row=1 , column=11)

W14=tk.Button(master, bg="white",text="W14" ,height=10 , width=4,anchor='s')
W14.grid(row=1 , column=12)

W15=tk.Button(master, bg="white",text="W15" ,height=10 , width=4,anchor='s')
W15.grid(row=1 , column=13)

##-------------------------------------------------------------------------------------

B1=tk.Button(master ,bg="black" , fg="white",text="B1" ,height=5 ,width=2)
B1.grid(row=1,columnspan=2,sticky='N')

B2 =tk.Button(master ,bg="black" , fg="white",text="B2" ,height=5 ,width=2)
B2.grid(row=1,columnspan=4,sticky='N')

B3 =tk.Button(master , bg="black", fg="white",text="B3" ,height=5 ,width=2)
B3.grid(row=1,column=3 ,columnspan=2,sticky='N')

B4=tk.Button(master,bg="black" ,fg="white",text="B4" , height=5 ,width=2)
B4.grid(row=1, column = 4 , columnspan=2,sticky='N')

B5 =tk.Button(master,bg="black" ,fg="white",text="B5" ,width=2, height=5)
B5.grid(row=1, column = 5 , columnspan=2,sticky='N')

B6 =tk.Button(master ,bg="black" , fg="white",text="B6" ,height=5 ,width=2)
B6.grid(row=1,column=7,columnspan=2,sticky='N')

B7=tk.Button(master ,bg="black" , fg="white",text="B7" ,height=5 ,width=2)
B7.grid(row=1,column=8,columnspan=2,sticky='N')

B8 =tk.Button(master , bg="black", fg="white",text="B8" ,height=5 ,width=2)
B8.grid(row=1,column=10 ,columnspan=2,sticky='N')

B9 =tk.Button(master,bg="black" ,fg="white",text="B9" , height=5 ,width=2)
B9.grid(row=1, column = 11 , columnspan=2,sticky='N')

B10 =tk.Button(master,bg="black" ,fg="white",text="B10" ,width=2, height=5)
B10.grid(row=1, column = 12 , columnspan=2,sticky='N')



master.mainloop()

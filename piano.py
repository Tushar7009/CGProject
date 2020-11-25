import tkinter as tk
import pygame
import time
from tkinter import *
global n
n=None
pygame.mixer.pre_init(50100,-16,1,512)
pygame.init()

master=tk.Tk()
master.title("My Piano")

Label = tk.Label(master , text="-----CG PROJECT-----")
Label.grid(row=0 , columnspan=22)
##-------------------------------

def change_vol():
    sounds.music.set_volume(vol.get())
def piano(event):
    if isinstance(event, str):
        num = event
    else:
        num = event.char

    if num=="Q" or num=="q":

        W1.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\Tushar Gupta\OneDrive\Desktop\Music_Notes\A.wav')
        sound.play()

        master.after(100,lambda: W1.config(bg="white"))

    elif num=="w" or num=="W":
        W2.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\Tushar Gupta\OneDrive\Desktop\Music_Notes\B.wav')
        sound.play()
        master.after(100,lambda: W2.config(bg="white"))

    elif num=="e" or num=="E":
        W3.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\Tushar Gupta\OneDrive\Desktop\Music_Notes\Bb.wav')
        sound.play()
        master.after(100,lambda: W3.config(bg="white"))

    elif num=="R" or num=="r":
        W4.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\Tushar Gupta\OneDrive\Desktop\Music_Notes\C_s.wav')
        sound.play()
        master.after(100,lambda: W4.config(bg="white"))

    elif num=="t" or num=="T":
        W5.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\Tushar Gupta\OneDrive\Desktop\Music_Notes\C_s1.wav')
        sound.play()
        master.after(100,lambda: W5.config(bg="white"))

    elif num=="Y" or num=="y":
        W6.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\Tushar Gupta\OneDrive\Desktop\Music_Notes\C1.wav')
        sound.play()
        master.after(100,lambda: W6.config(bg="white"))

    elif num=="u" or num=="U":
        W7.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\Tushar Gupta\OneDrive\Desktop\Music_Notes\D.wav')
        sound.play()
        master.after(100,lambda: W7.config(bg="white"))

    elif num=="A" or num=="a":
        W8.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\Tushar Gupta\OneDrive\Desktop\Music_Notes\D_s.wav')
        sound.play()
        master.after(100,lambda: W8.config(bg="white"))

    elif num=="s" or num=="S":
        W9.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\Tushar Gupta\OneDrive\Desktop\Music_Notes\D_s1.wav')
        sound.play()
        master.after(100,lambda: W9.config(bg="white"))

    elif num=="D" or num=="d":
        W10.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\Tushar Gupta\OneDrive\Desktop\Music_Notes\D1.wav')
        sound.play()
        master.after(100,lambda: W10.config(bg="white"))

    elif num=="F" or num=="f":
        W11.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\Tushar Gupta\OneDrive\Desktop\Music_Notes\E.wav')
        sound.play()
        master.after(100,lambda: W11.config(bg="white"))

    elif num=="G" or num=="g":
        W12.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\Tushar Gupta\OneDrive\Desktop\Music_Notes\F.wav')
        sound.play()
        master.after(100,lambda: W12.config(bg="white"))

    elif num=="H" or num=="h":
        W13.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\Tushar Gupta\OneDrive\Desktop\Music_Notes\F_s.wav')
        sound.play()
        master.after(100,lambda: W13.config(bg="white"))

    elif num=="J" or num=="j":
        W14.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\Tushar Gupta\OneDrive\Desktop\Music_Notes\F1.wav')
        sound.play()
        master.after(100,lambda: W14.config(bg="white"))

    elif num=="1":
        B1.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\Tushar Gupta\OneDrive\Desktop\Music_Notes\G.wav')
        sound.play()
        master.after(100,lambda: B1.config(bg="black"))

    elif num=="2" :
        B2.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\Tushar Gupta\OneDrive\Desktop\Music_Notes\G_s.wav')
        sound.play()
        master.after(100,lambda: B2.config(bg="black"))

    elif num=="3" :
        B3.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\Tushar Gupta\OneDrive\Desktop\Music_Notes\G_s.wav')
        sound.play()
        master.after(100,lambda: B3.config(bg="black"))

    elif num=="4" :
        B4.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\Tushar Gupta\OneDrive\Desktop\Music_Notes\G_s.wav')
        sound.play()
        master.after(100,lambda: B4.config(bg="black"))

    elif num=="5" :
        B5.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\Tushar Gupta\OneDrive\Desktop\Music_Notes\G_s.wav')
        sound.play()
        master.after(100,lambda: B5.config(bg="black"))
    elif num=="6" :
        B6.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\Tushar Gupta\OneDrive\Desktop\Music_Notes\G_s.wav')
        sound.play()
        master.after(100,lambda: B6.config(bg="black"))

    elif num=="7" :
        B7.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\Tushar Gupta\OneDrive\Desktop\Music_Notes\G_s.wav')
        sound.play()
        master.after(100,lambda: B7.config(bg="black"))

    elif num=="8" :
        B8.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\Tushar Gupta\OneDrive\Desktop\Music_Notes\G_s.wav')
        sound.play()
        master.after(100,lambda: B8.config(bg="black"))

    elif num=="9" :
        B9.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\Tushar Gupta\OneDrive\Desktop\Music_Notes\G_s.wav')
        sound.play()
        master.after(100,lambda: B9.config(bg="black"))

    elif num=="0" :
        B10.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\Tushar Gupta\OneDrive\Desktop\Music_Notes\G_s.wav')
        sound.play()
        master.after(100,lambda: B10.config(bg="black"))



def synth(event):
    if isinstance(event, str):
        num = event
    else:
        num = event.char

    if num=="Q" or num=="q":

        W1.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\Tushar Gupta\OneDrive\Desktop\Music_Notes\B.wav')
        sound.play()

        master.after(100,lambda: W1.config(bg="white"))

    elif num=="w" or num=="W":
        W2.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\Tushar Gupta\OneDrive\Desktop\Music_Notes\B.wav')
        sound.play()
        master.after(100,lambda: W2.config(bg="white"))

    elif num=="e" or num=="E":
        W3.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\Tushar Gupta\OneDrive\Desktop\Music_Notes\Bb.wav')
        sound.play()
        master.after(100,lambda: W3.config(bg="white"))

    elif num=="R" or num=="r":
        W4.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\Tushar Gupta\OneDrive\Desktop\Music_Notes\C_s.wav')
        sound.play()
        master.after(100,lambda: W4.config(bg="white"))

    elif num=="t" or num=="T":
        W5.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\Tushar Gupta\OneDrive\Desktop\Music_Notes\C_s1.wav')
        sound.play()
        master.after(100,lambda: W5.config(bg="white"))

    elif num=="Y" or num=="y":
        W6.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\Tushar Gupta\OneDrive\Desktop\Music_Notes\C1.wav')
        sound.play()
        master.after(100,lambda: W6.config(bg="white"))

    elif num=="u" or num=="U":
        W7.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\Tushar Gupta\OneDrive\Desktop\Music_Notes\D.wav')
        sound.play()
        master.after(100,lambda: W7.config(bg="white"))

    elif num=="A" or num=="a":
        W8.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\Tushar Gupta\OneDrive\Desktop\Music_Notes\D_s.wav')
        sound.play()
        master.after(100,lambda: W8.config(bg="white"))

    elif num=="s" or num=="S":
        W9.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\Tushar Gupta\OneDrive\Desktop\Music_Notes\D_s1.wav')
        sound.play()
        master.after(100,lambda: W9.config(bg="white"))

    elif num=="D" or num=="d":
        W10.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\Tushar Gupta\OneDrive\Desktop\Music_Notes\D1.wav')
        sound.play()
        master.after(100,lambda: W10.config(bg="white"))

    elif num=="F" or num=="f":
        W11.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\Tushar Gupta\OneDrive\Desktop\Music_Notes\E.wav')
        sound.play()
        master.after(100,lambda: W11.config(bg="white"))

    elif num=="G" or num=="g":
        W12.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\Tushar Gupta\OneDrive\Desktop\Music_Notes\F.wav')
        sound.play()
        master.after(100,lambda: W12.config(bg="white"))

    elif num=="H" or num=="h":
        W13.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\Tushar Gupta\OneDrive\Desktop\Music_Notes\F_s.wav')
        sound.play()
        master.after(100,lambda: W13.config(bg="white"))

    elif num=="J" or num=="j":
        W14.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\Tushar Gupta\OneDrive\Desktop\Music_Notes\F1.wav')
        sound.play()
        master.after(100,lambda: W14.config(bg="white"))

    elif num=="1":
        B1.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\Tushar Gupta\OneDrive\Desktop\Music_Notes\G.wav')
        sound.play()
        master.after(100,lambda: B1.config(bg="black"))

    elif num=="2" :
        B2.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\Tushar Gupta\OneDrive\Desktop\Music_Notes\G_s.wav')
        sound.play()
        master.after(100,lambda: B2.config(bg="black"))

    elif num=="3" :
        B3.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\Tushar Gupta\OneDrive\Desktop\Music_Notes\G_s.wav')
        sound.play()
        master.after(100,lambda: B3.config(bg="black"))

    elif num=="4" :
        B4.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\Tushar Gupta\OneDrive\Desktop\Music_Notes\G_s.wav')
        sound.play()
        master.after(100,lambda: B4.config(bg="black"))

    elif num=="5" :
        B5.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\Tushar Gupta\OneDrive\Desktop\Music_Notes\G_s.wav')
        sound.play()
        master.after(100,lambda: B5.config(bg="black"))
    elif num=="6" :
        B6.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\Tushar Gupta\OneDrive\Desktop\Music_Notes\G_s.wav')
        sound.play()
        master.after(100,lambda: B6.config(bg="black"))

    elif num=="7" :
        B7.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\Tushar Gupta\OneDrive\Desktop\Music_Notes\G_s.wav')
        sound.play()
        master.after(100,lambda: B7.config(bg="black"))

    elif num=="8" :
        B8.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\Tushar Gupta\OneDrive\Desktop\Music_Notes\G_s.wav')
        sound.play()
        master.after(100,lambda: B8.config(bg="black"))

    elif num=="9" :
        B9.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\Tushar Gupta\OneDrive\Desktop\Music_Notes\G_s.wav')
        sound.play()
        master.after(100,lambda: B9.config(bg="black"))

    elif num=="0" :
        B10.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\Tushar Gupta\OneDrive\Desktop\Music_Notes\G_s.wav')
        sound.play()
        master.after(100,lambda: B10.config(bg="black"))





def press(event):
    print(n)
    if n==1:
        piano(event)
    else:
        synth(event)
def d(event):
    press(event)
master.bind("<Key>",d)
"""def retrieve_input():
    inputvalue=tb.get("1.0","end-1c")
    print(inputvalue)
    return inputvalue"""
def sw(m):
    n=m
    print(n)
    return n




"""tb = Text(
master,height=1,width=4
)

tb.grid(row=4,column=0)
print(tb)"""
buttonCommit=Button(master, height=1, width=4, text="piano",
                    command=lambda: sw(1))
#command=lambda: retrieve_input() >>> just means do this when i press the button
buttonCommit.grid(row=4,column=1)
buttonCommit=Button(master, height=1, width=4, text="synth",
                    command=lambda: sw(2))
#command=lambda: retrieve_input() >>> just means do this when i press the button
buttonCommit.grid(row=4,column=2)
#Buttons for keyboard
W1 =tk.Button(master, bg="white",text="Q",command=lambda:press("q"), height=10 , width=4,anchor='s')
W1.grid(row=2,column=0)

W2 =tk.Button(master, bg="white", text="W" ,height=10,command=lambda:press("w") ,width=4,anchor='s')
W2.grid(row=2 , column=1)

W3 =tk.Button(master, bg="white", text="E" ,height=10 ,command=lambda:press("e") ,width=4,anchor='s')
W3.grid(row=2 , column=2)

W4 =tk.Button(master, bg="white", text="R" ,height=10 , width=4,anchor='s',command=lambda:press("r"))
W4.grid(row=2 , column=3)

W5 =tk.Button(master, bg="white",text="T" ,height=10 , width=4,anchor='s',command=lambda:press("t"))
W5.grid(row=2 , column=4)

W6 =tk.Button(master, bg="white",text="Y" ,height=10 , width=4,anchor='s',command=lambda:press("y"))
W6.grid(row=2 , column=5)

W7 =tk.Button(master, bg="white",text="U" ,height=10 , width=4,anchor='s',command=lambda:press("u"))
W7.grid(row=2 , column=6)

W8 =tk.Button(master, bg="white",text="A", height=10 , width=4,anchor='s',command=lambda:press("a"))
W8.grid(row=2,column=7)

W9 =tk.Button(master, bg="white", text="S" ,height=10 , width=4,anchor='s',command=lambda:press("s"))
W9.grid(row=2, column=8)

W10 =tk.Button(master, bg="white", text="D" ,height=10 , width=4,anchor='s',command=lambda:press("d"))
W10.grid(row=2 , column=9)

W11=tk.Button(master, bg="white", text="F" ,height=10 , width=4,anchor='s',command=lambda:press("f"))
W11.grid(row=2 , column=10)

W12=tk.Button(master, bg="white",text="G" ,height=10 , width=4,anchor='s',command=lambda:press("g"))
W12.grid(row=2 , column=11)

W13=tk.Button(master, bg="white",text="H" ,height=10 , width=4,anchor='s',command=lambda:press("h"))
W13.grid(row=2 , column=12)

W14=tk.Button(master, bg="white",text="J" ,height=10 , width=4,anchor='s',command=lambda:press("j"))
W14.grid(row=2 , column=13)

W15=tk.Button(master, bg="white",text="K" ,height=10 , width=4,anchor='s',command=lambda:press("k"))
W15.grid(row=2 , column=14)

W16=tk.Button(master, bg="white",text="L" ,height=10 , width=4,anchor='s',command=lambda:press("l"))
W16.grid(row=2 , column=15)

W17=tk.Button(master, bg="white",text="M" ,height=10 , width=4,anchor='s',command=lambda:press("m"))
W17.grid(row=2 , column=16)

W18=tk.Button(master, bg="white",text="N" ,height=10 , width=4,anchor='s',command=lambda:press("n"))
W18.grid(row=2 , column=17)

W19=tk.Button(master, bg="white",text="O" ,height=10 , width=4,anchor='s',command=lambda:press("o"))
W19.grid(row=2 , column=18)

W20=tk.Button(master, bg="white",text="P" ,height=10 , width=4,anchor='s',command=lambda:press("p"))
W20.grid(row=2 , column=19)

W21=tk.Button(master, bg="white",text="Q" ,height=10 , width=4,anchor='s',command=lambda:press("q"))
W21.grid(row=2 , column=20)
##-------------------------------------------------------------------------------------

B1=tk.Button(master ,bg="black" , fg="white",text="1" ,height=5 ,width=2,command=lambda:press("1"))
B1.grid(row=2,columnspan=2,sticky='N')

B2 =tk.Button(master ,bg="black" , fg="white",text="2" ,height=5 ,width=2,command=lambda:press("2"))
B2.grid(row=2,columnspan=4,sticky='N')

B3 =tk.Button(master , bg="black", fg="white",text="3" ,height=5 ,width=2,command=lambda:press("3"))
B3.grid(row=2,column=3 ,columnspan=2,sticky='N')

B4=tk.Button(master,bg="black" ,fg="white",text="4" , height=5 ,width=2,command=lambda:press("4"))
B4.grid(row=2, column = 4 , columnspan=2,sticky='N')

B5 =tk.Button(master,bg="black" ,fg="white",text="5" ,width=2, height=5,command=lambda:press("5"))
B5.grid(row=2, column = 5 , columnspan=2,sticky='N')

B6 =tk.Button(master ,bg="black" , fg="white",text="6" ,height=5 ,width=2,command=lambda:press("6"))
B6.grid(row=2,column=7,columnspan=2,sticky='N')

B7=tk.Button(master ,bg="black" , fg="white",text="7" ,height=5 ,width=2,command=lambda:press("7"))
B7.grid(row=2,column=8,columnspan=2,sticky='N')

B8 =tk.Button(master , bg="black", fg="white",text="8" ,height=5 ,width=2,command=lambda:press("8"))
B8.grid(row=2,column=10 ,columnspan=2,sticky='N')

B9 =tk.Button(master,bg="black" ,fg="white",text="9" , height=5 ,width=2,command=lambda:press("9"))
B9.grid(row=2, column = 11 , columnspan=2,sticky='N')

B10 =tk.Button(master,bg="black" ,fg="white",text="0" ,width=2, height=5,command=lambda:press("0"))
B10.grid(row=2, column = 12 , columnspan=2,sticky='N')

B11 =tk.Button(master,bg="black" ,fg="white",text="-" ,width=2, height=5,command=lambda:press("-"))
B11.grid(row=2, column = 14 , columnspan=2,sticky='N')

B12 =tk.Button(master,bg="black" ,fg="white",text="=" ,width=2, height=5,command=lambda:press("="))
B12.grid(row=2, column = 15 , columnspan=2,sticky='N')

B13 =tk.Button(master,bg="black" ,fg="white",text="1" ,width=2, height=5,command=lambda:press("1"))
B13.grid(row=2, column = 17 , columnspan=2,sticky='N')

B14 =tk.Button(master,bg="black" ,fg="white",text="2" ,width=2, height=5,command=lambda:press("2"))
B14.grid(row=2, column = 18 , columnspan=2,sticky='N')

B15 =tk.Button(master,bg="black" ,fg="white",text="3" ,width=2, height=5,command=lambda:press("3"))
B15.grid(row=2, column = 19 , columnspan=2,sticky='N')


master.mainloop()

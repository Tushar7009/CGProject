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

    if num=="Q" or num=="q":
        W1.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\HITESHWAR SINGH\Desktop\Music_Notes\A.wav')
        sound.play()
        master.after(100,lambda: W1.config(bg="white"))

    elif num=="w" or num=="W":
        W2.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\HITESHWAR SINGH\Desktop\Music_Notes\B.wav')
        sound.play()
        master.after(100,lambda: W2.config(bg="white"))

    elif num=="e" or num=="E":
        W3.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\HITESHWAR SINGH\Desktop\Music_Notes\Bb.wav')
        sound.play()
        master.after(100,lambda: W3.config(bg="white"))

    elif num=="R" or num=="r":
        W4.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\HITESHWAR SINGH\Desktop\Music_Notes\C_s.wav')
        sound.play()
        master.after(100,lambda: W4.config(bg="white"))

    elif num=="t" or num=="T":
        W5.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\HITESHWAR SINGH\Desktop\Music_Notes\C_s1.wav')
        sound.play()
        master.after(100,lambda: W5.config(bg="white"))

    elif num=="Y" or num=="y":
        W6.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\HITESHWAR SINGH\Desktop\Music_Notes\C1.wav')
        sound.play()
        master.after(100,lambda: W6.config(bg="white"))

    elif num=="u" or num=="U":
        W7.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\HITESHWAR SINGH\Desktop\Music_Notes\D.wav')
        sound.play()
        master.after(100,lambda: W7.config(bg="white"))

    elif num=="A" or num=="a":
        W8.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\HITESHWAR SINGH\Desktop\Music_Notes\D_s.wav')
        sound.play()
        master.after(100,lambda: W8.config(bg="white"))

    elif num=="s" or num=="S":
        W9.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\HITESHWAR SINGH\Desktop\Music_Notes\D_s1.wav')
        sound.play()
        master.after(100,lambda: W9.config(bg="white"))

    elif num=="D" or num=="d":
        W10.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\HITESHWAR SINGH\Desktop\Music_Notes\D1.wav')
        sound.play()
        master.after(100,lambda: W10.config(bg="white"))

    elif num=="F" or num=="f":
        W11.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\HITESHWAR SINGH\Desktop\Music_Notes\E.wav')
        sound.play()
        master.after(100,lambda: W11.config(bg="white"))

    elif num=="G" or num=="g":
        W12.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\HITESHWAR SINGH\Desktop\Music_Notes\F.wav')
        sound.play()
        master.after(100,lambda: W12.config(bg="white"))

    elif num=="H" or num=="h":
        W13.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\HITESHWAR SINGH\Desktop\Music_Notes\F_s.wav')
        sound.play()
        master.after(100,lambda: W13.config(bg="white"))

    elif num=="J" or num=="j":
        W14.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\HITESHWAR SINGH\Desktop\Music_Notes\F1.wav')
        sound.play()
        master.after(100,lambda: W14.config(bg="white"))

    elif num=="1":
        B1.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\HITESHWAR SINGH\Desktop\Music_Notes\G.wav')
        sound.play()
        master.after(100,lambda: B1.config(bg="black"))

    elif num=="2" :
        B2.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\HITESHWAR SINGH\Desktop\Music_Notes\G_s.wav')
        sound.play()
        master.after(100,lambda: B2.config(bg="black"))

    elif num=="3" :
        B3.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\HITESHWAR SINGH\Desktop\Music_Notes\G_s.wav')
        sound.play()
        master.after(100,lambda: B3.config(bg="black"))

    elif num=="4" :
        B4.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\HITESHWAR SINGH\Desktop\Music_Notes\G_s.wav')
        sound.play()
        master.after(100,lambda: B4.config(bg="black"))

    elif num=="5" :
        B5.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\HITESHWAR SINGH\Desktop\Music_Notes\G_s.wav')
        sound.play()
        master.after(100,lambda: B5.config(bg="black"))
    elif num=="6" :
        B6.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\HITESHWAR SINGH\Desktop\Music_Notes\G_s.wav')
        sound.play()
        master.after(100,lambda: B6.config(bg="black"))

    elif num=="7" :
        B7.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\HITESHWAR SINGH\Desktop\Music_Notes\G_s.wav')
        sound.play()
        master.after(100,lambda: B7.config(bg="black"))

    elif num=="8" :
        B8.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\HITESHWAR SINGH\Desktop\Music_Notes\G_s.wav')
        sound.play()
        master.after(100,lambda: B8.config(bg="black"))

    elif num=="9" :
        B9.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\HITESHWAR SINGH\Desktop\Music_Notes\G_s.wav')
        sound.play()
        master.after(100,lambda: B9.config(bg="black"))

    elif num=="0" :
        B10.config(bg="#66b5ff")
        sound = pygame.mixer.Sound(r'C:\Users\HITESHWAR SINGH\Desktop\Music_Notes\G_s.wav')
        sound.play()
        master.after(100,lambda: B10.config(bg="black"))



def d(event):
    press(event)
master.bind("<Key>",d)


#Buttons for keyboard
W1 =tk.Button(master, bg="white",text="Q",command=lambda:press("q"), height=10 , width=4,anchor='s')
W1.grid(row=1,column=0)

W2 =tk.Button(master, bg="white", text="W" ,height=10,command=lambda:press("w") ,width=4,anchor='s')
W2.grid(row=1 , column=1)

W3 =tk.Button(master, bg="white", text="E" ,height=10 ,command=lambda:press("e") ,width=4,anchor='s')
W3.grid(row=1 , column=2)

W4 =tk.Button(master, bg="white", text="R" ,height=10 , width=4,anchor='s',command=lambda:press("r"))
W4.grid(row=1 , column=3)

W5 =tk.Button(master, bg="white",text="T" ,height=10 , width=4,anchor='s',command=lambda:press("t"))
W5.grid(row=1 , column=4)

W6 =tk.Button(master, bg="white",text="Y" ,height=10 , width=4,anchor='s',command=lambda:press("y"))
W6.grid(row=1 , column=5)

W7 =tk.Button(master, bg="white",text="U" ,height=10 , width=4,anchor='s',command=lambda:press("u"))
W7.grid(row=1 , column=6)

W8 =tk.Button(master, bg="white",text="A", height=10 , width=4,anchor='s',command=lambda:press("a"))
W8.grid(row=1,column=7)

W9 =tk.Button(master, bg="white", text="S" ,height=10 , width=4,anchor='s',command=lambda:press("s"))
W9.grid(row=1 , column=8)

W10 =tk.Button(master, bg="white", text="D" ,height=10 , width=4,anchor='s',command=lambda:press("d"))
W10.grid(row=1 , column=9)

W11=tk.Button(master, bg="white", text="F" ,height=10 , width=4,anchor='s',command=lambda:press("f"))
W11.grid(row=1 , column=10)

W12=tk.Button(master, bg="white",text="G" ,height=10 , width=4,anchor='s',command=lambda:press("g"))
W12.grid(row=1 , column=11)

W13=tk.Button(master, bg="white",text="H" ,height=10 , width=4,anchor='s',command=lambda:press("h"))
W13.grid(row=1 , column=12)

W14=tk.Button(master, bg="white",text="J" ,height=10 , width=4,anchor='s',command=lambda:press("j"))
W14.grid(row=1 , column=13)

##-------------------------------------------------------------------------------------

B1=tk.Button(master ,bg="black" , fg="white",text="1" ,height=5 ,width=2,command=lambda:press("1"))
B1.grid(row=1,columnspan=2,sticky='N')

B2 =tk.Button(master ,bg="black" , fg="white",text="2" ,height=5 ,width=2,command=lambda:press("2"))
B2.grid(row=1,columnspan=4,sticky='N')

B3 =tk.Button(master , bg="black", fg="white",text="3" ,height=5 ,width=2,command=lambda:press("3"))
B3.grid(row=1,column=3 ,columnspan=2,sticky='N')

B4=tk.Button(master,bg="black" ,fg="white",text="4" , height=5 ,width=2,command=lambda:press("4"))
B4.grid(row=1, column = 4 , columnspan=2,sticky='N')

B5 =tk.Button(master,bg="black" ,fg="white",text="5" ,width=2, height=5,command=lambda:press("5"))
B5.grid(row=1, column = 5 , columnspan=2,sticky='N')

B6 =tk.Button(master ,bg="black" , fg="white",text="6" ,height=5 ,width=2,command=lambda:press("6"))
B6.grid(row=1,column=7,columnspan=2,sticky='N')

B7=tk.Button(master ,bg="black" , fg="white",text="7" ,height=5 ,width=2,command=lambda:press("7"))
B7.grid(row=1,column=8,columnspan=2,sticky='N')

B8 =tk.Button(master , bg="black", fg="white",text="8" ,height=5 ,width=2,command=lambda:press("8"))
B8.grid(row=1,column=10 ,columnspan=2,sticky='N')

B9 =tk.Button(master,bg="black" ,fg="white",text="9" , height=5 ,width=2,command=lambda:press("9"))
B9.grid(row=1, column = 11 , columnspan=2,sticky='N')

B10 =tk.Button(master,bg="black" ,fg="white",text="0" ,width=2, height=5,command=lambda:press("0"))
B10.grid(row=1, column = 12 , columnspan=2,sticky='N')



master.mainloop()

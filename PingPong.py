from time import sleep
from tkinter import *
window = Tk()
window.title("ping-pong")
c = Canvas(window, height=300, width=400, bg="black")
rand = c.create_rectangle(3, 3, 400, 300, outline="darkgreen")
c.pack()
player = c.create_rectangle(0, 60, 10, 200, fill="white")
player2 = c.create_rectangle(390, 60, 400, 200, fill="white")

ball = c.create_rectangle(190, 90, 200, 100, fill="white")

def PlayerBewegung(event):
    key = event.keysym
    if key == "Up":
        c.move(player2, 0, -8)        
    elif key == "Down":
        c.move(player2, 0, 8)
     
def Player2BewegungW(event):
        c.move(player, 0, -8)
def Player2BewegungS(event):
        c.move(player, 0, 8)    

c.bind_all("<Key>", PlayerBewegung)
c.bind_all("<KeyPress-s>", Player2BewegungS)
c.bind_all("<KeyPress-w>", Player2BewegungW)
ball_richtung_x = 1
ball_richtung_y = 1
c.move(ball, ball_richtung_x, ball_richtung_y)
window.mainloop()
while True:
        c.move(ball, ball_richtung_x,ball_richtung_y)
        sleep(0.01)
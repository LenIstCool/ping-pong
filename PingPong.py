from time import sleep
from tkinter import *
scorePlayerA = 0
scorePlayerB = 0
time = 0
i = 0
window = Tk()
window.title("ping-pong")
c = Canvas(window, height=400, width=500, bg="black")
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
window.pack()

while True:
        c.move(ball, 1 ,2)
        window.update()
        sleep(0.01)
        
        
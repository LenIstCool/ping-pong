               
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
ball_y = 200
ball_x = 190


# test branches
player_y = 10
player_x = 0

player2_x = 390
player2_y = 400
ball = c.create_rectangle(ball_x, 90, ball_y, 100, fill="white")

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
geschw_x = 1
geschw_y = 0.5
a = 0
b = 10
while True:
        print(c.coords(ball))
        print(c.coords(player2))
        
        if ball_x and ball_y == player2_x and player2_y:
                geschw_x = geschw_x + 10
                geschw_y = geschw_y + 10 
                sleep(0.1)
                window.update()
                exit()
        elif  a != b:       
                c.move(ball, geschw_x, geschw_y)
                window.update()
                sleep(0.01)                     
window.mainloop()
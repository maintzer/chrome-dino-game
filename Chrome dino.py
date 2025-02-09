import time
import math
from tkinter import *
import random

#variables
WIDTH=700
HEIGHT=300
yspeed = -3
xspeed = -4
g=23
score = 0
count = 0
end = False
count2 = 0
count3 = 0
birdheight = 0
hiscore = 0
var = 2

# making the game window
tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT, background='white')
tk.title('Chrome dinosaur game - Remastered - Remastered')
canvas.pack()

# boxes used to define location of moving items for collision logic and that
dinobox = canvas.create_rectangle(30, 201, 50, 251, outline='red')
thing = canvas.create_rectangle(0, 0, 1, 1)
thing1 = canvas.create_rectangle(0, 0, 1, 1)
thing2 = canvas.create_rectangle(0, 0, 1, 1)
thing3 = canvas.create_rectangle(0, 0, 1, 1)
smallcactusbox = canvas.create_rectangle(WIDTH, 210, WIDTH+15, 250, outline='red')
bigcactusbox = canvas.create_rectangle(WIDTH+300, 195, WIDTH+325, 250, outline='red')
cactusgroupbox = canvas.create_rectangle(WIDTH+800, 210, WIDTH+880, 250, outline='red')
birdbox = canvas.create_rectangle(10000, 200, 10028, 220, outline='red')
# images that are pasted onto their boxes
thedino1 = PhotoImage(file=r'"C:\Users\felix\Pictures\chromedino1.png"')
dino1 = canvas.create_image(40, 226, image=thedino1)
thedino2 = PhotoImage(file=r'"C:\Users\felix\Pictures\chromedino2.png"')
dino2 = canvas.create_image(40, 226, image=thedino2)
thedino3 = PhotoImage(file=r'"C:\Users\felix\Pictures\chromedino3.png"')
dino3 = canvas.create_image(40, 226, image=thedino3)
thesmallcactus = PhotoImage(file=r'"C:\Users\felix\Documents\smallcactus.png"')
smallcactus = canvas.create_image(WIDTH+7.5, 230, image=thesmallcactus)
thebigcactus = PhotoImage(file=r'"C:\Users\felix\Documents\bigcactus.png"')
bigcactus = canvas.create_image(WIDTH+312.5, 222.5, image=thebigcactus)
thecactusgroup = PhotoImage(file=r'"C:\Users\felix\Documents\cactusgroup.png"')
cactusgroup = canvas.create_image(WIDTH+840, 230, image=thecactusgroup)
thebird1 = PhotoImage(file=r'"C:\Users\felix\Documents\bird1.png"')
bird1 = canvas.create_image(10014, 210, image=thebird1)
thebird2 = PhotoImage(file=r'"C:\Users\felix\Documents\bird2.png"')
bird2 = canvas.create_image(10014, 210, image=thebird2)
horizonline = canvas.create_rectangle(0, 250, WIDTH, 251)

# the jump function, thing.
def jump(event):
    canvas.move(thing, 1, 0)
    tk.update()
# to keep score as an iteger. cba to do it properly. room for optimisation here.
def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier
# the restart switch, thing 1.
def restart(event):
    canvas.move(thing1, 1, 0)
    tk.update()

# binding functions to events
canvas.bind('<KeyPress-w>', jump)
canvas.focus_set()
canvas.bind('<KeyPress-space>', jump)
canvas.focus_set()
canvas.bind('<Up>', jump)
canvas.focus_set()
canvas.bind('<Button-1>', jump)
canvas.focus_set()
canvas.bind('<Return>', restart)
canvas.focus_set()

# main loop. using 'things' to keep everything in here so it dont get messy.
while True:
    # on-screen text
    playerscore = canvas.create_text(620, 20, text='Score : '+str(round_up(score, 1)), font=('courier'))
    playagain = canvas.create_text(350, 100, text='Press ENTER to play again', font=('courier', 27))
    highscore = canvas.create_text(400, 20, text='HighScore : '+str(round_up(hiscore, 1)), font='courier')
    # master rng. assign different numbers to item to randomise when they spawn in
    waitcall = random.randint(0, 200)
    # coordinates
    pos = canvas.coords(thing)
    pos1 = canvas.coords(dinobox)
    pos2 = canvas.coords(horizonline)
    pos3 = canvas.coords(smallcactusbox)
    pos4 = canvas.coords(bigcactusbox)
    pos5 = canvas.coords(cactusgroupbox)
    pos6 = canvas.coords(thing1)
    pos7 = canvas.coords(dino1)
    pos7 = canvas.coords(dino2)
    pos7 = canvas.coords(dino3)
    pos8 = canvas.coords(birdbox)
    # dino doesnt automatically move eack frame. see lines gravity and jumpingness of dino.
    canvas.move(smallcactusbox, xspeed, 0)
    canvas.move(smallcactus, xspeed, 0)
    canvas.move(bigcactusbox, xspeed, 0)
    canvas.move(bigcactus, xspeed, 0)
    canvas.move(cactusgroupbox, xspeed, 0)
    canvas.move(cactusgroup, xspeed, 0)
    canvas.move(birdbox, xspeed-2, 0)
    canvas.move(bird1, xspeed-2, 0)
    canvas.move(bird2, xspeed-2, 0)
    # jumpingness of dino
    if pos[0] == 1 :
        if pos1[3]>=pos2[3]-10 :
            yspeed = -6
            canvas.move(dinobox, 0, yspeed)
            canvas.move(dino1, 0, yspeed)
            canvas.move(dino2, 0, yspeed)
            canvas.move(dino3, 0, yspeed)
            canvas.move(thing, -1, 0)
    # speeding up the game as score increases
    if end == False:
        xspeed = -4-(score/5)
    # hide playagain message during game
    if xspeed < 0 :
        canvas.itemconfigure(playagain, state=HIDDEN)
    if xspeed == 0 :
        canvas.itemconfigure(playagain, state=NORMAL)
    # only show jumping dino while its in the air
    if pos1[3] < pos2[1]:
        canvas.itemconfigure(dino3, state=NORMAL)
        canvas.itemconfigure(dino2, state=HIDDEN)
        canvas.itemconfigure(dino1, state=HIDDEN)
    # make it RUN!
    if pos1[3] >= pos2[1]:
        canvas.itemconfigure(dino3, state=HIDDEN)
        if count2 > 0:
            canvas.itemconfigure(dino2, state=NORMAL)
            canvas.itemconfigure(dino1, state=HIDDEN)
            canvas.itemconfigure(bird2, state=NORMAL)
            canvas.itemconfigure(bird1, state=HIDDEN)
        if count2 > 0.2:
            canvas.itemconfigure(dino1, state=NORMAL)
            canvas.itemconfigure(dino2, state=HIDDEN)
            canvas.itemconfigure(bird1, state=NORMAL)
            canvas.itemconfigure(bird2, state=HIDDEN)
        if count2 > 0.4:
            count2 = 0
    # make birds wings flap
    if count3 > 0:
        canvas.itemconfigure(bird2, state=NORMAL)
        canvas.itemconfigure(bird1, state=HIDDEN)
    if count3 > 0.2:
        canvas.itemconfigure(bird1, state=NORMAL)
        canvas.itemconfigure(bird2, state=HIDDEN)
    if count3 > 0.4:
        count3 = 0
    # let there be GRAVITY!!
    if pos1[3] < pos2[1] :
        yspeed = yspeed+g*0.01
        canvas.move(dinobox, 0, yspeed)
        canvas.move(dino1, 0, yspeed)
        canvas.move(dino2, 0, yspeed)
        canvas.move(dino3, 0, yspeed)
    # to return items to other side of screen at their waitcall
    if waitcall == 0 and pos3[2]<0:
        canvas.move(smallcactusbox, WIDTH-pos3[0], 0)
        canvas.move(smallcactus, WIDTH-pos3[0], 0)
    if waitcall == 1 and pos4[2]<0:
        canvas.move(bigcactusbox, WIDTH-pos4[0], 0)
        canvas.move(bigcactus, WIDTH-pos4[0], 0)
    if waitcall == 2 and pos5[2]<0:
        canvas.move(cactusgroupbox, WIDTH-pos5[0], 0)
        canvas.move(cactusgroup, WIDTH-pos5[0], 0)
    if waitcall == 3 and pos8[2] < 0:
        birdheight = random.randint(-1, 1)
        if 201 > (pos8[1] + birdheight*50) > 149 :
            canvas.move(birdbox, 0, birdheight*50)
            canvas.move(bird1, 0, birdheight*50)
            canvas.move(bird2, 0, birdheight*50)
        canvas.move(birdbox, WIDTH-pos8[0], 0)
        canvas.move(bird1, WIDTH-pos8[0], 0)
        canvas.move(bird2, WIDTH-pos8[0], 0)
    # collision logic
    if pos3[3]+50 > pos1[3] > pos3[1] and (pos3[0]-20) < pos1[0] < pos3[2] :
        xspeed = 0
        yspeed = 0
        tk.update()
        end = True
    if pos4[3]+50 > pos1[3] > pos4[1] and (pos4[0]-20) < pos1[0] < pos4[2] :
        xspeed = 0
        yspeed = 0
        tk.update()
        end = True
    if pos5[3]+50 > pos1[3] > pos5[1] and (pos5[0]-20) < pos1[0] < pos5[2] :
        xspeed = 0
        yspeed = 0
        tk.update()
        end = True
    if pos8[3]+50 > pos1[3] > pos8[1] and (pos8[0]-20) < pos1[0] < pos8[2] :
        xspeed = 0
        yspeed = 0
        tk.update()
        end = True
    tk.update()
    time.sleep(var)
    var = 0
    # restarting the game. needs to be after collision logic or xspeed keeps resetting to 0.
    if pos6[0] == 1:
        canvas.move(smallcactusbox, WIDTH+300, 0)
        canvas.move(smallcactus, WIDTH+300, 0)
        canvas.move(bigcactusbox, WIDTH-pos4[0]+300, 0)
        canvas.move(bigcactus, WIDTH-pos4[0]+300, 0)
        canvas.move(cactusgroupbox, WIDTH-pos5[0]+600, 0)
        canvas.move(cactusgroup, WIDTH-pos5[0]+600, 0)
        canvas.move(birdbox, WIDTH-pos8[0]+10000, 0)
        canvas.move(bird1, WIDTH-pos8[0]+10000, 0)
        canvas.move(bird2, WIDTH-pos8[0]+10000, 0)
        xspeed = -4
        score = 0
        count = 0
        canvas.move(thing1, -1, 0)
        end = False
    time.sleep(0.01)
    if end == False:
        score += 0.01
        if score > hiscore:
            hiscore = score
    count += 0.01
    count2 += 0.01
    count3 += 0.01
    tk.update()
    # deleting text after the update so they dont all pile up
    canvas.delete(playerscore)
    canvas.delete(playagain)
    canvas.delete(highscore)
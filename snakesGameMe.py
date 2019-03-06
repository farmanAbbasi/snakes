import turtle
import time
import random
import winsound
from playsound import playsound

def checkCollision(segments):
    #stopping bg music and playing dying sound
        winsound.PlaySound(None, winsound.SND_ASYNC)
        playsound('gameover.wav',False)
        
        head.goto(0,0)
        head.direction='stop'
        
        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
            
        #Clear the segments
        segments=[]

        #Update score after collision
        score=0
        pen.clear()
        pen.write('Score: {0}   High Score: {1}'.format(score,high_score),align='center',font=('Arial',22,'normal','bold'))
        
        #Reset Delay
        delay=0.2
    

delay=0.2# for speed of snake
segments=[]
# Score
score = 0
high_score = 0
#random colors
colors  = ["red","green","blue","orange","purple","pink","yellow","white"]
c=''

# Set up the screen
wn=turtle.Screen()
wn.title("Snake Game")
wn.bgcolor('lightblue')
#wn.bgpic('background-image.gif')
wn.update()
wn.setup(width=600,height=600)
wn.tracer(0)#screen refresh so that we can't see things moving or more precisely
#it stops any update of screen and we manually update it which allows us to make it fast

#snake head
head=turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('black')
head.penup()
head.goto(0,0)
head.direction='stop'

#snake food
food=turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(0,100)

#Pen for score
pen=turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write('Score: {0}   High Score: {0}'.format(score,high_score),align='center',font=('Arial',22,'normal','bold'))

#starting with music is not used as i want to play music when first food is eaten
#winsound.PlaySound("background-score.wav", winsound.SND_ASYNC | winsound.SND_FILENAME)

#functions
def move():
    if head.direction=='up':
        y=head.ycor()
        head.sety(y+20)
    if head.direction=='down':
        y=head.ycor()
        head.sety(y-20)
    if head.direction=='left':
        x=head.xcor()
        head.setx(x-20)
    if head.direction=='right':
        x=head.xcor()
        head.setx(x+20)
        
def go_up():
    if head.direction!='down':
        head.direction='up'
def go_down():
    if head.direction!='up':
        head.direction='down'
def go_left():
    if head.direction!='right':
        head.direction='left'
def go_right():
    if head.direction!='left':
        head.direction='right'

#keyboard bindings
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_up,"Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

while True:
    
    wn.update()
    #Check for collision with the food---------------------------------------------------------------------------------------------------------------------------------
    if head.distance(food)<20:
        
        #make sound 
        playsound('eat2.wav',False)
        cprevious=c
        #Move the food to random position
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        c=random.choice(colors)
        food.color(c)
        food.goto(x,y)
        
        #Update score after eating note : white has highest score
        if cprevious=='white':
            score+=100
        else:    
            score+=10
        
        #Add segment to the chain
        new_segment=turtle.Turtle()
        new_segment.speed(0)#this is refresh speed to max
        new_segment.shape('square')
        new_segment.color('gray')
        new_segment.penup()
        segments.append(new_segment)
        
        #if food is eaten for the first time then start music
        if len(segments)==1:
            winsound.PlaySound("background-score.wav", winsound.SND_ASYNC | winsound.SND_FILENAME | winsound.SND_LOOP )

        #Set high score
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write('Score: {0}   High Score: {1}'.format(score,high_score),align='center',font=('Arial',22,'normal','bold'))

        # Shorten the delay
        if delay !=0.01:# so that it is never zero
            delay -= 0.005
        else:
            delay-=0.001

    #Check for collision with border------------------------------------------------------------------------------------------------------------------------------------
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        checkCollision(segments)      

    #Check for collision with self------------------------------------------------------------------------------------------------------------------------------------
    for segment in segments:
        if head.distance(segment)<20:
            checkCollision(segments)            

    #Append food-------------------------------------------------------------------------------------------------------------------------------------------------
    #abhi toh only segment is added on screen and on the segments array
    #now append thses on back of snake head
    #to do this if 10 segments are there 10 will goto 9 and 9 will go 8 and so on
    #upto 1 as 1 will goto 0 and now 0 is special case that will goto heads previous place
    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        #segments[index].goto(x,y)
        #what this does was connect them without gaps
        #for gaps use these 4 conditions
        if head.direction=='up':
            segments[index].goto(x,y-3)
        if head.direction=='down':
            segments[index].goto(x,y+3)
        if head.direction=='right':
            segments[index].goto(x-3,y)
        if head.direction=='left':
            segments[index].goto(x+3,y)    
        
    #now move segment[0] to head position
    if len(segments) > 0:
        x=head.xcor()
        y=head.ycor()
        #segments[0].goto(x,y)
        #what this does was connect them without gaps
        #for gaps use these 4 conditions
        if head.direction=='up':
            segments[0].goto(x,y-3)
        if head.direction=='down':
            segments[0].goto(x,y+3)
        if head.direction=='right':
            segments[0].goto(x-3,y)
        if head.direction=='left':
            segments[0].goto(x+3,y)
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------
    move()
    time.sleep(delay)
#abruplty closing of screen ko rokta hai--------------------------------------------------------------------------------------------------------------------------------    
wn.mainloop()

    



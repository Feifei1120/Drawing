from turtle import *
screensize(500,500)

#head
pensize(5)
home()
seth(0)
pd()

color("black")
circle(20,80)#0
circle(200,30)#1
circle(30,60)#2
circle(200,29.5)#3
color("black")
circle(20,60)#4
circle(-150,200)#5
circle(-50,10)#6
circle(50,70)#7

#nose about place
x_nose =xcor()
y_nose =ycor()

circle(30,62)#8
circle(200,15)#9

#nose
pu()
goto(x_nose,y_nose+25)
seth(90)
pd()
begin_fill()
circle(8)
end_fill()

#eyes




import turtle
t = turtle.Turtle()
tb = turtle.Turtle()
ty = turtle.Turtle()

t.shape('turtle')
tb.shape('turtle')
ty.shape('turtle')

sc = turtle.Screen()

t.color('green')
tb.color('blue')
ty.color('yellow')
ty.speed(10)
tb.write('Start Ismail,', font=('Courier,32,bold'), align = ('right'))
tb.write('Good Morning,', font= ('Courier,32,bold'), align = ('left'))
x= int(input('Enter the steps you want yout turtle to move'))
def go_forward():
    t.forward(x)

def go_up():
    t.setheading(90)

def go_down():
    t.setheading(270)

def go_right():
    t.setheading(360)

def go_left():
    t.setheading(180)

def on_click(x,y):
    sc.tracer(0)
    t.setheading(t.towards(x,y))
    t.goto(x,y)
    sc.tracer(1)
    print(t.pos())

def on_drag(x,y):
    sc.tracer(0)
    t.goto(x,y)
    sc.tracer(1)

#linking the keys with the functions
sc.listen()
sc.onkey(go_forward,'space')
sc.onkey(go_up,'w')
sc.onkey(go_down,'s')
sc.onkey(go_left,'a')
sc.onkey(go_right,'d')
sc.onclick(on_click)
t.onclick(on_drag)
tb.goto(100,30)





turtle.done()

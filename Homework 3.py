#Problem 1
n = int(input("Enter the number of numbers to be summed: "))
total = 0
for i in range(1, n+1):
    num = float(input('Enter number: '))
    total = total + num
print('The sum of your numbers is ', total, '.', sep='')

print('')
#problem 2
n = int(input("Enter the number of numbers you wish to average: "))
total = 0
for i in range(1, n+1):
    num = float(input("Enter any number: "))
    total = total + num
    average = total / n
    print("The average is ", average, '.', sep='')


#problem 3
#from graphics import *
#def main():
    #center = Point(130,130)

#c = Circle(Point(30,40),25)
#c.setFill("blue")
#c.setOutline("red")

#r = Rectangle(Point(20,20), Point(40,40))
#r.setFill(color_rgb(0,255,150))
#r.setWidth(3)

#l = Line(Point(100,100), Point(100,200))
#l.setOutline("red4")
#l.setArrow("first")

#shape = Polygon(Point(5,5), Point(10,10), Point(5,10), Point(10,5))
#shape.setFill("orange")

#t = Text(Point(100,100), "Hello World!")
#t.setFace("courier")
#t.setSize(16)
#t.setStyle("italic")
#win = GraphWin()
#Oval(Point(50,50), Point(60, 100)).draw(win)   
#c.draw(win)
#r.draw(win)
#l.draw(win)
#shape.draw(win)
#t.draw(win)

#win.getMouse()
#win.close()
#main()


#problem 4
#from graphics import *
#def main():
    #win = GraphWin()
    #shape = Circle(Point(50,50), 20)
    #shape.setOutline("red")
    #shape.setFill("red")
    #shape.draw(win)
    #for i in range(10):
        #p = win.getMouse()
        #c= shape.getCenter()
        #dx = p.getX() - c.getX()
        #dy = p.getY() - c.getY()
        #shape.move(dx,dy)
        
    #win.getMouse()
    #win.close()
#main()
#The red circle appears. You move it ten times with the cursor. 

print('')
#problem 5
from graphics import *
def main():
    win = GraphWin()
    c1 = Circle(Point(100,100), 50)
    c1.setFill('white')
    c1.draw(win)
    
    c2 = Circle(Point(100,100), 40)
    c2.setFill('black')
    c2.draw(win)
               
    c3 = Circle(Point(100,100), 30)
    c3.setFill('blue')
    c3.draw(win)
               
    c4 = Circle(Point(100,100), 20)
    c4.setFill('red')
    c4.draw(win)
               
    c5 = Circle(Point(100,100), 10)
    c5.setFill('yellow')
    c5.draw(win)

    win.getMouse()
    win.close()
main()

print('')
#problem 6
from graphics import *
def main():
    win = GraphWin()
    outline = Circle(Point(100,100), 50)
    outline.setOutline('white')
    outline.draw(win)

    left_eye = Circle(Point(77,80), 5)
    left_eye.setFill('white')
    left_eye.draw(win)

    right_eye = Circle(Point(123,80), 5)
    right_eye.setFill('white')
    right_eye.draw(win)

    nose = Line(Point(100,90), Point(100,110))
    nose.setOutline('white')
    nose.draw(win)

    mouth = Polygon(Point(80,120), Point(130,120), Point(100,130))
    mouth.setFill('white')
    mouth.draw(win)

    win.getMouse()
    win.close()
main()

print('')
#problem 7
from graphics import *
from math import sqrt
def main():
    win = GraphWin()
    win.setBackground('grey')
    
    text = Text(Point(100,20), 'Click on two points to draw the line segment')
    text.setSize(8)
    text.draw(win)

    pt1 = win.getMouse()
    pt1.draw(win)
    pt2 = win.getMouse()
    line = Line(pt1, pt2)
    line.setWidth(2)
    line.draw(win)

    mid_x = (pt1.getX() + pt2.getX()) / 2
    mid_y = (pt1.getY() + pt2.getY()) / 2
    midpt = Circle(Point(mid_x, mid_y), 2)
    midpt.setOutline('blue')
    midpt.setFill('blue')
    midpt.draw(win)

    dx = pt2.getX() - pt1.getX()
    dy = pt2.getY() - pt1.getY()
    slope = - dy / dx
    length = sqrt(dx**2 + dy**2)
    text.setText('Slope: ' + format(slope, '0.4') + '\nLength: ' + \
                 format(length, '0.4') + ' px')
    win.getMouse()
    win.close()
main()

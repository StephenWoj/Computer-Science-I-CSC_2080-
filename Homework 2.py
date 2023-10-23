#Problem 1
#a)
#for i in range(5):
    #print(i * i)
#0
#1
#4
#9
#16

#b)
#for d in [3,1,4,1,5]:
    #print(d, end=" ")
#3 1 4 1 5

#c)
#for i in range(4):
    #print("Hello")
#Hello
#Hello
#Hello
#Hello

#d)
#for i in range(5):
    #print(i, 2**i)
#0 1
#1 2
#2 4
#3 8
#4 16

#Problem 2
#a)
#print(4.0 / 10.0 + 3.5 * 2)
#7.4
#float

#c)
#print(abs(4 - 20 // 3) ** 3)
#8
#int

#e)
#print(3 * 10 // 3 + 10 % 3)
#11
#int

#Problem 3
#import math
#b)
#n = float(input("Enter a number for n: "))
#output = n * (n-1) / 2
#print(output)

#c)
#r = float(input("Enter a number for r: "))
#output = 4 * math.pi * r ** 2
#print(output)

#Problem 4
#b)
#for i in [1,3,5,7,9]:
#    print(i, ":", i**3)
#  1 : 1
#  3 : 27
#  5 : 125
#  7 : 343
#  9 : 729

#c) 
#x = 2
#y = 10
#for j in range(0, y, x):
#    print(j, end="")
#    print(x + y)
#12
#Problem 5
x1, y1 = eval(input('Enter the coordinates of the first point: '))
x2, y2 = eval(input('Enter the coordinates of the second point: '))
s = (y2 - y1) / (x2 - x1)
print('The slope of your line is ', s, '.', sep='')

print('')
#Problem 6
x1, y1 = eval(input('Enter the coordinates of the first point: '))
x2, y2 = eval(input('Enter the coordinates of the second point: '))
d = ( (x2-x1) **2 + (y2-y1) **2) ** 0.5 
print('Distance = %f' %(d))

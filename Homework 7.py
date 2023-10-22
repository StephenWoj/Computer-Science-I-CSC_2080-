#Problem 1
#a) Definite loop vs Indefinite loop
#Both loops cause the same code to repeat several times.
#Definite loop repeat a specifice number of times before the code is run.
#Indefinite loop will just continue repeating until the expression is false.

#b) For loop vs. While loop
#Both loops are an example of how Python implements loop structures.
#For loop is used for definite loop and while loop is used for indefinite loop.

#c) Interactive loop vs. Sentinel loop
#Both loops are structures of indefinite loop.
#Interactive loop asks if the user wants to continue after getting each input 
#while a sentinel loop will repeatly prompt the user for input but will allow 
#the loop to end when a sentinel value is input.

#d) Sentinel loop vs. End-of-file loop
#Both loops are structures of indefinite loop.
#End-of-file loop will continue getting an input from a file until th end.
#Sentinel loop works the same way except that now you are getting the input from file.

#Problem 2
#a)
        #not (P and Q)
#P| |Q| |P and Q| |not (P and Q)
#T| |T| |   T   | |     F
#T| |F| |   F   | |     F
#F| |T| |   F   | |     T
#F| |F| |   F   | |     T

#b)
      #(not P) and Q
#P| |Q| |not P | |(not P) and Q
#T| |T| |   F  | |     F
#T| |F| |   F  | |     F
#F| |T| |   T  | |     T
#F| |F| |   T  | |     F

#c)
        #(not P) or (not Q)
#P| |Q| |not P | not Q |(not P) or (not Q)
#T| |T| |   F  |   F   |     F
#T| |F| |   F  |   T   |     T
#F| |T| |   T  |   F   |     T
#F| |F| |   T  |   T   |     T

#d)
        #(P and Q) or R
#P| |Q| |R| |P and Q|(P and Q) or R
#T| |T| |T| |   T   |     T
#T| |T| |F| |   T   |     T
#T| |F| |T| |   F   |     T
#T| |F| |F| |   F   |     F
#F| |T| |T| |   F   |     T
#F| |T| |F| |   F   |     F
#F| |F| |T| |   F   |     T
#F| |F| |F| |   F   |     F

#e)
#(P or R) and (Q or R)
#P| |Q| |R| |P or R| Q or R| (P and Q) or R
#T| |T| |T| |   T  |   T   |       T
#T| |T| |F| |   T  |   T   |       T
#T| |F| |T| |   T  |   T   |       T
#T| |F| |F| |   T  |   F   |       F
#F| |T| |T| |   T  |   T   |       T
#F| |T| |F| |   F  |   T   |       F
#F| |F| |T| |   T  |   T   |       T
#F| |F| |F| |   F  |   F   |       F

#Problem 3
#a)
#total = 0
#for num in range(n + 1):
    #total += num
#c)
#total = o
#user_num = eval(input('Enter a number, 999 to quit: '))
#while user_num != 999:
    #total += user_num
    #user_num = eval(input('Enter a number, 999 to quit: '))

#Problem 4
n = eval(input('Enter a positive number: '))

prev = 1
fib = 1
for i in range(2,n):
        temp = prev
        prev = fib
        fib = temp + fib

print('Fibonacci('+ str(n) +') is',fib)

#Problem 5
n = eval(input('Enter a positive number: '))

print(str(n) + ', ', end="")
while n != 1:
        if n % 2 == 0:
                n = n //2
        else:
                n = 3*n + 1

        if n != 1:
                print(str(n) +', ', end="")
        else:
                print(1)


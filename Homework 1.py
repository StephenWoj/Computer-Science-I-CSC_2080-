#Problem 2
print("Hello, world!")
print("Hello", "world!")
#1a has comma between Hello and world. 1b prints out a phrase.
print(3)
print(3.0)
#1c and 1d print out the numbers in the function.
print(2+3)
print(2.0+3.0)
print("2" + "3")
#1e and 1f print out 5 or 5.0 as the answer. 1g prints out 23 due to the numbers.
print(2 * 3)
print(2 ** 3)
#1i multiplies 2 and 3 to equal 6. 1j multiplies 2 three times to equal 8.
print(7 / 3)
print(2//3)
#1k divied 7 and 3 to equal 2.3333333333333335. 2//3 just answers the whole number.

print('')
#Problem 3
def main():
    n = eval(input('How many numbers should I print?: '))
    x = eval(input('Enter a number between 0 and 1: '))
    for i in range(n):
        x = 3.9 * x * (1 - x)
        print(x)
main()

print('')
#Problem 4        
km_to_mi = 0.62
kilometer = eval(input('How many kilometres?: '))
miles = kilometer * km_to_mi
print(miles,'miles')

print('')
#Problem 5
def main(): 
    t = eval(input('How many years for money will be compounded?: '))
    A = 10000 * (1 + 0.08 / 12) ** 12 * t
    print('The final amount is', round(A, 2), 'dollars')
    

main()

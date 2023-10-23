#Problem 1
def Ee_igh():
    return ', Ee-igh, Ee-igh, Oh!'

def macD(animal, sound):
    print('Old MacDonald had a farm' + Ee_igh())
    print('And on that farm he had a', animal + Ee_igh())
    print('With a', sound + ', there a', sound + ', everywhere a', sound + ',' , sound + '.')
    print('Old MacDonald had a farm' + Ee_igh())

def main():
    macD('cow', 'moo')
    print()
    macD('pig', 'oink')
    print()
    macD('sheep', 'baa')
    print()
    macD('turkey', 'gobble')
    print()
    macD('horse', 'niegh')

main()
print('')
#Problem 2
def avgfun(n, num):
    total = 0
    total = total + num
    average = total / n
    return average
def main():
    n = int(input("Enter the number of numbers you wish to average: "))
    for i in range(1, n+1):
        num = float(input("Enter any number: "))
    print("The average is ")
    print(avgfun(n, num))
main()
print('')
#Problem 3
from math import sqrt
def d(dx, dy):
    length = sqrt(dx**2 + dy**2)
    return length

def s(dx, dy):
    slope =  dy / dx
    return slope

def main():
    first_x = int(input("Enter the first X value: "))
    second_x = int(input("Enter the second X value: "))
    first_y = int(input("Enter the first Y value: "))
    second_y = int(input("Enter the second Y value: "))
    dy = (second_y - first_y)
    dx = (second_x - first_x)
    print('The slope is')
    print(s(dx, dy))
    print('The distance is')
    print(d(dx, dy))   

main()
print('')
#Problem 4
def sumList(nums):
    total = 0
    for num in nums:
        total += num
    return total
def main():
    list_of_lists = [[], [2], [1,2,4,10], [-1,-6,1,6], [1.1,2.2]]
    for lst in list_of_lists:
        print(sumList(lst))
main()
print('')
print('Problem 5')
def get_some_strings():
    n = int(input("Number of strings: "))
    return n
def main():
    my_list = list()
    for i in range(get_some_strings()):
        my_str = input("Enter string: ")
        my_list.append(my_str)
        print(my_list)
main()







#Problem 1
#In a try/except, the try block runs first. If it raise an exception,
#then it passes out of the try block until a match is found.
#In the ordinary decision structures, if is the first condition.
#If it fails, then elif condition is tested.


#Problem 2
score = eval(input('Enter your exam score: '))
if score >= 0 and score <= 100:
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'
    print('Your grade is', grade)
else:
    print('Invalid score.')

print('')
#Problem 3
def time(time_str):
    hr_str, min_str = time_str.split(':')
    hr = int(hr_str)
    minute = int(min_str)
    return hr + minute / 60
def main():
    pre_rate = 2.5
    post_rate = 1.75

    start_str = input('Enter the start time in 24hr format: ')
    start = time(start_str)
    end_str = input('Enter the end time in 24hr format: ')
    end = time(end_str)

    if end < 21:
        cost = (end-start)*pre_rate
    elif start < 21 and end >= 21:
        cost = (21-start)*pre_rate + (end-21)*post_rate
    else:
        cost = (end-start)*post_rate
    print('The total babysitting bill comes to ${0:0.2}.'.format(cost))
main()

print('')
#Problem 4
age = int(input('How old are you: '))
citizenship = int(input('How many years have you been a citizen: '))

if age >= 30 and citizenship >= 9:
        print('Your eligible to run for the Senate or the House of Representatives.')
elif age >= 25 and citizenship >= 7:
        print('Your eligible to run for the House of Representives')
else:
    print('Your not eligible to run for the Senate or House of Representatives.')

print('')
#Problem 5
#Homework 2 Problem 5
try:
    x1, y1 = eval(input('Enter the coordinates of the first point: '))
    x2, y2 = eval(input('Enter the coordinates of the second point: '))
    s = (y2 - y1) / (x2 - x1)
    print('The slope of your line is ', s, '.', sep='')
except NameError:
    print('Invaild coordinates')
except TypeError:
    print('Do x and y coordinates together')
            




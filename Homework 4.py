#Problem 1
#s1 = "spam"
#s2 = "ni!"

#print(s1[1])
#print(s1[2] + s2[:2])
#print(s1.upper())

#Problem 2
#s1 = "spam"
#s2 = "ni!"
#print(s2[:2].upper())
#print(s1[:])
#print([s1[:2], s1[3]])

#Problem 3
#for w in "Now is the winter of our discontent...".split():
    #print(w)
#for w in "Mississippi".split("i"):
    #print(w, end=" ")
#msg = ""
#for ch in "secret":
    #msg = msg + chr(ord(ch)+1)
    #print(msg)

#Problem 4
print('grades = "', end='')
x = ('F'*60 + 'D'*10 + 'C'*10 + 'B'*10 + 'A'*10)
print (x, end='"')

print('')
#Problem 5
scores = 'F'*60 + 'D'*10 + 'C'*10 + 'B'*10 + 'A'*11
exam_score = eval(input('Points scored on the exam: '))
print('The grade for that score is  ' + scores[exam_score] + '.')

print('')
#Problem 6
user_str = input('Type in a phrase: ')
word_list = user_str.split()
acronym = ''
for word in word_list:
    acronym += word[0].upper()
print('The phrase is', acronym + '.')

print('')
#Problem 7
alphabet = 'abcdefghijklmnopqrstuvwxyz'
name = input('Enter a name: ')
name_value = 0
for ch in name:
    name_value += alphabet.find(ch.lower())+ 1
print('The numeric value of', name, 'is', str(name_value) + '.')

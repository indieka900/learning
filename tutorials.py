def break_all():
    for j in range(1, 5):
        for i in range(1,4):
            if i*j == 6:
                return(i) # will stop when i*j = 6
            print(i*j)
#reak_all()
def break_loop():
    for i in range(1, 5):
        if (i == 4):
            return(i)
        print(i)
    return(5)
#break_loop()
#for index, item in enumerate(['one', 'two', 'three', 'four']):
    #print(index, '::', item)
d = {"a": 1, "b": 2, "c": 3}
#for key in d:
#    print(key)
#for values in d.values():
#    print(values)
lst = ['alpha', 'bravo', 'charlie', 'delta', 'echo']
#for s in lst:
    #print(s[:1])  #will display the first letter in each of the element
#for idx, s in enumerate(lst):
#    print("%s has an index of %d" % (s, idx)) #will display index of each element in a list
from array import *
my_array = array('i', [1,2,3,4,5])
#my_array.append(6)  # will insert 6 as a last digit
#my_array.insert(0,9)  #will insert 9 in index 0
my_extnd_array = array('i', [7,8,9,10])
my_array.extend(my_extnd_array)  #it extends the array
#for i in my_array:
    #print(i)
s = {1,2,2,3,4,4}
x = list(s)
#print(x[2])
#function is a bunch of code that performs a particular task
#def greetings_tune(name):
    #print('welcome '+name)
#greetings_tune('john')
#def greetings_tune(name, age):
#    print(f"welcome {name} you are  {(age)} years old.")
#    print('Welcome ',name, 'you are' ,age)
#greetings_tune('john',27)
#def salary(nam,Basic_salary,sales):
#    commision = 0
#    if sales >= 100000:
#        commision = sales *0.02
#    salary = Basic_salary + commision
#    print(f"{nam}'s salary:{salary}")
#salary("Jared",100000,150000)
#salary("Joseph",123000,4522340)
#salary("Jose",123343,4566)
counter = 0
x = 12.435
'''while counter < 3:
    print("Inside loop is %1.2f" %x )
    counter += 1
else:
    print("Inside else")
    print(1,2,3,4,5,sep='#')'''
'''for val in 'joseph':
    if val == 'p':
        break
    print(val)
print('The end!!!')
for val in 'joseph indieka':
    if val == 'p' or val == 'i':
        continue
    print(val)
print('The end!!!')
while True:
    num = int(input('Enter the integer: '))
    print('The cube of',num,'is',num**3)
n = int(input('Enter n: '))
sum = 1
i = 1
while i <= n:
    sum += i
    i += 1
    print(i,end=' ')
print('\nThe sum is: ',sum)
vowels = 'AEIOU'
while True:
    v = input('Enter the  vowel: ').upper()
    if v in vowels:
        break
    print('That is not a vowel try again')
print('Thank you!!!')
import random
while True:
    input('Press enter to roll the dice')
    num = random.randint(1,6)
    print('You got',num)
    opt = input('Do you want to try again(y/n)').lower()
    if opt == 'n':
        print('Thanks for playing!')
        break
def greet(name):
    print('Hello',name,'\nGood Morning!!')
greet('jose.')
greet('Mark')
def value(num):
    if num >= 0:
        return num
    else:
        return -num
print(value(5))
print(value(-9))
def mine():
    x = 200
    print('Value inside functions:',x)
x = 132
mine()
print('Outerside functions:',x)
def add(x,y):
    sum = x + y
    return sum
num = int(input('Enter the first number: '))
num1 = int(input('Enter the second number: '))
print('The sum is',add(num,num1))
def greet(name,msg):
    print('Hello',name,msg)
greet('God','Loves me')
def greet(*names):
    for name in names:
        print('Hello',name)
greet('Joseph','Mark','Lyn','Mitchele')'''

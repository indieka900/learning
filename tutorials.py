'''def break_all():
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
while counter < 3:
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
greet('Joseph','Mark','Lyn','Mitchele')
def greet(name,msg='Hi'):
    print(name,msg)
greet('Joseph')
greet('Ann')
def recury(x):
    if x == 1:
        return 1
    else:
        return(x*recury(x-1))

num = int(input("Enter the number: "))
if num >= 1:
    print('The factorial of',num,'is',recury(num))
    for n in range(num+1,0,-1):
        print(n,end=' ')
double = lambda x: x * 8
print(double(5))
my_list = [1,5,3,7,4,6,80]
new_list = list(filter(lambda x: (x%2 == 0),my_list)) #use of filter where it illuminates the item which is not divisible by 2
print(new_list)
my_list = [1,5,3,7,4,6,80]
new_list = list(map(lambda x: (x*2),my_list)) #use of map it will multiply everything by 2
print(new_list)
import math
print(math.pi)
print(math.e
import sys
for i in sys.path:
    print(i))
y = 0b11011001 #binary
m = 0xFBC #hexadecimal
n = 0o15 #octal
print(y)
print(m))
from decimal import Decimal as D
y = D('1.5') * D('3.20')
print(y)
import random
#print(random.randrange(000,999))
y = ['a','b','c','d','e']
print(random.choice(y))
print(random.shuffle(y))
my_lst = ['j','r','p','b','p']
print('m' in my_lst)
print(my_lst[1:-3])
print(my_lst.count('r'))
print(my_lst.index('p'))
count = 0
for letter in 'Hello World':
    if (letter == 'l'):
        count += 1
#print(count)
#print('He said, "What\vs there"')
print('He said, "What\x61 s there"')
print(r'He said, "What\x61 is there"')
password = "friend"
pwd = input("Enter the password to login: ")
if pwd == password:
    print("Login succesfully")
else:
    print("Incorrect password")
light = input("Enter the light colour: ").lower()
if light == "red":
    print("Do not cross")
elif light == "green":
    print("You may cross \nbye!!!")
elif light == "yellow":
    print("Wait a little ")
else:
    print("Invalid light colour!!!")
num = int(input("Enter the number: "))
if num <= 100 and num > 0:
    if num < 50:
        print("The number is less then 50")
    if num == 50:
        print("The number is 50")
    elif num > 50:
        print("The number is greater than 50 ")
else:
    print("Invalid Range")
print("{},{} and {} are good students.".format('john','joseph','dan'))
print("{2},{0} and {1} are good students.".format('john','joseph','dan'))
print("Binary represantation of {0} is {0:b}.".format(14))
print("The string alignment is",end=' ')
print("|{:<10}|{:<10}|{:<10}|".format('butter','bread','ham'))
print("This will split this line into list".split())
print('will split this line into list'.find('ne'))
print("Happy birthday girl".replace('birthday','Christmas'))
#sets
a = set() #creating empty set
print(type(a))
c = {1,6,2,4,3,5,7,1}
#my_set.discard(1)
#my_set.remove(6)
#print(my_set)
b = {23,43,54,15,32,1,6,4,7,5}
print(c|b) # union of the sets
print(c&b) # intersection of the sets
print(b-c) # set difference
print(c-b)
print(c^b) #symetric difference
for letter in set('apple'):
    print(letter)
for i in range(21):
    for j in range(i+1):
        print("@",end='')
    print("weekend ni kesho",end='')
    print("")
squares= {x: x**2 for x in range(10)}
print(squares)
squares= {x: x*x for x in range(10) if x%2 != 0}
print(squares)
for n in squares:
    print(squares[n])
countries = ["Nigeria","South Africa","Kenya","China","Germany","Canada"]
countries[0]="United states"
#print(countries)
list1 = [2,4,5,1,3]
list2 = ["banana","apple","Mangoes","oranges"]
#list1.extend(list2)
#print(list1)
list2.append("Cherry")
list2.insert(1,"pumkin")
list2.remove("apple")
#list2.clear()
#print(list2)
list1.sort()
#print(list1)
list2.pop()
#print(list2.pop())
names = ["Symon","Vicky",["Frankline","Tony",["Joseph","Ann"]]]
print(names[2][2][0])
names1 = ["Emmanuel","Jared",["Frank","Irene",["Patterson","Bruno"],"Peter"]]
#names[2][2].insert(2,names1[2][2][1])
print(names)
nmae = "John dor"
print(list(nmae))
import random
n=0.1
y=random.uniform(0.1,10.0)
#print("{:.2f}".format(y))
#lambda function
P = lambda x: x * 5
#print(P(5)) # is same as
def P(x):
    return x * 5
#print(P(5))
#lambda can also be used with filter which evaluates for a specific condition
#like here it evaluates and print even numbers in the list
my_list = [1,3,2,8,4,5,10,9]
#new_list = list(filter(lambda x: (x%2==0),my_list))
#print(new_list)
#Also lambda can be used with map
#like here map is used to double all the elements inthe list
new_list = list(map(lambda x: x * 2 , my_list))
#print(new_list)
for i in my_list:
    print(i*2,end=' ')
import decimal
#print(decimal.Decimal(0.1 + 1.2))
import fractions
#print(fractions.Fraction(1.5))
import math as m
print(m.pi)
print(m.cos(31))
print(m.exp(1))
print(m.log10(100)) #10 is a base
print(m.sinh(60))
print(m.fabs(31))
print(m.factorial(10))
marks = {}.fromkeys(['Math','English','Science'],2)
for items in marks.items():
    print(items)
squares = {x: x*x for x in range(0,101,5)}
for i in squares:
    print(i,end=' = ')
    print(squares[i])
import sys
while True:
    try:
        x = int(input("Enter the integer: "))
        r = 1/x
        print(r)
        break
    except:
        print("Oops!!",sys.exc_info () [0],"occured")
class Error(Exception):
    pass
class ValueTooSmallError(Error):
    pass
class ValueTooLargeError(Error):
    pass
number = 10
while True:
    try:
        i_number = int(input("Enter the number: "))
        if i_number < number:
            raise ValueTooSmallError
        elif i_number > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("This value is too small, try again!")
        print()
    except ValueTooLargeError:
        print("Value is too large, Try again!")
        print()
print("Congratulations!! you got it right")
def outer_function():
    a = 20
    def inner_fuction():
        a = 30
        #print("a =",a)
    inner_fuction()
    #print("a =", a)
a = 10
outer_function()
#print("a =",a)
class MyClass:
    "This is my class"
    a =10
    def func(self):
        print('Hello')
ob = MyClass()
print(MyClass.a)
#print(MyClass.func)
#print(MyClass.__doc__)
print(ob.func())
class ComplexNumber:
    def __init__(self,r=0,i=0):
        self.real = r
        self.image = i
    def getdata(self):
        print("{0}+{1}j".format(self.real,self.image))
c1 = ComplexNumber(2,4)
#del c1.image #deleting aatributes and objects
#del c1 #deleting an object
print(c1.getdata())
class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]
    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]
    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])
class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)
    def findArea(self):
        a, b, c = self.sides
# calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)
class Square(Polygon):
    def __init__(self):
        Polygon.__init__(self,2)
    def area(self):
        a,b = self.sides
        R = a*a
        P = a * 4
        print("The area is "+str(R))
        print("The perimeter of the square is "+str(P))
#t = Square()
#t.inputSides()
#t.dispSides()
#t.area()
class Point:
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
    def __mul__(self, other):
        """in addition we use __add__, substraction __sub__
        power is __pow__, division __truediv__ e.t.c"""
        x = self.x * other.x
        y = self.y * other.y
        return Point(x,y)
    def __lt__(self, other):
        """Overloading comparisons operators in python
        like here we are compairing points using < sign
        other signs like <= is __le__,= is __eq__,!= is __ne__
        > is __gt__ >= is __ge__"""
        self_mag = (self.x ** 2) + (self.y ** 2)
        other_mag = (other.x ** 2) + (other.y **2)
        return self_mag < other_mag
p1 = Point(2,3)
p2 = Point(-2,8)
print(Point(1,1) < Point(-2,-3))
print(p1>p2)
my_list = [3,7,5,6,2,9]
my_iter = iter(my_list)
#print(next(my_iter))
#print(next(my_iter))
#print(next(my_iter))
#print(my_iter.__next__())
class PowTwo:
    """A class to implement an iterator of powers of two"""
    def __init__(self, max = 0):
        self.max = max
    def __iter__(self):
        self.n = 3
        return self
    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration
#a = PowTwo(4)
#i = iter(a)
#print(next(i))
#print(next(i))
#print(next(i))
for k in PowTwo(10):
    print(k)
class Inflter:
    """Infinite iterator to return all odd numbers"""
    def __iter__(self):
        self.num = 1
        return self
    def __next__(self):
        num = self.num
        self.num += 2
        return num
a = iter(Inflter())
for i in Inflter():
    """will print infinite odd numbers"""
    print(i)
def my_gen():
    """a simple generator functon"""
    n=1
    print("this will be printed first")
    yield n
    n += 1
    print("This is printed second")
    yield n
    n += 1
    print("This is printed atlast")
    yield n
a = my_gen()
print(next(a))
print(next(a))
print(next(a))
#OR
for item in my_gen():
    print(item)
def rev_str(my_str):
    length = len(my_str)
    for i in range(length-1,-1,-1):
        yield my_str[i]
#for char in rev_str("hellojoseph"):
    #print(char,end=' ')
#list comprehension
lst = [3,6,4,8,2]
lst.sort()
#print([x**2 for x in lst])
#generator expression
a = (k**2 for k in lst)
#same as this but it produces one at atime as compared to the abive one
#print(next(a))
#print(sum(k**2 for k in lst))
#print(max(k**2 for k in lst))

# a simple code to generate powers of two
def gen(max=0):
    n=0
    while n < max:
        yield 2 ** n
        n += 1
b = gen(10)
print(next(b))
print(next(b))
#print(next(b))
#print(next(b))
for i in gen(12):
    print(i)
#nested function
def print_msg(msg):
    def printer():
        print(msg)
    return printer
an = print_msg("Hello")
an()
def make_multi(n):
    def multi(x):
        return x*n
    return  multi
times3 = make_multi(4)
times5 = make_multi(6)
#print(times3(6))
#print(times5(times3(3)))
def first(msg):
    print(msg)
#first("Joseph")
second = first
#second("Hello")
def inc(x):
    return x + 1
def dec(x):
    return x -1
def operator(func, x):
    result = func(x)
    return result
#print(operator(dec,5))
def is_called(age):
    print(age)
    def is_returned():
        print("Hello")
    return is_returned()
#is_called(23)
def smart_devide(func):
    def inner(a,b):
        print("I am going to divide",a,"and",b)
        if b == 0:
            print("Whoops! cannot divide")
            return
        return func(a,b)
    return inner
@smart_devide
def divide(a,b):
    return a/b
# same like
"""def div(a,b):
    return a/b
div = divide
print(div(2,5))"""
#print(divide(4,0))
# same as(The whole code)
def divided(a,b):
    print("I am going to divide", a, "and", b)
    if b == 0:
        print("Oops cannot be divided")
    else:
        return a/b
#print(divide(2,5))
#print(divide(4,0))
def star(func):
    def inner(*args,**kwargs):
        print("*" * 30)
        func(*args,**kwargs)
        print("*" * 30)
    return inner

def percent(func):
    def inner(*args,**kwargs):
        print("%" * 30)
        func(*args,**kwargs)
        print("%" * 30)
    return inner

#decoration
@star
@percent #oder also matters
def printer(msg):
    print(msg)
#print(printer("Helo"))
#The above decoration is same as
def printer(msg):
    print(msg)
#printer = star(percent(printer))
class Celsious:
    def __init__(self,temperature = 0):
        self.temperature = temperature
    def to_faraday(self):
        return (self.temperature * 1.8) + 32
man = Celsious()
man.temperature = 134
print(man.to_faraday())'''

#usefull examples
"""
#finding the squareroot of real or complex numbers
import cmath
#num = eval(input("Enter the number: "))
#num_sqrt = cmath.sqrt(num)
#print("The square root of {0} is {1:0.3f}+{2:0.3f}j".format(num,num_sqrt.real,num_sqrt.imag))
import math
numm = 25
nu_s = math.sqrt(numm)
#print(nu_s)
#program to calculate the quadratic equation
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
d = (b**2)-(4*a*c)
ans1 = (-b-math.sqrt(d))/(2*a)
ans2 = (-b+math.sqrt(d))/(2*a)
print("The solutions are {} and {}".format(ans1,ans2))
# to check if a number is a prime number
num = int(input("Enter a number to test: "))
if num > 1:
    for k in range(2,num):
        if (num % k) == 0:
            print(num,"is not a prime number")
            print(k,"divides",num,num//k,"times")
            break
    else:
        print(num,"is a prime number")
else:
    print(num, "is not a prime number!")

#print prime numbers in acertain interval and finding the sum of them
sum = 0
lor = int(input("Enter the lower range: "))
up = int(input("Enter the upper range: "))
for num in range(lor,up+1):
    if num > 1:
        for j in range(2,num):
            if ( num%j ) == 0:
                break
        else:
            sum+=num
            print(num)
print("The sum of the prime numbers is ",sum)
#To print the factors of a number
num = int(input("Enter a number: "))
if num >0:
    print("The factors are:")
    for i in range(1,num+1):
        if (num%i) == 0:
            print(i)
else:
    print("The factorial doesn't exist")

#to add natural number to acertain level provided
num = int(input("Enter a number: "))
sum =0
while num>0:
    sum += num
    num -= 1
    print(num)
print(sum)
#Python Program to Convert Decimal to Binary, Octal and Hexadecimal
dec = int(input("Enter the integer: "))
print("The decimal value of",dec,"is: ")
print("",bin(dec),"in binary\n",oct(dec),"in octal\n",hex(dec),"in hexadecimal")
"""

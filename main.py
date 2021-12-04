#2D lists
#drinks = ["coffee","soda","tea","water"]
#dinner = ["Ugali","Pizza","hotdog"]
#dessert = ["cake","Maandazi"]

#food = [drinks,dinner,dessert]
#print(food[0][3])


#TUPPLE
#student = (22,"Ali","J0seph","J0seph")
#print(student.count("J0seph"))
#print(student.index("J0seph"))

#for k in student:
   # print(k)
#if "Ali" in student:
   # print('Here it is!')

#SETS
#utensils = {"plate","knife",
#            "spoon","bowl"}
#names = {"john","jose","ali","iguna","wanja","spoon"}
#utensils.add("cup")
#utensils.remove("spoon")
#utensils.clear()
#names.update(utensils)
#dinner_time = names.union(utensils)
#for m in dinner_time:
    #print(m)
#print(utensils.difference(names))
#print(utensils.intersection(names))

#dictionaries
#grades = {"john":"A","joseph":"B","Ali":"C",
 #         "Ann":"D","Wanja":"E"}
#grades.update({'jared':'X'})
#grades.update({'joseph':'W'})
#grades.pop('john')
#print(grades["joseph"])
#print(grades.items())
#print(grades.get('joseph'))
#for i in grades.items():
#    print(i)

#index operator
#name = 'jose ali'
#if(name[0].islower()):
   # name =name.capitalize()
   # print(name)
#first_name = name[:5].upper()
#last_name = name[-3:]
#last_letter = name[-1]
#print(last_name)
#print(last_letter)

#fuction
#def hello():
    #print('ali is also joseph if you don"t know')
#hello()
#def hello(fname,lname,times):
    #print('helloooooooo'+" "+lname+' '+fname)
    #print('you have learned '+str(times) +'times!!!\nwow')
#my_name = 'ali'
#hello('Joseph','Ali',12)

#return statement
#def math(num1,num2):
    #result = num1 + num2
    #return result
#y = math(6,4)
#print(y)

#keyword arguments
#def fullname(first,middle,last):
 #   print('Hello '+first+' '+middle+' '+last)
#fullname('joseph','indieka','ali')
#def fullname(first,middle,last):
 #   print('Hello '+first+' '+middle+' '+last)
#fullname(last='ali',middle='indieka',first='joseph')

#nested function call
#num = input('enter a positive number: ')
#num = float(num)
#num = abs(num)
#num = round(num)
#print(num)
#0115505691(moureen)
#print(round(abs(float(input('enter a positive number: ')))))

#scope
#name = 'joseph'
#def display():
#    name = 'jj'
#    print(name)
#display()
#print(name)

#*args
#def add(*jj):
   # sum = 0
  #  for i in jj:
 #       sum += i
#    return sum
#print(add(1,4,6,7,3))
#def add(*jj):
#    sum = 0
#    jj = list(jj)
#    jj[1] = 21
#    for i in jj:
#        sum += i
#    return sum
#print(add(1,4,6,7,3))

#**kwargs
#def hello(**jj):
#    print('Hello',end=' ')
#    for key,value in jj.items():
#        print(value,end=' ')
#hello(title='Mr',fname='joseph',lname='ali')

#str.format()
#animal = 'cow'
#grass = 'nepier'
#print('The {} ate the {}.'.format(animal,grass))
#print('The {1} ate the {0}.'.format(grass,animal))
#print('my name is {name} also {lname}.'.format(name='joseph',
#                                               lname= 'ali'))
#text = 'i brought {} and the {} the same day'
#print(text.format(animal,grass))
#num = 3.34565
#number = 745343
#print('The number is {:.2f}'.format(num))
#print('The number is {:,}'.format(number))
#print('The number is {:b}'.format(number))
#print('The number is {:o}'.format(number))
#print('The number is {:x}'.format(number))
#print('The number is {:E}'.format(number))

#random pseudo
#import random
#x = random.randint(000,999)
#y = random.random()
#myname = ['john','jael','asus','mark']
#w = random.choice(myname)
#cards = [1,2,3,4,5,6,7,8,9,'J','Q','K','A']
#random.shuffle(cards)
#print(x)

#exception
#try:
#    numerator = int(input('Enter a number to divide '))
#    denominator = int(input('Enter a number to divide by '))
#    result = numerator/denominator
#except ZeroDivisionError as e:
#    print(e)
#    print('You cannot divide by zero')
#except ValueError as e:
#    print(e)
#    print('Enter only numbers please')
#except Exception as e:
#    print(e)
#    print('something went wrong')
#else:
#    print('{:.4f}'.format(result))
#finally:
#    print('this will always execute')

#file detection
#import os
#path = 'C:\\Users\\user\\Desktop\\pyth.txt'
#if os.path.exists(path):
#    print('it exists')
#    if os.path.isfile(path):
#        print('That is a file')
#else:
    #print('there is nothing')

# reading a file using python
#with open('C:\\Users\\user\\Desktop\\pyth.txt') as file:
#    print(file.read())

#moving files
#import os
#source = "file.txt"
#destination = "C:\\Users\\user\\Desktop\file.txt"
#try:
#   if os.path.exists(destination):
#        print('DONE!!')
#    else:
#        os.replace(source,destination)
#        print(source+' was moved')
#except FileNotFoundError:
#    print(source+' was not fount')

#delete files using python
#import os
#os.remove('trial.py')
#os.rmdir(path)  deletes an empty folder
#shutil.rmtree(path) deletes directory containing path
#print('was deleted')

#modules in python
#import message as msg
#msg.hello()
#msg.bye()
#help('modules')

#classes in python
#from car import Car
#car1 = Car("Chevy","Corvette",2021,"blue")
#car2 = Car("Ford","Mustang",2024,"Red")
#Car.wheels = 5 #changes the default in the class
#car2.wheels = 3 #changes only the specified item like car2
#print(car2.make)
#print(car1.model)
#print(car2.wheels)
#print(car1.color)
#car2.drive()
#car1.stop()

#inherritance in python
#class Animal:
#    alive = True
#    def eat(self):
#        print("The animal is eating")
#    def sleep(self):
#        print("The animal is sleeping")
#class Rabbit(Animal):
#    def run(self):
#        print("This rabbit is running")
#class Fish(Animal):
#    def swim(self):
#        print("The fish is swimming")
#class Hawk(Animal):
#    def fly(self):
#        print("The hawk is flying")
#rabbit = Rabbit()
#fish = Fish()
#hawk = Hawk()
#print(rabbit.alive)
#fish.eat()
#hawk.sleep()
#rabbit.run()
#fish.swim()
#hawk.fly()

#Multi level inherritance
#class Organism:
#    alive =True
#class Animal(Organism):
#    def eat(self):
#        print("This animal is eating")
#class Dog(Animal):
#    def eat(self): #to just specialize to one class
#        print("The dog is eating the meat")
#    def bark(self):
#        print("The dog is barking")
#dog = Dog()
#print(dog.alive)
#dog.eat()
#dog.bark()

#method chaining in python
#import time
#class Car:
#    def turn_on(self):
#        print("The engine has started")
#        return self
#    def drive(self):
#        print("The car is driving")
#        return self
#    def brake(self):
#        print("The car has stopped")
#        return self
#    def turn_off(self):
#        print("The engine has turned off")
#        return self
#car = Car()
#car.turn_on().drive()
#time.sleep(1)
#car.brake().turn_off()

#discusson
name = "joseph"
#print("my name is "+ name)
first_name = "Python-coder"
#print(first_name)
age = 20
#print("Your name is " +name+" also known as  "+first_name+" and you are "+str(age)+"old")
a = "john"
A = "Doh"
#print(a +A)
#number = float(input("Enter the number"))
#print(number)
its_raining = True
#print(its_raining)
#print(type(its_raining))
#Name = input("Enter your name: ")
#print(Name)

#num1 = int(input("Enter the first number: "))
#num2 = int(input("Enter the second number: "))
#sum = num1 / num2
#print("{:.2f}".format(sum))
#print("Hello world")
#from datetime import datetime
#a = datetime(2021,10,6,1,0,0)
#b = datetime(2016,10,1,23,5,59)
#print((a-b).total_seconds())
from enum import Enum
class Color(Enum):
    red = 1
    green = 2
    blue = 3
#for c in Color:
#    print(c)
#print(Color(2))
#a = 10
#b = 2
#print(a**b)

num=[1,65,78,23,56,7,5]
for i in range(len(num)):
    for n in range(i+1, len(num)):
        if num[i]>num[n]:
            k = num[i]
            num[i]=num[n]
            num[n]=k
#print(num)
#i = 0
#while i < 7:
#    print(i)
#    if i == 4:
#        print("Breaking from loop")
#        break   # will stop @ i==4 it won't continue to 7
#    i += 1
#for i in (0, 1, 2, 3, 4, 5):
#    if i == 2 or i == 4:
#        continue   #will skip 2 and 4
#    print(i)
#while True:
#    for i in range(1,5):
#        if i == 2:
#            break
    #print(i)


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
import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('purple')
t.speed(10)
col = ['yellow','blue','white','green','violet','yellow']
c=0
for i in range(70):
    t.forward(i*10)
    t.right(144)
    t.color(col[c])
    if c==5:
        c=0
    else:
        c+=1

 # This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#import filecmp
import unittest
import logging
import time
import keyword

# import driver as driver
# from selenium.webdriver import DesiredCapabilities
# from turtledemo.chaos import g
# from selenium.webdriver.chrome import webdriver
# import openpyxl
from selenium.webdriver.chrome.options import Options



#def print_hi(name):#Use a breakpoint in the code line below to debug your sscript.

#print(f'Hi,{name}')  #Press Ctrl+F8 to toggle the breakpoint
# Press the green button in the gutter to run the script.

#if __name__ == '__main__':
    #print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#comment


print(10+30)
print(keyword.kwlist) # print keywrod from 3.x python version


# variables -------------//-----------------

a=10
b=90
f=9.7 #float ()Dynamicaly values do not need to spcify data type int float etc..

# String

name="test"  # double cote
name1='test-one' #sinlge coute
print(name)
print(name1)
print(a)

# chaining variable with multiple values
a,b1,c,name=100,30.5,45,"test string" # diferent value from all the variables

print(a,b1,c,name)

#  2 ways to assign al the values to the variable
a,b2,c=10,10,10

#a,b,c=10
print(a,b2,c)

#assign y value to x and x value to y ----/------
x=1
y=2

y,x=x,y

# data types (Numbers, String, List, Tupe, Dictionary, Boolean)

x1=100 #int
y=10.4  #float
s="test" # String
b=True #boolean type'

# To know the data type of variable
print(type(x1)) # return what type of data type
print(type(y))
print(type(s))
print(type(b))

# Concatenation
print(10+10)
print(10+10.5)
print("welcome"+"python")
print(True+5)
print(10+False)
print(True+True) # true =1; false =0
#print(10+ "Welcome")
#print(True+"Welcome") # type error - invalid statement


#Agenda - Swappping - re-decalration - Delete Variable
x=10;
y=20;
print("Before swapping values are:",x,y)
x,y=y,x
print("After swapping values are:",x,y)

#re-declaration of variable - we can re-declare a variable multiple times
a=10;
print(a)

a=100;
print(a)

#Delete variables  (del) kewyword
a=10;
print(a)
del a # delete the variable - will give name error

# How to take input from the user 2.x  input function = take any type of data
# raw_input function = take only string type data
# python 3.x - input functions takes only String Data

num1=input("Enter first num") # treated all the input as string  format and concatinate the two values
num2=input("Enter second num")
print(num1+num2)

#type cast to convertinto interger format
num1=int(input("Enter first num")) # treated all the input as string  format and concatinate the two values
num2=int(input("Enter second num"))
print(num1+num2)

#type cast to convertinto interger format
num1=(input("Enter first num")) # treated all the input as string  format and concatinate the two values
num2=(input("Enter second num"))
print(int(num1)+int(num2)) # type cast into interger format and concatinate


#type cast to convertinto interger to float  format - Value error
num1=(input("Enter first num")) # treated all the input as string  format and concatinate the two values
num2=(input("Enter second num"))
print(int(num1)+float(num2)) # type cast into interger format and concatinate


#Float can hold interger but interger can not hold float
num1=(input("Enter first num")) #10.5
num2=(input("Enter second num")) #10
print(int(num1)+float(num2)) # float can hold interger


#Formatin the output data with the % & {}
#%d int
#%s String
#%f or %g float

# print the value in the console
name="test"
age=25;
sal=100;

print(name,age,sal)
print("Name is:", name)
print("Age is: ", age)
print("Salary is:", sal)
# printing using operators %d %s &f
print("Name is: %s Age: %d sal: %f"%(name,age,sal))

print("Name:{} Age:{} Salary:{}.".format(name,age,sal))

# base on the index
print("Name:{0} Age:{1} Salary:{2}.".format(name,age,sal))

print("Name:{0} Age:{0} Salary:{0}.".format(name,age,sal))# print test test test base on index 0

# Flow control statemets - conditional, Iterative, transfer

# Conditional ifelse elseif

#Example 1
a=10;
if a>20:
  print("True Condition")
else:
    print("False Condition")

# if true
a=10;
if True:
  print("True Condition")
else:
    print("False Condition")

# If False
a=10;
if False:
    print("True Condition")
else:
    print("False Condition")

# Even odd number (% reminder)
a=10;
if a%2==0:
    print("Number is Even ")
else:
    print("Number is Odd")

# Write multiple statements udern if else blocsk

if True:
    print("Statement1")
    print("Statement2")
    print("Statement3")
else:
    print("Statement4")
    print("Statement5")

print("This is not part of the if else block")


# Write multiple statements in a single line
print ("Welcome") if True else print("Pyhton")
print ("Welcome") if False else print("Pyhton")

print ("Welcome") if 10<20 else print("Pyhton") #Welcome
print ("Welcome") if 10>20 else print("Pyhton") #Python

# add ()
(print("Welcome"), print("Welcome2")) if True else (print("Pyhton1"),print("Python2"))
(print("Welcome"), print("Welcome2")) if False else (print("Pyhton1"),print("Python2"))


#elif condition
a=10;
if a==10:
    print("Ten")
elif a==20:
    print("twenty")
elif a==30:
    print("Thirty")
else:
    print("Not Listed")

# Interactive loops for loop =range() function
print(list(1))#[0,1,2,3,4,5,6,7,8,9]
print(list(5,10))#[5,6,7,8,9]


print(list(1,10,2))#[1,3,5,7,9] Odd numbers
print(list(0,10,2))#[0,2,4,6,8] even numbers


print(list(10,1,-1))#[10,9,8,7,6,5,4,3,2,] decrement

print(list(-10,-5))#[-10,-9-8-6] Negative
print(list(-10,-5,2))#[-10,-8,-6] Negative Decrement by 2


# Range()
for i in range(10): #by default statig value is 0
    print(i)

#print Odd number
print(list(1,10,2))#[1,3,5,7,9] Odd numbers
for i in range(1,10,2):
    print(i)

print(list(0,10,2))#[0,2,4,6,8] even numbers
# print even numbers
for i in range(2,10,2): # default value is 2
     print(i) #2,4,6,8


print(list(10,1,-1))#[10,9,8,7,6,5,4,3,2,] decrement
for i in range(10,1,-1):
    print(i)


print(list(-10,-5))#[-10,-9-8-6] Negative
for i in range(-10,-5):
    print(i)


print(list,(-10,-5,2))#[-10,-8,-6] Negative Decrement by 2
for i in range(10,-5,2):
    print(i)


#While loop  = use when you dont know the end value - while loop repeat till the condition become false
#print 1...9 numbers
i=1 # initial
while i<10: # condition
    print(i) # print
    i=i+1 # increment

#print 10...1 number in decending order
i=10
while i>=1:
    print(i)
    i=i+1


#Decerement value
i=10
while i<=1:
    print(i) #10,9,8,7,6,5,4,3,2,1
    i=i+1


# Jump Transfer  Statements break and continuing
for i in range(1,10):
    if i==5:
        break
    print(i)#1,2,3,4

#continuing
for i in range(1,20):
    if i==5:
        continue
    print(i)# 1,2,3,4,6,7,8,9, will jump the number 5 because of the continue


#Numbers Types Conversion Built in Function

x=10
print(float(x)) # to convert into float

x=10.5
print(int(x)) # to covnert to interger

# to findout the dat type
print(type(x))
print(type(int(x)))
print(type(float(x)))


# Built in Functions max() min()

print("Max of 80,100,100:" ,max(80,100,100)) #80,100,1000:1000
print("Max of -10,10,5:" ,max(-10,10,5))#-10,10,5:10
print("Min of 80,100,100:" ,min(80,100,100))#80,100,1000:80
print("Min of -10,10,5:" ,min(80,100,100))#-10,10,5:-10

large=max(10,20,30,40,50)
print(large)#50

smaler=min(10,20,40,50)
print(smaler)#10

# Strings collection of charaters
# String are immutable can not be modfied once is created
# Every Object in python is store in memory and we can use id to get the memory address
name="test"
name='test'
print(name)

name1=str("welcome")

str="welcome"
str2="Welcome2"

print(id(str))#57439322
print(id(str2))#5739232

print(id(str),id(str2))#57660416 57660416 memory location

str2=str2+"to python"
print(id(str1),id(str2))  #57660416 59955200 memory location

#Operation on Strings String Index start from 0  and + to concatinate and * repetitino operator for string

str="Welcome"
print(str+"to python")
print(str*3)#welcome welcome welcome

#Slicin String - subset string from orginal string by usinf []  slicin operato systax s[start:end] will return part of the string

str="Welcome"
print(str[1:3])#el
print(str[:6])#welcome
print(str[4:])#ome
print(str[1:-1])#elcome


#ord()  ASCII code and arch() return character represeted by ASCII number

print(ord(A))#65
print(chr(65))#A

#String Functions len() return length max() return high ASCII value min() return lowest ASCII value

print(len("hello"))#5
print(max("abc"))#c
print(min("bc"))#a

#in and not in operator to check exiostency of operators

str3= "welcome"
print("come" in str3)# true
print("come" not in str3) # false

print("wel" in str3)# true
print("xayx" in str3)# false

print("wel" not in str3)# false
print("xayx" not in str3)# true

# String comparison (>< <= >= == !=) tp compare two string lexicographically using ASCII values of characters

print("tim" == "tie")# false
print("free" !="freedom")#true
print("arrow" > "aron")#true
print("teeth" >= "tee")#True
print("yellow" <= "fellow")#false
print("abc">"")#true

# Iterating String using loop

str4="hello"
for i in str4:
    print(str4)
    print(str4,end="\n") # default behavior
    print(str4 ,end="")# print string without a new line
    print(str4 ,end="foo")# now print() will print foo after every string


s="Python"
for i in s:
    print(s)# print python 6 times becasue has 6 characters

s="Pyhton"
for i in s:
    print(i)# print each character P Y T h t o n


#Testing Strings isalnum() isalpha() isdigi5() isidentifier() is lower() issupper() isspace()

s1="welcome to python"
print(s1.isalnum()) # true if string is alphanumeric
print(s1.isalpha() +"welcome") # true is String contains onluy lphabet
print(s1.isdigit() + "2012") # true if string contains only digits
print(s1.isidentifier()+"first Number") # true if string has valid identifier
print(s1.islower()) # true if string is in lowecase
print(s1.isupper()+ "Welcome") #true if string in upercase
print(s1.isspace()+"") # true if string conatains only whitespace


# Searching SubString

str5=" welcome to python"

print(str5.endswith("thon"))#true
print(str5.startswith("good"))#false
print(str5.find("come"))#3
print(str5.find("become"))#-1
print(str.rfind("o"))#15
print(str.count("o"))#3

# converting fuctions video 12


# list  add delete very similar like  array value
list1= list()# create empty list
list2=list([22,32,12]) # create a list with element 22,32,12,
list2 = list(["tom","jeety"])# creat list with String
list3=list("pyhton")#create a list with characters p,y,t,h,o,n


#Accessing elements in list you can use index operator[]
listnum = [10,20,30,40]
print(listnum[1])#access second element in the list
print(listnum[0])#access first element in the list


print(2 in listnum) #true
print(2 not in listnum) #false
print(len(listnum))#4
print(min(listnum))#1
print(max(linstnum))#4
print(sum(listnum))#1200

#list slicing [start:end]
list4 =[11,12,22,33,44,55]
print(list4[0:5]) # will return list start from index 0
print(list4[:3])#0
print(list4[2:])# end of index set to last index

# + opertor joint two list  * operator replicates the element in the list

list5 = [11,33]
list6 =[1,9]
list7 = list5+list6
ptint(list7) # [11,33,1,9]

list9=[1,2,3,4]
list10=list4*3
print(list10)#1234,1234,1234,1234 replicates the element in the list

#in  in list not in operator determine wheaterh the eleme exist or not

list11=[11,22,33,44,55,77,88]
print(22 in list11) # true
print(22 not in list11) # false

list11 = [1,2,3,4,5,6,7]
for i in list11:
      print(i)
      print(i,end="")#1,2,3,4,6,7



# commonly used list methods with return type append(object) count(object) extend(object) index(object) insert(indes)
# remove(object) reverse(none) sort(none) pop(object)


list12=[2,3,4,5,65,66,77]
list12.append(4)
print(list12)

print(list12.count(4))#
list13=[99,77]

list12.extend(list13)
print(list12) # value will be add to the list

print([list12.index(4)])

list12.insert(2,3)
print(list12)


#list12.pop(2)# return the value end remove from the list
print(list12.pop(2))

list12.removed(2)
print(list12)

list12.reverse(5) # reversed
print(list12)

list12.sort() # sort order
print(list12)


# File habndler

f=open("filepath C:\demo\src\file.txt")
print(file.read())# read the file content
print(file.read(10))# read the numbers of characte from the file
file.close

f=open("filepath C:\demo\src\file.txt")
print(file.readlines ())# read the file content in array format
print(file.read(10))# read the numbers of characte from the file
file.close

f=open("filepath C:\demo\src\file.txt")
print(file.readline ())# readline without (S) read  only the first line from the file
print(file.read(10))# read the numbers of characte from the file
file.close


# loop statement to read all the data from the file
f=open("filepath C:\demo\src\file.txt")
for i in file:
    print(f)
    file.close()


# class collection varibbles and methods  object is physical oentity wich is create for a class class is blue print of object.
class Demo:
    def function(self):
        pass
    def fucntiontest(self):
         print("Name is:",name1)

# Fucntion in the class called method and function outside of class called pure function.

class DemoUsed:
    def function(self): # seld represet this function belogs to this class
        pass
    def fucntiontest(self, parameter):
         print("Parameter Name is:",parameter)

# create object
obj=DemoUsed()
obj.function()
obj.fucntiontest("parameter Test") # calling a function

#Instance method & static method
class Instance:
    def m1(self): # instance method
        print("INstance meethod")

    @staticmethod
    def m2(): #static method do not specify any self keywords
        print("Static method")


mc=Instance()
mc.m1()# instance method
Instance.m2()# static method

#in a static function self keyword is passing as argument parameter
class Instance:
    def m1(self): # instance method
        print("INstance meethod")

    @staticmethod
    def m2(self): #static method do not specify any self keywords when do is called as parameter argument
        print("Static method")
Instance.m2(10)# static method calling a self as parameter need to pass argument

# Declaring class variable by and accesing by using self keyword
class selfvariable:
 a,b = 100,200

 def add(self):
     print(self.a + self.b)# accessing the class variable by using self keyword
 def mult(self):
     print(self.a * self.b)# mutipledef mult(self):
 def divide(self):
     print(self.a / self.b)# divide
 def reminder(self):
     print(self.a % self.b)# reminder
 def subtraction(self):
     print(self.a - self.b)#minus

obj=selfvariable() #calling the methods
obj.add()
obj.mult()
obj.divide()

# global class and local variables

x=20; #globla variables
class GlobalVariable:
 a=10 #class varaibles
 b=40

 def localvaraiable(self,h,j): # local varibales
     print(h+j)#local variables #300
     print(self.a+self.b)# accessng class variable
     print(x)# global varibale

obj=GlobalVariable()
obj.localvaraiable(100+200) # acccesing local variable with 2 parameters h,j

# global variables and local varibles are the same

d,t=10,20 # global
class Globalocaldesame:

    d,t=10,20 # class varaible
def addGlobal_Local_Same_Name(self,d,t): #local variable
    print(d+t) # access loval variables
    print(self.d + self.t)# access class variables
    print(globals()['d']+ globals()['t'])#access the same name d,t global variable

obj=Globalocaldesame
obj.addGlobal_Local_Same_Name(200,400)

#creating object they will have diferent memory location
class objectmemorylocation:
  def Displayed(self):
      print("allocate diferement memory location")

obj1=objectmemorylocation
obj1.Displayed() #object  ocupied one memory location

obj2=objectmemorylocation
obj2.Displayed()# occupied different memory location


# name object & nameless object
class Nameless_object:
  def Displayed(self):
      print("Nameless objcet can called the method directly")

obj1=objectmemorylocation # Name objcet
obj1.Displayed()

objectmemorylocation.Displayed()#Nameless object can called the method directly.

#how to chekc memory location of object

class Check_object_memory_location:
  def Displayed_Check_objMemory_location(self):
      print("Check memory location")

obj1=Displayed_Check_objMemory_location()
obj2.Displayed_Check_objMemory_location() #object  ocupied one memory location
obj3=obj1

print(id(obj1)) #6253666
print(id(obj2)) #6235876
print(id(obj3)) #6253666 obj1 and obj3 will point to the same location

#verify if the are point to the same locatino
print(objs1 is obj2)# false
print(obj2 is obj3)#true
print(obj2 is not obj2)#true
print(obj1 is not obj3)#false


# Opps - Inheritance

# Single Inheritance one parent for one child
class A:
    def  m1(self):
        print("thie is parent class A")

class B(A):# class B inheritate class A

 def m2(self):
     print("this is chi cldlass B")

obj=A()# create boject
obj.m1()# calling the mthod m1

obj=B()
obj.m1()# class A
obj.m2()#Class B


obj.m2()#300

#Multlevel Inheritance
class MultA():
    iA,jA=20,30
    def m1(self):
        print(self.iA+self.jA)
class MultB(MultA):
    iB,jB=40,50
    def m2(self):
        print(self.iB+self.jB)
class MultC(MultA):
    iC,jC=60,70
    def m3(self):
        print(self.iC+self.jC)


MultA=MultA()
MultA.m1()
MultB=MultB()
MultB.m2()
MultB.m1()



#Hierrachical Inherintance # one perent from multiple child classes
class A1:
    x,y=10
    def m1(self):
        print(self.x + self.y)

class B1(A1):
    a,b=100,200
    def m2(self):
        print(self.a +self.b)


class C1(A1):
  i1,j1=100,300
  def m3(self):
      print(self.i1 + self.j1)

a=A()# create class instance
a.m1()# from class A

b=B() #creat class instance
b.m1()# from class A
b.m1()# from class B

c=c()# create class instance
c.m1()# from class A
c.m2()# from class B
c.m3()# from class C


#multiple Inherintance
class clA1:
 h,n=2,3
def m1(self):
 print(self.h + self.n)



 class clB1:
       a, b = 100, 200
       def m2(self):
           print(self.a + self.b)



class clC1(clA1,clB1): # Multiple Inherintance one child class  can habe multiple parent
    i1, j1 = 100, 300
    def m3(self):
        print(self.i1 + self.j1)

clC1=clC1()# create class instance
clC1.m1()# from class A
clC1.m2()# from class B
clC1.m3() # from class c


#Hybrid Inherintance (Hierachical and multiple)
class HibridA():
       g=10
       def H1(self):
        print(self.g)

class HibridB():
        gb=20
        def m2(self):
            print(self.gb)
class HibridC():
         gc=30
         def m3(self):
             print(self.gc)


#Polymorphism Object can com in manh type of form and we access using the same method
# One object behave in multiple ways
# achiving by method overriding and  method overloading


#Overriding Method

class Bank:
    def rateofinterested(self):# the same method perfrom one job return 0
        return 0
class ICICI_Bank:
    def rateofinterested(self):# the same method perform diferent job return 10.5
        return 10.5

objBank=Bank()
objBank.rateofinterested()

objICICI_Bank=ICICI_Bank()
print(objICICI_Bank.rateofinterested())# overrriden bank method


#Method overloading = the same method name with diferent parameters

class Human:
      def sayhello(self,name=None):# Overloading the same method with different behaviour (Polymorphism)
          if name is not None:
              print("Hello" + name)
          else:
              print("Hello")

obj=Human()
obj.sayhello()# not pass parameter says hello only
obj.sayhello("Ulisses")# if pass parameter will say Hello Ulisses

#one more example
class car:
    def run(self,run=None):
        if run=="100 Kilometer":
            print("you got speed ticket")
            if run=="80 Kilometers":
                print("you need to reduce speed")
                if run is None:
                    print("you need star the car")

obj=car()
obj.run()
obj.run("100 Kilometers")
obj.run("80 Kilometers")

#one more example

class overloading:
    def overloading_m1(self, int):# the same name the same parameter int diferent return (polymorphism)
        return 10
    def overloading_m1(self, int):# the same name the same parameter int diferent return (Polymorphism)
        return 20

obj=overloading()
obj.overloading_m1()

class overrriden:
    def overrriden_m1(self,int): #The same method name different parameters int float diferent return (Polymorphism)
        return 10
    def overrriden_m1(self, float):
        return 15.5

obj=overrriden()
obj.overrriden_m1()


# Encapsulation is when you restric the access to the methods and variables by using private variables and methods
#preveting the data to be modify

class myEncapsulation:
    __a=100 #private vairable
    def dispalyed(self):
        print(self.__a) # private variable by usinf __ uderscore_undercore twice

obj=myEncapsulation()
obj.dispalyed()

# calling the method outside of the class
print(myEncapsulation.__a) # cannot be accessed outside of the class because is private



# private method
class myEncapsulation:

    def __dispalyedPrivate(self): # private method
        print("this is private method") # private variable by usinf __ uderscore_undercore twice
    def displayedNonePrivate(self):# None private method
        print("This is none private method")
        self.__dispalyedPrivate()
        self.displayedNonePrivate()


obj=myEncapsulation()# creating instance of the class to called the methods and variables outside of the class
obj.displayedNonePrivate()# allowed because is not private method and can be called outside of the class

# calling the method outside of the class
obj.__dispalyedPrivate() # cannot be accessed outside of the class because is private


#We can access private variabled outside of class indirectly using methods by using self keyowrd
#class variable can be acces by using self keyword

class indirectlyPrivaeAccess:
    __empid=110 # private method
    def getempId(self,eid): # none private method
        self.__empid=eid
    def displayedEmpID(self): # none privagte method
        print(self.__empid)

# we can access those variable outside of class by creating a object
obj=indirectlyPrivaeAccess()
obj.displayedEmpID()# now we can access __empid=110 variable because we calling the variable from the displayed method

#change the value indirect from outside of the class
obj.getempId(405)# we are passing the new value into the eid --> self --> __empid==110 private variable


#Abstraction the class the contain one or more abstract method
#they only have definition no body only the implementation
#they can not be instantiated and required subclasses to provide implementation for  the abstract methods
# we need to implement the abstract methods in the subclass
# we can only create object of abstract class in the subclass not in the abstract class

from abc import ABC,abstractmethod
class abstractA(ABC):# ABC is pre-define abstract class from the ABC module need to import (from ABD imprt ABC)
        def displayedAbstract(self):
            None # mo implementatin in the abstract method

# implemeting abstract method in the subclass

class sub_abstract(abstractA):
    def displayed_subclass(self):
        print("this is displayed method")#

#can not create object from abstract class only for the subclass (sub_abstract)
obj=sub_abstract()
obj.displayedAbstract()# will be called the method of the child class displayed_subclass() adn print message

#constructor in the abstract class
# subclass need to do the implemetation of all the
# abstract methods before creating object outside of the abstract class


from abc import ABC, abstractmethod

class xAbstract(ABC):
    @abstractmethod
    def m1(self):
        pass
    @abstractmethod
    def m2(self):
        pass

class ySubclass(xAbstract):

    def m1(self):#implemeting the abstract methods
        print("this is m1")

obj=ySubclass()
obj.m1()


class zSubclass(ySubclass):
    def m2(self):#implements the abstract methods
        print("this is M2 method")


obj=zSubclass()
obj.m2()#abstract method
obj.m1()# absrtract method


#constructor in abstract class
from abc import ABC,abstractmethod

class cal_abstract(ABC):
    def __init__(self, value):#constructor
        self.value=value# meake the local variable as class variable
    @abstractmethod
    def add(self):
        pass
    @abstractmethod
    def sub(self):
        pass

class implementAbstract(cal_abstract):

    def add(self):
        print(self.value+100)

    def sub(self):
        print(self.value-50)

obj=cal_abstract(200)# will be store in (__self.value=value) constructor pass to parameter def(self,value) as class varaible
obj.add()
obj.sub()


#Modules is a python file that contains functions that we can access from different module - like JAVA.util
# to access the module used import operation

#import operations
operations.add(56,78)
operations.sub(78,90)

#other approach
#from operations import add,sub
add(455,67)
sub(23,45)

# can create a object from the operation moduele
obj=add(67,90)
print(add(98,76))


# other apraoch
#from operations import *
add(45,32)# will print from operation module
sub(23,45) # will print from operations module

#from management import *
add()# Will print from management add()
sub()# will print from manange sub()

# specify the class inorder to call the fuction from different modules
#obj=operation.add()# calling the class and specific method
#print(obj=operations.sub(23,45))

obj=management.sub(45)
obj=management.add()

#creqting object of the module and calling the method
obj=operation.add()# module name dot class name
obj.add()

#hom many methods and functions are in the modulec

#import methodsu_module
print(dir(methodsu_module))# will displayd the class inside of the module not the methods

#import noclass_functions
print(dri(noclass_functions))# will print the function that is method not in a class in python


# args and kwargs allows to pass number variables as argument like it float in java

def sum(*args):
    s=0
    for i in args:
        s+=i #s=s+1 1,2,3,6
        print(sum)
sum(12,34,56,78)# accepst anu numbers of argument in multiple values

#list
def mu_three(a,b,c):
    print(a,b,c)
args=[1,2,3,]#list variable have to be the same as number of parameters
mu_three(*args)

#kwargs allowed to pass variable numbers of keyword func_name(name='tim',team='school') key value parin **

def three_param(a,b,c):
    print(a,b,c)
array={'a':"one",'b':"two",'c':"three"}# passing key values to the functons
three_param(**a)

# how to reviced the argument
def my_func(**kargs):# passing multiple keys and values
    for i,j in kargs.items():
        print(i,j)
        my_func(name='tom',sport='tennis', salary=100)# key value pair you can keep adding values

#lambda functions has no name is know lambada function can take any number of argument and only have one expressino
x= lambda a : a+10
print(x(5))#passing singel variable

x = lambda a,b :a*b
print(x(5,4))#passing multiple variables

x= lambda a,b,c : a+b+c
print(x(2,3,4))

# all exception is condisederate as error
#exception syntax error and logic error - event that disrupt the normal flow of the program""
#try except else finally
# a=50/0 - zerdivisoin error logic error
# s=none
#print(s.__len__())#  atteibute error

print("prgram starter")
print(10/0) # zero division error  las print will not displayed
print("program completer")

# applaaied exception
print("prgram starter")
try:
 print(10/0) # zero division error  las print will not displayed
except ZeroDivisionError:
 print("Entered to except block and handle exception")

print("program completer")

# different type of statement
# applaaied exception
print("prgram starter")
try:
 print(10/0) # zero division error  las print will not displayed
except TypeError:
 print("Entered to except block and handle exception")

#multiple except blocvks
# applaaied exception
print("prgram starter")
try:
 print(10/0) # zero division error  las print will not displayed
except typeError:
 print("Entered to  wrong except block and handle exception")

except ZeroDivisionError:
    print("Entered to right except block and handle exception")


#else and finally block

#multiple except blocvks
# applaaied exception
print("prgram starter")
try:
 print(10/0) # zero division error  las print will not displayed
except typeError:
 print("Entered to  wrong except block and handle exception")

except ZeroDivisionError:
    print("Entered to right except block and handle exception")

else:# if none of the except block is not executed else will be executed / else block do not handle any exception
    print("program is completed")

#case1 : Throw exception ---> except
#case2 : Not Throw exceptino ---> executed only if the statment not throw any exception

finally:
    print("Enter to finally block ")# finally will always be executed

#case1 : exeption occured  ---> except finally
#case2 : exception ocurred ---> not handle finally
#case3: Eception not occured except block will not execute ---> else block ---> finally will be execute


# Super keywords is to invoke parent class methods,variables and constructor

class superA:
    def m1(self):
        print("this is method from class A")

class superB(superA):
    def m2(self):
        print("thi is method from class B")
        super().m1()#calling the parent class method by using super keyword

obj=superB()
obj.m2()


#Example 2
class superC:
    a,b=10,20

class superD(superC):
    i,j=100,200
    def m1(self,x,y):
        print(x+y)#local variables
        print(self.i+self.j)# child class variables
        print(self.a+self.b)#parent class varaibles

obj=superD()
obj.m1(1,2)#3


#example 3
a,b=15,20 #global
class superE:
 a,b=10,20 # parenet local varialse

class superF(superE):
  a,b=100,200 #child locald variables

  def m1_superF(self, a, b):
      print(a + b)  # m1() local variable
      print(self.a + self.b)  # child class variable a,b=100,200
      print(super().a + super().b)  # # parent class variables a,b=10,20
      print(globals()['a'] + globals()['b'])  # globals variables
      pass


bobj=superF()
bobj.m1_superF(1,2)

#super to invoke parent class constructor

class constructorA:
     def __init__(self):
         print("Constructor from constrocutor A class  ")

class constrocutorB(constructorA):# child constructor will be invoke fisrt
    def __init__(self):
        print("constrocutro from B class ")
        super().__init__()# will  inovke the parent constocutorA
        constructorA.__init__()# will invoke the parent constructor

cobj=constrocutorB()


# local class variables example

class myclass:
    def values(self,val1,val2):
        print(val1) # local variables
        print(val2)
        self.val1=val1
        self.val2+val2 #convert into class variables
    def add(self):
        print(self.val1,self.val2)

mcobj=myclass
mcobj.values(10,20)
mcobj.add()

#invoke a costructor

class invoke_constructor:
      def __init__(self,val1, val2):
         print(val1)  # local variables
         print(val2)
         self.val1 = val1
         self.val2 + val2  # self.val2 point to calss /convert into class variables +val2 point to local

      def add(self):
          print(self.val1, self.val2)

#creating object and calling the methods
mcobj = myclass(20,34)# calling the constructor
mcobj.values(10, 20)# calling the local variables
mcobj.add()#calling the local variables

#calling method in a mehtod form the same class
class mycalssa:
    def m1(self):
        print("this is m1 method")
        self.m2(200)# coverting m2() into gloabl

    def m2(self,a):
     print("this is a method m2",a)

obj=mycalssa()
obj.m1()

#passing arguments into the constructor

class constructor_passArgument:
    name="test constructor name"
    def __init__(self,name):#passing parameter in the constructor
        print(name)# point to the local constructo variable
        print(self.name)# point to the class variable  name="test constructor name"

objc=constructor_passArgument("this is my name")#calling the costructor paremeter name



# Invoke constructo Example codec
class ConstructorEmp:
    def __init__(self,eid,ename,esal):
        self.eid=eid
        self.ename=ename
        self.esal=esal

    def dispalyed(self):
        print("EmpId:{} Empname{} EmpSal{}".format(self.eid, self.ename, self.esal))
        print("EmpId:% Empname:% EmpSal:%g" %(self.eid, self.ename, self.esal))

obje=ConstructorEmp(200,"smith",10000)
obje.dispalyed()

# __str__(self) will called the displayed function no need to create object
class ConstructorEmp:
    def __init__(self,eid,ename,esal):
        self.eid=eid
        self.ename=ename
        self.esal=esal

    def __str__(self):
        print("EmpId:{} Empname{} EmpSal{}".format(self.eid, self.ename, self.esal))
        print("EmpId:% Empname:% EmpSal:%g" %(self.eid, self.ename, self.esal))

obje=ConstructorEmp(200,"smith",10000)
#obje.dispalyed() no need to create
print(obje)

# destrroined object
# when you destoried the object del function automaticallyu executer

# __str__(self) will called the displayed function no need to create object
class ConstructorEmp:
    def __del__(self,eid,ename,esal):
        self.eid=eid
        self.ename=ename
        self.esal=esal

    def displayed(self):
        print("EmpId:{} Empname{} EmpSal{}".format(self.eid, self.ename, self.esal))
        print("EmpId:% Empname:% EmpSal:%g" %(self.eid, self.ename, self.esal))

obje=ConstructorEmp(200,"smith",10000)
obje1.displayed()

del obje1 # will destroyed the object

#--------------//-------------------//-------------------
#Selenium with python - pip install -U selenium to install - list to see the dowloads
#-------------//--------------------/---------------------
#from selenium import webdriver
#from selenium.webdriver.common.by import By
#import time
#time.sleep(3)
#import from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome(executable_path="")
driver.implicitly_wait(5)
driver.maximaze_window()
driver.get("url")

status =driver.find_element_by_id("id").is_selected()
print(status)

status=driver.find_element_by_id("").is_selected()
drp.select_by_value

# id expah CSS etc
driver.find_element(BY.XPATH,"//*[@id='name']").click()
driver.find_element(BY.ID,"//*[@id='name']").clear()
driver.find_element(BY.CSS,"//*[@id='name']").send_Keys("")
driver.find_element_by_id("id")


#explicit wait expected condition
wait=WebDriverWait(driver,10)

element = wait.until(EC.element_to_be_clickble(BY.XPATH("//*[@id='name']")))
element.click()

button = driver.wait.until(EC.presence_of_element_located((By.ID, "password")))
self.driver.execute_script("document.getElementById('password').value='trellologin2021@1234$'")

my_string = "trellologin2021@1234$";
elem = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "password")))
self.driver.execute_script("document.getElementById('manage_description').click()")
self.driver.execute_script("arguments[0].setAttribute('value', '" + my_string + "')", elem);



#How to find how many inputboxes present in the page
inputboxes=driver.find_elements(nBy.CLASSE_NAME,name)
print(len(inputboxes))

# to get the status of the input boxes
status=driver.find_element_by_id("id").is_displayed() #true or false
print(status)

status=driver.find_element_by_id("id").is_enabled()#true or false
print(status)

# Radio Buton isSelected() or not
status=driver.find_element_by_id("id").is_selected() #true or false
print(status)# print the status of the radiobutton
driver.find_element_by_id("id").click()# click on the radion button


#checkBoxes
status=driver.find_element_by_id("checbbox_id").is_selected() #true or false
print(status)
driver.find_element_by_id("checbbox_id").click()# click on the checkbox

#dropDown
#from selenium.webdriver.support.ui import Select
drp=Select(driver.find_element_by_id("dropDown_id"))# creat object of select class and pass driver

element=driver.find_element_by_id("dropDown_id")
drp=Select(element)

drp.select_by_value("value")
drp.select_by_Visible_text("text")
drp.select_BY_index(2)

#count len() the drop down and select by value
drp.driver.find_element_by_id("dropDown_id")
print(len(drp.options))# print how manu options are avaliable in the dropdown

all_options=drp.options # store all the option int he variable
for option in all_options:
    print(option.text)
print("Number of links in the page",len(links))

#read each link
for link in links: # loop into the liks element and store in the link variable
    print(link.text)# extract the tezt from the webElement
    #click on the link
    driver.find_element(BY.LINK_TEXT,"register").click()
    driver.find_element(BY.PARTIAL_LINK_TEXT, "reg").click()


#working with alert pop up driver.switch_to_alert()
driver.find_element(BY.PARTIAL_LINK_TEXT,"register").click()# click on the alert widow
time.sleep(5)
driver.switch_to_alert().accept()# close alert windon byusing ok button
driver.switch_to_alert().dismiss()#close alert bu suing cancel button


#Working with Frames switch_to.frame(name or id)
driver.swith_to.frame("id or name")
driver.find_element_by_id("idname").click
driver.swith_to.default_content()# switchback to default frame


# working with windowns current_windon_handle
print(driver.curren_window_handel())#parent windon #CDwindon(*&(*&(9879797###

driver.window_handles()# return all the handles valus of opened browser windons
for handle in handles: # loop throun the values
    driver.swith_to.window(handle)
    print(driver.title)

    #to close specific browser
    if driver.title=="framewindono":
        driver.close()#close only parent windon

    #close all browser
    driver.quit()# close all teh browser windonw
    driver.close()# close the current browser windons

    # #fluent wait
    # wait = WebDriverWait(driver, 20, poll_frequency=3, ignored_execptions=[ElementClickInterceptedException])
    # self.element = wait.until(EC.element_to_be_clickable(By.XPATH("password"))).send_keys(trello_password)
    #
    #     element = self.driver.find_element_by_xpath(self.textbox_password_id)
    #     self.wait = WebDriverWait(driver, 10)
    #     for self.elemenets in element:
    #         self.wait.until(EC.visibility_of(elemenets))
    #         self.wait.until(EC.element_to_be_clickable(elemenets))
    #         #self.element.send_keys(trello_passwor
#-----------------//-------------- Press Enter Key -----
# elem = driver.find_element_by_id("quick-search-query")
#         elem.send_keys("remote")
#         elem.send_keys(Keys.ARROW_DOWN)
#         elem.send_keys(Keys.Return)
#
#         first_option = WebDriverWait(driver, 150).until(
#         EC.visibility_of_element_located((By.XPATH, "//*[@id='password']")))
#         first_option.send_keys("trellologin2021@gmail.com")

#working with web_tables, tr = roles, td = collum, tbody = header
#count the tr
# driver.find_element_by_id("table/tbdoy/tr")# find all the element that match with multiple trs
# rows=len(driver.find_element_by_id("table/tbdoy/tr"))# will count how many element tr are there and store in a variable rows

# count the th
#driver.find_element_by_id("table/tbdoy/th")# find all the element that match with multiple trs
#cols=len(driver.find_element_by_id("table/tbdoy/tr[1]/th"))# th=will count how many element th colluns are there and store in a variable rows

# print rows and colums
# print(rows)
# print(cols)

#looping  and priting all the values in the table
# print("head1"+"  "+"heaf2"+"  "+"head3")#print haders of the table
# for row in range(2,rows+1):# get second role
#     for col in ranage(1,cols+1):#get first colum
#         c.text # str to convert to string
#         print(value,end=' ')
#         print()

#scrool down the pages

driver.execute_script("window.scrollBy(0,500)","")#scrool by pixel

self.driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)

# scrool by element found
#element=driver.find_element_by_id("teable/tbdoy/tr")#find the element
driver.execute_script("arguments[0].scrollntoView();",element)#scroll down till element  found

# scrool to the end of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")#Scroll to the end of the page


#mouse actiond drag and drop etc need to import --- #from selenium.webdriver import ActionsChains

# #element that need to be mouse over
# admin=driver.find_element_by_id("teable/tbdoy/tr")#mouse over to admin
# usermgt=driver.find_element_by_id("teable/tbdoy/tr")#mpuse over  to usermanagement
# user=driver.find_element_by_id("teable/tbdoy/tr")#mouse over than clik to user
#
# actions=ActionChains(driver)#create object of action chain class
# actions.move_to_element(admin).move_to_element(usermgt).move_to_element().click().perform()
#
# #Double click action
# element=driver.find_element_by_id("ttr")#find the element and store in a variable
# actions=ActionChains(driver)#create object of action chain class
# actions.double_click(element).perform() #double click action


# #Right click context_click
# element=driver.find_element_by_id("ttr")#find the element and store in a variable
# actions=ActionChains(driver)#create object of action chain class
# actions.context_click(element).perform() #double click action
#
#
#
# #drag and drop source element and target element drag and drop
# source_element=driver.find_element_by_id("ttr")#find the element and store in a variable
# target_element=driver.find_element_by_id("id")
#
# actions=ActionChains(driver)#create object of action chain class
# actions.drag_and_drop(source_element,target_element).perform() #double click action
#
#
# # Autocomplete
# driver.find_elements_by_id("email")/sendkeys("s")
# listElements = driver.find_elements_by_expath("//*[@id='form-login'']")
# for ele in listElements:
#     print(ele.text)
#     ele.click()
#     #------//or--break
#     if ele.text=="atlassina":
#         ele.click()
#         break

#autocomplet boostrap
# elementvalue = Element.get_attribute("innerHTML")
# print("value of element dropdown" + elementvalue)
# if elementvalue.find("JavaScript") != -1:
#         element.click()
#         exit()





#uploading documents
#driver.find_element_by_id("idname").sendKes("c://document_path.text or jpeg etc")

#dowloading document from the page
#driver.find_element_by_id("id").click()#kust click on the dowload link

#import chorOptions #-- from selenium.webdriver.chrome.options import Options

#chromeOptions=Options() #create oitons object
chromeOptions.add_experimental_option("prefs ",{"dowload.default_directory": "c:\dowloadedfiles"})# key value
#driver=webdriver.chrome(executable_path="c:\driver\chromedriver.exe",chrome_options=chromeOptions)
driver.get("url")

def get_browser():
    if "browser" not in g:
        options = webdriver.ChromeOptions()
        options.add_argument("no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=800,600")
        options.add_argument("--disable-dev-shm-usage")
        options.set_headless()

    #     g.browser = webdriver.Remote(
    #         command_executor=f"http://{host}:4444/wd/hub",
    #         desired_capabilities=DesiredCapabilities.CHROME,
    #         options=options,
    #     )
    # return g.browser



#read data from exel-xl--import openpy
path="c:\path.xlsx"
workbook=openpyxl.load_workbook(path)
sheet=workbook.active

rows=sheet.max_row
cols=sheet.max_colum
print(rows)
print(col)

for r in range(1,rows+1):
    for c in range(1,cols+1):
        print(sheet.cell(row=r,colum=c).value,end="   ")#end="  "  to give spaec

        #get out of the loop
        print()## to give space


#Write datat D exel file  --->#import openpyxl --.read from file
path="c:\path.xlsx"
workbook=openpyxl.load_workbook(path)
sheet=workbook.active

for r in range(1,6):
    for c in range(1,4):
        sheet.cell(row=r,colum=c).value="Welcome"
workbook.save(path)


#Data Driver Test DDT(functions  to be called in other classes) - need to import to other class
# class XLUtils():
# def getColumCOunt(file,sheetName):
#     workbook = openpyxl.load_workbook(file)
#     sheet = workbook.get_sheet_By_name(sheetName)
#     return (sheet.max_colum)
#
# def readData(file,sheetName,rownum,columnno):
#     workbook = openpyxl.load_workbook(file)
#     sheet = workbook.get_sheet_By_name(sheetName)
#     return sheet.cell(row=rownum,colum= columnno).value
#
# def writeData(file,sheetName,rownum,columnno,data):
#     workbook = openpyxl.load_workbook(file)
#     sheet = workbook.get_sheet_By_name(sheetName)
#     return sheet.cell(row=rownum, colum=columnno).value = data
#     workbook.save(file)

#
# #in the login page --> inport Xlutils in order to acess the methods
# #second file DataDrive test
# driver=webdrive.chrome(executable_path="c:\srivcer.exe")
# driver.getr(url_login)
# driver,maximize_window()
# path="c:\excelsheet.xlsx"
# rows=XLUtils.getRowCount(path,'shee1')
# for r in rage(2+rows+1):
#     username=XLUtils.reaData(path,"sheet1",r,1)#r =row 1=colum numne in the excel
#     password=XLUtils.readData(path,"sheet1",r,2) #2 = second colum in the excel
#
#     driver.find_element_by_id("id").sendKeys(username)
#     driver.find_element_by_id("id").sendKeys(password)
#
#
#     if driver.tittle=="page tittle":
#         print("test passed")
#         XLUtils.writeData(file,"sheet1",r,3,"testpassed ")#writer data into the excel = test passed
#     else:
#         print("testFailed ")
#         #XLUtils.writeData(file, "sheet1", r, 3, "testFaild ")#writer data into the excel = test failed
#
#      driver.find_element_by_link_test("Logo").click()#to go back to the home page and star the loop gain


#Cookies store data from user action  to re-meber the action
#captura all the cookies from teh browser

cookies=driver.get_cookies()
print(len(cookies)) # print all the cookies
print(cookies)#printall the cookies pair

#add cookies
#cookies={"name":"Mycookeis","value":"8927262626"}
driver.add_cookie(cookie)# add new cookies

cookies=driver.get_cookies()#
print(len(cookies))#print number of cookies to see the list update
print(cookies)

#delete cokkies
driver.delete_cookie("mycookies")
cookies=driver.get_cookies()
print(len(cookies))


#Take screen shoots files
driver=webdrive.chrome(executable_path="c:\srivcer.exe")
driver.getr(url_login)
driver,maximize_window()

driver.save_screenshot("c:\screenshoot\homePage.pnp") # accept all files
driver.save_screenshot_as_file("c:\screenshoot\homePage2.png")#accept only png

#auto complete
#log files level DEBUG INFO WARNING ERROR CRITICAL------>import logging



#tp send to a file istead of teh cosole
logging,basicConfig(filename="c://pathofthefile//test.log",
            format='%(asctime)s: %(levelname)s:  %(message)s',
            datefmt='%m/%d/%y %I:%M:%s %p',
            level=logging.DEBUG)
                    # got the file path past and change foward slah //
logging.debug("this is a log message")
logging.info("this is a log message")
logging.warning("this is a log message")
logging.error("this is a log message")
logging.critical("this is a log message")

#Unite Test framework to organizze yout code ---import unittest model

# import unittest
class Test(unittest.TestCase):
    def test_firstTest(self):
        print("this is the first Unittest Case")

if __name__=="__main":
    unitetest.main()# main method like in JAVA main(string[] args )

#using selenium webdriver
#import unittest
#from selenium import selenium

class searchengineTest(unittest.TestCase):
    def test_goole(self):#google chrome
        self.driver=webdriver.Chrome(executable_patch="c:\driverptaht.\chrome.exe")
        driver.get("url")
        print(self.driver.get.tittle+"title of the page")

    def test_binsearch(self):# bin swearch engine
        self.driver = webdriver.Chrome(executable_patch="c:\driverptaht.\chrome.exe")
        driver.get("url")
        print(self.driver.get.tittle + "title of the page")

if __name__=="__main":
    unitetest.main()# to run as unittest code


#Unitest keyword setup teardown setupClass teardownClass setupMOdule teardownModule

#import unittest

class AppTEstng(unittest.TestCase):

    @classmethod
    def setUp(self):# like Before class in testNG = execute multiple time in the method
        print("this is login test")

    @classmethod
    def tesrDown(self):# like After class in TestNG = execute mutile time in the method
        print("this is log out test ")


    def test_search(self):
        print(" This is search test")
    def test_advancesearch(self):
        print("this is advance search")

    def test_prepaidRecharge(self):
        print("this is prepaid charge")

    def test_postpaidcharge(self):
        print("This is post paidCharge test")

if __name__=="__main":# all the four method will be executed
    unitetest.main()


# # set up class = will execute in the class level
#     class AppTEstng(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):# like Before class in testNG = execute once the class started
#         print("Open application ")
#
#     @classmethod
#     def tesrDownClass(cls):# like After class in TestNG = execute once the class down
#         print("Close application  ")
#
#
#     def test_search(self):
#         print(" This is search test")
#     def test_advancesearch(self):
#         print("this is advance search")
#
#     def test_prepaidRecharge(self):
#         print("this is prepaid charge")
#
#     def test_postpaidcharge(self):
#         print("This is post paidCharge test")
#
# if __name__=="__main":# all the four method will be executed
#     unitetest.main()
#

#Set up MODULE tear DOWn MODULE --> noeed to be created outside of the class
# import unittest


    @classmethod
    def setUpModule(cls):# like Before class in testNG = execute once when MODULE start
        print("set Module ")

    @classmethod
    def tesrDownMModule(cls):# like After class in TestNG = execute oncewhe the MODUEL finished
        print("tear doiwn Module  ")


class AppTEstng(unittest.TestCase):
    def test_search(self):
        print(" This is search test")
    def test_advancesearch(self):
        print("this is advance search")

    def test_prepaidRecharge(self):
        print("this is prepaid charge")

    def test_postpaidcharge(self):
        print("This is post paidCharge test")

if __name__=="__main":# all the fou.r method will be executed
    unitetest.main()

##Skip Test methods skip test reason or base on --  @unittest.SkipTest

class AppTEstng(unittest.TestCase):

    @unittest.SkipTest
    def test_search(self):
        print(" This is search test")

    @unittest.skip("I am skipping this test with message ")
    def test_advancesearch(self):
        print("this is advance search")

    @unittest.skipIf(1==1,"condition one = to one ")
    def test_prepaidRecharge(self):
        print("this is prepaid charge")

    def test_postpaidcharge(self):
        print("This is post paidCharge test")

if __name__=="__main":# all the four method will be executed
    unitetest.main()


#ASSERTIONS - os a verification or check point asserEquls --assertNOtEquals

# class assertion(unittest.TestCase):
#
# #driver=webdrive.chrome(executable_path="c:\srivcer.exe")
# driver.getr("hhtps://www.google.com")
# title_of_Webpage=driver.title
#
# #assertion
# self.asserEquals("google",title_of_Webpage, "webpage title is not same")
#
# #assertNOtEqisl = negative condition
# self.asserNotE=quals("google",title_of_Webpage, "webpage title is not same ")# both not equsl return true test pass
#
#
# #asser true or false
# pageTitle=driver.title
# #assert false
# self.assertFalse(pageTitle == "google")
#
# #assert true
# self.asserTrue(pageTitle =="goole")


if __name__=="__main":# all the four method will be executed
    unitetest.main()


#NOT NONE ASSERTINOno
class notNone(unittest.TestCase):
    def test_notNone(self):
        driver=webdriver.Chrome(executable_path="c:\srivcer.exe")
        driver = None
        self.asserIsNone(driver)
        self.asserIsNotNone(driver)

driver.getr("hhtps://www.google.com")
title_of_Webpage=driver.title


#assetIN asset Not in
class noAssetNOtin(unittest.TestCase):
    def assert_notNone(self):
        list="pyhton","selinium","java"
        self.assertIn("ruby".list)#fail
        self.assertNotIn("python",list)#fail

#assert greateh or equal less lesseuqsl
class noAssetNgrea(unittest.TestCase):
    def assert_notNone(self):

        self.assertGreater(100,10)#fail
        self.assertGreaterEqual(100,10)#fail

        self.assertLess(100, 10)  # fail
        self.assertLessEqual(100, 10)  # fail


#### run tesst on desired browser
#pytest -s -v TC001_loginPage/test_login.py --browser chrome
#pytest -s -v TC001_loginPage/test_login.py --browser firefox

# Run test in paralled
#pytest -s -v  -n=3 TC001_loginPage/test_login.py --browser chrome
#pytest -s -v -n=4 TC001_loginPage/test_login.py --browser friefox



# trello api
import requests
import json

main_trello_endpoint = "https://api.trello.com/1/"
trello_key="2938402983409843089"
trello_token="987989879879787"
application_list_id="paodsia09-09asda09-0asd"

# #create card
# def create_trello_card(card_name, card_description):
#     create_trello_card_emd_point = main_trello_endpoint="cards"
#     jsonObj = {"key"}trello_key,"token":trello_token,"idlist":application_list_id,"name":card_name
#     "desc",card_description
#
#     new_card =request.post(create_trello_card_emd_point,json=jsonObj))

#     print(json.load(new_card.text ))
#
# #Trello API
#
# def get_browser():
#     if "browser" not in g:
#         options = webdriver.ChromeOptions()
#         options.add_argument("no-sandbox")
#         options.add_argument("--disable-gpu")
#         options.add_argument("--window-size=800,600")
#         options.add_argument("--disable-dev-shm-usage")
#         options.set_headless()
#         host = "chrome" if current_app.config["DEBUG"] else "127.0.0.1"
#         g.browser = webdriver.Remote(
#             command_executor=f"http://{host}:4444/wd/hub",
#             desired_capabilities=DesiredCapabilities.CHROME,
#             options=options,
#         )
#     return g.browser
#
#
#  def chrome(headless=False):
#      # support to get response status and headers
#      d = DesiredCapabilities.CHROME
#      d['loggingPrefs'] = {'performance': 'ALL'}
#      opt = webdriver.ChromeOptions()
#      if headless:
#          opt.add_argument("--headless")
#      opt.add_argument("--disable-xss-auditor")
#      opt.add_argument("--disable-web-security")
#      opt.add_argument("--allow-running-insecure-content")
#      opt.add_argument("--no-sandbox")
#      opt.add_argument("--disable-setuid-sandbox")
#      opt.add_argument("--disable-webgl")
#      opt.add_argument("--disable-popup-blocking")
#      # prefs = {"profile.managed_default_content_settings.images": 2,
#      #          'notifications': 2,
#      #          }
#      # opt.add_experimental_option("prefs", prefs)
#      browser = webdriver.Chrome(options=opt, desired_capabilities=d)
#      browser.implicitly_wait(10)
#      browser.set_page_load_timeout(20)
#      return browser

 #
 # def headless(self, path: str, proxy: str = "") -> None:
 #     ua = UserAgent()
 #     userAgent = ua.random
 #     options = webdriver.ChromeOptions()
 #     options.add_argument("headless")
 #     options.add_argument("window-size=1500,1200")
 #     options.add_argument("no-sandbox")
 #     options.add_argument("disable-dev-shm-usage")
 #     options.add_argument("disable-gpu")
 #     options.add_argument("log-level=3")
 #     options.add_argument(f"user-agent={userAgent}")
 #
 #     if proxy != "":
 #         self.proxy = True
 #         options.add_argument("proxy-server={}".format(proxy))
 #
 #     self.driver = webdriver.Chrome(path, chrome_options=options)
 #     self.set_config()
 #     self._headless = True
 #
 #

def load_driver(settings):
    """
    Load the Selenium driver depending on the browser
    (Edge and Safari are not running yet)
    """
    driver = None
    if settings['browser'] == 'firefox':
        firefox_profile = webdriver.FirefoxProfile(settings['browser_path'])
        driver = webdriver.Firefox(firefox_profile)
    elif settings['browser'] == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('user-data-dir=' +
                                    settings['browser_path'])
        driver = webdriver.Chrome(options=chrome_options)
    elif settings['browser'] == 'safari':
        pass
    elif settings['browser'] == 'edge':
        pass

    return driver


def get_page(url):
    chrome_options = webdriver.ChromeOptions()
    #ua_argument = 'User-Agent="'+GetUserAgent()+'"'
    #chrome_options.add_argument(ua_argument)
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument('log-level=3')
    try:
        driver = webdriver.Chrome(chrome_options=chrome_options)
        #driver.set_page_load_timeout(6)
        # driver.set_script_timeout(6)
        driver.get(url)
        # time.sleep(0.5)
        driver.quit()
    except:
        driver.quit()
        print("timeout")



# javaScritp Executor
driver.execute_script("return document.title")
driver.execute_script("return document.URL")
print("this is page load " + driver.execute_script("return document.readyState"))
driver.execute_script("windows.location = 'https://youtube.com")



element = self.driver.find_element_by_xpath(self.slack_email_xpath)
self.driver.execute_script("arguments[0].click();", element)


userN= driver.find_element_by_id("user-search']")
driver.execute_script("arguments[0].click();", userN)
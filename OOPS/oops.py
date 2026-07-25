#OOPS:- Object oriented programming. 
#imperative approach in python:- 
a=12
b=12
print(a+b)
#the above is the program which shows the imperative approach, where supoose i want to add another numbers i have to create new variables for exmaple c and d.
c=12
d=12
# you have to use the program many times to do same task.
# Functional approach in python :- we create functions which takes two variables and add them. no we can take that variables multiple times.
def addition(a,b):
    print(a+b)
(addition(12,12))   
(addition(23,23))
# NOTE :- FOR BETTER DEFINITION OF IMPERATIVE PROGRAMMIN,FUNCTIONAL PROGRAMMIN, OOOP, SEE CHATGPT OOPS CHAT. AND ALSO LEARN RETURN AND PRINT VALUE DIFFERENCE IN THERE. 
#NOTE:- CHATGPT'S DEFINITION OF IMPERATIVE PROGRAMMING,FUNCTIONAL PROGRAMMING AND OBJECT-ORIENTED PROGRAMMING. 
#(1) IMPERATIVE PROGRAMMING :- YOU WRITE THE SEQUENBCE OF STEPS THE COMPUTER SHOULD PERFORM. 
#EXAMPLE :- a=12
b=12
print(a+b)
#(2) Functional programming :- You organize work into reusable functions that take inputs and return outputs. 
def addition(a,b):
    return a + b 
#(3) Object-Oriented Programming(OOP):- You organize code around objects that contain both data(attributes) and behaviour(methods).
class calculator:
    def addition(self,a,b):
        return a+b
#NOTE :- return sends a value back to the place where the function was called. 
#NOTE :- OOPS IS THE PROGRAMMING METHOD BASED BON THE CONCEPT OF "OBJECTS", WHICH CAN CONTAIN DATA(ATTRIBUTES) AND CODE(METHODS).
# Advantages of oops :- (1) it makes code reusable, (2) you can excute multiple things together. (3) provides security, (4) and is helpful for management tasks.


#NOTE :- CLASSES :- FOR CREATING THE CLASSES FIRST WE HAVE TO UNDERSTAND THE STATEMENT. TO CREATE THE CLASS YOU HAVE TO WRITE:-  class<classname>
# class is basically blueprint for the objects. 
class Factory:                                            #NOTE :- START CLASS NAME WITH CAPITAL LETTER.
    #NOTE:-  THERE ARE TWO THINGS INSIDE THE CLASS ATTRIBUTES AND METHODS.
    #NOTE:- ATTRIBUTES ARE THE VARIABLES DEFINED INSIDE THE CLASS. METHODS ARE THE FUNCTIONS DEFINED INSIDE  THE CLASS.
    a=12 #attribute
    
    def hello():  #method
        print("hello are you my nigga ? ")
    
    print(" hello how are you i am getting initialized ")  # when we run the code the whole class works for one time , like ek baari main hi saara class ka samaan run ho jaata hain. 
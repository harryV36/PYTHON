#OOPS:- Object oriented programming. 
#imperative approach in python:- 
# a=12
# b=12
# print(a+b)
# #the above is the program which shows the imperative approach, where supoose i want to add another numbers i have to create new variables for exmaple c and d.
# c=12
# d=12
# # you have to use the program many times to do same task.
# # Functional approach in python :- we create functions which takes two variables and add them. no we can take that variables multiple times.
# def addition(a,b):
#     print(a+b)
# (addition(12,12))   
# (addition(23,23))
# # NOTE :- FOR BETTER DEFINITION OF IMPERATIVE PROGRAMMIN,FUNCTIONAL PROGRAMMIN, OOOP, SEE CHATGPT OOPS CHAT. AND ALSO LEARN RETURN AND PRINT VALUE DIFFERENCE IN THERE. 
# #NOTE:- CHATGPT'S DEFINITION OF IMPERATIVE PROGRAMMING,FUNCTIONAL PROGRAMMING AND OBJECT-ORIENTED PROGRAMMING. 
# #(1) IMPERATIVE PROGRAMMING :- YOU WRITE THE SEQUENBCE OF STEPS THE COMPUTER SHOULD PERFORM. 
# #EXAMPLE :- a=12
# b=12
# print(a+b)
# #(2) Functional programming :- You organize work into reusable functions that take inputs and return outputs. 
# def addition(a,b):
#     return a + b 
# #(3) Object-Oriented Programming(OOP):- You organize code around objects that contain both data(attributes) and behaviour(methods).
# class calculator:
#     def addition(self,a,b):
#         return a+b
#NOTE :- return sends a value back to the place where the function was called. 
#NOTE :- OOPS IS THE PROGRAMMING METHOD BASED BON THE CONCEPT OF "OBJECTS", WHICH CAN CONTAIN DATA(ATTRIBUTES) AND CODE(METHODS).
# Advantages of oops :- (1) it makes code reusable, (2) you can excute multiple things together. (3) provides security, (4) and is helpful for management tasks.


#NOTE :- CLASSES :- FOR CREATING THE CLASSES FIRST WE HAVE TO UNDERSTAND THE STATEMENT. TO CREATE THE CLASS YOU HAVE TO WRITE:-  class<classname>
# class is basically blueprint for the objects. 
# class Factory:                                            #NOTE :- START CLASS NAME WITH CAPITAL LETTER.
#     #NOTE:-  THERE ARE TWO THINGS INSIDE THE CLASS ATTRIBUTES AND METHODS.
#     #NOTE:- ATTRIBUTES ARE THE VARIABLES DEFINED INSIDE THE CLASS. METHODS ARE THE FUNCTIONS DEFINED INSIDE  THE CLASS.
#     a=12 #attribute
    
#     def hello(self):  #method
#         print("hello  how are you my nigga ? ")
    
#     print(" hello how are you i am getting initialized ")  # when we run the code the whole class works for one time , like ek baari main hi saara class ka samaan run ho jaata hain. 

# # calling the factory class :- 
# # obj = Factory() # object created and object is instance of class like kid of class it has every power function of class. 
# # printing a outside like this print(a) is difficult cauz it is not in global case. 
# # To print a :- we can do something like this :-
# print(Factory().a)   #NOTE :- printing variable which is local case of the Factory class. 
# Factory().hello()  #NOTE:- calling the hello() function which is inside the Factory class. # This line will print two things first the sentence that is in the print statement in the function and then None cauz we did not used return. 

# #OBJECTS IN OOPS 
# #Objects is usually company that create shoes using blueprint(class). 
# #NOTE:- Objects synatx :-
# obj=Factory()
# print(obj.a) # excessing the value from class using object obj. 
# # we can also acess function using object :- 
# obj.hello()
# # we can create multiple objects also. 
# obj1=Factory()
# obj2=Factory()
# obj3=Factory()
#NOTE :- All above objects have powers and  functions of the class Factory. 
#NOTE :- FOR WAY BETTER EXPLANATION REFER GPT NOTES. 

#  WHAT IS self() ? 
# NOTE :- CONSTRUCTORS 
# class Factory:
#     a=12 # attribute 
#     def hello(self):
#         print("How are you ? ")
    
# obj=Factory()
# obj2=Factory()
 
 #NOTE :- SECTION A :- CONSTRUCTOR :- THROUGH IT U CAN EXCEPT PARAMETERS FROM USER. A CONSTRUCTOR IS A METHOD THAT RUN AUTOMATICALLY WHEN WE CALL A CLASS AND THIS CONSTRUCTOR TARGETS OBJECT LOCATION AND ALSO IT EXCEPT PARAMETERS. 
# THEY ARE ALSO KNOWN AS DUNDER METHODS. LEARN ABOUT THEM.
# CREATING A CONSTRUCTOR FUNCTION:- 
# class Factory:
    # def __init__(self,material,zips,pockets):
#         print(self) # this will print locations. 
#         self.material=material                # pass the line so below this another code can be written. 
#         self.zips=zips
#         self.pockets=pockets
#     def show(self):         # this is the method. this method will print the object details. 
#         print(f"your objects details are {self.material},{self.zips},{self.pockets}")
        
# # Factory()   # if you tap on it you can see the arguments the class Factory wants we call it. # what is work of self is that it points out the location of object.  
# reebok=Factory("leather",3,2) # what we do here is that we called Factory class inside the variable reebok and the reebok becomes instance of the class Factory , that is what we call object so , here reebok became object. 
# campus=Factory("nylon",3,3)
# reebok.show()
# # now reebok has all acess of the class Factory. 
# # self keyword is targetting the location of reebok. 
# #FOR ABOVE CODE EXPLANTION SEE YOUR NOTEBOOK, OOPS PART. 
# #NOTE :- MULTIPLE OBJECTS CAN HAVE THERE MULTIPLE DETAILING TYPES. 
# #NOTE :- SOME CLEAR EXPLANATIONS :- 
# # _init_() is a special method(called a constructor in beginner courses) that runs automatically whenever a new object is created.
# # self refers to the current object that is being created or used. another definition can be self refers to the current object. it let us store or access data belonging to that object. 
# # Python thinks of self as teh current object,not a memory object. 
# # when we think reebok=Factory(..) here during call self becomes reebok , and suppose for another object campus, during the call self becomes campus. that's it. 
# #NOTE :- we read self.name=name as store the value ofn name inside this object.
# print(reebok.pockets)
# print(campus.pockets)
# this is how you can save multiple items :- this is what object-oriented means we create class and use it and create objects using class and unn objects ki seperate details hoti h and unko hum RAM ka use krke store krlete hain. 
    
#NOTE:- SECTION B :- METHODS AND ATTRIBUTES. 
#NOTE:- TYPES OF ATTRIBUTES :- 
#DEFINITION OF ATTRIBUTES:- ATTRIBUTES ARE THE VARIABLES THAT ARE DEFINED INSIDE THE CLASS. 
# class Animal:
#     # we will create multiple types of methods and attributes inside this class. 
#     #NOTE:- class attribute :- A normal variable created inside a class is a class attribute. 
#     #NOTE:- Instance Attribute:- A attribute created using an instance like self.name,slef.age etc. it is known as instance attribute. Instance is basically Object. object location can be also called instance. 
#     def __init__(self,age):
#         self.age=age #instance attribute, how to identify instance attribute there will be self with it. 
#     #TYPES OF METHODS:- 
#     #(1) Instance Method :- An instance method works with instance(object) of the class. This method can access and modify instance attributes. 
#     def show(self): # instance method # An instance method is a normal method whose first parameter is self. it works with a specific object.  and instance methods are easiest to work with. 
#         print(f"how are you ? and your age is {self.age} ") 
#     #NOTE :- CLASS METHOD :- THIS METHOD WORKS WITH THE CLASS ITSELF, IT WILL NOT TARGET THE INSTANCE(OBJECT). WE HAVE TO USE @classmethod decorator for creating the class method and it takes cls as their first parameter.
#     @classmethod 
#     def hello(cls):   # you can write self here but self is used when we are targetting location of object and instance. 
#         print(" how are you bro ?") 
#     # NOTE :- the above function is the example of class method and it targets directly the class. 
#     # A class method can be called using either the class or an object. 
#     #NOTE :- EXAMPLE :- 
#     # class Factory:
#     #     @classmethod
#     #     def hello(cls):
#     #         print("hello")
        
#     # Factory.hello()
#     # obj=Factory()
#     # obj.hello()
    
#     #NOTE:- Static Method :- This method doesn't access class or instance directly it also uses a decorator @staticmethod. it just acts like a regular fuction placed inside a class. 
#     @staticmethod
#     def static():
#         print("how are you ?")
    
# obj=Animal(12)   # creating instance of class Animal and #NOTE:- ALWAYS REMEMBER TO KEEP IDENTATION SAME AS CLASS WHENEVER YOU ARE CEATING AN INSTANCE OR CALLING AN FUNCTION INSIDE THE CLASS. 
# obj.show() 
# obj.hello() # calling class method but but always remember cls doesn't target object it targets only the class. so if we wrote something like this in def hello(cls): print(f"how are you brother {cls.age}"), this will not work as cls isn't targetting any instance. and why it is targetting class we'll have answer in few mins. 
# obj.static() # calling static method using obj object. 

# NOTE :- ANALOGY TO UNDERSTAND THE OOPS METHODS AND ATTRIBUTES :- 
class School:
    total_students=0 # class attribute given for class method. 
    def students(self,name,age):
        self.name=name
        self.age=age
        School.total_students +=1 # counting number of students.
        print(f"student name is {self.name} and his/her age is {self.age}")
        
    @ classmethod 
    def show_total(cls):
        print(cls.total_students)
    
    @staticmethod
    def add(a,b): #NOTE :- If a Function already receives values through parameters, you usually don't need to ask the user  for input inside that function. Choose one approach :- either pass arguments as parameters or collect them with input(). or if you want to take numbers from user or any data so don't take parameters, just do this :- def add() : a=int(input(" first number :- ")) , b=int(input(" second number :- ")). then call print(School.add())
        return a+b    #NOTE :- print line will never be used after return cause when pyhton sees return the function ends immediately. 
obj1=School()
obj1.students("HARRY",22)

obj2=School()
obj2.students("SHUBHAM",21)

obj3=School()
obj3.students("SAURABH",22)

School.show_total()

print(School.add(15,25))

# DONE WITH METHODS AND ATTRIBUTES. 
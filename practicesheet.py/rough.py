# print("4".isdigit())
# # how to check all built-in functions related to string in python. 
# print(dir(str))

# checking different ways to determine taht the stored variable is an integer.
# NOTE :- AN PERSON ON STACKOVERFLOW IS SAYING TO CHECK TYPE OF A VARIABLE IS BY USING TypeError exception, i am not currently working on this idea but but do some research about it and do some experiments about it. 
# some ways told by person on stackoverflow :- 
# (a) isinstance(<var>, int).
# holy some advance stuff but do read the stackoverflow article on it. this is exercise for exception handling. 

# checking some if condition doubt :- 
# a=int(input(" enter the number :- "))
# if a==type(int):
#     print(" the variable a is an integer")
# a = int(input("Enter number: ")) # important points to remember differences between various type operations. 

# print(a)
# print(type(a))
# print(type(int)) 

# print(type(5))
# print(int)
# print(type(5) == int)



#OOPS ROUGH WORK
# def hello():
#     print("hello")

# x=hello()
# print(x) 

def hello(name):
    print("Hello",name)

hello("Himanshu")
# calling function and giving it a argument. 
#NOTE:- def hello(name): ; here in this line name is the parameter given to hello function. 
#NOTE:- print("Hello",name) ; here name works as a local variable. 
#NOTE:- hello("Himanshu") ; here in this line Himanshu is the argument given to function hello. An argument is the actual value or data you pass into a function when you call it. 

class Factory:   # class Factory created. 
    def hello(self):
        print("Hello")
factory=Factory()    # Creates a Factory object and stores its reference in the variable 'factory'. or another simple explaination would be :- An object of the Factory class is created and storede in the variable 'factory'. 
factory.hello()      # how Python evaluates this it secretly changes it inside and it becomes something like :- Factory.hello(factory).
#NOTE:- in above line , python is basically saying that which Factory object should run the hello() method. the answer is factory. 



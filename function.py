#FUNCTIONS IN PYTHON. 
#primitive approach vs functional approach. 

#functions are the block of code whoch can be execuyted whenever we want. 
# there are many build-in fnctions in python. example :- print(),input(),len(). 

# print(" hello are you ? ") #in built python function. 
# there are multiple pre-built functions in python. 
# how to create functions in python and use. 
# user-defined functions are the functions built by user for his own works or needs. 
# we use def ( means define) to build user-defined functions. 
# def hello(): 
#     print(" this is the hello function so i am doing hello")
#     # this will print nothing as function is not called. 
# hello() # calling of hello() function. 

#parameters and arguments :- 
# parameters are the variables listed inside the function. 
# def sum(a,b): # a and b here are parameters. 
#     print(f" the sum of your numbers is :- { a + b } ")
# sum(12,12) # these are arguments. 12 and 12
# # the thing is you accept is parameters. 
# # the thing u provide to parameters is arguments. 
# sum(5,5) # calling function sum other time. # example of positinal arguments. 
# functions are reusable so we can do the partcular task many many times as you want. 

# types of arguements and parameters. 
# there are three types of arguments which can be passed to parameters. 

# def hello(name,age):
#     print(f"you name is {name} and your age is {age}")
# hello(age=22,name="himanshu") # keyword argument. here we can directly give values to keywords wuthout following the structure. 


# def sum(a,b=45): # default parameter/ default argument. 
#     print(f" the sum is {a+b}")
# sum(12) # we can also replace the value of b here. 

# checking if the string is palindrome or not using user defined functions. 
# def palindrome(st):
#     rev=""
#     for i in range(len(st)-1,-1,-1):
#         rev=rev+st[i]
#     if rev==st:
#         print("palindrome")
#     else:
#         print(" not a palindrome") 
# palindrome("naman")
# palindrome("cursor")
        
def hello():
    return " hello are you my nigga "      # return is used provide the value at block where you called your function. 

hello()
print(hello()) 
# learn difference between return and print(). very very very very important. 
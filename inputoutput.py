# INPUT AND OUTPUT
#PRINT IS USED FOR OUTPUT ONLY AND ONLY.
#print("hello how are you ?")
#name="akarsh"
#age="23"
#print(name,age) # print name and age together.

# FORMATTED STRING IN PYTHON. 
#print("hello my name is",name,"my age is",age) # one way of writing the line hello my name is akarsh my age is 23. 
#print(f"my name is {name} and my age is {age}")# FORMATTED STRING KEHTI H KI YARR AAP BAAR BAAR EK HI MULTIPLE STRINGS MT BANAO EK HI STRING USE KRO. AND WE USE f for FORMATTED STRING. 
#{}must be used in formatted string which tells the compiler that we are using something which doesn't come in terms of strings.

#INPUT STATEMENTS{ input statement basically mean asking user the question and where we ask question at terminal, in this case we use input function}
#input(" Hello what is your age ") # YOU CAN WRITE NOW OUTPUT ON TERMINAL. 
#ANY RESULT IS NOT PRINTED CAUZ NO PRINT FUNCTION USED, IT IS NIT BEING SAVED ANYWHERE IT IS STRES IN GARBAGE MEMORY, TO SAVE IT USE VARIABLE.
#name = input(" hello what is your damn fucking name ?")
#print(name) # deafult datatype is string, when ever we store any variable thorugh input variable it datatype is defaultly string, to convert string to any other datatype use type conversion. 
#age = int(input("Hello bitch ass nigga what is your damn fucking age?"))
#print(age)
#print(type(age))

# ACCEPT A NUMBER FROM A USER {QUESTION 1}
n1=int(input("put any fking number u want"))
print(n1)

#ACCEPT THE AGE FROM THE USER AND PRINT IT {QUESTION2}
age=int(input("what is your age user?"))
user_age=age
print(user_age)

# my own try to print user_name is himanshu. 
name=input("what is your name ?")
print(f"user_name is {name}")

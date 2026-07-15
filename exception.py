# NOTE :- code is a system of words,letters,numbers,etc. that are used instead of real letters or words to make a message or information secret. 
# Errors :- errors occur due to mistakes in the code that prevent it from running. These can be syntax errors or logical errors. 
# TYPES OF ERRORS :- 
# syntax error meaning error realted to syntax. 
# syntax is basically rules that define the structure of a language. 
# identation is used to organise and group statements into blocks of code. 
# identation error :- An indentation error happens when Python cannot understand which lines of code belong together because the spaces at the beginning of a line are missing, extra, or inconsistent. ( chatgpt definition )
# Tab error :- A TabError happens when you mix tabs and spaces to indent your code. Python wants you to use only one indentation style consistently.  
# # NOTE :- ALWAYS USE 4 SPACES FOR IDENTATION. 
# THESE ERRORS CAN'T BE HANDLED. 

#   IF WE REMOVE THESE ABOVE THREE ERRORS THE REMAINING IS EXCEPTIONS. 
#(a) zero division error :- suppose there is a code in which is we divide the 10 by the number that has been given by the user. 
# a=int(input(" enter your number :- ")) 
# d=10/a
# print(10/a)

# print(" ok ! Division has been completed.")  # this line is interesting as it is been printed when the whole code above it runs but but when zerodivision error happens, the below code line which is this one doesn't run as well. so the code stops because of an exception so that's why i should know how to handle exceptions. this is called EXCEPTION HANDLING. 
# now suppose someone put 0 as a input so 10/0 is undefined value in maths and python, so python will give ZeroDivisionError: division by zero. 
# the above is the example of exception which is not the problem of syntax of python, this is the factual error. 



# EXCEPTIONS :- EXCEPTIONS are unexpected events or errors that occurs during the excution of a program which disrupts the normal flow of the program. 
# Handling Exceptions are known as exception handling. 

# IMPORTANT KEYWORDS IN EXCEPTION HANDLING :- 
# (1) try :-  wraps the block of code that might cause an exception. 
# syntax of try :- try : 
#                       print(10/a)
# the above will give error cause try chlta hai except ke saath. 
# except :- handle the exception if it occurs. 
# syntax of except and try : 
#                        try : 
#                              print(10/a)
#                        except ZeroDivisionError:
#                             print(" sorry you cannot divide by 0")                       
# executing the above concept into the code :- 
# a=int(input(" enter your number :- ")) 
# # d=10/a   # NOTE :- this line will cause error as  the ZeroDivisionError would occur before the try block. so the exception ahndling won't be done then. 
# try:
#     d=10/a # NOTE :- always remember you have to wrote the code that will give exception errot inside try:. the whole code not just print or bits of code. 
#     print(d)

# except ZeroDivisionError:
#     print("sorry , you cannot divide by 0")
# print(" ok ! Division has been completed.")




# chatgpt challenge part :- if the user enters both 0 and any other value than integer, then how should the code should have been written ?  
# d=10/a   # NOTE :- this line will cause error as  the ZeroDivisionError would occur before the try block. so the exception ahndling won't be done then. 
#NOTE:- Experiment  1:- using continue and asking for a's value again.
try:
    a=int(input("enter your number :- "))
except ValueError:
    print(" give integer value to the variable ")
    # continue 
a=int(input(" enter ur number :- "))
try:
    d=10/a # NOTE :- always remember you have to wrote the code that will give exception errot inside try:. the whole code not just print or bits of code. 
    print(d)

except ZeroDivisionError:
    print("sorry , you cannot divide by 0")
print(" ok ! Division has been completed.")
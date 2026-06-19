# FOR LOOP QUESTIONS. 
# Question 1 is Accept an integer and print hello world n times,
# n=int(input("enter the integer ")) 
# for i in range(1,n+1):
#     print("hello world") 

# Question 2 :- print natural numbers up to n. 
# n=int(input(" enter the number"))
# for i in range(1,n+1):
#     print(i)

#Question 3 :- print natural numbers n to 1. # reverse for loop. print n to 1.  
# n=int(input("enter the number : "))
# for i in range(n,0,-1):
#     print(i) 

# Question 4:- take a number as a input  and print its table. 
# n=int(input("enter the number : "))
# for i in range(n,(n*10)+1,n):
#     print(i)
# what if n=0:- 
# n=int(input("enter the number : "))
# if n==0:
#     print(" please enter a non zero number")
# else: 
#     for i in range(n,(n*10)+1,n):
#       print(i)

# # Question 5 :- sum up to n terms. 
# n=int(input(" enter the value of n "))
# sum=0 
# for i in range(1,n+1,1):
#     sum=sum+i
     
# print(sum) 

# #Question 6 :- factorial of number
# n=int(input("enter the n : "))
# mul=1
# for i in range(n,0,-1):
#     mul=mul*i
# print(mul)
# Question 7 :- print the sum of all even and odd numbers in range separately. 
# n=int(input(" enter the value of n : "))
# sum1=0
# sum2=0 # always when you are declaring variables do it outside loops, or it will be not be permanent like the value will repeat it self. 
# for i in range(0,n,1):
#     if i%2==0:
#      sum1=sum1+i
#     else:
#         sum2=sum2+i
# print(sum1)
# print(sum2)

# Question 8 :- print all the factors of the number. ( same logic as above) 
# n=int(input("enter the value of n : ")) 
# #fac=0 # you can ignore this but this was my first logic. 
# for i in range(1,n+1,1):
#     if n%i==0:
#         #fac=i # logic here is storing something that doesn't change the logic is useless. 
#         print(i) 

# Question 9:- accept a number and check if it is a perfect number or not. 
# perfect number is a number whose sumof factors is equal to the number itself. 
# example :- 6 :- 1+2+3=6 
# code :- 
# n=int(input(" enter the value of n : "))
# sum=0
# for i in range(1,n,1): 
#     if n%i==0:
#         sum=sum+i
# if sum==n:
#     print(n," is the perfect number")
# else:
#     print(n,"is not the perfect number") 

#Question 10 :- check wheather the number is prime or not. 
# prime number whose only factor is it and 1. 
# code :- 
# n=int(input(" enter number :-  ")) 
# total_divisor=0
# for i in range(1,n+1,1):
#     if n%i==0:
#         total_divisor+=1
# if total_divisor==2:
#     print(n,"is a prime number ")
# else:
#     print(n,"is not a prime number")

# Question 11 :- reverse the string without using build functions. 
# a=" himanshu verma "
# #print(len(a))
# for i  in range(14,-1,-1):
#     print(a[i])
 
# chat gpt approach 2 :- 
# a="kitty"
# reverse=""
# for i in range(4,-1,-1):
#     reverse=reverse+a[i]
# print(reverse)

# chatgpt question accepting string from user and reversing it without knowing its length so the string could be anything.  
# a=input(" enter your string ") 
# length = len(a) 
# print(length)
# reverse=""
# for i in range(len(a)-1,-1,-1):
#     reverse=reverse+a[i] 
# print(reverse) # my own developed code. 

# check if given string is palindrome or not. 
# a=input(" enter your string :-  ")
# length=len(a)
# print(length)
# reverse=""
# for i in range(len(a)-1,-1,-1):
#     reverse=reverse+a[i]
# print(reverse)
# if reverse==a:
#     print(f"given string  which is {a} is a palindrome string.")
# else:
#     print(f"given string a which is {a} is not a palindrome string.")
         
# method 2 :- two pointer idea:- 
# a=input("enter the string :- ")
# length=len(a)
# print(length)
# for i in range(0,len(a)-1,1):
#     if a[i]==a[len(a)-1]:
#         print(f" given string {a} is a palindrome string. ")
#     else:
#         print(f"given string {a} is not a palindrome string. ") # wrong code but yeah try it later now move to question 13. understand how to convert the logic into algo and then algo into code by keeping it in mind that what should be done and what should be not. like what is needed in the code and algo and what is not according to the logic. 
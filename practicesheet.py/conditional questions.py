# # question 1 is Accept two numbers and print the greatest between them. 
# a=int(input("enter first number :"))
# b=int(input("enter second number :"))
# # now comparing both numbers :- 
# if a > b:
#     print("a is the greater than b which is :", a)
# elif b > a: 
#     print(" b is greater than a which is :", b)
# else:
#     print("both a and be are equal") 
    
    
# # second version of the same code :- 
# a=int(input("enter first number :"))
# b=int(input("enter the second number:"))
# if a>b:
#     print(" a is greater than b which is  : ", a)
# elif b>a:
#     print(" b is greater than a which is ", b)
# elif a==b:
#     print(" a is equal to b") 

# question 2 is to accept the gender from the user as char and print the respective greeting message. 
# name= input(" enter your name :")
# gender= (input(" enter your gender : "))
# if gender == "male":
#     print(f" Good Morning {name} Sir")
# else:
#     print(f"Good Morning {name} Ma'am")

# lessons learnt :- always give words in string form if you wamt to do the comparison. 
#(2) for words to take input just take simple input. 

# one problem in above code is that what if user put MALE,m,abc,robot then it will generate something like good morning akash ma'am, which is wrong. 
# to solve it writing two codes :- 
#(1) input validation :- 
# name= input(" enter your name :")
# gender= (input(" enter your gender : "))
# if gender == "male":
#     print(f" Good Morning {name} Sir")
# elif gender== "female":
#     print(f"Good Morning {name} Ma'am")
# else:
#     print("Error: Invalid gender entered")

# #(2) solution two using not in:- 
# n=input(" enter your name: ")
# g=input(" enter your gender :")
# if g == "male":
#     print(f"good morning {n} sir")
    
# elif g=="female":
#     print(f"good morning{n} ma'am")
    
# elif g not in["male","female"]:
#     print("invalid input")

# above codes handle the problem which is what if user enter MALE,ROBOT,robot,abc,cdc instead of male. 
# we solved it by using if,elif.elif in first code and not in in second code. 
# these solved the problem of MALE,robot,abc like invalid input. 

# now what if i put MALE,Male,FEMale something like this or m or f or what if i want to go for all inputs like m,male,MALE. 
# solution is below :- 

# name=input("enter your name : ")
# gender=input("enter your gender : ").lower() # or i can use is gender=gender.lower()
# if gender == "male" or "m"or "M":
#     print(f"good morning {name} sir")
# elif gender== "female" or "f" or "F":
#     print(f"good morning {name} ma'am")
# else:
#     print("invalid gender entered ")

# above code also has  error because line 67 for explanation see chatgpt. 
# better approach would be use gender== "male" or gender="m" no use of making conditions for MALE and M cauz already used lower() method. 
# or another approach is to use if gender in ["male","m"] 
#elif gender in ["male","m"]
# study truthy and falsey values. 

# QUESTION 3 :- Accept an integer check wheather it is an odd or even number. 
# number=int(input("enter the number"))
# reminder=number%2
# #checking if number is odd or even we would check it by dividing by 2 and if reminder is zero then it is even , reminder is not zero then odd.
# if reminder==0:
# print("number is even ")
# else:
# print(" number is odd")

#QUESTION 4 :- accept name and age from the user.check if the user is a valid voter or not. 
# name=input(" enter the name : ") 
# age=int(input(" enter age of the voter : "))
# #checking if voter is valid or not so we will do it by checking the age what is the legal age which is set by gov to vote.
# if age>= 18:     
#     print(f"{name} is valid voter and is eligible to vote") 
# else:     
#     print(f"{name} is not  eligible to vote")

#Question 5 :- accept a year and check if it is a leap year or not. 
# year=int(input(" enter year : "))
# yearDivide= year%4
# # we will check if the year is divisible by 4 or not, if it is then it is a leap year and if it is not then it is not an leap year. 
# #also you can check the leap year by dividing by 100,400. if a year is divisible by 100 then it is not  leap year and if it is divisible by 400, then it is leap year. 
# if yearDivide==0:
#     print(f"{year} is leap year.")
# else:
#     print(f"{year} is not leap year.")
# now above code is true but but still some logic is missing here, example would be 1900 is divisible by 4 but but it is not a leap yaer. 
# improving the logic:- 
# year=int(input("enter the year number "))
# condition1=year%4
# condition2=year%100
# condition3=year%400
# #improving conditions by using if condition and conditional and logical operators. 
# if condition1 == 0 and condition2!=0 and condition3== 0:
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year") 

# above code also has flaw as 2024 which is a loop year not satisfy the above logic. 
# another try with taking some hint from gpt :- 
# year=int(input("enter year : "))
# if year%4 == 0 and year%400==0 and not year%100==0:
#     print("year is leap year")
# else:
#     print("year is not leap year")
# also not correct answer issue with year 2000 so yeah there is issue. 
# there are twp ways to prove if year is leap year or not:- (1) divisible by 4 and not divisible by 100 (2) divisible by 400. 
#code A :- 
# year=int(input("enter year :- "))
# condition1= year%4==0 and year%100!=0
# condition2= year%400==0
# if condition1 or condition2:
#     print(f"{year} is leap year.")
# else:
#     print(f"{year} is not leap year")
# above is the correct attempt.. 

# question 6 is to take input of temperature in celcius:- 
#below 0°C :- "Freezing cold "
#0°C to 10°C :- "very cold" 
#10°C to 20°C :- "cold"
#20°C to 30°C :- "pleasant"
#30°C to 40°C :- "Hot"
#Above 40°C :- "very hot"

# we will solve it using multiple elif conditions which is allowed in python. 
temp=int(input(" enter temperature : "))
# applying conditions :- 
if temp<0:
    print("Freezing Cold")
elif temp>=0 and temp<=10:
    print(" Very Cold ")
elif temp>10 and temp<=20:
    print(" Cold ")
elif temp>20 and temp<=30:
    print(" Pleasant ")
elif temp>30 and temp<=40:
    print(" Hot ") 
elif temp > 40:
    print(" Very Hot ")
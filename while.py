# LEARNING WHILE LOOP 
# while loop repeats  the piece of block of code as long as a condition is True. 
# syntax :- while condition:
# code to execute 
# it is useful when the number of iterations is unknown before execution. 

# lets say i want to print from 1 to 30 so now printing it using while loop by taking a condition. 
# a=1 
# while a<=30:    # this condition is true, so while loop start running and also it can run infite times until the condition becomes true. 
#     print(a) 
    # ctrl c se terminal interupt hota hain. 
    # now above code will print 1 infinite times. 
    
# a=1
# while a<=30:
#     print(a) 
#     a=a+1 
    
# where to use while and for we will understand it by doing questions. 
#Question 1 :- separate each digit of a number and print it on the new line. 
# a=int(input(" enter your number "))
# algorithm :- whenever we divide/mod any number with 10 we get its last digit as a reminder. 
# so according to the online tutor in this question what we are going to do is suppose we ahve a number for example 256. 
# now we will divide it with 10 so it will be 256%10 so the reminder will be 6 which will be printed and seperated from the original number. 
# after doing this now the original number becomes 25, now doing same method which is 25%10 which will give reminder 5 so now it becomes 2. and 5 will be seperated from the original number and then printed. 
# now the number has 2 which will be further divided by 10 which will give us reminder 2. now it will be taken out of that box of original number and printed. 
# this is how all numbera are separated. 
# we will do floor division here instead of mod , to take store the reminder which will be the value after point for example :- doing 256//10 will give us 25.6, now we will save the reminder and then 25 will be runned further by loop fpr the process.
# we will setup while here by this ki jb tk 256 ki value  ye zero se greater h tb tk run krte jao, at the end of the jb tk ye floor divide hoga aakhir main iski value 0 hojayegi. 
# while a > 0:
#     print(a%10) # printing the last value. # iski madad se last digit print hongi. 
#     a=a//10 # reassgning the value of a. # iski madad se loop rukega.
    # for more explantion refer to chatgpt while loop chat. 

# Question 2 :- Accept a number and print its reverse using while loop. 
# algorithmic approach here should be :- first taking a number as input, which will be changed with every iteration. 
# now second , how will it change with every iteration :-  i think for now same as above question. how will it change which is a=a//10. 
# third , how will iteration stop :- a==0. 
# fourth, which is what work happens each iteration which will be responsible for giving us the output :- a%10. 
# also i think here what we have to do is that we can store a%10 in a varaible and then just print the variable outside loop and we have our reversed number. 
a=int(input(" enter your number :- "))
reverse_number=0
while a>0:
    reverse_number=a%10
    a=a//10
print(reverse_number)
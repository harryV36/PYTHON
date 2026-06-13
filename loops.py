#LOOPS IN PYTHON. 
#loops in python alows us to execute a block of code multiple times without rewrting it. 
#manual priting wull taje 100 or more line but loop just need two lines to print("hello world"). 
#two types of loops in pyhton:- 
#(1) for loop. :- in this we know how many items to remove from box. and for loop works based on numbers. 
#(2) while loop:- in this we give condition. while loop works on conditions. 
# function is something in which we use () like print() isd also a function. 
# range function :- a range function excepts three things (s,s,s) - (start,stop,steps. range function is used in for loop. like specificaly used with  for loop. 

# # for loop example :- 
# a=range(1,21,1)   # using i variable that will be iterated, and where in a which is a range. 
# for i in a:
#     print(i)

# for q in range(1,11,1):
#     print(q)
# # default values in range is 0 and stop value is not default and steps value deafult is 1. 
# for p in range(20):
#     print(p)

# can we run for loop in reverse order:- yes you can 
# going from 20 to 50 using range function :- 
# for i in range(20,51,1):
#     print(i)

# print(" gap ")

# # going from 16 to 1:- 
# for q in range(16,0,-1):
#     print(q)
    
# print("gap")

# for  s in range(-5,-16,-1):
#     print(s)

# printing the table of 5 :- 
# for i in range(5,51,5):
#     print(i)

# taking input of which number table user wants:- 
# n=int(input("which number table you want?"))
# for i in range(n,(n*10)+1,n):
#     print(i)

# loops for strings :-  using loops for strings. 
# a="shreyians"
# print(a[2])
# for i in range(0,9,1):
#     print(a[i])

# now what if string is too big we can't singly just count every character postition, so in this case we will first find the length of the string. 
# b="himanshu verma is a goat"
# print(len(b)) # we can find the length of the string using len() function. 
# for i in range(len(b)):
#     print(b[i])

# second way is to run directly for loop on the string:- 
# c="himanshu verma is cool"
# for i in c:
#     print(i)   # we can do it directly also without using range function. 

# break, continue , else statemnt in loops:- 
#break is basically stopping at a specific point. 
# continue is basically that i have four points like a , b ,c , d. now what i will do is that i have to go from a to b but wanna skip b to c and then continue our path from c to d. so in this situation we  will use continue statement. 

# example of break :- 
# for i in range(1,21):            # in this code i starting value is 1 till 21, now i==15 mean when i values becomes 15 break the loop and if not not then i will continue in else block. 
#     if i == 15:
#         break
#     else: 
#         print(i)   # output will be 1-14. 

# # continue example :- 
# for j in range(1,22):
#     if j == 14:                  # here python will skip 14 and continue the counting. this is example of continue.
#        continue 
#     print(j)

# else statement  works with break :- agr break chla toh else nhi chalega , agr break nhi chla toh else chlega... 
for i in range(1,25):
    if i==15:
        print("break statement is executed ")
        break
    print(i)
else:   # here else will be for loop not with if. 
        print("break statement is not executed ")

print(" GIVE SOME SPACE ") 

for j in range(1,25):
    if j==56:
        print("break statement is executed ")
        break
    print(j)
else:
    print(" break statement is not executed ")
# remember break run kia else nhi kia, break run nhi kia else runn krega. 
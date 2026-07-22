#NOTE :- LEARNING ALL READ METHODS IN FILE HANDLING. 
a=open("students.txt","w")
a.write("Rahul\nPriya\nAmit\nNeha") # NOTE :- here \n means new line. 
a.close() # first write in the file and close it. 
# then open file again and do the reading. 
a=open("students.txt","r")
# print(a.read(5)) #NOTE:- will read exactly 5 characters. #NOTE :- always use print function with read methods. 
# print(a.read()) #NOTE :- AFTER a.read(5) which prints 
# print(repr(a.readline())) #NOTE  :- repr() shows you the actual value printed by python. also this line will not print anything cause cursor is at empty string. 

# now above the cursor was at last so to tackle this problem we will use seek() function which will move cursor back at 0th position.
# print(a.read(5))
# print(a.read())
# a.seek(0) #NOTE :- THIS MOVES CURSOR BACK TO 0TH POSITION. 
# # print(repr(a.readline())) # NOTE :- now this will print Rahul which starts at 0th position in file. or print(a.readline()) which will read only one line and then it will give out put which is Rahul\n. 
# #NOTE :- EXPERIMENTAL LINE TOLD BY GPT:-
# print(a.readline(),end="") # NOTE what we did at this line is that we told print() whoch has in default end=\n to doesn't do any thing at end so cursor stops there. #NOTE :-  for more info read FILE HANDLING CHAT WITH GPT FOR BETTER UNDERSTANDING.

# #NOTE :- readlines() it reads all lines and store them in a list. 
# print(a.readlines())
# #you can now perform list operations on them. 
# lines=a.readlines()
# print(lines[0]) 

#NOTE :- now the above code line at print(lines[0]) will give the error cause you see the cursor first goes from rahul to neha and convert it into the list as readlines() told but now you saved a.readlines() into the lines variable to perform variable function.  and you do this print(lines[0]) but cursor is at empty position cause you know after readlines a list is created of all text written inside the list and then it is converted into a list. now cursor is at empty so it gives empty list [] at lines=a.readlines() and lines[0] is possible of empty string so this is will give IndexError: list index out of range. 

# NOTE :- TO SOLVE THE ABOVE PROBLEM WE CAN GO FOR TWO WAYS :- 
# FIRST WAY :- 
# lines=a.readlines()
# print(lines) # it will give a whole list. 
# print(lines[0]) # it will give rahul as a output. 
# Secind way is to use seek after readlines() :- 
print(a.readlines())
a.seek(0)
lines=a.readlines()
print(lines[0])



#NOTE :- WE ARE DONE WITH READ METHODS. 

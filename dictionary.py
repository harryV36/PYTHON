# dictioanary is a datatype which also exists in other programming languages but it is called hashmap there. 
# how to create dictionaries:- 
# d={} # this is an empty dictionary it is not consider an set, it will be consider an set when there are some values inside it. 
# print(type(d))
# c={1:"hello"} # dictionary have key-value pairs. 
# print(type(c))
# characteristics of dictionary :- 
#(1) dictionaries are mutable, you can change inside the dictionary once it is being created. you can add key-value pairs. you cannot change keys but you can change values of keys. 
#(2) all keys should be unique but values can be common. 
#(3) dictionary follows insertion order, there is no indexing but keys works asa index here. 
#(4) a dictionary can store any type of data and even an another dictionary. 

# a={10:100,20:200,30:300,40:400}
# # how to access values in dictionary:- 
# print(a[10]) # we can access the values in dictionary using the keys. 
# # NOTE :- we can perform CRUD(create,read,update,delete) operations on values but not all on keys cause the keys cannot be changed after the creation. 
# a[10]=1000 # changing/updating  value inside the dictionary. 
# print(a)
# # NOTE :- you cannot update the keys. 
# a.update({50:500}) # updating a new key-value pair inside the dictionary. 
# print(a)
# a[60]=600 # creating a new key-value pair, another method to do so. 
# print(a)
# del a[10] # deleting the key value pair. 
# print(a)

# NOTE :- HOW TO TRAVERSE A DICTIONARY MEANING HOW TO RUN LOOP ON DICTIONARY. 
# a={10:100,20:200,30:300,40:400}
# for i in a:
#     print(i) # NOTE :- here we see that when we were doing the same transversing on list , the iteration was being done on values of list, but if i do iteration on dictionary writing print(i) it will give us keys.
#     print(a[i]) # NOTE :- accessing the values of the dictionary. 
    
    
    
# b={1:10,2:20,3:30,4:40,5:50}
# for i in b.values(): # NOTE :- WE CAN DIRECTLY ACESS ALL VALUES USING THIS METHOD ALSO. 
#     print(i)
    
# for i in b.keys(): #NOTE :- WE CAN DIRECTLY ACCESS THE KEYS ALSO THIS WAY. 
#     print(i)
    
    
    
    
# DICTIONARY METHODS :-  there are not many dictionary methods but let see working of some. 
# help(dict)
# clear() :- removes all items from dictionary.
c={10:100,20:200,30:300,40:400,50:500}
# c.clear()
# print(c)

# NOTE :- CONCEPT OF DEEP COPYING AND SHALLOW COPYING 
# FIRST WE'LL UNDERSTAND THE CONCEPT BY LIST DATATYPE. 
# a=[1,2,3,4,5]
# b=a # here a will be copied into a. 
# b[0]=100 
# now we are changing the first element of the a so let's see the change will happen in b or a, as we are changing in b it does not make sense to a to be changed. let's firsat print a. 
# print(a)
# you can see a is also changed the first element of a has become 100, which was changed in b. 
# this means if we copy the list into another list , and change any thing in the copied list then main list will also be changed.
# NOTE :- THIS THING IS KNOWN AS DEEP COPYING, IT IS CALLED DEEP COPYING BECAUSE THE MAIN LIST GETS DEEPLY COPIED INSIDE THE COPIED LIST, THAT'S WHY CHANGES DONE IN COPIED LIST IS BEING SHOWN IN MAIN LIST ALSO.  

# NOTE :- SHALLOW COPY :- WE CAN CREATE SHALLOW COPY TO TACKLE THE DEEP COPYING PROBLEM. 
# WE USE copy() function for that. 
# b=a.copy()
# b[0]=100
# print(a)
# # NOTE :- now u can see in above code when we changed the first value of b, but then we printed the a but nothing is changed inside the b. 
# so this concept is also applicable in dictionary. 
#.copy() function always returns the shallow copy of the list or dictionary. 

# get() method :- saves the key-value pair in other dictionary from another main dictionary by writing the key-value in the get() as dictionary.get(key). so now we will print the variable and the value will be printed that was connected to key that was in get(). 
# c2=c.get(20)
# print(c2)

# print(c.items())  # NOTE :- returns set like object to show all values of dictionary. all key-value pairs in form of items. 
# print(c.keys()) # NOTE :- returns the set of keys. 


# QUESTIONS OF DICTIONARIES :- 
# QUESTION 1 :- WRITE A PYTHON SCRIPT TO MERGE TWO DICTIONARIES. 

# a={1:10,2:20,3:30}
# # b={4:40,5:50,6:60}
# merging two dictionaries :- 
# first way :- using update method. 
# a.update(b) # b will be upadted inside a.
# print(a)

# second way:-  using a loop.
# for i in b:
#     a[i]=b[i]
# print(a)
# in the above loop what we did is that we picked key value pairs from b and updated then inside the a using keys, now what if there's the same key in as b so it will update the value of that key inside a from b. that's how u smartly use loops.

# chatgpt sample code to understand what's happening in it :- 
# b = {10:100, 20:200}

# for i in b:
#     print(i, b[i]) 

# QUESTION 2 :- WRITE A PYTHON PROGRAM TO SUM ALL VALUES IN A DICTIONARY. 
# sum=0
# for i in a:
#     sum=sum+a[i]
# print(sum)  

# NOTE :- make it habit to write total for addition questions cauz sum is also a in-built function in python.   

# another way also using a.values() :
# total=0
# for i in a.values():
#     total=total + i
# print(f"your total of all values of the dictionary is :- ", total ) 

# another way using in-built method named sum :- 
# print(sum(a.values())) 

# QUESTION 3 :- count the frequency of each elements in a list. 
b=[1,1,1,2,2,2,3,3,3,4,4,4,5,5,6,7,8]
 #frequency here means that how many times an element is repeated or has occured in the list or a dictionary. 
# we will use dctionary here to count the frequency of all elements in the list. 
# we can count the frequency of one element using count function. 
# sample code :- 
# count=0
# for i in b:
#     if i==1:
#         count+=1
# print(count)
# but to count the frequency of all unknown elements in the list what we'll do i that we will use dictionary here. 
# dict={1:3,2:3,3:3,4:3,5:2,6:1,7:1,8:1} this kinda dictionary is what we have to get for the output. 
# d={}
# for i in b:
#     if i in d.keys():
#         d[i] +=1
#     else:
#         d[i]=1
# print(d)
# NOTE :- IN ABOVE CODE, WHAT IS HAPPENING IS THAT THERE'S THE LIST a, then we created d={}, an empty dictionary just like what we do with count and sum. 
# now, for i in b:
#          if i in d.key():
#          d[i] +=1 
#           else:
#           d[i]=1
# here first i which are the element in list b goes through if i in d.keys(), agar i as a key exist krt hain h dictionary d main toh uski value bada do +1. 
# aur agr woh nhi krta hain exist toh usko as a key add krdo dictionary main aur usko ek value 1 dedo. 
# now first i goes which is one if statemnt false and the else is runned so d[1]=1, so d={1:1}
# now another 1 comes , and if statement is runned and then is goes d[1]+=1, so it becomes d={1:2}. 
# and this how the frequency of all elements are counted. 

# QUESTION 4 :- write a python program to combine two dictionary by adding values for common keys. 
a={1:10,2:20,4:30}
b={4:40,5:50,6:60}

for i in b:
    if i in a.keys():
        a[i] += b[i] # updating of value of common keys. 
    else:
        a[i]=b[i]    # addition of key-value pair of b into a. 
print(a)

# DICTIONARY COMPLETED !!! 
#DATA STRUCTURES IN PYTHON. 
# REPRESENTING DATA IN STRUCTURED WAY IS CALLED DATA STRUCTURE. 
#when we are trying t0 store multiple values in a ssingle structure, it is is known as  data structures. 
# data structures are used to store,organize and manipulate data efficiently. Python provides several built-in data structures. 
# we have 4 types of in-build data structures in python :- list,Tuple,dictionary,set. 
# there are also custom data structures :- like stack,queue,linked list, graph, etc. around these data structures there are some algorithms thats's why there study is called data structires and algorithms. 

# IMPORTANT KEYWORDS TO KNOW BEFORE  STUDYING LIST :- 
# (1) MUTABLE :- WHEATHER A OBJECTS VALUE CAN BE CHANGED AFTER CREATION. AND LIST ALLOWS IT. SO LIST IS MUTABLE. 
# SYNTAX OF LIST :- 
# a=[12,13,14,15,16]  # list is indicated by [] ( square brackets). 
# DUPLICATES :- same value can occur many times in list. list allows it.
# heterogenous nature :- you can store different types of data types together in list. 
# ordered :- list maintains ordered sequence. we can access the elements in list through indexing. 
# list has indexing and slicing. 
# print(a[0]) # indexing of the list a. 
# print(a[0:3:1]) # slicing of the list a. 
# print(a[-2])

# # list transversing methods :- how can we run loops on list. 
# # first way using index :- 
# for i in range(len(a)):
#     # print(i)   # printing of index. 
#     print(a[i]) # printing of values. 

# # second way running loop  directly on values. 
# for i in a:
#     print(i)  
    
# # METHODS AND FUNCTIONS :- method is a function which is defined in  a class. method is also a kind of function. 
# # seeing the methods of the list :- 
# print(dir(list)) 
# help(list) # you can know about the list and its methods from this code line. 

# append function :- append the object to the end of the list. 
# a.append(17)  # a=[12,13,14,15,16,17] is the output. 
# print(a)

# insert needs index to insert that element at that index. 
# a.insert(1,2) # a.insert(index,element) a=[12,2,13,14,15,16]
# print(a)



# CHATGPT NOTES. 


# operations to be performed on the list :- 
# accessing the lis :- 
# print(a[0])
# # updating the list :- 
# a[0]=2
# print(a)
# # deleting element in the list :- 
# del a[0]
# print(a)

# membership in list :- finding wheather that particular element is part of the list or not. 
# print(13 in a) 

# # loop in list :- 
# for i in a: 
#     print(i)

# slicing in list :- 
# print(a[1:3])

# concatenation in list :- process of joining two or more strings, lists or tuples end to end to create a brand new object. 
# b=[17,18,19,20]
# print(a+b)

# repetition :- repeting the list to certain numbers. 
# print(a*3)


# different methods of list :- 
# append :- add one item at the end of the list. 
# a.append(17)
# print(a)

# extend :- add mutiple items in the list. 
# a.extend(17,18,19,20) # this will give error cause extend can only accept one argument. 
# instead to add multiple values give a list as a single argument to the extend() method. 
# a.extend([17,18,19,20]) # this is the correct way. 
# print(a) 

# insert() :- insert a element at a specific position. 
# a.insert(6,17)
# print(a)

# remove() :- remove by value/element. 
# a.remove(16)
# print(a)

# pop() :- remove by index and return the value which has been removed by the index. 
# a.pop(2)
# print(a)
# print(a.pop(2))
# print(a)

# clear() :- remove all items of the list. 
# a.clear()
# print(a)

# index() :- find the index of the particular element. 
# print(a.index(16)) 

# count() :- count occurences of the elements in the list.
# print(a.count(16))

#sort() :- sort the list into the order and it can also sort the strings comparing their index values.  
# b=[2,5,1,3]
# c=["banana","apple","pineapple"]
# b.sort()
# c.sort()
# print(b)
# print(c)  

#reverse() :- reverse the list order. 
# d=[1,2,3,4,5]
# d.reverse()
# print(d) 

#copy() :- make a copy of a list. 
# e=[1,2,3,4,5,6]
# print(e.copy())
# print(e) 

#len() :- count total elements of the list. 
# print(len(a)) 


# QUESTIONS BASED ON LIST :- 
# question 1 :-  print positive and negative elemnents of the list. 
# l=[1,-1,2,-2,-3,3,4,-4,5,-5] 
# print("positive elements are :- ")
# for i in l:
#     if i>=0:
#         print(i)
# print(" negative elements are :- ")
# for i in l:
#     if i<0:
#         print(i)

# question 2 :- mean of list of elements :- 
# l=[1,2,3,4,5]
# sum=0
# for i in l:
#     sum=sum+i
# print(sum)
# mean=sum/len(l)
# print(f"mean of the given list is {mean}.") 

# question 3 :- find the greatest element and print its index too. 
# l=[12,36,14,19,126,6,13]
# largest=l[0]
# index=0
# for i in range(len(l)):
#     if l[i]>largest:
#         largest=l[i]
#         index=i
# print(f" your largest number is {largest} at index {index}")

# question 4 :- find the second greatest element of the list. 
# l=[12,36,14,19,126,6,13] 
# largest=l[0]
# sec_large=l[0] 
# for i in l:
#     if i > largest:
#         sec_large=largest
#         largest=i
# print(sec_large,largest) # but this code has problem what if we found our largest value and second largest value is at small value and doesn't reach the true second largest value, for example :-  l = [12,126,45] now what if largest value gere is 126 which is true but second largest is stcuk at 12 not 44 so it can be problem. you can understand it by applying it on the code. 
# l=[12,100,90] 
# largest=l[0]
# sec_large=l[0] 
# for i in l:
#     if i > largest:
#         sec_large=largest
#         largest=i
# print(sec_large,largest) # see at this list the code fails so the code can't work for every list given by user. 

# l=[12,100,90]
# largest=l[0]
# sec_large=l[0]
# for i in l:
#     if i>largest:
#         sec_large=largest
#         largest=i
#     elif i < largest and i > sec_large:
#         sec_large=i
# print(largest,sec_large)    

# question 5 :- check if list is sorted or not. 
# a=[12,13,14,15,16] 
# for i in range(len(a)): # here we will take len(a)-1
#     if a[i]< a[i+1]: # this will give error cauz out of ramge it becomes. 
#         continue
#     else:
#         print(" your list is not sorted")
#         break

# for i in range(len(a)-1):
#     if a[i] < a[i+1]:
#         continue
#     else:
#         print(" your list is not sorted ")
#         break
# else:
#     print(" your list is sorted ")    
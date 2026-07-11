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
    
    
    
    
# DICTIONARY METHODS :- 
#
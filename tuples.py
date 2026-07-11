# TUPLES IN PYHTON. 
# tuples are immutbale, you can change anything in tuples. 
# we create tuple by using parenthesis (). 
# a=(1,2,3,4,5)
# print(type(a))
# # you cannot change the values of the tuple. that's why tuples are immutable. 
# # duplicate values are allowed in tuples. 
# # ordered :- you can acesss tuples using index values. 
# # tuples can have different type of data types in it. tuples can store different types of the data types. 
# # tuples are traverse in same manner as list :- 
# # two ways for traverse :
# (1) for  i in a: 
#     print(i)
# (2) for i in range(len(a)):
#     print(a[i]) 
    
# # the difference between tuple and list is of mutability and inmutability. 
# # tuples are kinda like strings cause of the imutable nature. 
# # two methods in tuples :- 
# (1) to find the index :- t.index().
# (2) count_5 :- t.count(number or value in the tuple)
# # tuple unpacking :- 
a,b,c,d=(1,2,3,4)  # example of tuple unpacking. 
print(a)
print(type(a))
e=(1,) # packing the tuple. 
print(type(e))
# SETS IN PYHTON. 
# hwo to create a set:- 
# a={1,2,3,4}    # values putted in curly braces without key-value pair is sets. 
# #{} this is an empty dictionary. 
# # characteristics of sets :- 
# #(1) sets are mutable you can change values in sets. 
# #(2) you cannot have  duplicate values in set that means every element inside the set is unique. 
# b={1,2,3,4,5,5,5,6}
# print(b)  # example of how every element is unique in set as no element can repeat once it is printed. 
#(3) sets are unordered and you cannnot acess them through index values. 
#indexing cannot be done with sets.
#sets in semi-heterogenous it can store some data types like string,numbers,tuples but not everything.

#how sets store values in python:- 
#each value in sets use hash-function.
# c=hash("hello")
# print(c)
# d=hash((1,2,34,45))
# print(d)
# hash values are always different. 
# only imutable / hashable objects can be stored in sets. 
# SET TRAVERSING 
# a={1,2,3,4,5}
# for i in a:
#     print(i) 
# # above will give the elements as it is but but in other list .....
# b={1,8,9,2,3,4,5}
# for i in b:
#     print(i)
# # u see the output of the above code is 1 2 3 4 5 8 9 , why because integers ki hash value ese store hoti h ki wih unhe represent krti h. so thats why they are orinted in numerical order. 

# c={1,8,9,"hello",2,4,5}
# for i in c:
#     print(i) # hello can be placed randomly as it depends on hash values. 

# SETS METHODS :- 
#sets method provide mutability to sets. and they can search hash values.
# a={1,2,3,4}
# a.add(5)  # adds an element to the sets. 
# print(a)
# a.remove(5) # removes an element and also gives error if the element is not found. 
# print(a)
# a.discard(4) # also removes the element and gives no error if the element is not found. 
# print(a)
# #popped_element=a.pop(), removes a random element. 
# a.pop()
# print(a) # it pop random values has it sees hash values, so te smalllest hash valueed element is removed first.
# a.clear() # empty whole set
# print(a) 

# some more methods/operations that can be performed between two sets. 
a={1,2,3,4,5}
b={4,5,8,9,10}
#union_set=a.union(b) unifies the two different sets.
s=a.union(b)
print(s)
#or
p=a|b
print(p) 

#intersection set :-
q=a.intersection(b)
r=a&b
print(q)
print(r)

# difference set :- 
t=a.difference(b)
u=b-a
print(t)
print(u)

# symmetric difference :- removing common part and joining two sets and their remainig elements. 
v=a.symmetric_difference(b)
w=a^b
print(v)
print(w)

# compound operators :- 
b-=a    # if we want the operations to be done inside the b only or a. there are also other compund operators u can use. 
print(a)
# shortcut for union is print(a | b) , | here is pipe operator which is a staright line. 
# shortcut for intersection of a and b is print(a & b )
# shortcut for difference of a and b is print(a-b).
# shortcut for  symmteric difference is print(a^b). 


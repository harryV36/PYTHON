#LOGICAL OPERATORS IN PYTHON. ( IMPORTANT AND CONNECTED WITH COMPARISON OPERATORS)
#WE CONNECT DIFFERENT COMPARISONS USING LOGICAL OPERATORS. 
# 3 TYPES OF LOGICAL OPERATORS:- 
#(1) and :- RETURNS TRUE IF BOTH CONDITIONS ARE TRUE.
# EXAMPLE :- 
print(123>100 ,34==34) # now in this example as we can see that there are two conditions which are both different and two and are seperated by a comma(,) and both are true, so the result here will be True True.
#what if i just want is that there comes only one True in reuslt instead of True True, so we will use "and" operator there as we know both conditons are true. 
print(126>100 and 36==36 ) # result is single True. 
print(135>125 and 56==56 and 89<178)
#now, and operation has this one rule that if anyone of the result is false then it will give false the answer doesn't matter if all other conditions are true.
print(5>6 and 2 < 3 and 4>7) # example of and operation here the result is false.
# breakpoint in and operation :- if the first condition that an operation is checking is false then it will not give true it will give false. 
print( 90 < 89 and 56 < 65 and 78 == 78 and 100 >99)

# or operation :- if any one condition is true then it will be give true, if not then it will give false. 
print( 12 != 12 or 67 == 56 or 10 > 5) # example of or operation. 

#(3) not operator:- reverse the boolean values.
print( not 12 == 12) # here the answer of 12 == 12 is true but we have use not so answer will be false. 

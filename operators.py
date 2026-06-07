#OPERATORS ARE THE SYMBOLS THAT PERFORM VARIOUS KIND OF DIFFERENT OPERATIONS ON VARIABLES. 
# ARITHMETIC OPERATORS :- MATHEMATICAL OPERATIONS ARE PERFORMED BY ARUTHMETIC OPERATORS. 
#THERE ARE 7 TYPES OF ARITHMATIC OPERATORS :- 
#addition,subtraction,multiplication,division,mod operation,floor division,exponential/power operation.
a=5
b=20
print(a+b) #ADDITION EXAMPLE. 
print(b-a) #SUBTRACTION EXAMPLE. 
print(a*b) #MULTIPLICATION EXAMPLE. 
print(b/a) #DIVISION EXAMPLE, HERE ANSWER WILL BE 4.0 CAUZ IF ANYTHING I NSRWITTEN IN FORM OF P/Q SO IT ANSWER WILL BE IN FLOAT DATATYPE ALWAYS. 
print(b//a) # FLOOR DIVISION GIVES ANSWER IN INTERGER FORM NOT IN POINT LIKE IT WILL GIVE ANSWER 4 NOT 4.0. REMOVES VALUE AFTER . LIKE IT WILL GIVE 6 INSTEAD OF 6.4
print(20%5)  # MOD OPERATION GIVES REMINDER OF THE DIVISION PROCESS. 
print(5**2) # power operation used to give power to number.

# ANOTHER EXAMPLE WITH VARIABLES :- 
c=2
d=3
sum = c+d
sub = d-c
mul = c*d
div = d/c 
flo = d//c 
mod = d%c
pow = d**c 

print(sum) #note :- whenever using the any variable to print something like in this example do not put "sum" like this it converts it into a string. 
print(sub)
print(mul)
print(div)
print(flo)
print(mod)
print(pow) 

# PYTHON FOLLOWS BODMAS TO SOLVE EQUATIONS. 
print(12+4/2) 
print(12+4//2)


# ASSIGNMENT OPERATORS( IMPORTANT) USED TO ASSIGN VALUES TO VARAIBLES. 
# = IS THE BASIC ASSIGNMENT OPERATOR.
e=23 
# compound assignment operators:- 
f=20
print(f+20) # task was to add 20 in f which is 20. 
# next task is to add 20 then add 40 then add 60. we have to do this in chronological order not ike straight adding 120 in the f. 
# we can reassign values in the varaible, # a = 20
                                          # a = 40
                                          #print(a)
                                          #it will print 40 cauz in python we can reassign the values to the variables. 

#a=20
#a=a+20
#print(a) output :- 40

# code 3 :-  a=20
#a=a+40
#a=a+40
#print(a) output is 80. 

# compound assignment operator removes the need to add number or do same operations multiple times. 
#for example taking above code 3 as the example we will use "+=" operator here. 
g=20
g+=40
g+=40
print("g is :",g)     
# in above code first g was 20 then added 40 which becomes 60 and then it is added 40 so it gives the output 100. 
#other compound assignment operators are :- -=,*=,/=,//=,**=,%=.  
h=2
h-=2
print("h is :",h) 
i=3
i*=3
print("i is :",i)                   
j=4
j/=2
print("j is :",j)
k=5
k//=5
print("k is :",k)
l=6
l**=2
print("l is :",l)
m=7
m%=2
print("m is :",m)

# COMPOUND ASSIGNMENT OPERATORS DONE. 
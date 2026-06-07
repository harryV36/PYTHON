# TYPE CONVERSION IN PYTHON.
# TYPE CONVERISON IS USED IN PYTHON TO CONVERT ONE TYPE OF DATA INTO ANOTHER TYPE OF DATATYPE. 
# TYPE CONVERSION FUNCTIONS :- int(),float(),str().bool() etc. [ used to convert one datatype into another datatype]. 
# example :- 
#a = 12 # integer datatype 
#a = str(a) # here we have change the dataype of string a from integer datatype to string datatype. 
#print(a)
#print(type(a))

# example 2 :- converting string to integer.
#b = "12"
#b=int(b) # if we write asd or any other character in string and convert it into integer it can't cauz the string value that has to be converted into integer has to be numerical only. 
#print(type(c))
#print(type(b))

# BOOLEAN CONVERSION :- CONVERTS ALL VALUE INTO TRUE AND FALSE. 
#a=12
#print(bool(a))
#d="asdf"
#print(bool(d))
#e=0
#print(bool(e)) 
# we figure out the bool value of a string like asdf and an integer like 12 it gives true but at 0 it guves false.
#why?
# because there are some truly values and some falsey values in pyhton, there are total falsey values :- false,0,0.0,"",[],(),{}.

# THERE ARE TWO TYPES OF TYPE CONVERSION :- IMPLICIT TYPE CONVERSION AND EXPICIT TYPE CONVERSION. 
# EXPLICIT TYPE CONVERSION IS THE TYPE CONVERSION WHERE WE WERE USING FUNCTIONS LIKE :- int(),bool(),str(),float().
#IMPLICIT TYPE CONVERSION IS THE TYPE OF TYPE CONVERSION WHERE PYTHON AUTOMATICALLY CONVERTS ONE DATATYPE INTO ANOTHER. 
f=12
print(12/3) # ANSWER IS 4.0 WHICH IS FLOAT. 

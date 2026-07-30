# 4 PILLARS OF OOPS :- 
# (1) INHERITANCE.
#(2) POLYMORPHISM. 
#(3) ENCAPSULATION. 
#(4) ABSTRACTION. 


#NOTE :- STARTING WITH INHERITANCE :-
#(1) INHERITANCE MEANS PROPERTY OR ANY POSSESION CAME FROM HIGHER TO HEIR. 
# INHERITANCE WORKS BETWEEN CLASSES. INHERITANCE ALLOWS CHILD CLASS TO INHERIT PROPERTIES AND BEHAVIOURS(ATTRIBUTES AND METHODS) FROM ANOTHER CLASS (PARENT CLASS). 
#CHILD CLASS WILL INHERIT PROPERTIES AND BEHAVIOUR OF PARENT CLASS. 
#BENEFITS OF INHERITANCE :- 
#(a) code reusability. 
#(b) Organized Structure. 
#(c) easy to maintaina and extend.

#NOTE :- SYNTAX OF INHERITANCE :- 
class Factorymumbai:  # parent class / super class 
    a= " I am attribute mentioned inside Factory"
    def hello(self):
        print(" hello i am a method ! mentioned inside the Factory class")
class Factorypune(Factorymumbai):    # child class / sub class.    #NOTE :- you do not use parameters inside the class but you use different class to inherit inside the class. 
    pass 
#NOTE:- above is the example of inheritance. 
#NOTE:- now Factoryoune can access the properties and behaviours of Factorymumbai. 
obj=Factorymumbai()
obj2=Factorypune()
print(obj.a)
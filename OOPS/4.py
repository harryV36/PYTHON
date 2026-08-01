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
# class Factorymumbai:  # parent class / super class 
#     a= " I am attribute mentioned inside Factory"
#     def hello(self):
#         print(" hello i am a method ! mentioned inside the Factory class")
# class Factorypune(Factorymumbai):    # child class / sub class.    #NOTE :- you do not use parameters inside the class but you use different class to inherit inside the class. 
#     pass 
# #NOTE:- above is the example of inheritance. 
# #NOTE:- now Factoryoune can access the properties and behaviours of Factorymumbai. 
# obj=Factorymumbai()
# obj2=Factorypune()
# print(obj.a)
# print(obj2.hello())    #it will also print None cause we are calling the function and printing some thing from the function and theere is nothing to return so it will return None. 
#NOTE :- Inherited class has  all the powers of parent class that means all the methods,attributes can be accessed by the instance of child class as well. 

# CONSTRUCTOR IN INHERITANCE :-
#NOTE :- lets say you ave created a parent class with a constructor function inside it and then this class is inherited by another class then the constructor function of parent class will work for the child class as well. 

# class Animal:
#     def __init__(self,name):
#         self.name=name # this is an instance attribute. 
#     def show(self):
#         print(f"hello your name is {self.name}")   

# class Human(Animal):
#     pass 
# animal1=Animal("harippa")  # instance of parent class. 
# animal1.show()
# person1=Human("Harry")    # instance of child class. 
# person1.show()


#NOTE :- THE ABOVE CODE TELLS US THAT EVEN CONSTRUCTOR FUNCTION OF THE PARENT CLASS CAN BE INHERITRED BY THE CHILD CLASS. 
#NOTE:- Lets say you need a new parameter in your child class you have to create a constructor function for your child class but the parameters that can be intialized in the parent class will be intialized using the super() function. Super function will target the parent class. 
# class Animal:
#     def __init__(self,name):
#         self.name=name # this is an instance attribute. 
#     def show(self):
#         print(f"hello your name is {self.name}")   

# class Human(Animal):
#     def __init__(self,name,age):
#          super().__init__(name)  #NOTE :- here we intiliazed the name cause it is already present in Animal. #NOTE:- super() function targets the parent class. 
#          self.age=age
#     def show(self):
#         print(f"hello your name is {self.name} and your age is {self.age}")
# animal1=Animal("Lion")  # instance of parent class. 
# person1=Human("Harry",21)   # instance of child class. 
# animal1.show()    # we cannot call show() from animal1 as there is age defined in Animal class. 
# person1.show()    # we can call show() from person1.
 
 #  NOTE :- THIS MEANS THAT IF YOU'RE CREATING EXTRA FEATURES IN SUB CLASS THEN SUB CLASS MAIN BHI SHOW FUNCTIONALITY BNANI PADEGI ALAG SE ! 


#NOTE :- TYPES OF INHERITANCE :- 
#(1) SINGLE INHERITANCE :- All the inheritance we saw above was single level.
#(2)MULTIPLE INHERITANCE :- means there will be two parent classes and one child class and the child class will inherit methods and attributes of both parent classes. 
 
 #NOTE :- EXAMPLE CODE OF MULTIPLE INEHERITANCE :- 
# class Animal:
#     def __init__(self,name):
#         pass  
# class Human:
#     def __init__(self,name,age):
#         pass
# class Robots(Human,Animal):
#     name3="charlie123"
# obj=Robots() # we are being asked name, this means that we targetting Animal constructor function, suppoose we want to target the constructor function of Human class to get name and age we have to put Human class first in parameeter then  Animal class.  
#NOTE :- THE CONSTRUCTOR FUCTION WILL BE INHERITED OF THE FIRST CLASS THAT HAS BEEN INHERITED.
# METHOD RESOLUTION ORDER THAT PYTHON FOLLOWS, IT IS CALLED MRO IN SHORT. 
#ABOVE IS THE EXAMPLE OF MULTIPLE INHERITANCE WHERE LAST IS INHERITING attributes FROM ABOVE BOTH CLASSES. AND ONE THING ALSO IF WE KEEP NAME variable same then charlie123 would be printed cause of method ovverriding.

#(3) MULTI-LEVEL INHERITANCE :- THIS IS THE BASIC CASE WHERE WE WILL HAVE GRANDPARENT CLASS->PARENT CLASS->CHILD CLASS. THE ATTRIBUTES AND METHODS ARE PASSED ON THROUGH ALL THE CLASSES. 

# EXAMPLE OF MULTI-LEVEL INHERITANCE WITH A SMALL PROJECT:- 
# class Factory:   #grandparent class
#     def __init__(self,material,zips):
#         self.material=material
#         self.zips=zips
# class BhopalFactory(Factory): #parent class
#     def __init__(self,material,zips,color):
#         super().__init__(material,zips)
#         self.color=color
# class PuneFactory(BhopalFactory): #child class
#     def __init__(self,material,zips,color,pockets):
#         super().__init__(material,zips,color)
#         self.pockets=pockets
# # print(dir(PuneFactory))

# bag=PuneFactory("Leather","YKK","BlACK",4)
# # print(PuneFactory)
# # print(PuneFactory.__init__)
# # print(PuneFactory.__dict__)
# # print(PuneFactory.__mro__)

# print(bag.material)
# print(bag.zips)
# print(bag.color)
# print(bag.pockets)
#NOTE :- WHOLE CONCEPT BEHIND THE ABOVE CODE :-  PuneFactory itself never creates the material attribute. It calls BhopalFactory.__init__() using super(), which in turn calls Factory.__init__(). The Factory constructor creates self.material and self.zips. Since all these constructors are initializing the same object (self), the PuneFactory object ends up with all four attributes: material, zips, color, and pockets. 

#(4) Hierarchical inheritance :- one parent two child. 
# Example of Hierarchical inheritance written by me on my own:- 

#(a) Vehicle Company hierarchical inheritance. 
# class Vehicle:
#     def __init__(self,company,fuel_type,wheels):
#         self.company=company
#         self.fuel_type=fuel_type
#         self.wheels=wheels
# class Car(Vehicle):
#     def __init__(self,company,fuel_type,wheels,doors,airbags):
#         super().__init__(company,fuel_type,wheels)
#         self.doors=doors
#         self.airbags=airbags
# class Bike(Vehicle):
#     def __init__(self,company,fuel_type,wheels,helmet_required,engine_cc):
#         super().__init__(company,fuel_type,wheels)
#         self.helmet_required=helmet_required
#         self.engine_cc=engine_cc

# Splendor=Bike("Hero","liquid","cast alloy","open_face" ,100)     
# print(Splendor.company)
# print(Splendor.engine_cc)
# print(Splendor.fuel_type)
# print(Splendor.helmet_required)
# print(Splendor.wheels)

# # print(Vehicle.__init__)
# # print(Car.__init__)
# Swift=Car("Maruti Suzuki","Petrol","alloy",4,2)
# print(Swift.company)
# print(Swift.fuel_type)
# print(Swift.wheels)
# print(Swift.doors)
# print(Swift.airbags)

#(2) Second Example of hierarchical inheritance:- class Bank 
# class Bank:
#     def __init__(self,bank_name,headquarters,ifsc_prefix):
#         self.bank_name=bank_name
#         self.headquarters=headquarters
#         self.ifsc_prefix=ifsc_prefix
# class MainBranch(Bank):
#     def __init__(self,bank_name,headquarters,ifsc_prefix,manager_name,total_staff):
#         super().__init__(bank_name,headquarters,ifsc_prefix)
#         self.manager_name=manager_name
#         self.total_staff=total_staff
# class RegionalBranch(Bank):
#     def __init__(self,bank_name,headquarters,ifsc_prefix,city,lockers_available):
#         super().__init__(bank_name,headquarters,ifsc_prefix)
#         self.city=city
#         self.lockers_available=lockers_available

# money=MainBranch("PNB","Delhi","PUNB","Rakesh Kumar",100)
# print(money.bank_name)
# print(money.headquarters)
# print(money.ifsc_prefix)
# print(money.manager_name)
# print(money.total_staff)

# reg=RegionalBranch("PNB","Delhi","PUNB","Hauz Khas",100)
# print(reg.bank_name)
# print(reg.headquarters)
# print(reg.city)
# print(reg.ifsc_prefix)
# print(reg.lockers_available)

# #(3) Third Example of hierarchical inheritance:- class Product
# class Product:
#     def __init__(self,name,price,brand):
#         self.name=name
#         self.price=price
#         self.brand=brand
# class Electronics(Product):
#     def __init__(self,name,price,brand,warranty,battery):
#         super().__init__(name,price,brand)
#         self.warranty=warranty
#         self.battery=battery
# class Clothing(Product):
#     def __init__(self,name,price,brand,size,fabric):
#         super().__init__(name,price,brand)
#         self.size=size
#         self.fabric=fabric

# mobile=Electronics("smartphone","25,000","samsung","1 year","LiPo")
# print(mobile.name)
# print(mobile.price)
# print(mobile.brand)
# print(mobile.warranty)
# print(mobile.battery)


# jac=Clothing("jacket","2,000","Jockey","S","leather")
# print(jac.name)
# print(jac.price)
# print(jac.brand)
# print(jac.size)
# print(jac.fabric)

#(4) Fourth Example of hierarchical inheritance :- class Hospital 
# class Hospital:
#     def __init__(self,hospital_name,city):
#         self.hospital_name=hospital_name
#         self.city=city
# class EmergencyWard(Hospital):
#     def __init__(self,hospital_name,city,ambulances,emergency_doctors):
#         super().__init__(hospital_name,city)
#         self.ambulances=ambulances
#         self.emergency_doctors=emergency_doctors
# class ICU(Hospital):
#     def __init__(self,hospital_name,city,ventilators,icu_beds):
#         super().__init__(hospital_name,city)
#         self.ventilators=ventilators
#         self.icu_beds=icu_beds

# hos=Hospital("MAX","DELHI")
# print(hos.hospital_name)
# print(hos.city)
# print(" all data of Hospital class")

# emer=EmergencyWard("MAX","DELHI",50,100)
# print(emer.hospital_name)
# print(emer.city)
# print(emer.ambulances)
# print(emer.emergency_doctors)
# print("All data of EmergencyWard class")

# icu=ICU("MAX","DELHI",50,50)
# print(icu.hospital_name)
# print(icu.city)
# print(icu.ventilators)
# print(icu.icu_beds)
# print("All data of ICU class ")


#(5) Fifth example of hierarchical inheritance :- class AIMODEL
# class AIMODEL:
#     def __init__(self,model_name,parameters,company):
#         self.model_name=model_name
#         self.parameters=parameters
#         self.company=company
# class chatbot(AIMODEL):
#     def __init__(self,model_name,parameters,company,languages_supported,voice_enabled):
#         super().__init__(model_name,parameters,company)
#         self.languages_supported=languages_supported
#         self.voice_enabled=voice_enabled
# class imagegenerator(AIMODEL):
#     def __init__(self,model_name,parameters,company,max_resolution,styles_supported):
#         super().__init__(model_name,parameters,company)
#         self.max_resolution=max_resolution
#         self.styles_supported=styles_supported

# ai=AIMODEL("Fable5.5",3,"Openai")
# print(ai.model_name)
# print(ai.parameters)
# print(ai.company)
# print("All data of the AIMODEL class printed.")
# bot=chatbot("Fable5.5",3,"Openai","hindi,english,punjabi","yes")
# print(bot.model_name)
# print(bot.parameters)
# print(bot.company)
# print(bot.languages_supported)
# print(bot.voice_enabled)
# print("All data of the chatbot class printed ")
# image=imagegenerator("Fable5.5",3,"Openai","1024x1024","Anime")
# print(image.model_name)
# print(image.parameters)
# print(image.company)
# print(image.max_resolution)
# print(image.styles_supported)


#NOTE:- POLYMORPHISM(2ND PILLAR OF OOPS)
#POLYMORPHISM IS A CORE CONCEPT IN OBJECT ORIENTED PROGRAMMING(OOP). THE WORD MEANS "MANY FORMS"- AND IN PROGRAMMING. IT ALLOWS THE SAME INTERFACE OR METHOD NAME TO BEHAVE DIFFERENTLY DEPENDING ON THE OBJECT OR CONTEXT. 
# when a same name methods/functions with different forms and functions. 
# def show():
#     print("how are you ?")
# def show():
    # print(" you are the best !")
# now we have two functions with same name but different print statements. what would this show() print on terminal it will print second show()function cause python overwrites the first one.
#NOTE:- now,what i wants is that i want both show()functions to run. so i will use the concept of OOPS here to solve the problem of overwriting. 
#TYPES OF POLYMORPHISM:-
#polymorphism can be achieved in python in two ways. in compile time languages there are 3 ways but python does not support method overloading. 
#Method overloading means having same name methods inside a class but parameters will be different but in python the lastest definiton will overwrite the previous one.
#(1)METHOD OVERRIDING :- 
# class Animal:
#      def show(self):
#          print("hello i am harry !")
# class Human(Animal):
#     def show(self):
#         print("how are you ? ")
# obj=Human() # the class human has access of bith methods and attributes in clasS Animal and also of the methods and attributes in Human class.
# obj.show()
#NOTE:- METHOD OVERRIDING :- in the above example we can see that obj is of Human class so, the show() function printed would be of Human class. 
# if someone asks you what is method overriding then explain him if you have a two classes one parent and child, the method of parent overrides by the childs method.
#NOTE:- IN SIMPLE WORDS WE CAN SAY IS THAT THE CHILD CLASS OVVERRIDES THE PARENT'S METHOD BY DEFINING A METHOD WITH THE SAME NAME. 

#METHOD OVERLOADING DOESN'T EXISTS IN PYTHON. 

#(2) DUCK TYPING 
#PYTHON FOLLOWS THE PHILOSOPHY:- IF IT WALKS LIKE A DUCK AND QUACKS LIKE A DUCK, IT MUST BE A DUCK. 
# class Animal:
#     def show(self):
#         print(" i am showing ")
# class Human:
#     def show(self):
#         print(" i am also showing !")

# obj=Animal()
# obj2=Human()
# obj.show()   # we call a method, do not print it.
# obj2.show()

#NOTE :- IN DUCK TYPING, THERE ARE TWO DIFFERENT CLASSES WHOM DOESN'T HAVE ANY RELATIONSHIP WITH EACH OTHER, THEY HAVE NO INHERITANCE RELATIONSHIP. 
#NOTE :- Duck Typing: Python focuses on what an object can do rather than what type/class the object belongs to. SIMPLE DEFINITION FOR DUCK TYPING. 
#NOTE:- METHOD OVERRIDING WORKS WITH INHERITANCE IN PYTHON.



#NOTE :- ENCAPSULATION :- putting data(variables) and code(functions) together in one place-inside a class.
# it also means hiding internal details of the class and how things work, and only showing what is needed. 
#it keeps data safe from being changed by mistake. 
#it makes your code clean and easy to use. 
#it gives control over what others can access or change. 
# code example to understand why we need encapsulation :- 
# class Factory:
#     a="pune"
#     def show(self):
#         print(" i am a pune factory guy !")
# obj=Factory()
# obj.a="bhopal" # changing the attribute inside the class. 
# print(obj.a)
#NOTE:- in above code the object 'obj' has access to all methods and attributes of class but i don't wanna give it. so in this scenario we use encapsulation. 
 
 #NOTE:- ACCESS MODIFIERS MEANS HOW WE GIVE ACCESS OF OUR ATTRIBUTES AND METHODS TO THE OBJECT OR INHERITED CLASSES. 
 #NOTE:- THERE ARE 3 TYPES OF ACCESS MODIFIERS:-
 #(1) PUBLIC ATTRIBUTES AND METHODS :- TILL NOW EVERY ATTRIBUTE AND METHOD WE CREATED ARE PUBLIC MEANS THE INHERITED CLASSES AND OBJECTS CAN ACCESS THEM NO MATTER WHAT.
class Factory:
    a="pune"
    def show(self):
        print("hello i am a pune facrory guy !")
class Bhopal(Factory):
    def show2(self):
        print(super().a)
obj=bhopal()

    
    
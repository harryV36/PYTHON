# FILE HANDLING BASIC PROJECT 
# FIRST WHAT WE ARE GONNA DO IS THAT WE WILL CREATE A NEW FOLDER AND IN THAT FOLDER WE WILL CREATE A NEW FILE NAME main.py. 
# we are going to do is that we are goling to do CRUD operations in this project.
# NOTE :- IN THIS PROJECT WE ARE NOT TARGETTING ARE WHOLE SYSTEM BUT OUR FILE HANDLING BASIC PROJECT FOLDER, SO WE CAN DO BASIC CRUD OPERATIONS IN THIS FOLDER ITSELF NOT IN OUR OPERATING SYSTEM. 

# what we are going to do is that we will user first options that what he want to do ? 
# below is the readfilefolder() function where what we are dloing is that we are creating afunction which will tell us the list of files inside our this folder. bhow many files or what names are ofg them are in the present folder where we are doing baisc crud operations.
# to read the path we need the library called pathlib. so we will import it. 
from pathlib import Path                                     #NOTE :- P should be capiotal of Path.

def readfileandfolder():
    print("I AM INSIDE READFILEANDFOLDER")
    path=Path(".")                                           # NOTE :- WRITE THE EMPTY STRING HERE LIKE THIS "" noit like this " "(this is not an empty string, this is the string with one space characters)               # what we did here is that we saved our path info in path variable and there is this empty space in Path(' '), the empty space gives you the path of directory that you are currently in. 
    print(path.resolve())                                     #NOTE :- print(path.resolve()) tells us the actual directory Python is searching. 
    items=list(path.rglob("*"))                              # NOTE :- THE ITEMS THAT ARE IN THIS PATH WE WANT TO READ IT SO WE WILL USE RECURSIVE CLOAK FUNCTION TEELS US THAT IN WHICH FOLDER AND PATH YOU ARE IN I WILL READ IT RECURSIVELY AND THEN I WILL PROVIDE THERE ITEMS TO YOU. 
    # print(items)
    for i, items in enumerate(items):                        # NOTE :- a list has index and values so if we want to save indices alg and values alg so we use enumerate function to run list. we can  run list thorugh enumerate function to store values and indices differently.  
        print(f"{i+1} : {items}")
def createfile():    # here we have opened and created and written in file.
    try:
        readfileandfolder() 
        name=input(" please tell your file name :- ")
        p=Path(name)  # NOTE :- HERE WE STORED WHOLE PATH IN 'p' variable. 
        if not p.exists() and p.is_file(): #NOTE :- if file doesn't exist already in the system then it will move to next line and whole new file will be created. p.is_file() ensures that p is the file. 
            #NOTE :- what happens in above line is that if p.exists() is true that files exists already in system then not will give false then else statement will ran and if p.exists() is false then not will turn it into true and it will run the next line with open statement which will create a new file. 
            #NOTE:- what not do is that it turns true into false and false into true. 
            with open(p,"w") as fs:
                data=input('what you want to write in this file :- ')
                fs.write(data)
            print(F"FILE CREATED SUCCESSFULLY !!")
        else:
            print("this file already exist")
    # NOTE :- IMPLEMETING EXCEPTION HANDLING IF THE USER GIVES GALAT FILE AND BECAUSE OF THIS BELOW PROGRAM STOPS.  
    except Exception as err:
        print(f"An error occurred as {err}") 
#NOTE :- WHAT ABOVE FUNCTIONS AND CODE LINES ARE DOING IS THAT THEY ARE CREATING A FILE AND ADDING SOME WRITTEN STUFF IN IT. 
def readfile():
    try:
        readfileandfolder()
        read=input("which file you want to read ? ")
        p=Path(read)                                           #NOTE :- HOW DOES IT WORK THE PATH IS THAT WE EITHER GIVE NAME IN PATH THEN WOH AGR EXIST KRTA HAIN TOH USKA PATH MIL JAYEGA AUR AGR NAHI KRTA HAIN TOH USKA PATH BN JAYEGA.
        if p.exists() and p.is_file():
            with open(p,"r") as fs:
                data=fs.read()
                print(data)
                print(" READ SUCCESSFULLY ! ")
        else:
            print(" the file doesn't exist  ")
    except Exception as err:
        print(f" an error occured as {err}")
    
    #NOTE :- ABOVE FUNCTION IS READING THE FILES. 
def updatefile():
    try:
        readfileandfolder()
        update=input(" tell which file you want to update")
        p=Path(update)
        if p.exists() and p.is_file():
            print(" press 1 for changing the name of your file")
            print("press 2 to overwrite the data of your file ")
            print("press 3 for appending some data into the file")
            res=int(input(" tell your response :- "))
            if res==1:
                name2=input(" tell your new  file name ? :- ")
                p2=Path(name2)
                p.rename(p2)
            if res==2:
                with open(p,'w') as fs:
                    data=input(" tell what you wanna write and this will overwrite the existing data in the file :- ")
                    fs.write(data)
            if res==3:
                with open(p,'a') as fs:
                    data=input(" tell what you wnat to append :- ")
                    fs.write(data)
    except Exception as err:
        print(f" an error occured as {err} ")
        
#NOTE :- here in above we are updating the file. we will ask the user three options when he has asked to update his file, (1) to change the name of the file. (2) to overwrite the already existing data in the chosen file. (3) to append some data into the file.
# NOTE :- HERE WE ARE ASKING USER WHAT OPERATIONS HE WANTS TO PERFORM. 

print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for deleting a file ")  

check = int(input("please tell your response :-  ")) # NOTE :- SAVING HIS RESPONSE IN check variable. 

#NOTE:- MAIN CODE BASE :- 
if check == 1:
    createfile()   # what we will do is that we are going towards the functional programming and for that we will use createfile() function, which is being declared above using def. 
if check==2:
    readfile()
if check==3: # NOTE :- HERE WE ASK THE USER FOR UPDATE AND WE GIVE HIM THREE OPTIONS :- (1) FILE NAME UPDATE  (2)  DATA OVERWRITE OF FILE. (3) APPEND THE DATA OF FILE.  
    updatefile()
    
# FILE HANDLING 

#NOTE :- Files :- any name with an extension is file.
# extension can be .py, .txt, .mp3 etc. and when we want to handle these files we will use file handling. 
# FILE HANDLING :- is basically handling files with extensions. 

#NOTE :- FILE HANDLING MEANS CREATING,READING,UPDATING,DELETING(CRUD) OPERATIONS THAT WE CAN PERFORM IN FILES. 
# WE HAVE TO USE open() function to open a file in python. 
# open() functions open a file for us. 
# you have to first give open() function a path. 
# p=open(r'C:\Users\Dell\Desktop\aiprojectinfo.txt')
# print(p.read())
# # p.close() #NOTE :- DO WORK ON THIS FILE. it will teach about encodings.  

# p=open(r'C:\Users\Dell\Desktop\file handling practice sample file.txt')
# print(p.read())
# NOTE :- ABOVE CODE IS SUCCESSFULL AND WE ARE READING THE FILE. 
# o=open(r'rough.py')
# print(o.read()) 
# NOTE :- the above code is giving error, cause first we just wrote the name of file not the location and the file doesn't exist in same folder or directory as this file. 
# import os 
# print(os.getcwd())
# q=open(r'filerough.py')
# print(q.read())

# NOTE :-  MODES OF OPENING :- 
#(1) 'r' :- Read(default) - file must exist.
#(2) 'w' :- Write-creates file or overwrites. 
#(3) 'a' :- Append - adds tgo end of the file. 
#(4) 'x' :- create-creates a new file,fails if it exists.

# NOTE :- CREATING A FILE :- 
s=open("superman.txt",'w') # 'r' is the default one. 
# when we run the above function superman.txt gets created in current workin directory(CWD) on its own. 
# to write in superman.txt:- 
s.write("Hello this is Himanshu and i am writing inside this file. and now what i am doing is that i am writing some text to see if write function can append some text at last of the line or it overwrites the existing line.") # what we are doing here is that we are writing some other lines in the already existing file which is opened already if we close this file and open it again and then write something the existing lines will be overwrriten, that's why we use 'a'. 
# s.append(" now i am using append function add some text inside the file at last. this is just testing phase text to see the working of the append function.") #NOTE :- THIS IS WRONG THEORY BY ME, .append() doesn't exist in file handling. so FCK THIS SHIT U WROTE. 
s.close() # used to close the file unless it will be opened always. 

# 'a' which is append here you can also create a new file using 'a'.
# 'x' is also used to create new file but you cannot create it or you can say it fails when the file is already is existing. 

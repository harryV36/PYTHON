#FINAL PRACTICE CHALLENGE BY GPT AFER LEARNING BASICS OF THE FILE HANDLING. 
a=open("employees.txt","w") # creating a new file using'a+' mode where we can append the data and also read it.  # use w instead of a+ cause it will then print previous outputs multiple whenver the file is called. #NOTE :- HERE WHAT I WROTE FIRST BEFORE CONSULTING WITH GPT IS THAT I WROTE :- a=open("employees.txt","a+") but he said to write w instead of a+ cause of the certain reasons mentioned earlier. 
a.write("Rahul\nPriya\nAmit\nNeha") # writing in the newly created file. # NOTE :- WHAT WE HAVE TO TAKE CARE IS THAT WE DO NOT USE .append() cause it is a list function not file handling function. and also write data into one string not into different strings. 
# NOTE :- JOB 1  IS DONE WHICH WAS TO CREATE A FILE AND ISNERT SOME DATA INTO IT. 
a=open("employees.txt","r")
data=a.readlines()
print(data)
# JOB 2 IS DONE WHICH WAS TO READ  THE WHOLE DATA/lines  INSIDE THE FILE AND return them as a  LIST USING readlines().
cleaned_data = []
for x in data:
    cleaned_data.append(x.strip())
print(cleaned_data,end="")

# print(len(cleaned_data[0])) # testing if there is space between strings or not. 

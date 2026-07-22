# learning difference between write and append function and 'a' and 'w'.
#NOTE:- testing phase :- creating a file at w mode and adding Hello in it. 
f=open("test.txt","w")
f.write("Hello")
f.close()

# NOTE:- second run where we will overwrite the test.txt.
f=open("test.txt","w")
f.write("python")
f.close()
#NOTE:- now what happened above is that when we opened the file second times with w. it empties the file and f.write("python"), overwrites the already written Hello in the file.
#NOTE :- now, suppose you want Hello to exist as well and don't want python to overwrite it, so what will we do is we use'a' append here. 
f=open("test.txt","a")
f.write("   langauge")
f.close()
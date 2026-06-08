#CONDITIONAL STATEMENT IN PYTHON :- where we have make decision on basis of some conditions, it allows decision making. 
# 3 types of conditional statements :- 
#(1) if :- executes if the condition is True.
#(2) if-else :- executes if True,another if false. 
#(3) if-elif-else :- checks the multiple conditions in sequence. 
# you can write conditions in else block. 

#a= 13
#if a > 21:
#     print("task A should be done") 
# else:
#     print("task B should be done ")
    # colon(:) is used here with conditional statements which gives us some blocks to write next line of code on and if we don't then it will give us the identation error. 

# money = int(input("pls provide me the money"))
# if money == 10:
#     print("i will buy the chocobar icecream")
# else: 
#     print("i will buy the mango dolly")
    
    
# cash=int(input("money given by father"))
# if cash == 10:
#     print("then i will buy one chips packet")
# elif cash > 10:
#     print("then i will buy two chips packet" )
    

# if-elif-else :-
#paisa = int(input(" paisa given by father for icecream :- "))
#if paisa==10:
    #print("i will buy chocobar")
#elif money==20:
    #print("i will buy mango vanilla")
#else:
    #print("i will buy the cone")

#code 2 :- 
note = int(input("note given"))
if note==10:
    print("buy the chcoc0bar")
elif note==20:
    print("buy the mango vanilla")
elif note == 30 or note == 40 or note==50:
    print("buy the cone")
else:
    print("you can buy whatever ice cream you want")
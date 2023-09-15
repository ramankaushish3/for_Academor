#rock paper scissor
import random
print("Enter 1 for Rock, 2 for Paper, 3 for scissor, else it will exit")
chance={1:"Rock",2:"Paper",3:"scissor"}
#print(chance[2])

while(True):
    user=int(input("Enter a choice : "))
    comp=random.randint(1,3)
    if(comp==1 and user==1):
        print("Computer chooses :",chance[comp]," and You chose : ",chance[user])
        print("You tied")
    elif(comp==1 and user==2):
        print("Computer chooses :",chance[comp]," and You chose : ",chance[user])
        print("You won")
    elif(comp==1 and user==1):
        print("Computer chooses :",chance[comp]," and You chose : ",chance[user])
        print("You loose")
    elif(comp==2 and user==2):
        print("Computer chooses :",chance[comp]," and You chose : ",chance[user])
        print("You tied")
    elif(comp==2 and user==3):
        print("Computer chooses :",chance[comp]," and You chose : ",chance[user])
        print("You won")
    elif(comp==2 and user==1):
        print("Computer chooses :",chance[comp]," and You chose : ",chance[user])
        print("You loose")
    elif(comp==3 and user==3):
        print("Computer chooses :",chance[comp]," and You chose : ",chance[user])
        print("You tied")
    elif(comp==3 and user==1):
        print("Computer chooses :",chance[comp]," and You chose : ",chance[user])
        print("You won")
    elif(comp==3 and user==2):
        print("Computer chooses :",chance[comp]," and You chose : ",chance[user])
        print("You loose")
    else:
        print("Game's Over...")
        break

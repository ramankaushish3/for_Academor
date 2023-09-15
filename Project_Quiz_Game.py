def check(guess,ans):
    global score
    at=1
    st = True
    while(st):
        if(guess.lower()==ans.lower()):
            st=False
            score=score+2
            at+=1
            print("Correct Answer")
        else:
            if(at<2):
                print("InCorrect answer, Try Again")
                guess = input("Enter answer again : ")
                at+=1
            elif(at==2):
                print("Correct answer is : ",ans)
                score=score-1
                st=False
print("There are 5 questions Compulsory to Answer\n 2 marks for Correct & -1 for incorrect")
print("You get 2 chances per question.")
score=0
a1  = input("What's world's tallest building : ")
check(a1,"burj khalifa")
a2  = input("What's world's highest peak : ")
check(a2,"mount everest")
a3  = input("What's boiling point of water in degree celcius : ")
check(a3,"100")
a4  = input("Who's CEO of Tesla : ")
check(a4,"elon musk")
a5  = input("What's world's longest river : ")
check(a5,"nile")
print("Score is : ",score)

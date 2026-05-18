print("Welcome to the CUET Quiz")
print("Please choose your subject")
print("1.Chemistry")
print("2.Physics")
score=0
while True:
    ch=int(input("Enter the choice:"))
    if ch==1:
        print("Here is a question for you")
        print("Q. What is the atomic number of Nickel")
        ans=int(input("Enter your answer:"))
        answer=28
        if ans==answer:
            print("You are correct")
            score+=1
        else:
            print("Try again")
    elif ch==2:
        print("Here is a question for you:")
        print("Q. If a 2A current flows from a circuit in 2 mins, what is the overall charge in coloumbs?")
        ans=int(input("Enter your answer"))
        answer=240
        if ans==answer:
            print("Correct answer")
            score+=1
        else:
            print("oh no, try again")
    print("do you wish to continue (y/n)")
    cho=input("Enter y/n")
    if cho=="n":
        break
else:
    print("invalid choice")
print("The final score is",score)
    
        

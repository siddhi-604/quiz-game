print("Welcome to my quiz!")

playing = input("Do you want to play? \n")


if playing.lower() != "yes":
    quit()

print("okay! let's play!\n ")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit" :
    print('correct!\n')
    score +=1
else:
    print('Incorrect!\n')

answer = input("What does ALU stand for? ")
if answer.lower() == "arithmetic logic unit" :
    print('correct!\n')
    score +=1
else:
    print('Incorrect!\n')

answer = input("What does DBMS stand for? ")
if answer.lower() == "database management system" :
    print('correct!\n')
    score +=1
else:
    print('Incorrect!\n')

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory" :
    print('correct!\n')
    score +=1
else:
    print('Incorrect!\n')


print("You got " +str(score) + " questions correct")
print("you got" + " " +str((score/4)*100) + "%.")

print("well done :)")
 

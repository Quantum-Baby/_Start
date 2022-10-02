# Rock/Stone, paper and scissor



def game_Win(computer, you) :
    # If two values are equals clear tie
    if computer == you : 
        return None
        
    # Check all posibilities when computer choose r
    elif computer == "r":
        if you == "p":
            return True
        elif you == "s":
            return False

    # Check all posibilities when computer choose p
    elif computer == "p":
        if you == "s":
            return True
        elif you == "r":
            return False

    # Check all posibilities when computer choose s
    elif computer == "s":
        if you == "r":
            return True
        elif you == "p":
            return False        
    
import random
print("Computer turn : Rock(r) Paper(p) or Scissor(s) ? ")
randNo = random.randint(1,3)

if randNo == 1:
    computer = "r"
elif randNo == 2:
    computer = "p"
elif randNo == 3:
    computer = "s"

you = input("Your turn : Rock(r) Paper(p) or Scissor(s) ? ")

a = game_Win(computer, you)

print(f"computer choose {computer}")
print(f"you choose {you}")

if a == None:
    print("The Game is tie !")
elif a:
    print("You Win @$!$@")
else :
    print("You Loose ! ")
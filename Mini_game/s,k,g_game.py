import random

option = ["s" , "k", "q"]
print("s = [سنگ] . k = [کاغذ] . q = [قیچی]")
pc_score = 0
user_score = 0
raund = True

while raund:
    user_choice = input("\n Enter your choice : ")
    pc_choice = random.choice(option)
    print(f"pc chioce is : {pc_choice}")

    if user_choice == pc_choice :
        print(" mosavi ")
    elif user_choice == "s":
        if pc_choice == "k":
            pc_score +=1 #pc win
        elif pc_choice == "q":
            user_score +=1 # user win
    elif user_choice == "k":
        if pc_choice == "s":
            user_score +=1 #user win
        elif pc_choice == "q":
           pc_score +=1 #pc win
    elif user_choice == "q":
        if pc_choice == "s":
            pc_score +=1 #pc win
        elif pc_choice == "k":
            user_score +=1 #user win
    print(f"your score =\t{user_score} \n and pc score =\t{pc_score}")
    if user_score == 3 or pc_score == 3:
        break

if user_score == 3:
    print(" you win the game! ")
else:
    print(" pc win the game! ")


# Guesses the number game

low = int(input("Enter the lower number :"))
high = int(input("Enter the higher number :"))


import random
r = random.randint(low , high)

guess_cunt = 5

while guess_cunt > 0:
    try:
        new_gusses = int(input(f'remaid gusses {guess_cunt} Enter your next gusses : \n'))

        if new_gusses > r:
            print("your gusses is higher than number ")
        
        elif new_gusses < r:
            print("Your gusses is lower than number")

        elif new_gusses == r:
            print("Great !!! you gusses the number!!!!!!!")
            break

        guess_cunt -=1

    except:
        print("Pleas enter the iniger valiue")
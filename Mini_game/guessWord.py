# guess the word game

word_list = ["ali" , "hossein", "hassan" , "word", "win" , "guess" ,
             "mohammad", "reza", "tehran" , " gorgan", "iran" , "dada"]

import random

r = random.choice(word_list)

guess_count = len(r)
guest_list = ["-"] * len(r)


while guess_count > 0:
    user_guess = input("Enter your char to guesses : \n").lower()

    if user_guess.isalpha():
        if user_guess in r:
            if user_guess in guest_list:
                print("You guessed befor enter a new guess")
            else:
                for indx,char in enumerate(r):
                    if char == user_guess:
                        guest_list[indx] = user_guess
                print(f'perfect => {" ".join(guest_list)}')

                if "-" not in guest_list:
                    print("won !!!")
                    break
                
        else:
            guess_count -=1
            print(f'wrong! => your guess count is {guess_count}')

    else:
        print("Entar the char valius")
    
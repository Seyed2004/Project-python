import random
import time

def question_genaror():
    number_1 = random.randint(1, 10)
    number_2 = random.randint(1, 10)

    operator_list = ["+", "-", "*"]
    selected_operator = random.choice(operator_list)

    print(f"{number_1} {selected_operator} {number_2} = ?")

    if selected_operator == "+":
        return number_1 + number_2
    elif selected_operator == "-":
        return number_1 - number_2
    else:
        return number_1 * number_2

question_number_limit = 5
question_number = 0
score = 0
time_limit = 10

while question_number < question_number_limit:
    # step 1) generate the random quastion (DONE)
    result = str(question_genaror())
    start_time = time.time()

    #step 2)get user answer (DONE)
    user_answer = input("Enter your answer :\n")
    end_time = time.time()
    time_dif = end_time - start_time

    #step 3)check the answer and time (DONE)

    if time_limit > time_dif:
        if result == user_answer:
            score +=1
            print(f"Perfect!!! \t your score is: {score} \n and your time is {time_dif}")
        else:
            print("Your answer is false")
        
    else:
        print("you are so late !!!")
    question_number +=1

print(f"your score is {score} for {question_number_limit}")
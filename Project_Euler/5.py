#$2520$ is the smallest number that can be divided by each of the numbers from $1$ to $10$ without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from  $1$ to $20$?

def Check_number(number):
    for i in range(2,21):
        if number % i !=0:
            return False
    return True

number = 2520
while True:
    if Check_number(number):
        break
    number +=1

print(number)

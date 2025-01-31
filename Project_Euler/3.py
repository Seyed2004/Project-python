#The prime factors of  13195 are 5,7,13,29.
#What is the largest prime factor of the number 600851475143

c = 2 # c is coefficient
number = 600851475143

while c * c < number:
    while number % c == 0:
        number = number / c
    c = c + 1

print(number) 
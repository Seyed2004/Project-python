# The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385.
#The square of the sum of the first ten natural numbers is,(1 + 2 + ... + 10)^2 = 55^2 = 3025.
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is $3025 - 385 = 2640$.
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


list_1 = []
list_2 = []

for i in range(1, 101):
    i = i **2
    list_1.append(i)


for i in range(1, 101):
    list_2.append(i)

number_1 = sum(list_1)
number_2 = sum(list_2) ** 2

print(f"number one is {number_1} and number two is {number_2}")
print(f"difference between the sum of the squares of the first one hundred natural numbers and the square of the sum is {number_2 - number_1}")

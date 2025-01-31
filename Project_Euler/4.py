#A palindromic number reads the same both ways.
#The largest palindrome made from the product of two $2$-digit numbers is $9009 = 91 \times 99$.
#Find the largest palindrome made from the product of two $3$-digit numbers.


list =[]
i = 999

def Check(number):
    string_n = str(number)
    rivers_n = string_n[::-1]
    if rivers_n == string_n:
        list.append(number)

while i > 99:
    for j in range(100, 999):
        Check(i * j)
    i = i-1

print(f"Max palindromic number is {max(list)} and sum of the number in list is {sum(list)}")
print(list)
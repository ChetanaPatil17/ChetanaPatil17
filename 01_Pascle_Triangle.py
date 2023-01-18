
from math import factorial


n = int(input("Enter the Number : "))
#n=5
for i in range(0, n):
    for j in range(n-i+1):
        print(end=" ")

    for j in range(i+1):

        # nCr = n!/r! * (n - r)!

        print(factorial(i)//(factorial(j) * factorial(i-j)), end=" ")
    print()
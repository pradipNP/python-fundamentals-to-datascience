# Implementing using Loop
limit = int(input("Enter the limit: "))
a=0
b=1

for i in range(limit):
    print(a, end=" ")
    a, b = b, a+b

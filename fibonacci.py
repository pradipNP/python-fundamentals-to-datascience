num = int(input("Enter the nth number: "))
a = 0
b = 1
count = 0

if num <= 0:
    print("Enter the positive number.")

elif num ==1:
    print("Fibonacci upto ",num,  "is :")
    print(a)

else:
    while(count<num):
        print(a, end = " ")
        #Update values
        # a = b
        # b =  a + b
       
        a, b = b, a + b
        
        # c = a+b
        # a=b
        # b=c
    
        count += 1


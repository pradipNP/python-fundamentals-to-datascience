count = 0
with open("numbers.txt", "r") as f:
    data = f.read()
    print(data)

    nums = data.split(",")
    for val in nums:
        if(int(val)%2 == 0):
            print(val)
            count += 1

print("Total no. of evens are:", count)
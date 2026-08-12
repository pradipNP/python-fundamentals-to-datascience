with open("file.txt", "r") as f:
    data = f.read()
    print(data)

#Note: if we are using "with" syntax, we don't have to use close()
#       because "with" syntax automatically closes.
with open("new.txt", "r") as f:
    data = f.read()
    print(data)

    if(data.find("learning") != -1):
        print("Found")
    else:
        print("Not found")
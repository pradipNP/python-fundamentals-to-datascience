with open("numbers.txt", "r") as f:
    data = f.read()
    print("File content:", data)

    num = ""
    even_numbers = []

    for i in range(len(data)):
        if data[i] == ",":
            # Convert accumulated num to integer and check if it's even
            if int(num) % 2 == 0:
                even_numbers.append(int(num))
            num = ""  # Reset num for the next number
        else:
            num += data[i]  # Accumulate characters for the current number

    # Process the last number (if any)
    if num:
        if int(num) % 2 == 0:
            even_numbers.append(int(num))

    print("Even numbers:", even_numbers)

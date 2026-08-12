student = {
    "name": "Pradeep",
    "age": 21,
    "marks" : {
        "Physics" : 98.4,
        "Chemistry" : 92.5,
        "Math" : 89
    }
}

#1 Dict.Keys()
print(student.keys()) 
print(list(student.keys())) #print in list
print(len(list(student.keys()))) #total numbers of keys

#2 Dict.Values()
print(student.values())
print(list(student.values())) #print in list
print(len(student.values()))

#3 Dict.items()  --returns all (keys and values) pairs as tuples
print(student.items())
print(list(student.items())) #print in list
print(len(student.items()))

#4 Dict.get("keys")  --returns the key according to value
print(student.get("name"))
print(student["name"]) #print the same value
#Then why we use both techniques to print the values?
#The main difference between the two is that the get() method returns None if the key is not
#print(student.get["name2"]) #It will print none because no key is there in the dictionary
# print(student["name2"]) will give the error


#5 Dict.update(newDict) --inserts the specified items to the dictionary
print(student.update({"name": "Aman"}))
print(student.update({"country": "Nepal"}))
print(student)
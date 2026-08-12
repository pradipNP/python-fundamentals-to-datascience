"""Dictionaries are used to store data values in key:value pairs.
They are unordered, mutable(changeable) and don't allow duplicate keys."""

info = {
    "name" : "Pradeep",
    "age" :  21,
    "roll" : 22054325,
    "marks" : 85.6,
}
print(info)
print("accessing the values with the help of keys from dictionary")
print("My name is:",info["name"])
print("age is:",info["age"])
print("roll no is:", info["roll"])
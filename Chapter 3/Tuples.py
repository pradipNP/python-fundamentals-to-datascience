# Tuples are the in-built data type that lets us create immutable sequences of values.

tup = (1,5,3,6,3,2,1)
print(tup)
print(tup[0])
print(tup[1:])

# tu[0] = 3  #TypeError: 'tuple' object does not support item assignment

tup1 = (1) #We must have to use at least one comma for assigning a tuple O/W it will behave a single intitialized element
print(tup1)
print(type(tup1))

tup2 = (1,) #This will behave as a tuple becz there is comma
print(tup2)
print(type(tup2))


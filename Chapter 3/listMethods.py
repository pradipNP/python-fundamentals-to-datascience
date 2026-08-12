list = [2,3,4,3,2,8,7,45]

#1. REVERSE
print("Original list: ", list)
list.reverse() #used for reverse of the list values
print("Reversed list: ", list)

#2. INSERT
list.insert(0,2) #inserting new value at index 0
print(list)

#3. APPEND
list.append(44) #append method is used for adding elements in the list at last position
#list.append(44,1) #this is error because it will take exactly one argument at once
list.append(1)
print(list)

#4. SORT
list.sort() #sort method is used for sorting the list in ascending order
print(list)
list.sort(reverse = True) #this is used for descending order
print(list)

#5. REMOVE
list.remove(2) #remove method is used for removing the first occurrence of the specified value
print(list)

#6. POP
list.pop(1)
#list.pop(1,0) #error because it will pop exactly single index's value of the list
print(list)
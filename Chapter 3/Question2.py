#WAP to check if a list contains a palindrome of elements.(Hint: use copy() method)
list = [1,2,3,2,1]
copied_list = list.copy()
print(list)

copied_list.reverse()
if (copied_list == list):
 print("It is palindrome")
else:
 print("It is not palindrome")

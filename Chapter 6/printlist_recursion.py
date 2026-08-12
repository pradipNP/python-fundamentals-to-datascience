#Write a recursive function to print all elements in a list.

def print_list(list,idx):
    if(idx == len(list)):
        return
    
    print(list[idx])
    print_list(list, idx+1)

name = ["Pk", "sk", "pl", "mk", "jd"]

print_list(name, 0)

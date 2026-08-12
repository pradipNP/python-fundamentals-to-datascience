name = ["Pradeep", "Aman", "Anuj", "pk"]
cities = ["Lumbini", "Bhw", "Butwal", "Patia", "Delhi"]

def print_len(list):
    print(len(list))

print_len(name)
print_len(cities)

def print_list(list):
    for item in list:
        print(item, end=(" "))

print_list(name)
print()
print_list(cities)
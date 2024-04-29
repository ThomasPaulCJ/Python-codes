# Create an empty dictionary
my_dict = {}

# Get user input for dictionary values
my_dict['name'] = input("Enter name: ")
my_dict['age'] = int(input("Enter age: "))
my_dict['city'] = input("Enter city: ")

# Traverse keys
for key in my_dict.keys():
    print(key)

# Traverse values
for value in my_dict.values():
    print(value)

# Traverse both keys and values
for key, value in my_dict.items():
    print(key, value)
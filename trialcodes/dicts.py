curly_dict = {"name": "Finn",
              "age": 22,
              "is_registered": False,
              "hobbies": ["reading", "gaming", "gym"],
              "cities": ("Shymkent", "Astana")
              }
print(type(curly_dict))  # <class 'dict'>
print(curly_dict)

functional_dict = dict([("name", "Finn"), 
                        ("age", 22), 
                        ("is_registered", False), 
                        ("hobbies", ["reading", "gaming", "gym"]), 
                        ("cities", ("Shymkent", "Astana"))])
print(type(functional_dict))  # <class 'dict'>
print(functional_dict)

# Accessing dictionary values
print(curly_dict["name"])  # Finn

try:
    print(curly_dict["surname"])  # Raises KeyError, because "surname" key does not exist
except KeyError as e:
    print(f"Error: {e}")

# Updating dictionary values
curly_dict["age"] = 21

# if there is no such key, it will be created
curly_dict["surname"] = "Arth"

print(curly_dict)

# Deleting a key-value pair
del curly_dict["surname"]

try:
    del curly_dict["somekey"]
except KeyError as e:
    print(f"Error: {e}")

print(curly_dict)

# Iterating over a dictionary
print("\n")
for key, value in curly_dict.items():
    print((key, value))

print("\n")
for pair in curly_dict.items():
    print(pair)

# Membership check
if "name" in curly_dict and curly_dict["name"]:
    print(f"Name exists and is not empty: {curly_dict['name']}")

# Dictionary manipulations
print(curly_dict.get("name"))
print(curly_dict.get("surname", "Joq esnarse"))  # Returns "Not found" if key does not exist

print("\n")
for pair in curly_dict.items():
    print(pair)

print("\n")
for key in curly_dict.keys():
    print(key)

print("\n")
for value in curly_dict.values():
    print(value)


curly_dict2 = {"surname": "Arth",
               "age": 22,
               "cities": ("Shymkent", "Astana", "Almaty")
               }

curly_dict.update(curly_dict2)
print("\nUpdated dictionary:")
print(curly_dict)

my_dictionary={
    "you":"18",
    "He":"18",
    "Area":"Burnsroad"
}

# keys gives keys in list form
print("\nkeys are...:",my_dictionary.keys())

# value gives values in list form
print("\nvalues...:", my_dictionary.values())

# items gives whole dict in tuple form
print("\n Items...:", my_dictionary.items())

# get 
print("\n get...:", my_dictionary.get("Area"))

# update adds the value of given key from new given
new_dict={"area":"Landhi"}
my_dictionary.update(new_dict)
print("\n New",my_dictionary)

# pop  delets the last key and value 
print(my_dictionary.pop("area"))
print("\n pop...:",my_dictionary)

# clear gives empty dictionary
my_dictionary.clear()
print("\n clear...:",my_dictionary)


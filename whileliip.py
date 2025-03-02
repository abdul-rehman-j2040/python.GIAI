password: str = "python123"
user_input: str=""

print("user_input != password is:",user_input != password)
while user_input != password:
   print("Incorrect Password")
   user_input = input("Enter password Please...!")

#                                                                        Methods Of Python In String

print("\n\t\t\t AT G-HOUSE")
print("\n====================================================================================================")

name = "you are so good,but you need to work over self more so you well be undefeatable"

# print(type(name))

print(name)

# it will capitalize the first alphabet of the placed string in the variable
print(name.capitalize())

# it will count the occurance of given word and tell the numbers of time it occured in the variable
print(name.count("you"))

# it will count the characters inside the variable along the space 
print(len(name))

# it find the index of first occurance of the given data in variable 
print(name.find("so"))

# it find the index of the given data in the variable
print(name.index("so"))

# it replaces the old value with the new 
print(name.replace("need","have"))

# it converts the whole string in the capitalize form 
print(name.upper())

print("\n==============================================================================================")

# ==========================================================================================================================

print("\n\t\t\t __________AT HOME__________")

"""
  Upper_Case_method:
  {Ye Method (Built-In function) Diye gaye String data ko
   start se end tak CAPITAL Letters me convert kardeta he}

"""
print("\n 1.Upper case Example")
str_1:str="Mohammad Yaseen"
print(str_1.upper())

"""
  Lower_method:
  {Ye Method (Built-In function) Diye gaye String data ko
   START SE END TAK "small" LETTERS ME CONVERT KARDETA HE}

"""
print("\n 2 .lower() Case Example")
str_2:str="Mohammad Yaseen"
print(str_2.lower())

"""
  strip_method:
  {Ye Method (Built-In function) Diye gaye String data ke 
  aage ya piche mojood extra space ko khatam kardeta he}

"""
print("\n 3 .strip() Example")
str_3 = " Mohammad-Yaseen "
print(str_3.strip())

"""
  rstrip_method:
  {Ye Method (Built-In function) Diye gaye String data ke last me 
  mojood sirf denote kiye gaye data/alphabet/character ko hi hata ta he}

"""

print("\n 4. rstrip('c') Example")
str_4 = "Mohammad-Yaseen_"
print(str_4.rstrip("_"))

"""
  replace_method:
  {Ye Method (Built-In function) Diye gaye String data me pichle 
   mention kiye gaye data ko  next mention kiye gaye data se 
   replace kardeta he}

"""
print("\n 5 .replace('old','new')<<<<..Example ")
str_5 = "Mohammad-Yaseen"
print(str_5.replace("Yaseen","Ahmed"))

"""
  split_method:
  {Ye Method (Built-In function) Diye gaye String data ko
  seperate karke python list ki tarha pest karta he}

"""

print("\n 6 .split_method('kfe','ghw')<<<..Example")
str_6 = "Mohammad-Yaseen Mohammad-Ahmed"
print(str_6.split(" "))

"""
  capitalize_Method:
  {Ye Method (Built-In function) Diye gaye String data ke 
  first alphabet ko capital kardeta he}

"""
print("\n 7 .Capitalize()<<..Example")
str_7 = "mohammad-Yaseen"
print(str_7.capitalize())

"""
  center_Method:
  {Ye Method (Built-In function) Diye gaye String data ko 
  bataye gaye tabs "50" tak aage gap de dega }

"""
print("\n 8 .center(1....00)")
str_8 = "Mohammad-Yaseen"
print(str_8.center(50))

"""
  center_Method.b.:
  {Ye Method (Built-In function) Diye gaye String data ko 
  bataye gaye count tabs "50" tak aage "," ya "." de dega }

"""
print("\n 9 .center(1....00)")
str_9 = "Mohammad-Yaseen"
print(str_9.center(50,"."))

"""
  count_Method:
  {Ye Method (Built-In function) Diye gaye String data me 
  har ek alphabet/word kitni bat arha he wi count kar ke
  bata ta he}

"""
print("\n 10 .count('a...,name,...z')")
str_10 = """ Mohammad-Yaseen , Mohammad-Ahmed and Mohammad-Ibrahiem Are younger 
             Brothers. """
print(str_10.count("Mohammad"))

"""
  index_Method:
  {Ye Method (Built-In function) Diye gaye String data ke 
  index number ka batata he}

"""
print("\n 11 .index('any thing')")
str_a = "Mohammad-Yaseen is a good boy."
print(f"{str_a.index('boy')} <<<..ye boy ka index no. he")

"""
  find_Method:
  {Ye Method (Built-In function) Diye gaye String data me 
  se mention kiye hue word ko 1st time me(occurance) find kar ke
  uska index bata ta he}

"""
print("\n 12 .find('anything')")
str_b = "My younger brothers 'Mohammad-Yaseen' and 'Mohammad-Ahmed' are good brothers "
print(f'{str_b.find("brothers")}<<<..ye brothers ka first occur pe index no. he')

"""
  end_Method:
  {Ye Method (Built-In function) Diye gaye String data me se
  mention kiye hue word ko chek karta he ke string us hi word se
  end ho rahi he ya nahi}

"""
print("\n 13 .endswith(last_word)")
str_c = "Mohammad-Yaseen is a good boy..!!!"
print(str_c)
print(str_c.endswith("!"))
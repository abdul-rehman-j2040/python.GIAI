#_______________________________________________________________________________LIST-METHODS_________________________________________________________________________________

# print("\n\t\t\t\t AT G-HOUSE")
# print("\n-----------------------------------------------------------------------------------------------")

# my_list = ["A B C D E F G H"]

# print("\n 1",my_list)

# # append it add ant given in last
# my_list.append("we")
# print("\n 2",my_list)

# # insert
# my_list.insert(1,'lol')
# print("\n 3",my_list)

# # reverse
# my_list.reverse()
# print("\n 4",my_list)

# # remove it removes the last item of list
# # my_list.remove("A")
# # print("\n 5",my_list)


# # pop
# print("\n 6", my_list.pop(2))

# # sort it 
# my_list.sort()
# print(my_list)


# # extend
# new_faculty = [" more ",4 ,5 ,6]
# print("\n 7 old",my_list)
# my_list.extend(new_faculty)
# print("\n 8 new",my_list)

# ==========================================================================================================================================================
print("\n\t\t\t '--------------------AT HOME--------------------'")

num = [1,2,3,4,5,6,7,8,9]
alphabets = ["Red","Blue","Green","Indigo","Orange","Voilet","Green","Orange"]

'''
sort()_method:
ye python ka built-in function he jo k list me mojood data ko 
alphabatically orderd vise ya phir numerically orders vise 
sort(tarteeb) se rakhta he 
ye list variable ke sath hi likha jata he but list variable
alag se baad me print karwaya jata he

'''

print("\n 1 .sort() ")
alphabets.sort()
print(alphabets)

num.sort()
print(num)

print("\n 2 .sort(reverse=True)")

alphabets.sort(reverse=True)
print(alphabets)

num.sort(reverse=True)
print(num)

'''
reverse()_method:
ye python ka built-in function he jo k list me mojood data ko 
list ke order se reverse(ulta) order deta he
ye bhi variable ke sath hi likha jata he but print just variable kia jata he

'''

print("\n 2 .reverse()")

num.reverse()
print(f"\n{num}")

alphabets.reverse()
print(f"\n{alphabets}")

'''
copy()_method:
ye python ka built-in function he jo k list me mojood data ki
copy return karta he
ye bhi variable ke sath hi likha jata he but print just variable kia jata he

'''
newlist = alphabets.copy()
print(f"\n 'OLD LIST___'{alphabets}")
print(f"\n'NEW COPY LIST___'{newlist}")

'''
count()_method:
ye python ka built-in function he jo k list me mojood data itrms ki
occurance ko count karta he or count value return deta he
ye print timt pe variable ke sath likha jata he

'''
print(f"\n 3 .count()")
print(f"\n{alphabets.count("Green")} 'Green' ki occurance ke no.")

# try:
#   num = int(input( "Enter a number :"))
#   print(num)

#   for a in range(1,11):
#         print(f"{num} X {a} = {num*a}")


# except Exception as error:
#     print(error)

# num1 = 10
# num2 = 0

# try:

#   div = num1/num2
#   print(div)

# except ZeroDivisionError:
#   print("number zero is not divisible")


# num1 = [1,2,3]
# num2 = 0

# try:

#   div = num1[2]
#   print(div)

# except ZeroDivisionError:
#   print("number zero is not divisible")

# except IndexError:
#   print("Please Provide Valid Index")

# numx = 5
# print("num x is outside the function", numx)

# def hello():
#     numx = 10
#     print("numx inside func",numx)
#     print("hello how r u")
# hello()
# print("num x is outside the function", numx)

"""
   jab ek comment inside function hoga or
   function k baad first line me hoga tab hi ye ek 'doc string' goga
   or isse print karane ka  tarika he:
   print statement function ka name then DOT. phir '2 X UNDERSCORE __' then 'doc' prir againdouble underscore __
   print(functionkaname.__doc__)

"""
# numx = 5
# print("num x is outside the function", numx)
# '''use two parameters and return their sum'''

# def hello(num1:int,num2:int) -> int:
#     return num1 + num2
# result = hello(3,8)
# print(hello.__doc__)
# print(result)

# ============================================
# 1. String 
# 2. Number / Integer
# 3. Boolean
# 4. List
# 5. Touple
# 6. Dictionary
# 7. Set
# ============================================

# names_list=["Azlan", "Ali","Umer","Azlan","Umer"]
# names_set={"Bilal","Azlan","Abdullah","Bilal","Umer","Azlan"}

# print(f"{names_list} name_list ")
# print(f"{names_set} name_set")


# names_list=["Azlan", "Ali","Umer","Azlan","Umer"]
# names_set={"Bilal","Azlan","Abdullah","Bilal","Umer","Azlan"}

# print(f"{names_list[0]} name_list ")

# # 1. it will give error coxz set do not have indexes 
#   2. and set is muteable
#   3. set gives only unique value, it gives any value just 1 time wether it is repeating
#   4. set is unoderd
# print(f"{names_set[0]} name_set")

'''
names_set={"Bilal","Azlan","Abdullah","Bilal","Umer","Azlan"}
print(names_set)

names_set.remove("Abdullah")

print(f"{names_set} updated")
 '''


# something else (5.) union
num_1 = {1,2,3}
num_2 = {4,5,6}
result = num_1.union(num_2)
print("result>>>>",result)

print(type(num_1))

# 1. note on notebook >>> 2.learnn abt colab >>> 3. learn abt github
num1=int(input("Enter 1st Number: "))
num2=int(input("Enter 2nd number: "))

def add():
  return num1 + num2
sum = add()
print(f"The Sum of {num1}, and {num2}, is: {sum}")

def minus():
  return num1 - num2
sub = minus()
print(f"The Subtraction of {num1}, and {num2}, is: {sub}")

def mul():
  return num1 * num2
multiply = mul()
print(f"The Multiplication of {num1}, and {num2}, is: {multiply}")

def divis():
  return num1 / num2
divide = divis()
print(f"The Division of {num1}, and {num2}, is: {divide}")
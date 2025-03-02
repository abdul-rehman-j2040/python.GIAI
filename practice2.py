def calculator():


    num1=int(input("Enter 1st Number: "))
    num2=int(input("Enter 2nd number: "))
    operator=input("Enter the Oprator '+','-','X' or'/'")

    # 1st function
    if operator == "+":
  
       sum = num1 + num2
       print(f"The Sum of {num1} and {num2} is : {sum}")

    # 2nd function
    elif operator == "-":

      sub = num1 - num2
      print(f"The Subtraction of {num1} and {num2} is: {sub}")

    # 3rd function
    elif operator == "X":
  
      multiply = num1 * num2
      print(f"The Multiplication of {num1} and {num2} is: {multiply}")


    # 4th function 
    elif operator == "/":
  
      divide = num1 / num2
      print(f"The Division of {num1}, and {num2}, is: {divide}")

    else:
     print("error")

calculator()   
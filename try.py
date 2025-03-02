def calculator():

   while True:    

    num1=int(input("Enter 1st Number: "))
    num2=int(input("Enter 2nd number: "))
    operator = input("Enter the Oprator '+','-','X' or'/'")

    match operator:
    # 1st function
        case _ if operator == "+" :
          sum = num1 + num2
          print(f"The Sum of {num1} and {num2} is : {sum}")
          print("\nprogram will continue executing again and again untill last operator")

    # 2nd function
        case _ if operator == "-":
          sub = num1 - num2
          print(f"The Subtraction of {num1} and {num2} is: {sub}")
          print("\nprogram will continue executing again and again untill last operator")

    # 3rd function
        case _ if operator == "X":
          multiply = num1 * num2
          print(f"The Multiplication of {num1} and {num2} is: {multiply}")
          print("\nprogram will continue executing again and again untill last operator")


    # 4th function 
        case _ if operator == "/":
          divide = num1 / num2
          print(f"The Division of {num1}, and {num2}, is: {divide}")
          print("\nProgram is completed")
          break
        case _ :
          print("error")

calculator()   
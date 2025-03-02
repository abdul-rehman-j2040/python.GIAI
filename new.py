import os

a_1= str(input(f"\n\t\tEnter your Name :"))
print(f"\n\t\twelcome {a_1}")

p_1 = str(input(f"Enter Your OTP please :"))

if p_1 == "123":

    a = int(input(f"Enter the number for running Table : "))
    print(f"The table is for number{a} : ")
    for i in range(1,16):

        def table():
            return a*i
        result = table()
        
        print(f"{a} X {i} = {result}")
            
    input("\n\t Press Enter for Next Program...")  # User ko prompt dene ke liye
    os.system('cls' if os.name == 'nt' else 'clear')  # Screen clear

else:
    print("Un Expected Error")

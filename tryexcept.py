name_a:str=(input("Enter your Name please..."))

match name_a:

    case _ if name_a == "Hamza":
        print("Hello Hamza nice to meet you")
        age:int=(input("PLEASE.. Enter Your Age, to know are you Eligible for dricinf or not: "))

        
        try:
            if age < 19:
                print("Sorry But you are 'NOT' Eligible")
            else:
              print("Yes you are Eligible for Driving")

        except SyntaxError as error:
            print      
    case _ if name_a == "Abdullah":
        print ("Assalam-O-Alaikum Abdullah Bhai")
        ans=int(input("You can Type Answer your Salam"))
        print("Jazakallah-Khair")
    case _ :
        
        print("I Do not know About you,Sorry We Could not Work Anymore...")

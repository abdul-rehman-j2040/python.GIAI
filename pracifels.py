# Writing A program to calculate the percentage by using if else function 

# printing total marks
Total_Marks=500
print("Total Matks:",Total_Marks)

# Taking Input Marks for each subject
Eng=int(input("Enter your marks for English: "))
Comp:int=(input("Enter your marks for Computer:"))
Maths:int=(input("Enter your marks for Maths:"))
Isl:int=(input("Enter your marks for Islamiyat:"))
Phy:int=(input("Enter your marks for physics:"))
Urdu:int=(input("Enter your marks for Urdu:"))


OB_Marks=(int(Eng) + int(Maths) + int(Comp) + int(Isl) + int(Phy) + int(Urdu))
print("Your Obtaine Marks Are:",OB_Marks)

percentage:int=((OB_Marks / Total_Marks)*100)
print("Your Percentage is:",percentage,"%")

if percentage >= 90 :
    print("Congratulations....🎉🎊✨ You've Achived 'A1_Grade'")

elif percentage >= 70 and percentage <= 89:
    print("Congratulations...✨ You've Achived 'A_Grade'")

elif percentage >= 60 and percentage <= 69:
    print("Congrats.🎆 You've Achived  B_Grade") 

elif percentage >=50 and percentage <= 59:
    print("Congrats.. You've Achived C_grade")

elif percentage >= 40 and percentage <= 49:
    print("You've Gained 'D_Grade' ")

else:
    print("You're Fail..")


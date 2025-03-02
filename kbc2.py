question1 = ['''The first Question is for 'Rs:10,000'
             'What is the 'Date' of PAKISTAN RESOLUTION...?''',
             "Option (A): 23rd March", "Option (B): 14th August",
             "Option (C): 3rd June", "Option (D): 5th February"]

print(f"\t\t\t\n{question1[0]}\n\t{question1[1]} \t\t{question1[2]} \n\t{question1[3]} \t\t{question1[4]}")
ans_1 = input(f"Enter Your Answer here  in form of A,B,C,D:")

if ans_1 == "A":
    print("Congratulations You answer is CORRECT")
else:
    print("sorry Bot your answer is WRONG")
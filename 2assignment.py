a=input("Enter your name:")
maths=float(input("Enter the marks of Maths:"))
science=float(input("Enter the marks of Science:"))
english=float(input("Enter the marks of English:"))
nepali=float(input("Enter the marks of Nepali:"))
total=float(maths+science+english+nepali)
percentage=(total/4)
print("YOU HAVE SECURED:",percentage,"%")
if percentage>=80:
    print(" YOUR GRADE IS A+")
    print("OUTSTANDING. KEEP IT UP.")
elif percentage>=70:
    print("YOUR GRADE IS A")
    print("VERY GOOD. YOU CAN DO BETTER.")
elif percentage>=60:
    print("YOUR GRADE IS A-")
    print("GOOD. YOU CAN DO BETTER.")
elif percentage>=50:
    print("YOUR GRADE IS B")
    print("YOU CAN DO BETTER.")
elif percentage>=40:
    print("YOUR GRADE IS B-")
    print("YOU CAN DO BETTER.")
else:
    print("YOUR ARE FAIL")
    print("TRY HARDER NEXT TIME.")
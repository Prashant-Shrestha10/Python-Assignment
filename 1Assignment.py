a = int(input("Enter a number: "))
b= int(input("Enter another number: "))
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
i=int(input("Enter your choice: "))
if i == 1:
 print("The sum is: ",a+b)
elif i==2:
 print("The difference is: ",a-b)
elif i==3:
 print("The product is: ",a*b)
elif i==4:
 print("The quotient is: ",a/b)
else:
 print("invalid input")

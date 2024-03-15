import random
random_number = random.randint(1, 100)
A= (random_number)
print(A)
COUNT=0
while True:
 B= int(input("ENTER Guess NUMBER:"))
 COUNT+=1
 if (B<1 or B>100):
  print("Not in range")
 elif (A+10<B):
  print("Too high")
 elif (A-10>B):
  print("Too low")
 else:
    print("Near")
 if(B==A):
  print("Correct")
  break
print("You guess right answer in",COUNT,"attempts")
 

 
  


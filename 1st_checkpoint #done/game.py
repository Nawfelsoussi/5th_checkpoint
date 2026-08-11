import random

print("WELCOME TO THE GUESS THE NUMBER GAME ; Choose the range for X ")
print("Lower bound is always 0")
a=0
while True :
   b= int(input("Enter the upper bound . It must be a multiple of 10 and should be written as 1 with extra zeros: "))
   q = int(len(str(b)))
   n = int(str(b).count("0"))
   first_digit= int(str(b)[0])
   if b%10 == 0 and first_digit==1 and  q-1 == n:
      break
   else: 
      print("That's not a multiple of 10 OR it's not written as it should be . Please try again ") 
   



print( f"The range for X is :  {a} <= X <= {b} " )
z= int(random.randint (a,b))
chances= int(2**int(len(str(b))))
chances2= int(2**int(len(str(b))))
print(f"- GUESS MY NUMBER - you have only  {chances} chances")
p=0

while a<=z<=b :
    chances = chances
    y= int(input("Input your guess: "))
    if y<z : 
        chances -=1
        print("Your guess is too low")
        p+=1
        print(f"{chances} chances are left !")
        breakpoint
        
        if p== chances2:
           print("No more chances.")
           print("My guess was : " +  str(z))
           break
    elif z<y :
        chances -=1
        print("Your guess is too high")
        p+=1 
        print(f"{chances} chances are left !")
        breakpoint
        
        if p==chances2:
         print("No more chances. ")
        
         print("My guess was : " + str(z))
         break
      
    elif z==y :
        print("Your guess is right !!")
        break

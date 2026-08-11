#Write a Python program that multiplies all the items in a list.
#Sample list= [2, 3, 6]
#Result = 36
print("Choose a value for each variable in [a, b, c]. The output is a * b * c . (Real numbers only)")
a= float(input("a = "))
b= float(input("b = "))
c= float(input("c = "))
mylist = [a,b,c]
result= 1
for num in mylist :
    result = result*num
print(f"a*b*c = {result}")
#DONE
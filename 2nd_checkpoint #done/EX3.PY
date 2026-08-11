#Write a Python program that combines two dictionaries by adding values for common keys.
#d1 = {'a': 100, 'b': 200, 'c':300}
#d2 = {'a': 300, 'b': 200, 'd':400}
#Expected result: {'a': 400, 'b': 400, 'd': 400, 'c': 300}
print("Input the values for each variable 'a'; 'b' ; 'c' : ")
a = float(input("input a1's value : "))
b = float(input("input b1's value : "))
c = float(input("input c1's value : "))
d1 = {
     

   
    'a': a,
    'b': b,
    'c':c
}
print(f"You have this dictionary {d1} . For  the 2nd dictionary please re-input the values for each variable 'a'; 'b' ; 'd' : ")
a = float(input("input a2's value : "))
b = float(input("input b2's value : "))
d = float(input("input d's value : "))
d2 = {
    'a': a,
    'b': b,
    'd':d
}
d3 = d1 | d2
z=0
for i in d1.keys()  :
    j=i

    for x in d2.keys():
        y=x
    
        if i==x:
         i = d1.get(i)
         x = d2.get(x)
         z = i + x
         d3.update({ j :z , y:z })
       
        
print(d3)
#DONE
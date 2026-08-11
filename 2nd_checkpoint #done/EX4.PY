#With a given integral number n, write a program to generate a dictionary that contains 
# (i, i*i) so that is an integral number between 1 and n (both included). Then the program should print the dictionary.
#  Suppose the following input is supplied to the program: 8.
#  Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
n = int(input("Please input the integral number n , knowing that the integral is starting from 1 to n : "))

d1 = {}
for i in range (1,n+1) :
    d1.update({ i : i**2})
print(d1)
#DONE



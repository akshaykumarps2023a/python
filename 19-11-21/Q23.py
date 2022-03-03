n = int(input("enter a number"))
n2 = int(input("enter 2 ed number"))
n3 = int(input('enter 3 ed number'))
if n>n2 and n>n3:
    print("largest number is :",n)
elif n2>n and n2>n3:
    print("largest number is :",n2)
else:
    print("larger number is",n3)

def fac(c):
    i=1
    for i in range(i,c+1):
        if(c%i==0):
            print("te factors are:",i)

n=int(input("enter the number:"))
fac(n)
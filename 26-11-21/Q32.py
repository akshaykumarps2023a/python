n=int(input("enter the limit"))
a=0
b=1
s=0
print(a)
print(b)
for i in range(1,n):
    s=a+b
    a=b
    b=s
    print(s)


#print(a+b+s)
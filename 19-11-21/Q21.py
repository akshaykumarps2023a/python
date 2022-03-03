n=input("enter a string")
ch=n[0]
n=n.replace(ch,"$")
n=ch+n[1:]
print(n)
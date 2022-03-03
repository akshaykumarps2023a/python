str=input("enter the strings:")
s=str.split(" ")
f=s[0]
s=s[-1]
ff=f[0]
sf=s[0]
temp=ff
ff=sf
sf=temp
print(ff+f[1:]+" "+sf+s[1:])
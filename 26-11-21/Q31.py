list=[]
s=0
n=int(input("enter the limit:"))
print("enter the value:")
for i in range(n):
    ele=int(input())
    list.append(ele)
    s=s+ele
print("sum",s)
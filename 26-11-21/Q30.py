list=[]
n=int(input("enter the limit:"))
print("enter the value:")
for i in range(n):
    ele=int(input())
    if(ele%2!=0):
        list.append(ele)

print(list)

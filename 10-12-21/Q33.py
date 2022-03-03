def fact(n):
    s = 1
    for i in range(1,n+1):
        s = s * i
    print("the factorial of ", n, "is:", s)

num = int(input("enter a number:"))
fact(num)




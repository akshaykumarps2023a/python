def long(a):
   f = len(a[0])
   temp =a[0]

   for i in a:
      if(len(i) > f):

         f = len(i)
         temp = i

   print("The word with the longest length is:", temp, " and length is ",f)
n=int(input("enter the number of words:"))
l=[]
for i in range(n):
    l=input()
#l= ["three", "Jane", "quick", "lesson", 'London', 'newyork']
print("The list is :")
print(l)
long(l)
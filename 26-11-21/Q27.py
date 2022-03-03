set1={"red","yellow","green"}
set2={'red','white','black'}
#print("the 1st set:",set1.pop(0))
element = next(iter(set1))
print("the 1nd set:",element)
print("the 2nd set:",set2)
s=set1.difference(set2)
print(s)
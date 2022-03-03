from graphics import rectangle,circle
from graphics.threeDgraphics import cuboid,sphere
l=int(input("enter the length:"))
b=int(input("enter the breadth:"))
rectangle.rectarea(l,b)
rectangle.perimetre(l,b)
r=int(input("enter the radius"))
circle.cirarea(r)
l=int(input("enter the length:"))
b=int(input("enter the breadth:"))
h=int(input("enter the height:"))
cuboid.cubarea(l,b,h)

r=int(input("enter the radius"))
sphere.sparea(r)
sphere.spperimetre(r)


import abc
import math

class Shape():
   def perimeter(self):
      pass
class Rectangle(Shape):
   def __init__(self, x,y):
      self.l = x
      self.b=y
   def perimeter(self):
      return (2*(self.l+self.b))
  
class Circle(Shape):
   def __init__(self, x):
      self.r = x
   def perimeter(self):
      return (2*math.pi*self.r)
class Square(Shape):
   def __init__(self, x):
      self.l = x
   def perimeter(self):
      return (4*self.l)
choice = 0
while (choice != ''):
    print("\n\nList of Shapes: \n 1.Circle\n 2.Rectangle \n 3.Square \n 4.Quit")
    choice = int(input("Enter Your choice :"))
    if choice == 1 :
        radius = float(input("Enter the radius of the Circle:"))
        obj = Circle(radius)
        print("\nThe perimeter is ",obj.perimeter())
    elif choice == 2:
        length = float(input("Enter the length of the Rectangle:"))
        breadth = float(input("Enter the breadth of the Rectangle:"))
        obj = Rectangle(length,breadth)
        print("\nThe perimeter is ",obj.perimeter())
    elif choice == 3:
        side = float(input("Enter the side of the Square:"))
        obj = Square(side)
        print("\nThe perimeter is ",obj.perimeter())
    elif choice == 4:
        break
    else:
        print ("Please Enter a valid key")
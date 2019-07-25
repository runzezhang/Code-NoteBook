# Description
# Implement a Rectangle class which include the following attributes and methods:

# Two public attributes width and height.
# A constructor which expects two parameters width and height of type int.
# A method getArea which would calculate the size of the rectangle and return.

# Description
# Implement a Rectangle class which include the following attributes and methods:

# Two public attributes width and height.
# A constructor which expects two parameters width and height of type int.
# A method getArea which would calculate the size of the rectangle and return.
# Have you met this question in a real interview?  
# Example
# Example1:
# Java:
#     Rectangle rec = new Rectangle(3, 4);
#     rec.getArea(); // should get 12，3*4=12

# Python:
#     rec = Rectangle(3, 4)
#     rec.getArea()

# Example2:
# Java:
#     Rectangle rec = new Rectangle(4, 4);
#     rec.getArea(); // should get 16，4*4=16

# Python:
#     rec = Rectangle(4, 4)
#     rec.getArea()

class Rectangle:

    '''
     * Define a constructor which expects two parameters width and height here.
    '''
    # write your code here
    def __init__(self, width, height):
     self.height = height
     self.width = width
    
    '''
     * Define a public method `getArea` which can calculate the area of the
     * rectangle and return.
    '''
    # write your code here
    def getArea(self):
        return self.width*self.height
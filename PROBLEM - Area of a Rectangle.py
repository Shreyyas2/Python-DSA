'''Problem Description: You are given the length and breadth of a rectangle. Your task is to compute and return the area of the rectangle.

Formula: To calculate the area of a rectangle:

Area=length×breadth


Input: Two floating-point numbers, length and breadth, representing the dimensions of the rectangle.


Output: A floating-point number representing the area of the rectangle.'''

length=float(input('enter Length:'))
breadth=float(input('enter Breadth:'))

def area_of_rectangle(length, breadth):
    """
    Function to calculate the area of a rectangle.
    
    Parameters:
    length (float): The length of the rectangle.
    breadth (float): The breadth of the rectangle.
    
    Returns:
    float: The area of the rectangle.
    """
    return length*breadth

print(area_of_rectangle(length, breadth))



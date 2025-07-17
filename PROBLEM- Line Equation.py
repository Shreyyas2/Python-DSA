'''Problem Description:
You are given the slope m and the y-intercept b of a line, along with a value x. Your task is to calculate and return the value of y using the equation of a line in slope-intercept form:

y=mx+b


Input: Three floating-point numbers: slope, intercept, and x.


Output: A floating-point number representing the value of yyy corresponding to the given xxx.'''

slope=float(input('enter slope:'))
intercept=float(input('enter intercept:'))
x=float(input('enter :'))

def calculate_y(slope, intercept, x):
    """
    Function to calculate the value of y using the slope-intercept form of a line.
    
    Parameters:
    slope (float): The slope of the line.
    intercept (float): The y-intercept of the line.
    x (float): The value of x for which y needs to be calculated.
    
    Returns:
    float: The calculated value of y.
    """
    m=slope
    b=intercept
    return m*x+b

print(calculate_y(slope, intercept, x))

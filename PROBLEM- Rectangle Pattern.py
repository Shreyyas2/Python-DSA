'''Rectangle Pattern

Problem Description: You are given two integers, n and m. Your task is to return a rectangle pattern of '*', where n represents the number of rows (length) and m represents the number of columns (breadth).

Input: Two integers n and m, where 1 <= n, m <= 100.

Output: A list of strings where each string represents a row of the rectangle pattern.

Example:

Input: n = 4, m = 5
Output: ['*****', '*****', '*****', '*****']
 
Input: n = 3, m = 2
Output: ['**', '**', '**']'''
n=int(input('enter any number:'))
m=int(input('enter any number:'))
def generate_rectangle(n, m):
    rectangle = []
    
    # Loop through each row from 1 to n
    for _ in range(n):
        # Create a row with m stars
        row = '*' * m
        # Add the row to the rectangle list
        rectangle.append(row)
    
    # Return the list of rectangle rows
    return rectangle

s=generate_rectangle(n, m)
print(s)

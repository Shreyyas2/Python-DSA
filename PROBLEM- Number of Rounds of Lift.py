'''Problem Description: You are given n, the total number of people, and capacity, the maximum number of people the lift can carry at a time. All people want to go from the ground floor to the top floor. Your task is to calculate the number of rounds the lift has to make to transport all the people to the top floor.


Input: Two integers, n and capacity, where n is the total number of people, and capacity is the maximum number of people the lift can carry in one round.


Output: An integer representing the number of rounds the lift needs to cover to transport all people to the top floor.'''

n=float(input('enter total number of people:'))
capacity=float(input('enter lift capacity:'))

def calculate_lift_rounds(n, capacity):
    """
    Function to calculate the number of rounds the lift needs to cover.
    
    Parameters:
    n (int): Total number of people.
    capacity (int): Maximum number of people the lift can carry in one round.
    
    Returns:
    int: The number of rounds required to transport all people to the top floor.
    """
    rounds=n//capacity
    if n%capacity !=0:
        return rounds+1
    else:
        return rounds
print(calculate_lift_rounds(n, capacity))




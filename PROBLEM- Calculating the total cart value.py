#Calculating the total cart value

def calc_total_cost(cart):
    total_cost=0
    for item in cart:
        total_cost+=item['price']*item['quantity']
    return total_cost

cart=[
    {'name':'apple','price':40,'quantity':4},
    {'name':'banana','price':30,'quantity':3},
    {'name':'kiwi','price':20,'quantity':2}
    ]

total_cost=calc_total_cost(cart)
print(total_cost)

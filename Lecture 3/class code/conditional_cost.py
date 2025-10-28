#input
quantity = int(input('What is the shipping quantity? '))
#process
total_cost= 1000*quantity

#conditional steps
if quantity <200 and quantity >= 100:
    total_cost=total_cost*(1-0.1)

if quantity >=200:
    total_cost = total_cost*(1-0.2)

#output
print('The total cost is ' +str(total_cost)+'.')

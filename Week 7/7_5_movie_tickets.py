customer_ages = []
order_active = True

while order_active:
    customer_age = input("\nEnter the customer's age: ")
    customer_ages.append(customer_age)

    repeat = input("Order more tickets? (y/n) ")
    if repeat == 'n':
        order_active = False

count = 0
total_cost = 0
for customer_age in customer_ages:
    customer_age = int(customer_age)
    count += 1
    cost = 0

    if (customer_age < 3):
        cost = 0
    elif (customer_age >= 3 and customer_age <=12):
        cost = 10
    else:
        cost = 15
    
    total_cost += cost

print(f"\nYour total cost is ${total_cost} for {count} tickets.")

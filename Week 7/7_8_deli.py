sandwiches = []
finished_sandwiches = []
orders_exist = True

while orders_exist:
    sandwich = input("\nWhat kind of sandwich would you like? ")
    sandwiches.append(sandwich)

    repeat = input("Order more sandwiches? (y/n) ")
    if repeat == 'n':
        orders_exist = False

for sandwich in sandwiches:
    print(f"Your {sandwich} sandwich is ready!")
    finished_sandwiches.append(sandwich)

print(f"\nSandwiches made:")
for finished_sandwich in finished_sandwiches:
    print(f"{finished_sandwich}")
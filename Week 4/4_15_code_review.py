guests = ['eddie van halen', 'david lee roth', 'albert einstein',
          'jerry garcia', 'neil armstrong', 'ozzy osbourne', 'stan lee',
          'rick flair']
print(f"The first three items in the list are {guests[0:3]}")
print(f"Three items from the middle of the list are {guests[3:6]}")
print(f"The last three items in the list are {guests[5:]}")

print("")

spotted_animals = ['dalmation', 'leopard', 'giraffe', 'jaguar']
for spotted_animal in spotted_animals:
    print(f"A {spotted_animal} has spots.")
print("All of these animals have spots.")

print("")

my_foods = ['pizza', 'steak', 'hamburgers', 'sushi', 'spaghetti',
            'philly cheesesteaks', 'lasagna']
my_foods.append('chocolate')
my_foods.append('ice cream')
for food in my_foods:
    print(f"One of my favorite foods is {food}.")
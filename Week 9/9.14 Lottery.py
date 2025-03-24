import random

def generate_random():
    list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20,'v', 'w', 'x', 'y', 'z']
    random_items = random.sample(list, 4)
    for item in random_items:
        print(f"{item} ")

print(f"""Any ticket matching these 4 numbers or letters wins a prize!:\n
{generate_random()}""")
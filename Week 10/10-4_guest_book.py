prompt = "\nWhat is your name?"
prompt += "\nEnter 'q' at any time to quit.\n"

active = True
while active:
    name = input(prompt)
    
    if name.lower() == 'q':
        active = False
    else:
        print(f"Hello, {name}! Thanks for visiting.")
        with open("guest_book.txt", "a") as file:
            file.write(f"{name} visited.\n")
print("Enter two numbers and I'll add them together.")
print("Enter 'q' at any time to quit.\n")

active = True
while active:
    first_input = input("First number: ")
    if first_input.lower() == 'q':
        active = False

    second_input = input("Second number: ")
    if second_input.lower() == 'q':
        active = False

    try:
        result = int(first_input) + int(second_input)
    except ValueError:
        print("One or both of your inputs were not numbers. Please try again.\n")
    else:
        print(f"The sum is: {result}\n")
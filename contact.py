def print_menu():
    print('1. Print Phone Numbers')
    print('2. Add a Phone Number')
    print('3. Remove a Phone Number')
    print('4. Lookup a Phone Number')
    print('5. Quit')
    print()

numbers = {}
menu_choice = 0
print_menu()


def list_contacts():
    print("Telephone Numbers:")
    for x in numbers.keys():
        print("Name: ", x, "\tNumber:", numbers[x])
    print()


def search():
    global name
    print("Lookup Number")
    name = input("Name: ")
    if name in numbers:
        print("The number is", numbers[name])
    else:
        print(name, "was not found")


def remove_contact():
    global name
    print("Remove Name and Number")
    name = input("Name: ")
    if name in numbers:
        del numbers[name]
    else:
        print(name, "was not found")


def add_contact():
    global name
    print("Add Name and Number")
    name = input("Name: ")
    phone = input("Number: ")
    numbers[name] = phone


while menu_choice != 5:
    menu_choice = int(input("Type in a number (1-5): "))
    if menu_choice == 1:
        list_contacts()
    elif menu_choice == 2:
        add_contact()
    elif menu_choice == 3:
        remove_contact()
    elif menu_choice == 4:
        search()
    elif menu_choice != 5:
        print_menu()
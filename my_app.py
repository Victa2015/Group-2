from my_contact import Contact


def print_menu():
    menu = ""

    menu += '1. Print Phone Numbers\n'
    menu += '2. Add a Phone Number\n'
    menu += '3. Remove a Phone Number\n'
    menu += '4. Lookup a Phone Number\n'
    menu += '5. Quit\n'
    menu += "\n"

    return menu


menu_choice = 0
print_menu()

my_app = Contact()

while menu_choice != 5:
    menu_choice = int(input("Type in a number (1-5): "))
    if menu_choice == 1:
        my_app.list()
    elif menu_choice == 2:
        my_app.create()
    elif menu_choice == 3:
        my_app.remove_contact()
    elif menu_choice == 4:
        my_app.search()
    elif menu_choice != 5:
        print_menu()

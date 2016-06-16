from my_contact import Contact


def print_menu():
    print('1. Print Phone Numbers')
    print('2. Add a Phone Number')
    print('3. Remove a Phone Number')
    print('4. Lookup a Phone Number')
    print('5. Quit')
    print()

menu_choice = 0
print_menu()

my_app = Contact()

while menu_choice != 5:
    menu_choice = int(input("Type in a number (1-5): "))
    if menu_choice == 1:
        my_app.list()
        #print_menu()
    elif menu_choice == 2:
        my_app.create()
        #print_menu()
    #elif menu_choice == 3:
        #remove_contact()
    #elif menu_choice == 4:
        #search()
    elif menu_choice != 5:
        print_menu()

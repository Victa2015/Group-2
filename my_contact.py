class Contact(object):
    numbers = {}

    def __init__(self):
        pass

    def list(self):
        print("Telephone Numbers:")
        for x in self.numbers.keys():
            print("Name: ", x, "\tNumber:", self.numbers[x])
        print()

    def create(self):
        print("Add Name and Number")
        name = input("Name: ")
        phone = input("Number: ")
        self.numbers[name] = phone

    def print_menu(self):
        print('1. Print Phone Numbers')
        print('2. Add a Phone Number')
        print('3. Remove a Phone Number')
        print('4. Lookup a Phone Number')
        print('5. Quit')
        print()
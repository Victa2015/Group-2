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
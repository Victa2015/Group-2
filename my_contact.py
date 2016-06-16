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
		
	def remove_contact(self):
		culprit = self.search()
		if culprit in self.numbers:
		 	del self.numbers[culprit]
			return "{0} was deleted".format(culprit)
		else:
			return "{0} could not be deleted".format(culprit)		
		
		
	def search(self):
		name = input("Name:")
		if name in self.numbers:
			return self.numbers[name]
		else:
			return "{0} was not found \n".format(name)
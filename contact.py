class Contact(object):
    name = ""
    phone_number = ""
    note_id = 0
    contacts_file = open("contacts_list.txt", "")

    def __init__(self):
        pass

    def create(self, name, phone_number):
        if name is None
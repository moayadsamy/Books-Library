import random

class Client:
    no_of_client = 0
    def __init__(self, id, full_name, age, id_no, phone_number):
        self.id = id
        self.full_name = full_name
        self.age = age
        self.id_no = id_no
        self.phone_number = phone_number
        Client.no_of_client += 1

    def get_id(self):
        return self.id

    def set_id(self , id):
        self.id = id

    def get_full_name(self):
        return self.full_name

    def set_full_name(self, full_name):
        self.full_name = full_name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_id_no(self):
        return self.id_no

    def set_id_no(self, id_no):
        self.id_no = id_no

    def get_phone_number(self):
        return self.phone_number

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number


class librarian(Client):
    def __init__(self, id, full_name, age, id_no, phone_number, salary = 0.0):
        super().__init__(id, full_name, age, id_no, phone_number)
        self.salary = salary
    def get_saLary(self):
        return self.salary
    def set_salary(self, salary):
        self.salary = salary
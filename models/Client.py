class Client:
    no_of_client = 0
    def __init__(self, full_name="none", age=0, id_no=0, phone_number=55):
        self.full_name = full_name
        self.age = age
        self.id_no = id_no
        self.phone_number = phone_number
        Client.no_of_client += 1

    def desk(self):
        print(f"name {self.full_name} and his age {self.age}")

Client1 = Client("moayad", "20")
Client1.desk()

Client1 = Client("moayad", "20")
Client1.desk()

Client1 = Client("moayad", "20")
Client1.desk()

Client1 = Client("moayad", "20")
Client1.desk()


    # def get_id(self):
    #     return self.id
    #
    # def set_id(self , id):
    #     self.id = id
    #
    # def get_full_name(self):
    #     return self.full_name
    #
    # def set_full_name(self, full_name):
    #     self.full_name = full_name
    #
    # def get_age(self):
    #     return self.age
    #
    # def set_age(self, age):
    #     self.age = age
    #
    # def get_id_no(self):
    #     return self.id_no
    #
    # def set_id_no(self, id_no):
    #     self.id_no = id_no
    #
    # def get_phone_number(self):
    #     return self.phone_number
    #
    # def set_phone_number(self, phone_number):
    #     self.phone_number = phone_number
    #


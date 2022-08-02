import Client
class librarian:

    def __init__(self, salary = 0.0):

        self.salary = salary
    def get_saLary(self):
        return self.salary
    def set_salary(self, salary):
        self.salary = salary

    def sal(self):
        print(f"salary : {self.salary}")

fdf = librarian()
fdf.sal()
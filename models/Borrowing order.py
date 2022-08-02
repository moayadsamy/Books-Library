from datetime import date
class Borrowing:
    def __init__(self, start_data, end_data, book_id, client_id, status):
        self.start_data = date.today()
        self.end_data = date.today()
        self.book_id = book_id
        self.client_id = client_id
        self.status = status


    def bor(self):
        print(f"start date : {self.start_data} and end date : {self.end_data} id book : {self.book_id} client id : {self.client_id} status : {self.status}")

borr1 = Borrowing("", "", "1212", "4545", "active")
borr1.bor()
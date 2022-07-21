class Book:

    __id_book = 0

    def __init__(self, title, description, author, status):
        Book.__id_book +=1
        self.id = Book.__id_book
        self.title = title
        self.description = description
        self.author = author
        self.status = status


    def bob(self):
        print(f"his name : {self.title} "
              f"description : {self.description} "
              f"author : {self.author} "
              f"status : {self.status}")


book1 = Book("الخيميائي", "راعي يسرد قصته مع الكنز", "للكاتب باولو كويلو", "تحفيزي")
book1.bob()

book2 = Book("فن اللامبالاة", "تعليم اللامبالاة", "للكاتب مارك ", "تعليمي")
book2.bob()


book3 = Book("ثرثرة فوق النيل", "الكاتب يسرد قصته مع اصدقاءه فوق النيل", "للكاتب نجيب محفوظ", "سرد قصة")
book3.bob()


book4 = Book("الاب الغني والاب الفقير", "الكاتب يسرد قصة اباه الغني واباه الفقير", "للكاتب ربورت تي ", "تعليمي")
book4.bob()


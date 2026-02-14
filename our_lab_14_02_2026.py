def add_NewReader():
    reader_id = int(input("Введите id читателя:"))
    surname = str(input("Введите фамилию пользователя"))
    first_name = str(input("Введите имя пользователя"))
    patronymic = str(input("Введите отчество пользователя:"))
    yearbirth = 0
    valid = False
    while not valid:
        try:
            yearbirth = int(input("Введите год рождения:"))
            valid = True
        except ValueError:
            print("Вводите число!")
    adress = str(input("Введите адресс читателя:"))
    return(reader_id,surname,first_name,patronymic,yearbirth,adress)

def add_NewBook():
        book_id = int(input("Введите id книги:"))
        book_title = str(input("Введите название книги:"))
        book_author = str(input("Введите автора книги:"))
        valid_yearpublic = False
        book_yearpublic = 0
        while not valid_yearpublic:
            try:
                book_yearpublic = int(input("Введите год издания:"))
                valid_yearpublic = True
            except ValueError:
                print("Вводите число")
        valid_page = False
        book_page = 0
        while not valid_page:
            try:
                book_page = int(input("Введите год издания:"))
                valid_page = True
            except ValueError:
                print("Вводите число")
        book_movement = []
        return(book_id,book_title,book_author,book_yearpublic,book_page,book_movement)


class Reader:
    def __init__(self, reader_id, surname, first_name, patronymic, yearbirth : int, adress):  
        self.reader_id = reader_id
        self.surname = surname
        self.first_name = first_name
        self.patronymic = patronymic
        self.yearbirth = yearbirth
        self.adress = adress

class Book:
    def __init__(self, book_id, book_title, book_author, book_yearpublic : int, book_page : int, book_movement : list):
        self.book_id = book_id
        self.book_title = book_title
        self.book_author = book_author
        self.book_yearpublic = book_yearpublic
        self.book_page = book_page
        self.book_movement = book_movement

#     def Get_Book(self):
#         for id, bookinf in self.Info_bookById.items():
#             print(f"{id} - {bookinf[0:2]}")
#         BookId = int(input("Введите id интересующей вас книги:"))
#         if BookId in self.Info_bookById.keys():
#             Date = input("Введите дату выдачи в формате ДД.ММ.ГГГГ:")
#             self.book_dateGiven = datetime.strptime(Date, "%d.%m.%Y").date()
#             if  self.GivenBook[self.Info_bookById[BookId][0:1]] not in self.GivenBook.keys():
#                 self.GivenBook[self.Info_bookById[BookId][0:1]] = []
#             self.GivenBook[self.Info_bookById[BookId][0:1]].append(self.book_dateGiven)
#         else:
#             print("Вводите верное значение, существующие среди выданных вам ранее книг")



readers = []
books = []
a = Reader(*add_NewReader())
b = Book(*add_NewBook())
readers.append(a)
for i in readers:
    print(i.adress)
    
    



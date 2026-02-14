from datetime import datetime

readers = []
books = []

def add_NewReader():
    reader_id = int(input("Введите id читателя:"))
    surname = str(input("Введите фамилию пользователя:"))
    first_name = str(input("Введите имя пользователя:"))
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
                book_page = int(input("Введите кол-во страниц:"))
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

    def Get_Book(self):
        for reader in readers:
            print(f"id : {reader.reader_id} ФИО - {reader.surname} {reader.first_name} {reader.patronymic} ")
        init_reader_id = int(input("Введите id читателя:"))
        for reader in readers:
            if init_reader_id == reader.reader_id:
                for value in books:
                    print(f"id : {value.book_id} Книга :{value.book_title} Автор: {value.book_author} ")
                init_book_id = int(input("Введите id интересующей вас книги:"))
                for value in books:
                    if init_book_id == value.book_id:
                        date = input("Введите дату в формате ДД.ММ.ГГГГ: ")
                        dateGiven = datetime.strptime(date, "%d.%m.%Y").date()
                        value.book_movement.append(init_reader_id)
                        value.book_movement.append(dateGiven)
                    else:
                        print("Введённый id неверен!")
            else:
                print("Введите id снова, в прошлом была допущена ошибка")

    def Return_Book(self):
        pass  

    def getUnissuedBooks(self):
        for book in books:
            if len(book.book_movement) == 0:
                print(book.title)

    def getUnreturnedBooks(self):
        for book in books:
            if len(book.book_movement) % 2 == 0:
                for reader in readers:
                    for id in book.book_movement:
                        if id == reader.reader_id:
                            print(f"Книга {book.book_title} у {reader.surname} {reader.first_name} {reader.patronymic}")

    def getBookHistory(self):
        pass
    
                


# a = Reader(*add_NewReader())
b = Book(*add_NewBook())
# readers.append(a)
# books.append(b)
# b = Book(10,20,30,40,50,[1, 2342])
a = Reader(1,2,3,4,5,6)
readers.append(a)
books.append(b)
for i in books:
    print(i.getUnreturnedBooks())
for i in books:
    i.Get_Book()
    print(i.book_movement)
    
    



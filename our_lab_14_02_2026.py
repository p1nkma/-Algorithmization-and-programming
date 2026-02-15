from datetime import datetime

readers = {}
books = {}

def init_NewReader():
    a = Reader(*add_NewReader())
    readers[a.reader_id] = a

def init_NewBook():
    b = Book(*add_NewBook())
    books[b.book_id] = b

def add_NewReader():
    reader_id = int(input("Введите id читателя:"))
    surname = str(input("Введите фамилию пользователя:"))
    first_name = str(input("Введите имя пользователя:"))
    patronymic = str(input("Введите отчество пользователя:"))
    yearbirth = 0
    isValid_yearbirth = False
    while not isValid_yearbirth:
        try:
            yearbirth = int(input("Введите год рождения:"))
            isValid_yearbirth = True
        except ValueError:
            print("Вводите число!")
    adress = str(input("Введите адресс читателя:"))
    return(reader_id,surname,first_name,patronymic,yearbirth,adress)

def add_NewBook():
        book_id = int(input("Введите id книги:"))
        book_title = str(input("Введите название книги:"))
        book_author = str(input("Введите автора книги:"))
        isValid_yearpublic = False
        book_yearpublic = 0
        while not isValid_yearpublic:
            try:
                book_yearpublic = int(input("Введите год издания:"))
                isValid_yearpublic = True
            except ValueError:
                print("Вводите число")
        isValid_page = False
        book_page = 0
        while not isValid_page:
            try:
                book_page = int(input("Введите кол-во страниц:"))
                isValid_page = True
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

    def get_Book(self):
        for reader in readers.values():
            print(f"id : {reader.reader_id} ФИО - {reader.surname} {reader.first_name} {reader.patronymic} ")
        init_reader_id = int(input("Введите id читателя:"))
        if init_reader_id in readers.keys():
            for value in books.values():
                print(f"id : {value.book_id} Книга :{value.book_title} Автор: {value.book_author} ")
            init_book_id = int(input("Введите id интересующей вас книги:"))
            if init_book_id in books.keys():
                date = input("Введите дату в формате ДД.ММ.ГГГГ: ")
                dateGiven = datetime.strptime(date, "%d.%m.%Y").date()
                s = [init_reader_id, dateGiven]
                value.book_movement.append(s)
            else:
                    print("Введённый id неверен!")

    def return_Book(self):
        init_reader_id = int(input("Введите id читателя:"))
        for book in books.values():
            if book.book_movement != []:
                if len(book.book_movement[-1]) == 2: #проверяем что в списке который мы передавали book_movement всего 2 записи
                    if init_reader_id == book.book_movement[-1][0]:
                        date = input("Введите дату в формате ДД.ММ.ГГГГ: ")
                        dateTaken = datetime.strptime(date, "%d.%m.%Y").date()
                        if dateTaken >= book.book_movement[-1][1]:
                            book.book_movement[-1].append(dateTaken)
                            return
                        else:
                            print("Дата сдачи раньше выдачи!")
                            return

    def getUnissuedBooks(self):
        print("Книги, которые еще ни разу никто не брал:")
        for book in books.values():
            if len(book.book_movement) == 0:
                print(book.book_title)

    def getUnreturnedBooks(self):
        for book in books.values():
            if book.book_movement != []:
                if len(book.book_movement[-1]) == 2: #проверяем что в списке который мы передавали book_movement всего 2 записи => есть id читателя и дата выдачи
                    for reader in readers.values():
                        if reader.reader_id == book.book_movement[-1][0]:
                            print(f"Книга: {book.book_title} у {reader.surname}  {reader.first_name} {reader.patronymic}")
                    
    def getBookMovement(self):
        for book in books.values():
            if book.book_movement != []:
                for reader in readers.values():
                    for id in book.book_movement:
                        if id[0] == reader.reader_id:
                            print(*id[1:3],book.book_title,f"{reader.surname} {reader.first_name} {reader.patronymic}")
            else:
                print(f"{book.book_title} не была выдана ни разу!")

def show_menu():
    print("\n" + "="*30)
    print("БИБЛИОТЕКА")
    print("="*30)
    print("1. Добавить читателя")
    print("2. Добавить книгу") 
    print("3. Выдать книгу")
    print("4. Вернуть книгу")
    print("5. Невыданные книги")
    print("6. Невозвращённые книги")
    print("7. Движение книг")
    print("0. Выход")
    print("="*30)

def main():
    while True:
        show_menu()
        choice = int(input("Выбор: "))
        
        if choice == 1:
            init_NewReader()
        elif choice == 2:
            init_NewBook()
        elif choice == 3:
            if books: books[list(books)[0]].get_Book()
        elif choice == 4:
            if books: books[list(books)[0]].return_Book()
        elif choice == 5:
            if books: books[list(books)[0]].getUnissuedBooks()
        elif choice == 6:
            if books: books[list(books)[0]].getUnreturnedBooks()
        elif choice == 7:
            if books: books[list(books)[0]].getBookMovement()
        elif choice == 0:
            break
        
        input("\nEnter...")


b = Book(1, "Война и мир", "Лев Толстой", 1869, 1225, [])
books[1] = b
b = Book(2, "Преступление и наказание", "Фёдор Достоевский", 1866, 671, [])
books[2] = b
b = Book(3, "Мастер и Маргарита", "Михаил Булгаков", 1967, 480, [])
books[3] = b
b = Book(4, "1984", "Джордж Оруэлл", 1949, 326, [])
books[4] = b
b = Book(5, "Гарри Поттер и философский камень", "Дж. К. Роулинг", 1997, 223, [])
books[5] = b
b = Book(6, "Алхимик", "Пауло Коэльо", 1988, 208, [])
books[6] = b
b = Book(7, "Маленький принц", "Антуан де Сент-Экзюпери", 1943, 96, [])
books[7] = b
b = Book(8, "Шерлок Холмс: Этюд в багровых тонах", "Артур Конан Дойл", 1887, 240, [])
books[8] = b
b = Book(9, "451 градус по Фаренгейту", "Рэй Брэдбери", 1953, 194, [])
books[9] = b
b = Book(10, "Дюна", "Фрэнк Герберт", 1965, 412, [])
books[10] = b

a = Reader(1, "Иванов", "Иван", "Иванович", 1990, "Москва, ул. Ленина 10")
readers[1] = a
a =Reader(2, "Петрова", "Мария", "Петровна", 1985, "СПб, Невский пр. 25")
readers[2] = a
a = Reader(3, "Сидоров", "Алексей", "Сергеевич", 1995, "Екатеринбург, ул. Мира 5")
readers[3] = a
a = Reader(4, "Козлова", "Анна", "Викторовна", 1988, "Новосибирск, Красный пр. 12")
readers[4] = a
a = Reader(5, "Смирнов", "Дмитрий", "Александрович", 1992, "Казань, Баумана 8")
readers[5] = a
a = Reader(6, "Васильева", "Елена", "Николаевна", 1982, "Ростов-на-Дону, Большая Садовая 3")
readers[6] = a
a = Reader(7, "Морозов", "Сергей", "Владимирович", 1998, "Самара, ул. Кирова 15")
readers[7] = a
a = Reader(8, "Новикова", "Ольга", "Юрьевна", 1993, "Челябинск, Кирова 20")
readers[8] = a
a = Reader(9, "Федоров", "Михаил", "Петрович", 1980, "Омск, Ленина 45")
readers[9] = a
a = Reader(10, "Попова", "Татьяна", "Игоревна", 1987, "Красноярск, проспект Мира 7")
readers[10] = a

if __name__ == "__main__":
    main()

from datetime import datetime
class Reader:
    def __init__(self, reader_id : int, Surname : str, First_name : str, Patronymic : str, YearBitth : int, Adress : str):
        self.reader_id = reader_id
        self.Surname = Surname
        self.First_name = First_name
        self.Patronymic = Patronymic
        self.YearBirth = YearBitth
        self.Adress = Adress
        self.Info_userById = {}

    def add_NewReader(self):
        user_info = []

        self.reader_id = int(input("Введите id читателя:"))

        self.Surname = str(input("Введите фамилию пользователя"))
        user_info.append(self.Surname)

        self.First_name = str(input("Введите имя пользователя"))
        user_info.append(self.First_name)

        self.Patronymic = str(input("Введите отчество пользователя:"))
        user_info.append(self.Patronymic)

        while True:
            try:
                birth_info = int(input("Введите год своего рождения:"))
                if 1800 <= birth_info <= datetime.now().year:
                    self.YearBirth = birth_info
                    user_info.append(birth_info)
                    break
                else:
                    print(f"Введите дату рождения от 1800 до {datetime.now().year}")
            except ValueError:
                print("Вводить надо число!")
                
        self.Adress = str(input("Введите адресс читателя:"))
        user_info.append(self.Adress)

        self.Info_userById[self.reader_id] = user_info

class Books(Reader):
    def __init__(self, book_id, book_title, book_author, book_yearpublic : int, book_page : int, book_movement : list, book_dateGiven, book_dateTaken):
        super().__init__()
        self.book_id = book_id
        self.book_title = book_title
        self.book_author = book_author
        self.book_yearpublic = book_yearpublic
        self.book_page = book_page
        self.book_movement = book_movement
        self.book_dateGiven = book_dateGiven
        self.book_dateTaken = book_dateTaken
        self.Info_bookById = {}
        self.GivenBook = {}
        
    def add_NewBook(self):
        book_info = []
        self.book_id = int(input("Введите id книги:"))

        self.book_title = str(input("Введите название книги:"))

        self.book_author = str(input("Введите автора книги:"))

        # Проверка при добавлении даты издания
        while True:
            try:
                bookpublic_info = int(input("Введите год издания книги:"))
                if bookpublic_info > 0:
                    self.book_yearpublic = bookpublic_info
                    book_info.append(bookpublic_info)
                    break
                else:
                    print("Введите дату издания > 0")
            except ValueError:
                print("Вводить надо число!")   

        # Проверка при добавлении кол-ва страниц книги
        while True:
            try:
                bookpage_info = int(input("Введите кол-во страниц книги:"))
                if bookpage_info > 0:
                    self.book_page = bookpage_info
                    book_info.append(bookpage_info)
                    break
                else:
                    print("Введите дату издания > 0")
            except ValueError:
                print("Вводить надо число!")

        self.Info_bookById[self.book_id] = book_info

    def Get_Book(self):
        for id, bookinf in self.Info_bookById.items():
            print(f"{id} - {bookinf[0:2]}")
        BookId = int(input("Введите id интересующей вас книги:"))
        if BookId in self.Info_bookById.keys():
            Date = input("Введите дату выдачи в формате ДД.ММ.ГГГГ:")
            self.book_dateGiven = datetime.strptime(Date, "%d.%m.%Y").date()
            if  self.GivenBook[self.Info_bookById[BookId][0:1]] not in self.GivenBook.keys():
                self.GivenBook[self.Info_bookById[BookId][0:1]] = []
            self.GivenBook[self.Info_bookById[BookId][0:1]].append(self.book_dateGiven)
        else:
            print("Вводите верное значение, существующие среди выданных вам ранее книг")
                   
lib = Books()
lib.add_NewBook()
lib.Get_Book()

        
    



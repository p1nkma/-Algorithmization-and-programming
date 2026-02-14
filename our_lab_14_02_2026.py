class Reader:
    def __init__(self, reader_id : int, Surname : str, First_name : str, Patronymic : str, YearBitth : int, Adress : str):
        self.reader_id = reader_id
        self.Surname = Surname
        self.First_name = First_name
        self.Patronymic = Patronymic
        self.YearBirth = YearBitth
        self.Adress = Adress
        self.InfoById = {}

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
                if 1800 <= birth_info <= 2026:
                    self.YearBirth = birth_info
                    user_info.append(birth_info)
                    break
                else:
                    print("Введите дату рождения от 1800 до 2026")
            except ValueError:
                print("Вводить надо число!")
                
        self.Adress = str(input("Введите адресс читателя:"))
        user_info.append(self.Adress)

        self.InfoById[self.reader_id] = user_info

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
    
        
    



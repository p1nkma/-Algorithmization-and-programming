# Дана БД библиотеки, необходимо реализовать следующие функции: 
# - поиск книг по году издания
# - по автору
# - по названию
# - по количеству штук в библиотеке
# - по автору и названию 
# При заполнении БД контролировать ввод данных о годе выпуска книги и количестве книг билиотеки (имеется ввиду данной книги)

# Необходимо для каждой книги вести учёт выдачи и сдачи в библиотеку (с помощью даты)

# Необходимо для каждой книги выдавать количество оставшихся в библиотеке на текущий момент и количество книг несданных в библиотеку (будет выдаваться "Автор" "Название книги" "Сколько ениг не сдано")

# Будет меню, описание класса, в классе будет инициализатор (конструктор), в классе будут методы по обработке записей. Всё остальное на свое усмотрение
class Library:

    def __init__(self):
        self.Book = None
        self.Books = []
        self.Author = {}
        self.BookAuthor = None
        self.YearPublication = {}
        self.BookYearPublication = None
        self.Reminder = {}
        self.BookReminder = None
        self.BookCount = {}
        self.DateGiven = {}
        self.DateTaken = {}

    def AddBook(self): 
        self.Book = str(input("Введите название книги:"))
        print(f"Название {self.Book} успешно сохранено")

        self.BookAuthor = str(input("Введите автора:"))
        # Cделаем так, чтобы если добавляли книгу того-же автора значения не перезаписывались, а сохранялись в список
        if self.BookAuthor in self.Author.keys():
            self.Author[self.BookAuthor].append(self.Book)
        else:
            # Сохраним связку ключ - значение, автор - название книги, для будущей организации поиска
            self.Books.append(self.Book)
            self.Author[self.BookAuthor] = self.Books
        print(f"Автор {self.BookAuthor} книги {self.Book} успешно сохранён")

        while True:
            try:
                AddYearPublication = int(input("Введите год издания книги:"))
                if 1 <= AddYearPublication <= 2026:
                    self.BookYearPublication = AddYearPublication
                    if self.BookYearPublication not in self.YearPublication:
                        self.YearPublication[self.BookYearPublication] = []
                    self.YearPublication[self.BookYearPublication].append(self.Book) 
                    break
                else:
                    print("Год должен быть от 1 до 2026!")
            except ValueError:
               print("Введите корректное число")

        while True:
            try:
                AddCountBook = int(input("Количество: "))
                if AddCountBook > 0:
                    self.BookReminder = AddCountBook  
                    if self.Book in self.BookCount.keys():
                        self.BookCount[self.Book] += self.BookReminder
                    else:
                        self.BookCount[self.Book] = self.BookReminder
                    if self.BookReminder not in self.Reminder:  
                        self.Reminder[self.BookReminder] = []
                    self.Reminder[self.BookReminder].append(self.Book)
            
                    print(f" Книга {self.Book} (кол-во: {self.BookReminder})")
                    break
                else:
                    print("Количество > 0!")
            except ValueError:
                print("Число!")

    def FindBookByYearPublication(self):
        year = int(input("Год: "))
        if year in self.YearPublication.keys():
            print("Книги:", self.YearPublication[year])
        else:
            print("Книги не найдены")

    def FindBookByAuthor(self):
        author = input("Автор: ")
        if author in self.Author:
            print("Книги:", self.Author[author])
        else:
            print("Автор не найден")

    def FindBookByTitle(self):
        title = input("Название: ")
        for author_books in self.Author.values():  
            if title in author_books:              
                print(f"Найдена: {title}")
                return
        print("Книга не найдена")

    def FindBookByReminder(self):
        count = int(input("Количество: "))
        if count in self.Reminder.keys():
            print("Книги:", self.Reminder[count])
        else:
            print("Не найдено")
    
    def FindByAuthorTitle(self):
        author,title = map(str,input("Введите автора книги и её название через пробел!").split())
        if author not in self.Author:
            print("Книга не найдена")
        else:
            for bookauthor, booktitle in self.Author.items():
                if bookauthor == author:
                    for name in booktitle:
                        if name == title:
                            print(f"Найдена книга: {name} автора {bookauthor}")
                                   
    def GetAllBooks(self):
        print("\n Все книги:")
        for author, books in self.Author.items():
            for book in books:
                print(f" {book} ({author})")
    def GetBookRemind(self):
        for book,count in self.BookCount.items():
            print(f"Книга {book} в количестве {count} шт")

    def GetBook(self):
        book = str(input("Введите название желаемой книги:"))
        if book in self.BookCount.keys():
            pass
            
def InitNewObject():
        x = Library()
        x.AddBook()
        x.AddBook()
        x.GetBookRemind()
InitNewObject()



    










    
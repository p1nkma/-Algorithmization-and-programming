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

    def AddBook(self): 
        self.Book = str(input("Введите название книги:"))
        print(f"Название {self.Book} успешно сохранено")

        self.BookAuthor = str(input("Введите автора:"))
        # Cделаем так, чтобы если добавляли книгу того-же автора значения не перезаписывались, а сохранялись в список
        if self.BookAuthor in self.Author.keys():
            self.Author[self.BookAuthor].append(self.Book)
            self.Author[self.BookAuthor] = self.Books
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
                    print(f"Год издания {self.BookYearPublication} успешно сохранён")
                    self.YearPublication[self.Book] = self.BookYearPublication
                    break
                else:
                    print("Год должен быть от 1 до 2026!")
            except ValueError:
               print("Введите корректное число")

        while True:
            try:    
                AddCountBook = int(input("Введите добавляемое кол-во книг:"))
                if AddCountBook > 0:
                    self.BookReminder = AddCountBook
                    print(f"Книга {self.Book} - в количесвте {self.BookReminder} Год издания - {self.BookYearPublication} Автор - {self.BookAuthor} успешно сохранена")
                    self.Reminder[self.Book] = self.BookReminder
                    break
                else:
                    print("Число должно быть >0!!!")

            except ValueError:
                print("Вводите корректное кол-во книг, значение > 0")

            #Добавляем наши данные в общий словарь, в котором key - название книги, а value - список, которых хранит в себе другие значения

    def FindBookByYearPublication(self):
        InitYearPublication = int(input("Введите интересующий вас год издания книги:"))
        for key in self.YearPublication.keys():
            if key == InitYearPublication:
                print(self.YearPublication[key])
            else:
                print("К сожалению книг данного года издания не найдено, если пожелаете другую, вновь воспользуйтесь навигацией через меню")

    def FindBookByAuthor(self):
        InitAuthorBook = str(input("Введите интересующего вас автора:"))
        for key in self.Author.keys():
            if key == InitAuthorBook:
                print(self.Author[key])
            else:
                print("К сожалению книг данного автора не найдено, если пожелаете другую, вновь воспользуйтесь навигацией через меню")
            
    def FindBookByTitle(self):
        InitTitleBook = str(input("Введите название интересующей вас книги:"))
        for value in self.Author.values():
            if value == InitTitleBook:
                print(value)
            else:
                print("К сожалению книг по данному названию не найдено, если пожелаете найти другую, вновь воспользуйтесь навигацией через меню")

    def FindBookByReminder(self):
        InitReminderBook = int(input("Введите остаток интересующей вас книги:"))
        for key in self.Reminder.keys():
            if self.Reminder[key] == InitReminderBook:
                print(key)
            else:
                print("К сожалению книг с данным остатком не найдено, если пожелаете другую, вновь воспользуйтесь навигацией через меню")

    def GetAllBooks(self):
        for key in self.Author.keys():
            print(f"Книга: {self.Author[key]} автор книги: {key}")

def InitNewObject():
        x = input("Введите имя новой книги:")
        x = Library()
        x.AddBook()
        x.AddBook()
        x.FindBookByAuthor()
InitNewObject()

# Надо пересмотреть логику в остатке и сделать поиск по значениям, ведь мы выдаём книги, следовательно он изменяется, соответсвенно сохраняем изменения, при изменении ключа будет ряд ошибок



    










    
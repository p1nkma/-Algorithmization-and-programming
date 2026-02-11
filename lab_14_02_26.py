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
        self.Author = None
        self.YearPublication = None
        self.Reminder = None

    def AddBook(self): 
        self.Book = str(input("Введите название книги:"))
        print(f"Название {self.Book} успешно сохранено")
        self.Author = str(input("Введите автора:"))
        print(f"Автор {self.Author} книги {self.Book} успешно сохранён")
        AddYearPublication = int(input("Введите год издания книги:"))
        if 1 <= AddYearPublication <= 2026:
            self.YearPublication = AddYearPublication
            print(f"Год издания {self.YearPublication} успешно сохранён")
        else:
            print(f"Год издания {AddYearPublication} не верен, в нашей библиотеке нет книг выпущенных до нашей эры или произведенний полученных из будущего")
            AddYearPublication = int(input("Введите новое значение в рамках от 1 до 2026г:"))
            print(f"Год издания {self.YearPublication} успешно сохранён")
        
    def GetAllBooks(self):
        print(self.Book , self.Author, self.YearPublication, self.Reminder , sep = "/n")

obj = Library()
obj.AddBook()
obj2 = Library()
obj2.AddBook()
obj.GetAllBooks()
obj2.GetAllBooks()






    
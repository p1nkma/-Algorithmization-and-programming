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
ListObjects = []

class Library:

    def __init__(self):
        self.Book = None
        self.Author = None
        self.YearPublication = None
        self.Reminder = None
        self.ListObjects = ListObjects

    def AddBook(self): 
        self.Book = str(input("Введите название книги:"))
        print(f"Название {self.Book} успешно сохранено")

        self.Author = str(input("Введите автора:"))
        print(f"Автор {self.Author} книги {self.Book} успешно сохранён")

        while True:
            try:
                AddYearPublication = int(input("Введите год издания книги:"))
                if 1 <= AddYearPublication <= 2026:
                    self.YearPublication = AddYearPublication
                    print(f"Год издания {self.YearPublication} успешно сохранён")
                    break
                else:
                    print("Год должен быть от 1 до 2026!")
            except ValueError:
               print("Введите корректное число")

        while True:
            try:    
                AddCountBook = int(input("Введите добавляемое кол-во книг:"))
                if AddCountBook > 0:
                    self.Reminder = AddCountBook
                    print(f"Книга {self.Book} - в количесвте {self.Reminder} Год издания - {self.YearPublication} Автор - {self.Author} успешно сохранена")
                    break
                else:
                    print("Число должно быть >0!!!")

            except ValueError:
                print("Вводите корректное кол-во книг, значение > 0")

    def FindBookYearPublication(self):
        FindedBookYearPublication = int(input("Введите искомый год публикации:"))
        for obj in ListObjects:
            print(obj)

def InitNewObject():
        x = input("Введите имя нового объекта:")
        x = Library()
        x.AddBook()
        ListObjects.append(x)
        x.FindBookYearPublication()
InitNewObject()




    










    
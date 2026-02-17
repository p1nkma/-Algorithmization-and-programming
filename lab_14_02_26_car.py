def add_new_car():
    car_brand = str(input("Введите марку автомобиля:"))

    isValid_release_year = False
    while not isValid_release_year:
        try:
            release_year = int(input("Введите год выпуска автомобиля:"))
            isValid_release_year = True
        except ValueError:
            print("Вводите число!")

    isValidCar_condition = False
    while not isValidCar_condition:
        try:
            is_clean = str(input("Ваша машина чистая Yes/No"))
            if is_clean == "Yes":
                car_condition = True
                isValidCar_condition = True
            elif is_clean == "No":
                car_condition = False
                isValidCar_condition = True
            else:
                print("Ввести надо Yes/No - попробуйте вновь")
        except ValueError:
            print("Введите yes/no, а не числовое значение")
    
    return(car_brand, release_year, car_condition)

def init_new_car(car):
    a = Car(*add_new_car())
    car.append_car_garage(a)

def process_car_service(car):
    for current_car in car.cars:
        if current_car.car_condition == True:
            current_car.car_condition = False
            print(f"К сожалению ваша {current_car.car_brand} {current_car.release_year} года выпуска стала грязной")
        else:
            wash = CarWash(current_car)
            wash.washing_car()
            print(f"Ваша машина {current_car.car_brand} грязная, но мы только что отправили её на мойку!")

class Car:
    def __init__(self,car_brand, release_year : int, car_condition : bool):
        self.car_brand = car_brand
        self.release_year = release_year
        self.car_condition = car_condition

class Garage:
    def __init__(self, cars : list):
        self.cars = cars
    
    def append_car_garage(self, car):
        self.cars.append(car)

class CarWash:
    def __init__(self, current_car):
        self.current_car = current_car

    def washing_car(self):
        self.current_car.car_condition = True

def main_menu():
    car = Garage([]) # Создаем один экземпляр гаража
    
    while True:
        print("\n=== ГЛАВНОЕ МЕНЮ ===")
        print("1. Добавить новую машину в гараж")
        print("2. Запустить цикл обслуживания (мойка/загрязнение)")
        print("3. Выйти из программы")
        
        choice = input("\nВыберите действие (1-3): ")
        
        if choice == "1":
            init_new_car(car)
                           
        elif choice == "2":
            process_car_service(car)
            
        elif choice == "3":
            print("Программа завершена. До свидания!")
            break
        else:
            print("Неверный ввод, попробуйте еще раз.")

# Запуск программы
if __name__ == "__main__":
    main_menu()

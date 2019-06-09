"""
Створити клас “Ноутбук” rотрий містить поля:
- швидкодія процесору (CPU, в гігагерцах)
- об'єм оперативної пам'яті
- назва фірми-виробника

Три додаткових поля, які найкраще описують даний клас
Конструктор (із вказаними дефолтними значеннями)
Деструктор
Метод, що повертає стрічкове представлення класу
Статичне поле
Статичний метод, що повертає значення статичного поля
В main() методі визначіть 3 об’єкти типу із завдання (з-за допомогою передачі різної кількості параметрів) та виведіть інформацію про них з-за допомогою методу з пункту 4 в консоль

"""
class Laptop:

    _number_of_faptops = 0

    def __init__(self, processorSpeed = 0, ram = 0, manufacturer = "None", color = "None", price = 0, cpu = "None"):
        self.processorSpeed = processorSpeed
        self.ram = ram
        self.manufacturer = manufacturer
        self.color = color
        self.price = price
        self.__cpu = cpu

    def __del__(self):
        print(self.manufacturer + " deleted")

    def __str__(self):
        return str(self.__dict__)

    @staticmethod
    def get_static_number_of_faptops():
        return Laptop._number_of_faptops

def main():
    asus = Laptop(3.9, 16, "Asus", "Black", 1200, "Intel")
    lenovo = Laptop(4, 8, "Lenovo")
    msi = Laptop(4.5, 32, "MSI", "White")
    print(asus)
    print(lenovo)
    print(msi)
    print(Laptop.get_static_number_of_faptops())

if __name__ == '__main__':
    main()

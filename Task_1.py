# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
# строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
# декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к
# типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
# реальных данных.

class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def create_int(cls, date):
        date = date.split('-')
        date = [int(date[i]) for i in range(len(date))]
        return date

    @staticmethod
    def check_date(list_numbers):
        month = {'1': 31, '2': 28, '3': 31, '4': 30, '5': 31, '6': 30, '7': 31, '8': 31, '9': 30, '10': 31, '11': 30,
                 '12': 31}

        if list_numbers[2] % 4 == 0:
            month['2'] = 29

        if 12 < list_numbers[1] or list_numbers[1] < 1:
            print('Ошибка! Месяц указан неверно!')
        elif list_numbers[0] > month[str(list_numbers[1])]:
            print('Ошибка! Число указано неверно!')
        elif list_numbers[2] <= 0:  # Т.к. это могут быть исторические даты - в условии не указано
            print('Ошибка! Год указан неверно!')
        else:
            print('Дата указана верно!')

    # Второй вариант взаимодействия методов
    def method_communication(self):
        return self.check_date(self.create_int('29-02-2020'))


# Первый вариант вывода
Date.check_date(Date.create_int('29-02-2020'))

# Второй вариант вывода
d = Date('26-03-1020')
d.method_communication()


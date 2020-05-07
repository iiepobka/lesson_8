# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в
# качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с
# ошибкой.
class ZDE(Exception):
    def __init__(self, number):
        self.number = number


inp_number_1 = input('Введите целое число цифрой - делимое: ')
inp_number_2 = input('Введите целое число цифрой - делитель: ')

try:
    inp_number_1 = int(inp_number_1)
    inp_number_2 = int(inp_number_2)
    if inp_number_2 == 0:
        raise ZDE('Ошибка. Делить на ноль нельзя!')
except ValueError:
    print('Ошибка! Требуется ввести число цифрами!')
except ZDE as error:
    print(error)
else:
    print(f'Вы ввели числа: {inp_number_1} - делимое и {inp_number_2} - делитель. ' \
          f'Частное равно: {inp_number_1 / inp_number_2}')

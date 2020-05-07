# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное
# число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив
# сложение и умножение созданных экземпляров. Проверьте корректность полученного
# результата.
class Complex_number:
    def __init__(self, c_number):
        self.c_number = c_number

    def __add__(self, other):
        return self.c_number + other.c_number

    def __mul__(self, other):
        return self.c_number * other.c_number


cn_1 = Complex_number(complex(7, 8))
cn_2 = Complex_number(complex(7, 5))
print(cn_1 + cn_2)
print(cn_1 * cn_2)
cn_1 = Complex_number(2 - 5j)
cn_2 = Complex_number(3 + 4j)
print(cn_1 + cn_2)
print(cn_1 * cn_2)

# Другой вариант
class Complex_number:
    def __init__(self, c_number_1, c_number_2):
        self.c_number_1 = c_number_1
        self.c_number_2 = c_number_2

    def __add__(self, other):
        return complex(self.c_number_1, self.c_number_2) + complex(other.c_number_1, other.c_number_2)

    def __mul__(self, other):
        return complex(self.c_number_1, self.c_number_2) * complex(other.c_number_1, other.c_number_2)


cn_1 = Complex_number(7, 8)
cn_2 = Complex_number(7, 5)
print(cn_1 + cn_2)
print(cn_1 * cn_2)

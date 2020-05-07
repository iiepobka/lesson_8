class Office_equipment:
    def __init__(self, type_office_equipment, producer_company, performance, service_life, paper_size, color, weight, \
                 overall_dimensions):
        self.type_office_equipment = type_office_equipment
        self.producer_company = producer_company
        self.performance = performance
        self.service_life = service_life
        self.paper_size = paper_size
        self.color = color
        self.weight = weight
        self.overall_dimensions = overall_dimensions

    def __str__(self):
        return f'Наименование оборудования: {self.type_office_equipment}\nКомпания-производитель оборудования: \
{self.producer_company}\nПроизводительность: {self.performance}\nРесурс работы: {self.service_life}\nРазмер \
бумаги: {self.paper_size}\nЦвет печати: {self.color}\nВес: {self.weight}\nГабариты: {self.overall_dimensions}'


class Printer(Office_equipment):
    def __init__(self, type_office_equipment, producer_company, performance, service_life, paper_size, color, weight, \
                 overall_dimensions, print_technology, tray_capacity):
        self.print_technology = print_technology
        self.tray_capacity = tray_capacity
        super().__init__(type_office_equipment, producer_company, performance, service_life, paper_size, color, weight, \
                         overall_dimensions)

    def __str__(self):
        return f'{super().__str__()}\nТип печати: {self.print_technology}\nЕмкость лотков: {self.tray_capacity}\n'


class Scanner(Office_equipment):
    def __init__(self, type_office_equipment, producer_company, performance, service_life, paper_size, color, weight, \
                 overall_dimensions, optical_resolution):
        self.optical_resolution = optical_resolution
        super().__init__(type_office_equipment, producer_company, performance, service_life, paper_size, color, weight, \
                         overall_dimensions)

    def __str__(self):
        return f'{super().__str__()}\nОптическое разрешение сканера: {self.optical_resolution}\n'


class Xerox(Office_equipment):
    def __init__(self, type_office_equipment, producer_company, performance, service_life, paper_size, color, weight, \
                 overall_dimensions, print_technology, tray_capacity, optical_resolution):
        self.print_technology = print_technology
        self.tray_capacity = tray_capacity
        self.optical_resolution = optical_resolution
        super().__init__(type_office_equipment, producer_company, performance, service_life, paper_size, color, weight, \
                         overall_dimensions)

    def __str__(self):
        return f'{super().__str__()}\nТип печати: {self.print_technology}\nЕмкость лотков: {self.tray_capacity}\n\
Оптическое разрешение сканера: {self.optical_resolution}\n'


p = Printer('принтер', '2', '3', '4', '5', '6', '7', '8', '9', '10')
s = Scanner('сканер', '2', '3', '4', '5', '6', '7', '8', '9')
x = Xerox('ксерокс', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11')


class Warehouse_Office_equipment:
    receipt = {'принтер': 20, 'сканер': 20, 'ксерокс': 20}
    departments = ['964', '065']
    dispatch = [{'принтер': 2, 'сканер': 2}, {'ксерокс': 1}]

    def add(self):
        while True:
            name = input('Введите наименование оргтехники, поступившей на склад (для выхода введите *): ')
            name = name.lower()
            if name == '*':
                break
            try:
                count = int(input('Введите кол-во единиц оргтехники, поступившей на склад: '))
            except ValueError:
                print('Ошибка! Введено не число!')
                continue

            if name in self.receipt.keys():
                self.receipt[name] = self.receipt[name] + count
            else:
                self.receipt[name] = count
        print(f'{"-" * 120}\nНа данный момент на складе:')
        for k, v in self.receipt.items():
            print(f'{k} - {v} шт.')
        print('-' * 120)

    def subtract(self):
        while True:
            department = input('Введите отдел, куда направлена оргтехника (для выхода введите *): ')
            department = department.lower()
            if department == '*':
                break
            name = input('Введите наименование оргтехники, направленной в отдел: ')
            name = name.lower()
            try:
                count = int(input('Введите кол-во единиц оргтехники выбывающей со склад: '))
            except ValueError:
                print('Ошибка! Введено не число!')
                continue
            if name in self.receipt.keys():
                if count <= self.receipt[name]:
                    self.receipt[name] = self.receipt[name] - count
                else:
                    print(f'Oшибка! Требуемое кол-во отсутствует на складе. На складе {self.receipt[name]} {name}(ов)')
                    continue
            else:
                print('Ошибка! Оргтехника отсутствует на складе')
                continue

            if department in self.departments:
                index = self.departments.index(department)
                if name in self.dispatch[index].keys():
                    self.dispatch[index][name] = self.dispatch[index][name] + count
                else:
                    self.dispatch[index][name] = count
            else:
                self.departments.append(department)
                self.dispatch.append({name: count})

    def print_all_equipment(self):
        for i in range(len(self.departments)):
            print(f'{"-" * 120}\nНа данный момент в отделе {self.departments[i]}:')
            for k, v in self.dispatch[i].items():
                print(f'{k} - {v} шт.')
            print('\nОписание оборудования:')
            if p.type_office_equipment in self.dispatch[i].keys():
                print(p)
            if s.type_office_equipment in self.dispatch[i].keys():
                print(s)
            if x.type_office_equipment in self.dispatch[i].keys():
                print(x)
        print(f'{"-" * 120}\nОстаток на складе:')
        for k, v in self.receipt.items():
            print(f'{k} - {v} шт.')

    def conclusion(self):
        return f'{self.add()}{self.subtract()}{self.print_all_equipment()}'


w = Warehouse_Office_equipment()
w.conclusion()

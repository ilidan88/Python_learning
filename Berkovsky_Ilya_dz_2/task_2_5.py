

from random import uniform


def transfer_list_in_str(list_in: list) -> str:
    """Преобразует каждый элемент списка (вещественное число) в строку вида '<r> руб <kk> коп' и
        формирует из них единую строковую переменную разделяя значения запятой."""
    new_list = []  # создаём новый список
    for price in list_in:  # Перебираем список
        ruble = int(price)  # Приводим рублик целому числу
        penni = int((price * 100) % 100)  # считаем копейки и приводим к целому числу
        new_list.append(f"{ruble:02} руб {penni:02} коп")  #n:02 - округление до 2х знаков. методом .append добавляем получившееся значение в список
    str_out = ", ".join(new_list) # методом .join выводим как строку
    return str_out


my_list = [95.89, 85.57, 46.06, 56.49, 17.43, 50.64, 41.75, 55.03, 12.97, 56.02, 93.66, 91.82, 34.63, 29.6, 71.39]  # автоматическая генерация случайных 15 чисел
print(f'Исходный список: {my_list}')
result_1 = transfer_list_in_str(my_list)
print(result_1)


def sort_prices(list_in: list) -> list:
    """Сортирует вещественные числа по возрастанию, не создавая нового списка"""
    list_in.sort()
    return list_in


my_list = [95.89, 85.57, 46.06, 56.49, 17.43, 50.64, 41.75, 55.03, 12.97, 56.02, 93.66, 91.82, 34.63, 29.6, 71.39]
result_2 = sort_prices(my_list)
# зафиксируйте здесь доказательство, что результат result_2 остался тем же объектом
print(result_2)


def sort_price_adv(list_in: list) -> list:
    """Создаёт новый список и возвращает список с элементами по убыванию"""
    list_out = list(reversed(list_in))
    return list_out


result_3 = sort_price_adv(my_list)
print(result_3)


def check_five_max_elements(list_in: list) -> list:
    """Проверяет элементы входного списка вещественных чисел и возвращает
        список из ПЯТИ максимальных значений"""
    list_out = []
    sort_list = sort_price_adv(list_in)
    for num in range(5):
        list_out.append(sort_list[num])
    return list_out


result_4 = check_five_max_elements(my_list)
print(result_4)
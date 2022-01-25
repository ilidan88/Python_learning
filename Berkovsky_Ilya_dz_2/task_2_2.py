


def convert_list_in_str(list_in: list) -> str:
    """Обособляет каждое целое число кавычками, добавляя кавычку до и после элемента
        списка, являющегося числом, и дополняет нулём до двух целочисленных разрядов.
        Формирует из списка результирующую строковую переменную и возвращает."""
    new_list = []
    for element in list_in:
        if element[0] in ['+', '-'] or element.isdigit():
            if element.isdigit():
                new_list.append(f'"{element.zfill(2)}"')
            else:
                new_list.append(f'"+{element[1:].zfill(2)}"')
        else:
            new_list.append(element)
    str_out = ' '.join(new_list)  # здесь полученная после всех преобразования строковая переменная"
    return str_out


my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = convert_list_in_str(my_list)
print(result)


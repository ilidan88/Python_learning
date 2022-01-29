

def convert_name_extract(list_in: list) -> list:
    """Извлекает имена из элементов и формирует список приветствий."""
    for list_out in range(len(list_in)):
        list_in[list_out] = list_in[list_out].split()
        list_in[list_out] = f'Привет, {list_in[list_out][-1].title()}!'
    return list_in


my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
result = convert_name_extract(my_list)
print(result)

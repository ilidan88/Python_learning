

def num_translate(value: str) -> str:
    """переводит числительное с английского на русский """
    str_out = dict_num_eng.get(value)
    return str_out


dict_num_eng = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }


print(num_translate('one'))
print(num_translate('eight'))


convert_map = ((1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
               (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
               (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'))


def read_data():
    return open('tests/inputFile5.txt').read().split(',')


def write_data(my_new_list):
    with open('outputFile.txt', 'w') as f:
        for lines in my_new_list:
            for elem in lines:
                f.write(str(elem))
            f.write('\n')


def arab_to_roman(number):
    result = ''
    for arab, roman in convert_map:
        while number >= arab:
            result += roman
            number -= arab
    return result


def roman_to_arab(txt):
    txt = txt.upper()
    result = 0
    for arab, roman in convert_map:
        while txt.startswith(roman):
            result += arab
            txt = txt[len(roman):]
    return result


array = []
for el in read_data():
    if any(map(str.isdigit, el)):
        array.append(str(arab_to_roman(int(el))))
    else:
        array.append(str(roman_to_arab(el)))
write_data(array)

# print(arab_to_roman(int(read_data()[0])))
# write_data(arab_to_roman(int(read_data()[0])))


# for i in (0, 4, 8, 9, 31, 46, 99, 583, 888, 1668, 1989, 2009, 2010, 2011, 3999):
#     arab = arab_to_roman(i)
#     roman = roman_to_arab(arab)
#     print(i, arab, roman)

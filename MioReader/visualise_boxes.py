import matplotlib.pyplot as plt
from pylab import *

parent_file_path = 'C:\\Users\\Данила\\Searches\\Desktop\\mio\\MioReader\\DataConverterPython\\GorbPlusRes\\'  # расположение файлов


def combine_column(data, colum_a, colum_b):
    for i in range(len(data)):
        if colum_b > len(data[i]):
            print('!!error on line{}'.format(data[i]))
        else:
            data[i].append(data[i][colum_a] + data[i][colum_b])


def get_unical_element_in_list(data):
    elements = []
    for value in data:
        if not value in elements:
            elements.append(value)
    elements.sort()
    return elements


def drawing_data(data, sorting_elements):
    result_data = []
    for i in range(len(sorting_elements)):
        result_data.append([])
        get_type = sorting_elements[i]
        print('Work with {} type'.format(get_type))
        for j in range(len(data[0])):
            if data[1][j] == get_type:
                result_data[i].append(int(data[0][j]))
    return result_data


def read_data(file, colum_values, colum_types):
    reading_data = []
    i = 0
    reading_data.append([])
    reading_data.append([])
    for line in file:
        splited_line = line.split(';')
        reading_data[0].append(splited_line[colum_values])
        reading_data[1].append(splited_line[colum_types])
        i = i + 1
    return reading_data


def draw_box_by_column(file_name, colum_values, colum_types):
    file = open(parent_file_path + file_name, 'r', encoding='utf-8')
    # пропускаем первую строку с описанием столбцов
    line_names = file.readline().split(';')

    next(file)

    total_data_to_draw = read_data(file, colum_values, colum_types)
    sorting_type = get_unical_element_in_list(total_data_to_draw[1])
    print('work with sorting type {}'.format(sorting_type))
    drawing_data_values = drawing_data(total_data_to_draw, sorting_type)

    print(file.readline())

    plt.title('Таблица распределения ' + line_names[colum_types] + ' от ' + line_names[colum_values])

    sorting_type.insert(0, ' ')
    if len(sorting_type) > 5:
        plt.boxplot(drawing_data_values, vert=False)
        plt.ylabel(line_names[colum_types].replace('\n', ' '))
        plt.yticks(range(len(sorting_type)), sorting_type)
        if colum_values in range(2, 7):
            plt.xlabel("ЦЛМ класса " + str(line_names[colum_values]) + " значение в у.е.")
        elif colum_values in range(7, 12):
            plt.xlabel("ЦЛМ класса " + str(line_names[colum_values]) + " значение в %")
    else:
        plt.boxplot(drawing_data_values, vert=True)
        plt.xticks(range(len(sorting_type)), sorting_type)
        plt.xlabel(line_names[colum_types].replace('\n', ' '))
        if colum_values in range(2, 7):
            plt.ylabel("ЦЛМ класса " + str(line_names[colum_values]) + " значение в у.е.")
        elif colum_values in range(7, 12):
            plt.ylabel("ЦЛМ класса " + str(line_names[colum_values]) + " значение в %")

    plt.savefig('Графики/' + str(file_name) + ' ' + str(line_names[colum_types].replace('\n', ' ')) + ' ' + str(
        line_names[colum_values]) + '.png')
    plt.close()
    file.close()


# 'W2Gorb_plus_res.csv'
# 'VGorb_plus_res.csv'

for k in range(2, 12):
    draw_box_by_column('W2Gorb_with_new_column.csv', k, 1)
    # draw_box_by_column('VGorb_plus_res.csv', i, 13)
    for j in range(12, 25):
        draw_box_by_column('W2Gorb_with_new_column.csv', k, j)
        # draw_box_by_column('VGorb_plus_res.csv', i, 13)

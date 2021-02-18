def read_data():
    with open('inputFile.txt', 'r') as f:
        return [[int(num) for num in line.split(',')] for line in f]


def shifting_elements(my_list, n):
    if n < 0:
        n = abs(n)
        for i in range(n):
            my_list.append(my_list.pop(0))
    else:
        for i in range(n):
            my_list.insert(0, my_list.pop())
    return my_list


def write_data(my_new_list):
    with open('outputFile.txt', 'w') as f:
        for lines in my_new_list:
            for el in lines:
                f.write(str(el) + ',')
            f.write('\n')


def solve_task():
    new_array = []
    i = 0
    for line in read_data():
        new_array.append(shifting_elements(line, 2 * (i % 2) - 1))
        i += 1
    write_data(new_array)


solve_task()
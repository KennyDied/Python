def read_data():
    return open('inputFile.txt').read().split(',')


def solve_task(my_list, n):
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
        for line in my_new_list:
            f.write(line + ',')


write_data(solve_task(read_data(), 2))
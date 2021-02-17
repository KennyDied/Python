def solve_task(lst, n):
    if n < 0:
        n = abs(n)
        for i in range(n):
            lst.append(lst.pop(0))
    else:
        for i in range(n):
            lst.insert(0, lst.pop())

first_list = [3, 5, 2, 4, 9, 1]
solve_task(first_list, 2)
print(first_list)

second_list = [3, 5, 2, 4, 9, 1]
solve_task(second_list, - 15)
print(second_list)

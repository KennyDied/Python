from numpy import sin, linspace
import matplotlib.pyplot as plt


def f(x):
    return sin(x) / x

#прямоугольники
def draw_bars(a, b, number_of_bars):
    intervals = (b-a)/number_of_bars
    x = intervals
    bar_height = []
    left = [a]
    new_interval = a
    while x <= b:
        bar_height.append(f(x))
        x = x + intervals
    while True:
        new_interval += intervals
        if new_interval == b:
            break
        left.append(new_interval)
    return bar_height, left, intervals

#сам метод
def solve(f, a, b, n):
    print("\nТекущее число разбиений: ", n)
    h = (b-a)/float(n)
    print("Текущий шаг:", h)
    total = sum([f((a + (k*h))) for k in range(0, n)])
    result = h * total
    print("Текущий результат: ", result)
    return result


#делаем разбиения
num_of_interval = 64
n = 2
a1 = solve(f, 1, 10, n)
n *= 2
a2 = solve(f, 1, 10, n)

while n < num_of_interval: #число разбиений
    n *= 2
    a1 = solve(f, 1, 10, n)
    n *= 2
    a2 = solve(f, 1, 10, n)


fig = plt.figure()

#рисуем функцию
x = linspace(0, 10, 100)
y = f(x)
plt.plot(x,y)

#задаем прямоугольники
left = draw_bars(0,10,num_of_interval)[1]
bar_height = draw_bars(0,10,num_of_interval)[0]
interval = draw_bars(0,10,num_of_interval)[2]

#рисуем прямоугольники и создаем окошко
plt.bar(left,bar_height,interval, color = 'yellow', align = 'edge', edgecolor = 'black')
plt.title('Approximating area under curves')
plt.ylabel('y')
plt.xlabel('x')

plt.show()
from math import sin


def solve(f, a, b, n):
    print("\nТекущее число разбиений: ", n)
    h = (b-a)/float(n)
    print("Текущий шаг:", h)
    total = sum([f((a + (k*h))) for k in range(0, n)])
    result = h * total
    print("Текущий результат: ", result)
    return result


def f(x):
    return sin(x)/x


print("Используем метод средних прямоугольников")
print("Интегрируемая функция: f(x) = sin(x) / x")
print("Точность: 0.001")

n = 2
a1 = solve(f, 1, 10, n)
n *= 2
a2 = solve(f, 1, 10, n)

while abs(a1 - a2) > 0.001:
    n *= 2
    a1 = solve(f, 1, 10, n)
    n *= 2
    a2 = solve(f, 1, 10, n)

print("\nОтвет:", a2, "\nКоличество разбиений:", n)
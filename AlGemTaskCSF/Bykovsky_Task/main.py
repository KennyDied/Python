import matplotlib.pyplot as plt
from math import sin, cos, pi

plt.title('Асторида')
plt.xlabel('Ось x')
plt.ylabel('Ось y')
plt.grid()

R = 1
n = range(1000)
t = [2 * pi * i / 100 for i in n]
x = [R * cos(t[i]) ** 3 for i in n]
y = [R * sin(t[i]) ** 3 for i in n]

plt.plot(x, y, 'r')
plt.show()
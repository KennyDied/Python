
def read_data():
    c = []
    with open('inputFile.txt', 'r') as f:
        for line in f:
            arr_bigger = []
            for num in line.strip().split('; '):
                arr_small = []
                for i in num:
                    if i.isdigit():
                        arr_small.append(int(i))
                arr_bigger.append(arr_small)
            c.append(arr_bigger)
    return c



def length2(a, b):
    return (a[0] - b[0])**2 + (a[1] - b[1])**2


# подобны ли 2 треугольника, заданные отсортированными массивами длин сторон
def is_sim(sample, triangle):
    if sample[0] * triangle[1] != sample[1] * triangle[0]:
        return False
    elif sample[0] * triangle[2] != sample[2] * triangle[0]:
        return False
    elif sample[1] * triangle[2] != sample[2] * triangle[1]:
        return False
    else:
        return True


# преобразование массивов координат в массивы длин сторон
def make_triangles(v):
    triangles = []
    for el in v:
        a2 = length2(el[0], el[1])
        b2 = length2(el[0], el[2])
        c2 = length2(el[1], el[2])
        triangle = [a2, b2, c2]
        triangle.sort()
        triangles.append(triangle)
    return triangles


# основной код


tr = read_data()
# tr = [[[0, 0], [3, 0], [0, 3]], [[4, 0], [8, 0], [4, 4]]]
triangles = make_triangles(tr)
print(triangles)
for i in range(1, len(triangles)):
    if is_sim(triangles[0], triangles[i]):
        print("found similar trinangle: ")
        print(triangles[0], triangles[i])
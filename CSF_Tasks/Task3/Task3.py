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


# квадрат растояния
def length2(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


# подобны ли 2 треугольника, заданные отсортированными массивами длин сторон
def is_triangles_similar(triangle1, triangle2):
    if triangle1[0] * triangle2[1] != triangle1[1] * triangle2[0]:
        return False
    elif triangle1[0] * triangle2[2] != triangle1[2] * triangle2[0]:
        return False
    elif triangle1[1] * triangle2[2] != triangle1[2] * triangle2[1]:
        return False
    else:
        return True


def write_data(triangles):
    output = open('outputFile.txt', 'w')

    output_str = str(triangles) + "\n"
    for i in range(1, len(triangles)):
        if is_triangles_similar(triangles[0], triangles[i]):
            output_str += "found similar triangles:  \n"
            output_str += str(triangles[0]) + str(triangles[i]) + "\n"
    output.write(output_str)


triangles = make_triangles(read_data())
write_data(triangles)
firstside = float(input('Введите длину первого катета: '))
secondside = float(input('Введите длину второго катета: '))
hipotenuse = (firstside + secondside) ** 0.5
triangle_area = 0.5 * firstside * secondside
triangle_perimeter = firstside + secondside + hipotenuse
print('Площадь треугольника равна:' , triangle_area)
print('Периметр треугольника равен:' , triangle_perimeter)
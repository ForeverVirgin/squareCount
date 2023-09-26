import math

# Функция count_square принимает на вход произвольные параметры.
# Если получен 1 параметр типа int, то объект считается кругом, а параметр - его радиусом.
# Возвращается площадь этого круга.
# Если получено 3 параметра типа int, то объект считается треугольником, а параметры - длинами его сторон.
# Возвращается площадь этого треугольника.
# Во всех иных случаях возвращается arg_error()

def count_square(*args):
  if(len(args) == 1):
    if type(args[0]) == type(0):
      return count_square_circle(args[0])
    else:
      return arg_error()
  if(len(args) == 3):
    for i in args:
      if(type(i) != type(0)):
        return arg_error()
    return count_square_triangle(args)
  else:
    return arg_error()

# Расчет площади круга

def count_square_circle(radius):
  return math.pi*(radius**2)

# Расчет площади треугольника. Если прямоугольный, то полупроизведение катетов, иначе по формуле Герона.

def count_square_triangle(args):

  if(args[0]+args[1]>args[2] and args[1]+args[2]>args[0] and args[0]+args[2]>args[1]):
    if not isRectangular(args[0],args[1],args[2]):
        p = (args[0] + args[1] + args[2]) / 2
        return math.sqrt(p*(p-args[0])*(p-args[1])*(p-args[2]))
    else:
        c1, c2 = isRectangular(args[0],args[1],args[2])
        return c1*c2/2
  else:
    return "Impossible triangle"

# Действия при вводе неправильных аргументов в функцию count_square. В данном случае возвращает строку "Argument error"

def arg_error():
  return "Argument error"

# Проверка на то, является ли треугольник прямоугольным

def isRectangular(a, b, c):
    if a**2 + b**2 == c**2:
        return a, b
    elif a**2 + c**2 == b**2:
        return a, c
    elif b**2 + c**2 == a**2:
        return b, c
    else:
        return False

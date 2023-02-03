for i in range(10, 100):
    a = i ** 2
    b = str(a)[::-1]
    if str(a) == b:
        c = i ** 3
        d = str(c)[::-1]
        if str(c) == d:
            print('Исходное число:', i, '\nЧисло в квадрате:', b, '\nЧисло в кубе:', c)
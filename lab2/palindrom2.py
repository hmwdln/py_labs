for i in range(10, 101):
    a = i ** 2
    check_square = a 
    result = 0 
    while(a > 0): 
        first = a % 10 
        result = result * 10 + first
        a = a // 10 
    if (check_square == result): 
        b = i ** 3
        temp = b
        res = 0
        while(b > 0): 
            second = b % 10 
            res = res * 10 + second
            b = b // 10 
        if (temp == res):
            print('Исходное число:', i, '\nЧисло в квадрате:', result, '\nЧисло в кубе:', res)
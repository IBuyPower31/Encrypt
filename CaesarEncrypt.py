import math
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"  # Алфавит для кодирования по методу цезаря


def Encrypt(i, k):
    res = int()
    if i + k >= 33:
        res = math.fabs(33 - i - k)
    else:
        res = i + k# Проверка на отрицательное число и выход за границы алфавита
    return alphabet[res]


def FindSymbol(symbol, k):
    for i in range(0, len(alphabet)):
        if alphabet[i] == symbol:
            symbol = Encrypt(i, k)
    return symbol



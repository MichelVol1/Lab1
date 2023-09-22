while True:
    num = input("Введите ваше число или Exit для выхода:")
    if num == "Exit":
        break
    if not num.isdigit():
        print("Ошибка вввода")
        continue
    num = int(num)
    a = 0
    max = 0
    while num > 0:
        a = num % 10
        num = num // 10
        if a > max:
            max = a
    print(max)

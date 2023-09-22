while True:
    str = input("Введите список или Exit для выхода:")
    if not str.isdigit():
        print("Ошибка вввода")
        continue
    if str == "Exit":
        break
    spis= []
    for i in str:
        spis.append(int(i))
    print(spis)
    min = None;
    for i in spis:
        if i % 2 == 0:
            if min is None or min > i:
                min = i
    if min == None:
        print(spis[0])
    else:
        print(min)
    print("Преобразование:")
    kol = spis.count(0)
    spis = [elem for elem in spis if elem != 0]
    for i in range(kol):
        spis.insert(0,0)
    print(spis)
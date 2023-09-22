import random

dict ={
    'Фигурка Аист':['Белый аист это самый известный из аистов.',32,346],
    'Фигурка Тапир':['Тапи́ры это травоядные животные из отряда непарнокопытных.',39,306],
    'Мягкая игрушка Акула':['Коллекционные мягкие игрушки от бренда Button Blue.',40,287],
    'Кукла Барби':['Игровой набор Barbie от бренда Mattel.',89,156],
    'Набор автомобилей Hot Wheels':['Собери коллекцию Hot Wheels с этим набором от Mattel.',134,198]
}

while True:
    print("Меню")
    print("1.Просмотр описания")
    print("2.Просмотр цены")
    print("3.Просмотр количества")
    print("4.Всю информацию")
    print("5.Покупка")
    print("6.До свидание")
    n = input("Введите")
    if n == "1":
        for i in dict:
          print(i, '-',dict[i][0])
    elif n == "2":
        for i in dict:
            print(i, '-', dict[i][1],"Byn")
    elif n == "3":
        for i in dict:
            print(i, '-', dict[i][2],"штук")
    elif n == "4":
        for i in dict:
          print(i,'-',dict[i])
    elif n == "5":
        while True:
           str = input("Введите название игрушки:")
           if not str in dict:
               print("На складе нет товара с таким названием")
               continue
           kol = input("Введите количество игрушек")
           if not kol.isdigit():
               print("Ошибка ввода, повторите ввод!!!")
               continue
           kol=int(kol)
           if dict[str][2]<kol :
                   print("На складе нет такого большого количества товара")
                   continue
           print("Цена покупки = ",dict[str][1],"Byn","*",kol," штук"," = ",dict[str][1]*kol,"Byn")
           print("Все верно?")
           j = input("Да(Д)/Нет(Н)")
           if j == 'Д':
             print("Было товара ",dict[str][2])
             dict[str][2]= dict[str][2]-kol
             print("Стало товара",dict[str][2])
             print("Выуспешно купили товар,чек №", random.randint(1,100) )
             break
           elif j == 'Н':
             print("Повторите ввод")
             continue
           else:
             print("Ошибка ввода, повторите ввод!!!")
             continue
    elif n == "6":
       break;
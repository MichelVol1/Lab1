while True:
 str = input("Введите своё предложение для Exit для выхода: ")
 if str == "Exit":
     print("Выход из программы...")
     break
 start = str.find("(")
 end = str.find(")")
 if start == -1 or end == -1:
     print(" В предложении есть только одна скобочка!!! ")
     continue
 if start == end:
    print(" В предложении не скобочек!!! ")
    continue
 print(str[0:start] + str[end + 1:])
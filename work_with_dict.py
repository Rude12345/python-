result = dict()

while True:
    name = input('Введите имя и фамилию нового контакта (через пробел): ')
    cont = int(input('Введите номер телефона: '))
    if name not in result:
        result[name] = cont
    print(f'Текущий словарь контактов: {result}\n')
    for i in result:
        print(i, result[i])
    else:
        print('Такой человек уже есть в контактах.')
    break

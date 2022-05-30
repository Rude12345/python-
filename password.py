while True:
    password = list(input('Придумайте пароль: '))
    l = len(password)
    s = len(list(filter(lambda x: x.isupper(), password)))
    n = len(list(filter(lambda x: x.isdigit(), password)))
    if (1 >= 9) and (s >= 1) and (n >= 3):
        print('Это надёжный пароль!')
        break
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
from random import choice
print('Здравствуй пользователь! Пожалуйста, выбери режим игры - Одна игра или До трёх побед')
rejim_igri = input('')
rejimi_igri = ['Одна игра', 'До трёх побед']
while rejim_igri not in rejimi_igri:
    print('Пожалуйста, выбери режим игры - Одна игра или До трёх побед')
    rejim_igri = input('')
if rejim_igri == 'Одна игра':
    print('Пожалуйста, введите Камень, Ножницы или Бумага')
    Polz = input('')
    lis = ['Камень', 'Ножницы', 'Бумага']
    if Polz not in lis:
        while Polz not in lis:
            print('Пожалуйста, введите Камень, Ножницы, или Бумага')
            Polz = input('')
    AI = choice(lis)
    if Polz == AI:
        print('Ничья!')
    elif Polz == 'Камень' and AI == 'Ножницы':
        print('''Пользователь выбрал Камень, компьютер - Ножницы.
Пользователь победил!''')
    elif Polz == 'Ножницы' and AI == 'Бумага':
        print('''Пользователь выбрал Ножницы, компьютер - Бумагу.
Пользователь победил!''')
    elif Polz == 'Бумага' and AI == 'Камень':
        print('''Пользователь выбрал Бумагу, компьютер - Камень.
Пользователь победил!''')
    elif Polz == 'Ножницы' and AI == 'Камень':
        print('''Пользователь выбрал Ножницы, компьютер - Камень.
Компьютер победил!''')
    elif Polz == 'Камень' and AI == 'Бумага':
        print('''Пользователь выбрал Камень, компьютер - Бумагу.
Компьютер победил!''')
    elif Polz == 'Бумага' and AI == 'Ножницы':
        print('''Пользователь выбрал Бумагу, компьютер - Ножницы.
Компьютер победил!''')
    print('Спасибо за игру!')
else:
    ochki_kompa = 0
    ochki_cheloveka = 0
    round_po_schetu = 0
    while ochki_cheloveka != 3 and ochki_kompa != 3:
        print('Пожалуйста, введите Камень, Ножницы или Бумага')
        Polz = input('')
        lis = ['Камень', 'Ножницы', 'Бумага']
        if Polz not in lis:
            while Polz not in lis:
                print('Пожалуйста, введите Камень, Ножницы, или Бумага')
                Polz = input('')
        AI = choice(lis)
        if Polz == AI:
            print('Ничья!')
        elif Polz == 'Камень' and AI == 'Ножницы':
            ochki_cheloveka += 1
            round_po_schetu += 1
            print(f'''Пользователь выбрал Камень, компьютер - Ножницы.
Пользователь победил в {round_po_schetu} раунде!
Счёт: Компьютер - {ochki_kompa}, Человек - {ochki_cheloveka}.''')
        elif Polz == 'Ножницы' and AI == 'Бумага':
            ochki_cheloveka += 1
            round_po_schetu += 1
            print(f'''Пользователь выбрал Ножницы, компьютер - Бумагу.
Пользователь победил в {round_po_schetu} раунде!
Счёт: Компьютер - {ochki_kompa}, Человек - {ochki_cheloveka}.''')
        elif Polz == 'Бумага' and AI == 'Камень':
            ochki_cheloveka += 1
            round_po_schetu += 1
            print(f'''Пользователь выбрал Бумагу, компьютер - Камень.
Пользователь победил в {round_po_schetu} раунде!
Счёт: Компьютер - {ochki_kompa}, Человек - {ochki_cheloveka}.''')
        elif Polz == 'Ножницы' and AI == 'Камень':
            ochki_kompa += 1
            round_po_schetu += 1
            print(f'''Пользователь выбрал Ножницы, компьютер - Камень.
Компьютер победил в {round_po_schetu} раунде!
Счёт: Компьютер - {ochki_kompa}, Человек - {ochki_cheloveka}.''')
        elif Polz == 'Камень' and AI == 'Бумага':
            ochki_kompa += 1
            round_po_schetu += 1
            print(f'''Пользователь выбрал Камень, компьютер - Бумагу.
Компьютер победил в {round_po_schetu} раунде!
Счёт: Компьютер - {ochki_kompa}, Человек - {ochki_cheloveka}.''')
        elif Polz == 'Бумага' and AI == 'Ножницы':
            ochki_kompa += 1
            round_po_schetu += 1
            print(f'''Пользователь выбрал Бумагу, компьютер - Ножницы.
Компьютер победил в {round_po_schetu} раунде!
Счёт: Компьютер - {ochki_kompa}, Человек - {ochki_cheloveka}.''')
    else:
        print('Спасибо за игру! Желаешь сыграть ещё раз?')

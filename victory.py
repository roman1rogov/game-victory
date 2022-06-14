
while True:
    right_answer = 0
    wrong_answer = 0
# год рождения Пикассо 1881

    picasso_year = int(input('Введите год рождения Пикассо: '))
    if picasso_year == 1881:
        right_answer += 1
    else:
        wrong_answer += 1

# год рождения Репина 1844
    repin_year = int(input('Введите год рождения Репина: '))
    if repin_year == 1844:
        right_answer += 1
    else:
        wrong_answer += 1

# год рождения Могилана 1480
    magellan_year = int(input('Введите год рождения Могилан: '))
    if magellan_year == 1480:
        right_answer += 1
    else:
        wrong_answer += 1

# год рождения Эйнштейна 1879
    einstein_year = int(input('Введите год рождения Эйнштейна: '))
    if einstein_year == 1879:
        right_answer += 1
    else:
        wrong_answer += 1

# год рождения Ньютона 1643
    newton_year = int(input('Введите год рождения Ньютона: '))
    if newton_year == 1643:
        right_answer += 1
    else:
        wrong_answer += 1
    right_percent = right_answer * 100 / 5
    wrong_percent = wrong_answer * 100 / 5
    print('Правильно:', right_answer)
    print('Не правильно:', wrong_answer)
    print('Процент правильно:', right_percent)
    print('Процент не правильно:', wrong_percent)
    resume_victory = (input('Продолжим игру: '))
    if resume_victory == 'нет':
        break
print('GameOver')

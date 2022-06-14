#Проверяем Год и день рождения пушкина.
birth_year= int(input("Введите год рождения А.С.Пушкина: "))
if birth_year == 1799:
    birthday = int(input("Введите день рождения: "))
    if birthday == 6:
        print("Верно")
    elif birthday != 6:
        print('Неверный день рождения')
else:
    print("Не верный год рождения")

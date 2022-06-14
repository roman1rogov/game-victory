#день и год рождения через цикл while
birth_year = int(input("Введите год рождения А.С.Пушкина: "))

while birth_year != 1799:
    print("Не верно")
    birth_year = int(input("Введите год рождения А.С.Пушкина: "))

birthday = int(input("Введите день рождения А.С.Пушкина: "))

while birthday != 6:
    print('Не верно')
    birthday = int(input("Введите день рождения А.С.Пушкина: "))

print("Верно")
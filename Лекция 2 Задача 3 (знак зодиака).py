print('Добрый день, вас приветствует программа для определения знака зодиака по дате рождения!')
month = input('Введите месяц рождения: ')
day = int(input('Введите число рождение: '))

if month.lower() == 'март':
    if day < 21:
        print('Рыбы')
    else:
        print('Овен')
elif month.lower() == 'апрель':
    if day < 21:
        print('Овен')
    else:
        print('Телец')
elif month.lower() == 'май':
    if day < 22:
        print('Телец')
    else:
        print('Близнецы')
elif month.lower() == 'июнь':
    if day < 22 :
        print('Близнецы')
    else:
        print('Рак')
elif month.lower() == 'июль':
    if day < 23:
        print('Рак')
    else:
        print('Лев')
elif month.lower() == 'август':
    if day < 24:
        print('Лев')
    else:
        print('Дева')
elif month.lower() == 'сентябрь':
    if day < 23:
        print('Дева')
    else:
        print('Весы')
elif month.lower() == 'октябрь':
    if day < 24:
        print('Весы')
    else:
        print('Скорпион')
elif month.lower() == 'ноябрь':
    if day < 23:
        print('Скорпион')
    else:
        print('Стрелец')
elif month.lower() == 'декабрь':
    if day < 22:
        print('Стрелец')
    else:
        print('Козерог')
elif month.lower() == 'январь':
    if day < 21:
        print('Козерог')
    else:
        print('Водолец')
elif month.lower() == 'февраль':
    if day < 19:
        print('Водолец')
    else:
        print('Рыбы')

        
        


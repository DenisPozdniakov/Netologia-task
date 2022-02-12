queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]

dict_queries = {'1 слово': 0, '2 слова': 0, '3 слова': 0}

for i in queries:
    x = i.split()
    if len(x) == 1:
        p = 1 / len(queries) * 100
        dict_queries['1 слово'] += p
    elif len(x) == 2:
        p = 1 / len(queries) * 100
        dict_queries['2 слова'] += p
    elif len(x) == 3:
        p = 1/len(queries) * 100
        dict_queries['3 слова'] += p

for i in dict_queries:
    dict_queries[i] = str(round(dict_queries[i])) + '%'

for key, value in dict_queries.items():
    print(f'Поисковые запросы, включающие {key} составляют {value} от всех поисковых запросов')




        
        



    

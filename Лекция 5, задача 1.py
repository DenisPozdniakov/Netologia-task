import time
documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }

def people_number_doc(doc=documents):
    '''Функция запрашивает у юзера номер документа,
    выводит информацию об имене владельца, если документ существует'''
    print('Введите номер документа')
    num = input()
    flag = False
    for docs in doc:
        if docs['number'] == num:
            print('Документ принадлежит : ' ,docs['name'])
            flag = True
    if flag == False:
        print('Документ с данным номером отсутствует в картотеке')

def shelf_number_doc(dir=directories):
    '''Фунция запрашивает у юзера номер документа, при его наличие
    выводит номер полки'''
    print('Введите номер документа')
    num = input()
    flag = False
    for i in dir:
        if num in dir[i]:
            print('Номер полки с вашим документом: ' ,i)
            flag = True
    if flag == False:
        print('Документ с данным номером отсутствует в картотеке')

def show_list_doc(doc=documents):
    '''Функция выводит список всех документов в удобном для чтения формате'''
    for docs in doc:
        print(*docs.values())

def document_add(docs=documents, dir=directories):
    '''Функция запрашивает данные документа и добавляет в картотеку и присваивает номер полки'''
    print('Укажите тип документа, номер документа и имя владельца, в формате:\nтип/номер/имя фамилия (без лишних пробелов)')
    doc = input().split('/')
    if len(doc) != 3:
        print('Вы ввели данные в некорректном формате, пожалуйста попробуйте еще раз. Документ не добавлен')
    else:
        dict1 = {'type': doc[0], 'number': doc[1], 'name': doc[2]}
        docs.append(dict1)
        print('Документ добавлен в картотеку, пожалуйста, укажите полку для хранения.')
        flag = True
        while flag == True:
            print('Введите номер полки (без кавычек), на которую добавить документы из списка: ', list(dir.keys()))
            num_dir = input()
            if num_dir not in dir.keys():
                print('Данной полки не существует, либо вы указали некорректные данные, \nпожалуйста, выберете полку из списка: ')
            else:
                flag = False
                dir[num_dir].append(doc[1])
                print('документ успешно добавлен на полку')
    
def delete_doc(docs=documents, dir=directories):
    '''Функция запрашивает у юзера номер документа и удаляет его из картотеки и с полки'''
    print('Введите номер документа, который необходимо удалить: ')
    number_doc = input()
    flag = True
    for i in docs:
        if number_doc in list(i.values()):
            docs.remove(i)
            flag = False
            for k in dir:
                if number_doc in dir[k]:
                    dir[k].remove(number_doc)
            print('Документ удален')  
    if flag == True:
        print('Данный документ отсутствует в картотеке. Повторите операцию')

def move_doc(dir=directories):
    ''' Функция запрашивает у юзера номер документа и позволяет изменить полку хранения'''
    print('Введите номер документа')
    number_doc = input()
    if number_doc not in list(dir.values()):
        print('Вы указали некорректный номер документа')
    flag = False
    for k in dir:
        if number_doc in dir[k] and flag == False:
            print('Сейчас документ хранится на полке под номером:', k,'\n----------------------')   
            print('Введите номер полки, на которую переместить документ, доступные полки: ', list(dir.keys()))
            number_dir = input()
            flag = True
            if number_dir in dir:
                dir[k].remove(number_doc)
                dir[number_dir].append(number_doc)
                print('Успешно!')
            else:
                print('Вы указали некорректную полку. Проведите операцию заново')

            
def add_shelf(dir=directories):
    ''' Функиция позволяет добавить уникальную полку хранения'''
    print('Введите номер полки для добавления: ')
    number_dir = input()
    if number_dir in dir:
        print('Данная полка уже существует, повторите операцию заново')
    else:
        dir[number_dir] = []
        print('Полка добавлена')
            
def main():
    print('------------------------\
\nДоступные команды: l - Показать список всех документов; a - Добавить новый документ в картотеку;\
\n----------------\ns - вывести номер полки хранения документа по его номеру; p - Вывести имя Владельца документа, по его номеру\
\n----------------\nd - Удалить документ из картотеки по его номеру; m - сменить текущую полку документа по его номеру;\
\n----------------\nas - Добавить новую полку для хранения документов; exit - Завершить работу')
    print('-------------')
    print('Введите команду:')
    command = input()
    return command

### Основная программа:
flag1 = True
while flag1 == True:
    command = main()
    if command == 'l':
        show_list_doc()
        time.sleep(5)
    elif command == 'a':
        document_add()
        time.sleep(5)
    elif command == 's':
        shelf_number_doc()
        time.sleep(5)
    elif command == 'p':
        people_number_doc()
        time.sleep(5)
    elif command == 'd':
        delete_doc()
        time.sleep(5)
    elif command == 'm':
        move_doc()
        time.sleep(5)
    elif command == 'as':
        add_shelf()
        time.sleep(5)
    elif command == 'exit':
        print('Программа завершает работу, все изменения сохранены')
        flag1 = False
    else:
        print('Не удалось распознать команду, попробуйте заново')
    
    

            
      
    



    





        

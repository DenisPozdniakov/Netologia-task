### Функция добавления новых пользователей
def add_user():
  print('Укажите пол пользователя (м/ж): ')
  gender_user = input().lower()
  print('Укажите никнейм пользователя на англ расскладке:')
  nickname_user = input()
  if gender_user == 'м':
    boys.append(nickname_user)
  elif gender_user == 'ж':
    girls.append(nickname_user)
  else:
    print('Вы указали некорректный "Пол", пожалуйста повторите операцию')
def main():
  boys.sort()
  girls.sort()
  print('Идеальные пары:')
  for i in range(len(boys)):
    print(boys[i], 'и', girls[i])
  
    
### Основная программа
boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

print('Добрый день, вас привествует сервис знакомств, требуется ли добавить новых пользователей? да/нет')
question_add_users = input().lower()
if question_add_users == 'да':
  flag = True
  while flag == True:
    add_user()
    print('Добавить еще пользователя?')
    question_add_users_into_while = input().lower()
    if question_add_users_into_while == 'нет':
      flag = False
      print('Указанные пользователи добавлены в поиск!')

## Проверяем соразмерность списков
if len(boys) != len(girls):
  if len(boys) > len(girls):
    x1,x2 = 'Мужчин', 'Женщин'
  else:
    x2,x1 = 'Мужчин', 'Женщин'
  print('К сожалению мы не можем подобрать идеальную пару, т.к. количество {0} превышает количество {1}, пожалуйста добавьте пользователей: {1}'.format(x1,x2))
  add_user()
  main()
else:
  main()





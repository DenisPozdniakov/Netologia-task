boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

if len(boys) == len(girls):
  boys.sort(), girls.sort()
  y = list(zip(boys,girls))
  print('Идеальные пары:')
  for i in range(len(y)):
    print('{0} и {1}'.format(y[i][0], y[i][1]))

else:
  print('К сожалению мы не можем подобрать идеальные пары, т.к. количество пользователей не соизмеримо')




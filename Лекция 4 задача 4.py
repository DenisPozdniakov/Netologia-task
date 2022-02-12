stats = {'facebook': 55, 'yandex': 120, 'vk': 115,
         'google': 99, 'email': 42, 'ok': 98}

count_max = 0
name_stats_max = ''
for stat in stats:
    if stats[stat] > count_max:
        count_max = stats[stat]
        name_stats_max = stat

print(name_stats_max)

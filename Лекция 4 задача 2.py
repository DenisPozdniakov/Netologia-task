ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}


unique_ids = []

for i in ids.values():
    for k in i:
        if k not in unique_ids:
            unique_ids.append(k)

print(unique_ids)


###### Вариант через множества

##set_ids = set()
##
##for i in ids.values():
##    set_ids.update(set(i))
##       
##print(set_ids)




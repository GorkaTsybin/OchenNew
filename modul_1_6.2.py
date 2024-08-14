my_dict = {'Факел': 45, 'Родина': 40, 'Орёл': 36}
print(my_dict)
my_dict['Орёл'] = 46
print(my_dict)
my_dict['Титан'] = 38
print(my_dict)
del my_dict['Родина']
print(my_dict)
my_dict.update({'Академия': 55,
                'Легионер': 56})
print(my_dict)
print(my_dict.get('Авангард', 'Такой команды нет'))
my_set = {1, 2, 3, 4, 5, 1, 2, 3, 4, 'Orel', (1, 2, 3, 4)}
print(my_set)
print(my_set.add(6))
print(my_set)
print(my_set.discard(5))
print(my_set)


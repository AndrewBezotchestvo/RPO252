articuls = {13123, 21333, 22123, 22222, 22222}
print(type(articuls))
print(articuls)

print(list(articuls)[0]) #индексация вовзможна только при приобразовании в list

for item in articuls:
    print(item)

articuls.add(12331)
articuls.add(22173)
print(articuls)

articuls.remove(21333)
articuls.discard(21333)
print(articuls)

articuls.pop() #лучшие не использовать
print(articuls)

#операции с несколькими множествами
articuls = {13123, 21333, 22123, 22222, 22222}
articuls_new = {13123, 21333, 22123, 34234, 12122}

#объединение
# articuls.update(articuls_new)
# print(articuls)
articuls1 = articuls.union(articuls_new)
print(articuls1)
articuls2 = articuls | articuls_new
print(articuls2)

#пересечение
# articuls.intersection_update(articuls_new)
# print(articuls)
articuls3 = articuls.intersection(articuls_new)
print(articuls3)
articuls4 = articuls & articuls_new
print(articuls4)

#разница, уникальные элементы в 1 множестве
# articuls.difference_update(articuls_new)
# print(articuls)
articuls5 = articuls - articuls_new
print(articuls5)
articuls6 = articuls.difference(articuls_new)
print(articuls6)

#разница, уникальные элементы в обоих множествах
# articuls.symmetric_difference_update(articuls_new)
# print(articuls)
articuls7 = articuls ^ articuls_new
print(articuls7)
articuls8 = articuls.symmetric_difference(articuls_new)
print(articuls8)
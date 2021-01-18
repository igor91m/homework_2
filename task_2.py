'''
2. Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить
на своем месте. Для заполнения списка элементов необходимо использовать функцию input().
'''

# Добавление элементов списка путем input
second_list = []
# Количество элементов для списка
count = int(input('Enter number of elements: '))
i = 0
el = 0
while i < count:
    second_list.append(input('Enter next number: '))
    i += 1
for elem in range(int(len(second_list)/2)):
        second_list[el], second_list[el + 1] = second_list[el + 1], second_list[el]
        el += 2
print(second_list)
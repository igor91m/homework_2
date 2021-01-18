'''
4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
'''

person_first_str = input(f"Введите строку: ")
word_list = []
number = 1
for el in range(person_first_str.count(' ') + 1):
    word_list = person_first_str.split()
    # Что тут лучше цикл while или все же if ???
    if len(str(word_list)) <= 10:
        print(f" {number} {word_list [el]}")
        number += 1
    else:
        print(f"{number} {word_list [el] [0:10]}")
        number += 1

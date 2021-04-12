"""
Задание 3.
Определить количество различных (уникальных) подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените вычисление хешей для подстрок с помощью хеш-функций и множества

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
a
"""

# hash?
S = str(input("Введите строку S: "))

print(f"Строка {S} имеет длину {len(S)} сиволов.")

subs_set = set()
subs_dict = {}
for i in range(len(S)):
    for j in range(len(S)-1 if i == 0 else len(S), i, -1):
        subs_set.add(hash(S[i:j]))
        print(S[i:j], i, j)
        subs_dict[S[i:j]] = hash(S[i:j])

print(len(list(subs_dict.keys())), list(subs_dict.keys()))
print("Количество различных подстрок в этой строке:", len(subs_set))
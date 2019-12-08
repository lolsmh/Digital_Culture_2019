#!/usr/bin/python3
# -*- coding: utf-8 -*-
import codecs
import copy


def damerau_levenshtein_distance(s1, s2):
    d = {}
    lenstr1 = len(s1)
    lenstr2 = len(s2)
    for i in range(-1, lenstr1 + 1):
        d[(i, -1)] = i + 1
    for j in range(-1, lenstr2 + 1):
        d[(-1, j)] = j + 1

    for i in range(lenstr1):
        for j in range(lenstr2):
            if s1[i] == s2[j]:
                cost = 0
            else:
                cost = 1
            d[(i, j)] = min(
                d[(i - 1, j)] + 1,
                d[(i, j - 1)] + 1,
                d[(i - 1, j - 1)] + cost,
            )
            if i and j and s1[i] == s2[j - 1] and s1[i - 1] == s2[j]:
                d[(i, j)] = min(d[(i, j)], d[i - 2, j - 2] + cost)

    return d[lenstr1 - 1, lenstr2 - 1]


brain_in = codecs.open("dictout", "r", "utf_8_sig")
dict_in = codecs.open("dict1.txt", "r", "utf_8_sig")
f = dict_in.read()
temp_array = f.split()
dict_array = temp_array[::2]
insertion_array = temp_array[1::2]
with open("dictout") as file:
    array = [row.strip() for row in file]
unique_array = []
for x in array:
    if x not in unique_array:
        unique_array.append(x)
temp_error_array = set(unique_array).difference(dict_array)
error_array = list(temp_error_array)
error_array_copy = copy.deepcopy(error_array)
print("Количество словоформ: " + str(len(array)))
print("Количество уникальных словоформ: " + str(len(unique_array)))
print("Количество словоформ, присутствующих в словаре: " + str(len(set(unique_array).intersection(dict_array))))
print("Количество потенциальных ошибок: " + str(len(unique_array) - len(set(unique_array).intersection(dict_array))))
print("Слова с ошибками: " + str(error_array))
print("Исправленные ошибки:")
for i in range(len(error_array)):
    max = 0
    for j in range(len(dict_array)):
        dist = damerau_levenshtein_distance(error_array[i], dict_array[j])
        if dist == 1:
            if max < int(insertion_array[j]):
                max = j
        if dist == 2:
            if max < int(insertion_array[j]):
                max = j
    print(error_array[i] + ' - ' + dict_array[max] + ' - ' + str(
        damerau_levenshtein_distance(error_array[i], dict_array[max])))
    error_array[i] = dict_array[max]
for i in range(len(error_array_copy)):
    for j in range(len(array)):
        if array[j] == error_array_copy[i]:
            array[j] = error_array[i]
unique_array.clear()
for x in array:
    if x not in unique_array:
        unique_array.append(x)
temp_error_array = set(unique_array).difference(dict_array)
error_array = list(temp_error_array)
error_array_copy = copy.deepcopy(error_array)
print("Количество словоформ: " + str(len(array)))
print("Количество уникальных словоформ: " + str(len(unique_array)))
print("Количество словоформ, присутствующих в словаре: " + str(len(set(unique_array).intersection(dict_array))))
print("Количество потенциальных ошибок: " + str(len(unique_array) - len(set(unique_array).intersection(dict_array))))

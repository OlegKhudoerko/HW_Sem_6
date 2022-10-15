# 1. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента. Use comprehension.
# in
# 9

# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]

# in
# 10

# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]

from random import sample


def f_rnd(num):
    if not num.isnumeric():
        print("The data is incorrect")
        return []
    return sample(range(int(num)*3), int(num))


def ls_more(num):
    return [num[i] for i in range(1, len(num)) if num[i] > num[i - 1]]


ls = f_rnd(input("Введите количество чисел: "))
print(f"{ls} \n \r{ls_more(ls)}")

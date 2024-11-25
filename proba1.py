# РЕКУРСИЯ

def sum_list(arr):
    if not arr:
        return 0
    else:

        return arr[0] + sum_list(arr[1:])

# Пример использования:
my_list = [1, 2, 3, 4, 5,6]
result = sum_list(my_list)
print()
print("Сумма элементов списка:", result)  # Вывод: 15 [1](https://proghunter.ru/articles/recursion-in-python-overview-and-examples)


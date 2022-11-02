import random
from random import randint
def get_unique_list_numbers() -> list[int]:
    unique = []
    start = -10
    stop = 11
    count = 15
    list_numbers = [i for i in range(start,stop)]
    random.shuffle(list_numbers)
    return list_numbers[:count]
    # TODO написать функцию для получения списка уникальных целых чисел


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))

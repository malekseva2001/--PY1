import random
import string
def get_random_password() -> str:
    count = 8
    list_numbers_1 = list([i for i in range(0,10)])
    list_numbers_2 = list(string.ascii_letters)
    list_number_3 = list_numbers_1 + list_numbers_2
    return str(random.sample(list_number_3, count))

print(get_random_password(),type(get_random_password()))

from pprint import pprint
sis = "dec"
dict_dec = {num: int(num) for num in range(16)}
dict_bin = {num: bin(num) for num in range(16)}
dict_oct = {num: oct(num) for num in range(16)}
dict_hex = {num: hex(num) for num in range(16)}

pprint([dict_dec,dict_bin,dict_oct,dict_hex])


# TODO решить с помощью list comprehension и распечатать его


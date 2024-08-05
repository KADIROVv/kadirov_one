1.
import random as rd
def split_list(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]
lst = [rd.randint(10,50) for x in range(10)]
n = int(input("Sonni kirit>>> "))
natija = split_list(lst, n)
print(natija)


2.


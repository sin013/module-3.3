values_list = (1, False, 'что-то')
values_dict = {'a': 12, 'b': 'зачем', 'c': True}
values_list2 = (32, "почему")


def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(2)
print_params("кряква", False)
print_params(c=[1, 2, 5])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list2, False)
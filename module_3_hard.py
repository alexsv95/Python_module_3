# Задание "Раз, два, три, четыре, пять .... Это не всё?"


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

def sum_list(list_):
    sum = 0
    if isinstance(list_, int):
        sum += list_
    elif isinstance(list_, str):
        sum += len(list_)
    elif isinstance(list_, (list, tuple, set)):
        for i in list_:
            sum += sum_list(i)
    elif isinstance(list_, dict):
        for key, val in list_.items():
            sum += sum_list(key)
            sum += sum_list(val)
    return sum


result_2 = sum_list(data_structure)
print(result_2)

'''
def list_unpack(list_):
    if not list_:
        return list_
    if isinstance(list_[0], list):
        return list_unpack(list_[0]) + list_unpack(list_[1:])
    if isinstance(list_[0], tuple):
        return list(list_unpack(list_[0])) + list(list_unpack(list_[1:]))
    return list(list_[:1]) + list(list_unpack(list_[1:]))


# print(list_unpack([1,'strs',2,[4,5,(7,'strs',8,9)]]))
print(list_unpack(data_structure))
'''



# def tuple_unpack(list_):
#     if not list_:
#         return list_
#     if isinstance(list_[0], tuple):
#         return tuple_unpack(list_[0]) + tuple_unpack(list_[1:])
#     return list(list_[:1]) + list(tuple_unpack(list_[1:]))
#
#
# print(tuple_unpack((7,8,9)))


# def list_to_unpack(*args):
#     list_unpack = []
#     list_args = [*args]
#     if len(list_args) == 1:
#         return list_args[0]
#     else:
#         for i in args:
#             if isinstance(i, tuple) or isinstance(i, list) or isinstance(i, dict):
#                 return list_to_unpack(*list_args)

# def calculate_structure_sum(*args):
#     list_str = []
#     list_int = []
#     for i in args:
#         if not isinstance(i, tuple) and not isinstance(i, list) and not isinstance(i, dict):
#             return type(i)
#         else:

    #
    # if isinstance(args, l)
    # str_type = []
    # tuple_type = []
    # for j in args:
    #     if isinstance(j, tuple):
    #         tuple_type.append(j)
    # # for i in args:
    # #     if isinstance(i, str):
    # #         str_type.append(i)
    # return str_type

# result = list_to_unpack(*data_structure)
# print(result)


# list_str = {'123': 7, '4555': 2}
# list_tuple = 1, 2, 3)
# print(type(list_tuple))
#
# print(calculate_structure_sum(list_tuple))
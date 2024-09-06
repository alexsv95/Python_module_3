# domain = ['.ru', '.net', '.com']
# txt = "email@gm.ru"
#
# for i in domain:
#     if txt[-len(i):] == i:
#         print(True)
#     else:
#         print(False)
#
#
# print(txt[-3:])

def info (**kwargs: dict):
    print(kwargs)

info()
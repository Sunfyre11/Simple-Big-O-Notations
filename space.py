from hashlib import new


def create_list(n):

    new_list = []

    for num in range (n + 1):
        new_list.append('new')

    return new_list

print(create_list(5))
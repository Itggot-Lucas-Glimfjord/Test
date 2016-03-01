__author__ = 'Lucas'

def selection_sort(list):
    sorted_list = []

    while len(list) != 0:
        minst = 0
        x = 1

        while x < len(list):
            if list[minst] > list[x]:
                minst = x
            x += 1
        sorted_list.append(list.pop(minst))

    return sorted_list


#print selection_sort(list=[45,4,22,23,1,2,42,87,98])

def selectshort(list, sorted_list=[]):
    while len(list) > 0: sorted_list.append(list.pop(list.index(min(list))))
    return sorted_list

print selectshort(list=[45,4,22,23,1,2,42,87,98])





















def selection_sort(list):
    sorted_list = []

    while len(list) != 0:
        minst = 0
        x = 1
        while x < len(list):
            if list[minst] > list[x]:
                minst = x
            x += 1
        sorted_list.append(list[list.pop(minst)])
    return sorted_list
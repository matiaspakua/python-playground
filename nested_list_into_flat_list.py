# input list
my_list = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]

output = []


def RemoveNesting(my_list):
    """This function uses recursion, that is not the best aproach"""
    for i in my_list:
        if type(i) == list:
            RemoveNesting(i)
        else:
            output.append(i)

print('original items in list: ', my_list)
RemoveNesting(my_list)
print('List after remove nesting:', output)
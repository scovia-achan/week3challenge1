def list_sort(list1):
    even = []
    odd = []
    char = []
    mydictionary = dict()

    #checking whether list1 is of type list
    if not isinstance(list1, list):
        return 'invalid input'

    # 
    for i in list1:
        # the conditional checks whether i  is of type int and then 
        if isinstance(i, int):

            if i%2 == 0:
                even.append(i)
            else:
                odd.append(i)

        elif isinstance(i, str):
            char.append(i)
    mydictionary['even'] = sorted(even)
    mydictionary['odd'] = sorted(odd)
    mydictionary['char'] = sorted(char)
    return mydictionary
        
print(list_sort([10, 2, 8, 'c', 'f']))

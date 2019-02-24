def missing_numbers(number_list):
    first_list = [x for x in range(number_list[0], number_list[-1] + 1)]
    number_list = set(number_list)
    return (list(number_list ^ set(first_list)))

print(missing_numbers([1,2,3,5,6,7,9]))
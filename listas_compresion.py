def get_pairs(my_list):
    list_pair = []
    for n in my_list:
        if not (n % 2):
            list_pair.append(n)
    return list_pair

my_list = range(10000000)

def get_pairs_cool(my_list):
    return [n for n in my_list if not (n % 2)]

get_pairs_cool(my_list)
#'time output: 0.54s'

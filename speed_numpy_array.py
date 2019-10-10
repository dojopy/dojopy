import numpy as np

items = 1000000
mylist = range(items)
myarray = np.arange(items)

def operate_array():
    return [i*2 for i in myarray]

def operate_list():
    return [i*2 for i in mylist]


# operate_array()
operate_list()

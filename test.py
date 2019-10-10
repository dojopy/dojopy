#!/usr/bin/env python3

def nice(array, prefix):
    for a in array:
        if a.startswith(prefix):
            yield a
array = ['ok_apple', 'brother','syster' ,'ok_banana']
print(list(nice(array, 'ok')))

##########
def fun_nice(data='ok'):
    print(data*10)

def nice_2(large_str):
    new = ''
    for l in large_str:
        if not(l in new):
            new += '%s%s'%(l,str(large_str.count(l)))
    return new

large_str = 'AAAAaaBCCCDDe'
print(nice_2(large_str))

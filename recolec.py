import gc
from time import sleep
import sys

data = 'aaaaaaaaaaaa'*100000
while True:
    cmd = input('tu comando?')
    print(cmd)
    print(len(data))
    print(sys.getsizeof(data))

    if cmd == 'free':
        collected_objects = gc.collect()
        # del data
        print('liberado')
        print(len(data))
        print(sys.getsizeof(data))
        sleep(100)

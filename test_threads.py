from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from time import sleep
#
# def	pow(a):
# 	sleep(3)
# 	return a

def	pow(a):
	number = 100000000
	while number > 0:
		number -= 1
	return a

# with ThreadPoolExecutor(max_workers=5) as executor:
# 	future = executor.submit(pow, 323)
# 	future_ = executor.submit(pow, 323)
# 	print(future.result())
# 	print(future_.result())

with ProcessPoolExecutor(max_workers=3) as executor:
	future = executor.submit(pow, 323)
	future_ = executor.submit(pow, 323)
	future__ = executor.submit(pow, 323)
	print(future.result())
	print(future_.result())
	print(future__.result())

#!/usr/bin/env python3
import random
from numba import cuda

@cuda.jit
def monte_carlo_pi(nsamples):
    acc = 0
    for i in range(nsamples):
        x = random.random()
        y = random.random()
        if (x ** 2 + y ** 2) < 1.0:
            acc += 1
    return 4.0 * acc / nsamples

nice = monte_carlo_pi(10000000) #10M iteraciones
print(nice)

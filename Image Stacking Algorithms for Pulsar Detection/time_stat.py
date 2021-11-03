import numpy as np
import statistics
import time

def time_stat(func, size, ntrials):
  # the time to generate the random array is not included
  total = 0
  for i in range(ntrials):
    data = np.random.rand(size)
  # timer
    start = time.perf_counter()
    res = func(data)
    total += time.perf_counter() - start
  # returns the average run time
  return total/ntrials

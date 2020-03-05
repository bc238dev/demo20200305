print("--- Pi Demo (5 March 2020/Thr) ---")
import random
from math import sqrt

def estimate_pi(times):
  a = 0
  for i in range(times):
    x = random.random()
    y = random.random()
    d = sqrt(x**2 + y**2)
    if d <= 1:
      a += 1

  pi = 4.0*a/times
  return pi

pi = estimate_pi(10000)
print("Estimated pi", pi)
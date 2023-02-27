import math
import random
import time
from typing import Optional

# function const
STOCHASTIC_SCALE =  10      # adds randomness to Rastrigin function
SLEEP =             5       # adds some sleep to simulate computation process duration


# Rastrigin function (inverted for maximum)
def rastrigin_func_2D(
        xa: float,
        xb: float,
        const_a=                10,
        sscl=                   STOCHASTIC_SCALE,
        sleep: Optional[int]=   SLEEP):
    if sleep: time.sleep(sleep)
    result = 2*const_a + xa**2 - const_a*math.cos(2*math.pi*xa) + xb**2 - const_a*math.cos(2*math.pi*xb)
    if sscl: result += sscl * random.random()
    return -result

# Rastrigin function (inverted for maximum)
def rastrigin_func_ndim(
        const_a=                10,
        sscl=                   STOCHASTIC_SCALE,
        sleep: Optional[int]=   SLEEP,
        **params):
    if sleep: time.sleep(sleep)
    sub_values = [params[p]**2 - const_a*math.cos(2*math.pi*params[p]) for p in params]
    result = 2*const_a +sum(sub_values)
    if sscl: result += sscl * random.random()
    return -result

# function to test hpmser with exception
def func_exception(exception_prob=0.1, **kwargs):
    if random.random() < exception_prob: raise Exception('func_exception')
    return rastrigin_func_ndim(**kwargs)
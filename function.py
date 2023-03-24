import math
import random
import time
from typing import Optional


# N-dim Rastrigin function
def rastrigin_func_ndim(
        a: float=               10, # A parameter of rastrigin
        flatten: float=         10, # flattens values
        random_offset: float=   10, # adds random offset to value
        sleep: Optional[int]=   5,  # sleep N seconds
        **params                    # here go N params
):
    """
    little modified N-dim Rastrigin function
    N parameters should be given with **params
    modifications:
    - function returned value is inverted (for maximum)
    - added random offset to returned values
    - sleep simulates computation process
    """
    if sleep:
        var = sleep / 3
        sleep = sleep - 0.5*var + random.random()*var
        time.sleep(sleep)

    # original Rastrigin value
    _sub_values = [params[p]**2 - a * math.cos(2 * math.pi * params[p]) for p in params]
    result = a*len(params) + sum(_sub_values)
    result /= flatten                                   # flatten
    result += random_offset * (random.random() - 0.5)   # random
    return -result                                      # invert

# Rastrigin + random exception
def func_exception(exception_prob=0.1, **kwargs):
    if random.random() < exception_prob: raise Exception('func_exception')
    return rastrigin_func_ndim(**kwargs)
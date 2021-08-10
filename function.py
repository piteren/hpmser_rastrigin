import math
import random
import time
from tqdm import tqdm

from ptools.pms.paspa import PaSpa
from ptools.pms.hpmser import SRL

from psdd import get_psdd

# function options
STOCHASTIC_SCALE =  10
NDIM =              2
PARAM_RNG =         1.0
SLEEP =             5


# rastrigin function (inverted for maximum)
def rastrigin_func_2D(
        xa: float,
        xb: float,
        const_a=    10,
        sscl=       STOCHASTIC_SCALE,
        sleep: int= SLEEP):
    if sleep: time.sleep(sleep)
    result = 2*const_a + xa**2 - const_a*math.cos(2*math.pi*xa) + xb**2 - const_a*math.cos(2*math.pi*xb)
    if sscl: result += sscl * random.random()
    return -result

# rastrigin function (inverted for maximum)
def rastrigin_func_ndim(
        const_a=    10,
        sscl=       STOCHASTIC_SCALE,
        sleep: int= SLEEP,
        **params):
    if sleep: time.sleep(sleep)
    sub_values = [params[p]**2 - const_a*math.cos(2*math.pi*params[p]) for p in params]
    result = 2*const_a +sum(sub_values)
    if sscl: result += sscl * random.random()
    return -result

# plots some samples of func
def plot_func(
        ndim=       NDIM,
        rng=        PARAM_RNG,
        sscl=       STOCHASTIC_SCALE,
        n_samples=  3000):

    psdd = get_psdd(ndim, rng)
    paspa = PaSpa(psdd=psdd)
    srl = SRL(paspa=paspa, name=f'srl_{ndim}_{rng}_{sscl}')

    points = [paspa.sample_point() for _ in range(n_samples)]
    for pt in tqdm(points): srl.add_result(
        point=  pt,
        score=  rastrigin_func_ndim(
            **pt,
            sscl=   sscl,
            sleep=              0), force_no_update=True)

    #srl.print_distances()

    s_time = time.time()
    print('sorting...', end='')
    srl.smooth_and_sort()
    print(f', finished! ({time.time()-s_time:.1f}s)')

    srl.plot()


if __name__ == '__main__':

    # base 2dim examples
    plot_func(ndim=2, rng=0.5,  sscl=0,     n_samples=100)
    plot_func(ndim=2, rng=0.5,  sscl=50,    n_samples=100)
    plot_func(ndim=2, rng=0.5,  sscl=30,    n_samples=500)
    plot_func(ndim=2, rng=2.0,  sscl=30,    n_samples=100)
    plot_func(ndim=2, rng=2.0,  sscl=30,    n_samples=1000)
    plot_func(ndim=2, rng=2.0,  sscl=0,     n_samples=1000)

    # more dims
    #plot_func(ndim=2, rng=0.7, sscl=0,      n_samples=3000)
    #plot_func(ndim=3, rng=0.7, sscl=0,      n_samples=3000)
    #plot_func(ndim=5, rng=0.7, sscl=0,      n_samples=3000)

    #plot_func(ndim=2, rng=5.0, sscl=0,      n_samples=3000)

import math
import random
import time
from tqdm import tqdm

from ptools.pms.paspa import PaSpa
from ptools.pms.hpmser import hpmser_GX, SRL

NDIM = 2
RANGE = 1.0
STOCHASTIC_SCALE = 10

# rastrigin function (inverted for maximum)
def rastrigin_func_2D(
        xa: float,
        xb: float,
        const_a=    10,
        sleep=      1):
    if sleep: time.sleep(sleep)
    result = 2*const_a + xa**2 - const_a*math.cos(2*math.pi*xa) + xb**2 - const_a*math.cos(2*math.pi*xb)
    if STOCHASTIC_SCALE: result += STOCHASTIC_SCALE * random.random()
    return -result

# rastrigin function (inverted for maximum)
def rastrigin_func_ndim(
        const_a=    10,
        sleep=      1,
        **params):
    if sleep: time.sleep(sleep)
    sub_values = [params[p]**2 - const_a*math.cos(2*math.pi*params[p]) for p in params]
    result = 2*const_a +sum(sub_values)
    if STOCHASTIC_SCALE: result += STOCHASTIC_SCALE*random.random()
    return -result

# plots some samples of func
def plot_func(
        psd: dict,
        n_samples=3000):

    paspa = PaSpa(psd=psd)
    srl = SRL(paspa=paspa, name=f'srl_{NDIM}_{RANGE}_{STOCHASTIC_SCALE}')

    points = [paspa.sample_point() for _ in range(n_samples)]
    for pt in tqdm(points): srl.add_result(point=pt, score=rastrigin_func_ndim(**pt, sleep=0), force_no_update=True)
    #srl.print_distances()

    s_time = time.time()
    print('sorting...')
    srl.smooth_and_sort()
    print(f'{time.time()-s_time:.1f}')

    srl.plot()


if __name__ == '__main__':

    psd = {f'p{n}': [-RANGE,RANGE] for n in range(NDIM)}
    """
       {'p0':   [-0.5, 0.5],
        'p1':   [-0.5, 0.5],
        'p2':   [-0.5, 0.5]}
    """

    plot_func(psd)

    """
    hpmser_GX(
        func=           rastrigin_func_ndim,
        psd=            psd,
        devices=        [None]*10,
        #preferred_axes= ['p1','p2'],
        verb=           1)
    #"""
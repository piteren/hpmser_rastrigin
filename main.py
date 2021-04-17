import math
import random
import time
from tqdm import tqdm

from ptools.pms.paspa import PaSpa
from ptools.pms.hpmser import hpmser_GX, SRL

CASE = 'easy'

STOCHASTIC_SCALE = 10

RANGES = {
    'hardcore': { # many local minima
        'xa':   [-5.0, 5.0],
        'xb':   [-5.0, 5.0]},
    'hard': { # some local minima
        'xa':   [-2.0, 2.0],
        'xb':   [-2.0, 2.0]},
    'easy': { # one local minima
        'xa':   [-0.5, 0.5],
        'xb':   [-0.5, 0.5]},
    'hardcore_3D': { # some local minima
        'xa':   [-5.0, 5.0],
        'xb':   [-5.0, 5.0],
        'xc':   [-5.0, 5.0]},
    'hard_3D': { # some local minima
        'xa':   [-2.0, 2.0],
        'xb':   [-2.0, 2.0],
        'xc':   [-2.0, 2.0]},
    'easy_3D': { # one local minima
        'xa':   [-0.5, 0.5],
        'xb':   [-0.5, 0.5],
        'xc':   [-0.5, 0.5]}}


# rastrigin function (inverted for maximum)
def rastrigin_func(
        xa: float,
        xb: float,
        const_a=    10,
        sleep=      1):
    if sleep: time.sleep(sleep)
    result = 2*const_a + xa**2 - const_a*math.cos(2*math.pi*xa) + xb**2 - const_a*math.cos(2*math.pi*xb)
    if STOCHASTIC_SCALE: result += STOCHASTIC_SCALE * random.random()
    return -result

# rastrigin function (inverted for maximum)
def rastrigin_func_3D(
        xa: float,
        xb: float,
        xc: float,
        const_a=    10,
        sleep=      1):
    if sleep: time.sleep(sleep)
    result = 2*const_a + xa**2 - const_a*math.cos(2*math.pi*xa) + xb**2 - const_a*math.cos(2*math.pi*xb)  + xc**2 - const_a*math.cos(2*math.pi*xc)
    if STOCHASTIC_SCALE: result += STOCHASTIC_SCALE*random.random()
    return -result

# plots some samples of func
def plot_func(
        func,
        n_samples=  3000):
    paspa = PaSpa(psdd=RANGES[CASE])
    srl = SRL(paspa=paspa, name=f'srl_{CASE}')

    points = [paspa.sample_point() for _ in range(n_samples)]
    for pt in tqdm(points): srl.add_result(point=pt, score=func(**pt, sleep=0), force_no_update=True)
    #srl.print_distances()

    s_time = time.time()
    print('sorting...')
    srl.smooth_and_sort()
    print(f'{time.time()-s_time:.1f}')

    #"""
    s_time = time.time()
    pt = paspa.sample_point()
    srl.add_result(point=pt, score=func(**pt, sleep=0))
    print(f'{time.time()-s_time:.1f}')
    #"""

    srl.plot()


if __name__ == '__main__':

    rf = rastrigin_func_3D if '3D' in CASE else rastrigin_func

    plot_func(rf)

    """
    hpmser_GX(
        func=           rf,
        psd=            RANGES[CASE],
        devices=        [None]*10,
        #preferred_axes= ['xa','xb'],
        verb=           1)
    #"""
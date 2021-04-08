import math
import random
import time

from ptools.pms.paspa import PaSpa
from ptools.pms.hpmser import hpmser_GX, SeRes, SRL

CASE = 'easy'

STOCHASTIC_SCALE = 0

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
    srs = []
    for id in range(n_samples):
        pt = paspa.sample_point()
        val = func(**pt ,sleep=0)
        sr = SeRes(id=id, point=pt, score=val)
        srs.append(sr)
    srl.add_SR(srs)
    srl.plot()


if __name__ == '__main__':

    rf = rastrigin_func_3D if '3D' in CASE else rastrigin_func

    #plot_func(rf)

    #"""
    hpmser_GX(
        func=           rf,
        psd=            RANGES[CASE],
        use_GX=         True,
        distance_L2=    True,
        devices=        [None]*10,
        #preferred_axes= ['xa','xb'],
        verb=           1)
    #"""
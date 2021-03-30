import math
import random
import time

from ptools.pms.paspa import PaSpa
from ptools.pms.hpmser import hpmser, SeRes, SRL

# rastrigin function (inverted for maximum)
def rastrigin_func(
        xa: float,
        xb: float,
        const_a=    10,
        rnd=        1.0,
        sleep=      1):
    if sleep: time.sleep(sleep)
    result = 2*const_a + xa**2 - const_a*math.cos(2*math.pi*xa) + xb**2 - const_a*math.cos(2*math.pi*xb)
    if rnd: result += rnd * random.random()
    return -result

# rastrigin function (inverted for maximum)
def rastrigin_func_3D(
        xa: float,
        xb: float,
        xc: float,
        const_a=    10,
        rnd=        1.0,
        sleep=      1):
    if sleep: time.sleep(sleep)
    result = 2*const_a + xa**2 - const_a*math.cos(2*math.pi*xa) + xb**2 - const_a*math.cos(2*math.pi*xb)  + xc**2 - const_a*math.cos(2*math.pi*xc)
    if rnd: result += rnd*random.random()
    return -result


if __name__ == '__main__':

    case = 'hardcore'

    ranges = {
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

    rf = rastrigin_func_3D if '3D' in case else rastrigin_func

    """
    paspa = PaSpa(psd=ranges[case])
    srl = SRL(paspa=paspa, name=f'srl_{case}')
    for id in range(10000):
        pt = paspa.sample_point()
        val = rf(**pt ,sleep=0)
        sr = SeRes(id=id, point=pt, score=val)
        srl.add_SR(sr)
    srl.plot()
    """

    hpmser(
        func=           rf,
        psd=            ranges[case],
        L2=             True,
        devices=        [None]*10,
        #subprocess=     False,
        hpmser_FD=      True,
        #preferred_axes= ['xa','xb'],
        verb=           1)
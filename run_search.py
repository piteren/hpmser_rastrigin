from hpmser.search import hpmser
from pypaq.pms.paspa import PaSpa
from pypaq.lipytools.plots import three_dim

from psdd import get_psdd
from function import rastrigin_func_ndim, func_exception


def plot_psdd(psdd, func_const, n_samples=1000):

    paspa = PaSpa(psdd=psdd)
    points = [paspa.sample_point() for _ in range(n_samples)]

    fcc = {}
    fcc.update(func_const)
    fcc['sleep'] = 0
    vals = [rastrigin_func_ndim(**p, **fcc) for p in points]

    fcc['random_offset'] = 0
    print(f'maximum at (0,0): {rastrigin_func_ndim(p0=0, p1=0, **fcc)}')

    xyz = [(p['p0'], p['p1'], v) for p, v in zip(points, vals)]
    three_dim(xyz, name=f'{n_samples} samples')


if __name__ == '__main__':

    n_dim = 2
    param_range = 2
    random_offset = 0.5
    flatten = 10
    add_exceptions = False
    sleep = 1

    psdd = get_psdd(n_dim=n_dim, rng=param_range)
    func_const = {'a':0.5, 'flatten':flatten, 'random_offset':random_offset, 'sleep':sleep}

    #plot_psdd(psdd=psdd, func_const=func_const, n_samples=100)
    #plot_psdd(psdd=psdd, func_const=func_const, n_samples=1000)

    hpmser(
        func=       func_exception if add_exceptions else rastrigin_func_ndim,
        func_psdd=  psdd,
        func_const= func_const,
        devices=    [None]*10,
        n_loops=    1000,
        plot_axes=  ['p0','p1'],
        loglevel=   20)